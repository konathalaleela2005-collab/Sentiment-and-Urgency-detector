SENTIMENT & URGENCY DETECTOR

🧠 AI-Powered Customer Support Ticket Intelligence System

<p align="center">
<b>Sentiment & Urgency Detector</b> is an AI-based system that analyzes customer support tickets to automatically detect <b>Sentiment, Urgency, and Churn Risk</b> using Large Language Models (OpenAI + Hugging Face) and triggers real-time alerts through Discord for critical issues.
</p>

---

## 📌 Submission Identity (Placement Drive)

| Field            | Details                          |
| ---------------- | -------------------------------- |
| 🏢 Organization  | Infinity Computer Solutions      |
| 📂 Category      | Service Desk                     |
| 👥 Team Number   | Team 8                           |
| 🆔 UC ID         | UC-4                             |
| 🚀 Project Title | Sentiment & Urgency Detector     |
| 🧠 Domain        | AI / LLM-Based Automation System |
| 📅 Type          | Placement Drive Submission       |

---

## 👨‍💻 Team Members

| Name    | Role                                    |
| ------- | --------------------------------------- |
| Leela   | Project Lead & System Design            |
| Mohan   | Backend Developer (FastAPI Integration) |
| Lalitha | AI/ML Engineer (OpenAI + Hugging Face)  |
| Sunitha | Testing, Documentation & UI Support     |

---

## 🌟 Project Overview

Customer support teams receive thousands of tickets daily. Many critical messages containing **anger, urgency, frustration, or cancellation intent** are often missed due to manual handling.

This results in:

* Delayed responses
* Poor customer satisfaction
* Increased customer churn
* Revenue loss

### 💡 Our Solution

The system automatically:
✔ Detects sentiment of customer messages
✔ Calculates urgency level
✔ Identifies churn-risk behavior
✔ Generates AI-based explanations
✔ Sends real-time alerts via Discord

---

## ❗ Problem Statement

Organizations face difficulty in identifying high-priority tickets among large volumes of incoming customer requests.

Manual handling leads to:

* Slow response time
* Missed urgent complaints
* Inefficient escalation process

This project solves it using **AI-driven automation and LLM intelligence**.

---

## 🚀 Live Application

🌐 https://probable-space-adventure-69qr57x9xv6jf4w6x-8502.app.github.dev/

---

## 🎥 Live Demo Video

📽️ https://drive.google.com/file/d/1l609UCGY_uJ-B57SB1o6_vdm3HbB9MO6/view?usp=sharing

---

## ✨ Key Features

### 🤖 AI Intelligence Features

* 😊 Sentiment Detection (Positive / Neutral / Negative)
* ⚡ Urgency Scoring System
* 🚨 Churn Risk Prediction
* 🧠 Explainable AI Reasoning
* 📊 Confidence Score Generation

### 🔔 Automation Features

* Discord Webhook Alerts
* Real-time Ticket Analysis
* Automatic Escalation Trigger

### 📦 System Features

* REST API (FastAPI)
* JSON Structured Output
* Streamlit UI Support

---

## 🏗️ System Architecture

```text id="arch2"
Customer Ticket Input
        │
        ▼
LLM Processing Layer (OpenAI / Hugging Face)
        │
        ├── Sentiment Analysis
        ├── Urgency Detection
        ├── Churn Risk Analysis
        │
        ▼
Risk Evaluation Engine
        │
   High Risk?
        │
     YES ▼
Discord Webhook Alert System
        │
Support Team Notification
```

---

## 🛠️ Tech Stack

* 🐍 Python
* ⚡ FastAPI
* 🤖 OpenAI API
* 🧠 Hugging Face Models
* 🌐 Streamlit
* 🔗 Discord Webhooks
* 📦 JSON Processing
* 🧰 Git & GitHub

---

## 📁 Project Structure

```text id="struct2"
Sentiment-and-Urgency-detector/
│── app.py
│── requirements.txt
│── .env
│── backend/
│── ai_model/
│── utils/
│── alerts/
└── README.md
```

---

## ⚙️ Installation Steps

### 1️⃣ Clone Repository

```bash id="clone2"
git clone https://github.com/konathalaleela2005-collab/Sentiment-and-Urgency-detector
cd Sentiment-and-Urgency-detector
```

### 2️⃣ Create Virtual Environment

```bash id="venv2"
python -m venv venv
```

### 3️⃣ Activate Environment

```bash id="act2"
venv\Scripts\activate
```

### 4️⃣ Install Dependencies

```bash id="pip2"
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

```env id="env2"
OPENAI_API_KEY=your_api_key
DISCORD_WEBHOOK_URL=your_webhook_url
ALERT_THRESHOLD=0.75
```

---

## ▶️ Run Project

```bash id="run2"
python app.py
```

OR

```bash id="stream2"
streamlit run app.py
```

---

## 📥 Sample Input

```json id="in2"
{
  "ticket": "I am extremely disappointed. If this issue is not fixed today, I will cancel my subscription."
}
```

---

## 📤 Sample Output

```json id="out2"
{
  "sentiment": "Negative",
  "sentiment_score": 0.94,
  "urgency_score": 0.91,
  "churn_risk_score": 0.88,
  "overall_risk": "High",
  "flagged": true
}
```

---

## 🚨 Discord Alert Example

🚨 HIGH PRIORITY TICKET

Risk Level: HIGH
Sentiment Score: 0.94
Urgency Score: 0.91
Churn Risk Score: 0.88

Reason:

* Negative emotional tone
* Immediate action required
* Customer may churn

---

## 📊 Business Impact

✔ Faster response to critical tickets
✔ Reduced customer churn
✔ Improved support efficiency
✔ Automated escalation system
✔ Better customer satisfaction

---

## ⚠️ Challenges Faced

* Handling ambiguous customer tone
* Prompt optimization for LLM accuracy
* Reducing false positives
* Real-time webhook integration

---

## 🔮 Future Enhancements

* 🌍 Multi-language support
* 📊 Analytics dashboard
* 📩 Email/SMS alerts
* 🤖 Fine-tuned domain model
* 📈 Sentiment trend tracking

---

## 📸 Screenshots

*(Add UI screenshots here for stronger impact)*

---

## 🏁 Conclusion

The **Sentiment & Urgency Detector** demonstrates how Artificial Intelligence can transform customer support systems by automatically prioritizing critical tickets and enabling faster decision-making through LLM-based automation.

---

<p align="center">
💼 Built for Infinity Computer Solutions Placement Drive  
</p>

<p align="center">
🚀 AI-Powered Customer Support Intelligence System  
</p>
