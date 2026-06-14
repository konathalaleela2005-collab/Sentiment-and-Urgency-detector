import streamlit as st
from textblob import TextBlob

st.title("Sentiment & Urgency Detector")

message = st.text_area("Enter Customer Complaint")

if st.button("Analyze"):

    sentiment_score = TextBlob(message).sentiment.polarity

    # Sentiment detection
    if sentiment_score < 0:
        sentiment = "Angry / Negative"
    elif sentiment_score == 0:
        sentiment = "Neutral"
    else:
        sentiment = "Positive"

    # Urgency detection
    urgent_words = [
        "urgent",
        "immediately",
        "angry",
        "terrible",
        "issue",
        "failed",
        "frustrated"
    ]

    urgency = "Low"

    for word in urgent_words:
        if word in message.lower():
            urgency = "High"

    st.subheader("Result")
    st.write("Sentiment:", sentiment)
    st.write("Urgency:", urgency)