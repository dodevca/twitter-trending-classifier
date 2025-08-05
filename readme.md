# Twitter Trending Classifier — by Dodevca

A lightweight tool to classify Twitter/X posts into noise, neutral, and relevant categories using a combination of rule-based logic and Logistic Regression model.

---

## About This Project
This project automates the classification of trending Twitter/X posts to filter out irrelevant content. It combines a simple rule-based system with a Logistic Regression model to improve filtering accuracy. The application is built with Flask and integrates Google Colab notebooks for model training and experimentation.

---

## Tech Stack & Tools
| Category     | Stack                    |
|--------------|--------------------------|
| Back-end     | Flask                    |
| Notebook     | Google Colab (Jupyter)   |
| Storage      | Google Drive             |
| Front-end    | Bootstrap (basic styling)|

---

## Key Features
- Rule-based classification for Twitter/X posts.
- Simple web interface displaying classification results and prediction percentages.
- Integration with Google Colab for model retraining and adjustments.

---

## Live Demo
Access the live demo at: [https://twitter-classifier.dodevca.com](https://twitter-classifier.dodevca.com)

---

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

---

## Future Improvements
- [ ] Add real-time tweet classification using Twitter Streaming API.
- [ ] Expand slang dictionary coverage for better pre-processing.
- [ ] Develop a more comprehensive visualization dashboard.
- [ ] Implement a lightweight model serving architecture.

---

## Contact & Collaboration
Interested in collaborating or discussing this project?
Reach me at: [LinkedIn Profile](https://linkedin.com/in/dodevca) or visit [dodevca.com](https://dodevca.com).

---

## Signature
Made with structured precision by **Dodevca**