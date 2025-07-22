from flask import Flask, request, render_template

import os
import re
import json
import unicodedata
import pandas as pd
import joblib
import html

from nltk.tokenize import TweetTokenizer
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

app = Flask(__name__)

emoji_data_path = "dataset/emoji_to_text.csv"
slang_data_path = "dataset/twitter_trending_combined_slang_dict.json"
stem_data_path  = "dataset/twitter_trending_term_dict.json"
artefact_path   = "model/twitter_trending_classifier.pkl"

# Normalize Unicode
def normalize_unicode(text: str) -> str:
    if not isinstance(text, str):
        return ""

    return unicodedata.normalize("NFKC", text)

# Emoji Extraction 
df_emoji      = pd.read_csv(emoji_data_path)
emoji_map     = dict(zip(df_emoji["emoji"], df_emoji["makna"]))
emojis_sorted = sorted(emoji_map.keys(), key=len, reverse=True)
emoji_pattern = re.compile("|".join(map(re.escape, emojis_sorted)))

def replace_emoji(text: str) -> str:
    return emoji_pattern.sub(lambda m: " " + emoji_map[m.group(0)] + " ", text)

# Case Folding
def case_fold(text: str) -> str:
    return text.casefold()

# Cleaning Data
def clean_text(text: str) -> str:
    text = html.unescape(text)
    text = text.replace("\\n", " ").replace("\n", " ").replace("\r", " ")
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'#(\w+)', r'\1', text)
    text = re.sub(r'^\s*rt\s+', '', text)
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'\s+', ' ', text)

    return text.strip()

# Normalize Slang
with open(slang_data_path, 'r', encoding='utf-8') as f:
    slang_dict = json.load(f)

slang_keys = sorted(slang_dict.keys(), key=len, reverse=True)
pattern    = re.compile(r'\b(' + '|'.join(map(re.escape, slang_keys)) + r')\b')

def normalize_slang(text: str) -> str:
    if not isinstance(text, str):
        return text

    return pattern.sub(lambda match: slang_dict[match.group(0)], text)

# Tokenization
tweet_tokenizer = TweetTokenizer()

# Stopwords
sw_factory = StopWordRemoverFactory()
stopwords  = set(sw_factory.get_stop_words())

def remove_stopwords(tokens):
    return [t for t in tokens if t not in stopwords]

# Stemming
factory = StemmerFactory()
stemmer = factory.create_stemmer()

def load_term_dict(path=stem_data_path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    return None

term_dict = load_term_dict()

def stem_tokens(tokens: list[str]) -> list[str]:
    return [term_dict.get(t, stemmer.stem(t)) for t in tokens]

# Preprocess Data
def preprocess(raw: str) -> str:
    s      = normalize_unicode(raw)
    s      = replace_emoji(s)
    s      = case_fold(s)
    s      = clean_text(s)
    s      = normalize_slang(s)
    tokens = tweet_tokenizer.tokenize(s)
    tokens = [t for t in tokens if t]
    tokens = [t for t in tokens if len(t) > 2]
    tokens = remove_stopwords(tokens)
    tokens = stem_tokens(tokens)

    return " ".join(tokens)

# Load Model
obj     = joblib.load(artefact_path)
tfidf   = obj["tfidf"]
clf     = obj["clf"]
tf      = obj["threshold_factual"]
tr      = obj["threshold_relevant"]
classes = list(clf.classes_)

# Predict Tweet
def predict_tweet(raw_text, artefact_path=artefact_path):
    obj        = joblib.load(artefact_path)
    tfidf      = obj["tfidf"]
    clf        = obj["clf"]
    tf         = obj["threshold_factual"]
    tr         = obj["threshold_relevant"]
    text_final = preprocess(raw_text)
    Xv         = tfidf.transform([text_final])
    probs      = clf.predict_proba(Xv)[0]
    classes    = clf.classes_
    p_fact     = probs[classes=="factual"][0]
    p_rel      = probs[classes=="relevant"][0]
    p_noise    = probs[classes=="noise"][0]

    if p_fact > tf:
        label = "factual"
    elif p_rel  > tr:
        label = "relevant"
    else:
        label = "noise"

    return {
        "label": label,
        "confidence": {
            "factual":  f"{p_fact*100:.1f}%",
            "relevant": f"{p_rel*100:.1f}%",
            "noise":    f"{p_noise*100:.1f}%"
        }
    }

@app.route("/", methods=["GET", "POST"])
def index():
    text   = ""
    result = None

    if request.method == "POST":
        text   = request.form["text"]
        result = predict_tweet(text)

    return render_template("index.html", text=text, result=result)

if __name__ == "__main__":
    app.run(debug=True)