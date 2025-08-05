# Twitter Trending Classifier — by Dodevca

A lightweight tool to classify Twitter/X posts into noise, neutral, and relevant categories using a combination of rule-based logic and Logistic Regression model.

## About This Project
This project automates the classification of trending Twitter/X posts to filter out irrelevant content. It combines a simple rule-based system with a Logistic Regression model to improve filtering accuracy. The application is built with Flask and integrates Google Colab notebooks for model training and experimentation.

## Additional Information: Rules in each class
### Noise
- Containing sales offers, coupons, vouchers, or "check this link" for advertising or promotional purposes to encourage transactions.
- Phrases such as "click here!", "don't miss it!", "share if you agree!" without any context.
- Using trending hashtags but unrelated tweet content, solely to generate engagement.
- Short URLs (bit.ly, tinyurl, or other short URLs) without explaining the link content.
- Tagging multiple accounts (@user1 @user2 …) solely for promotional purposes.
- Tweets simply regurgitate keywords without addressing the topic.
### Factual
- Report data or observations using descriptive sentences. For example, "#Grok has been ranked #1 since 8:00 PM."
- Sentences without opinion or emotion are purely statistical, factual, or informative, and do not contain praise, criticism, or complaints.
- The structure resembles a news story or official report, usually using formal or semi-formal language.
- There are no sales pitches, commercial links, or calls to action.
### Relevant
- Express likes, dislikes, humor, or personal experiences related to the topic.
- Include reasons, criticism (positive or negative), or recommendations related to the topic.
- Contain questions for discussion, for example, "Has anyone attended this event #KonserMalamMinggu? What were your impressions?"
- Contain personal experiences or field observations presented in the form of a story.
- Contextual discussions that address the meaning or background of trending topics.
- Hashtags and mentions are used relevant to the content, not in a mass, unrelated way.

## Tech Stack & Tools
| Category     | Stack                    |
|--------------|--------------------------|
| Back-end     | Flask                    |
| Notebook     | Google Colab (Jupyter)   |
| Storage      | Google Drive             |
| Front-end    | Bootstrap (basic styling)|

## Key Features
- Rule-based classification for Twitter/X posts.
- Simple web interface displaying classification results and prediction percentages.
- Integration with Google Colab for model retraining and adjustments.

## Live Demo
Access the live demo at: [https://twitter-classifier.dodevca.com](https://twitter-classifier.dodevca.com)

## Installation and Usage (Local Setup)
1. Clone this repository.
2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Linux/MacOS
    # OR
    venv\Scripts\activate  # For Windows
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the Flask server:
    ```bash
    python app.py
    ```
4. Access the app at `http://localhost:5000`.

> Notebook file can be run independently inside `/notebook/twitter_trending_classifier.ipynb` for model retraining or modification.

## Future Improvements
- [ ] Add real-time tweet classification using Twitter Streaming API.
- [ ] Expand slang dictionary coverage for better pre-processing.
- [ ] Develop a more comprehensive visualization dashboard.
- [ ] Implement a lightweight model serving architecture.

## Contact & Collaboration
Interested in collaborating or discussing this project?
Reach me at: [LinkedIn Profile](https://linkedin.com/in/dodevca) or visit [dodevca.com](https://dodevca.com).

## Signature
Initiated by **Dodevca**, open for collaboration and continuous refinement.
