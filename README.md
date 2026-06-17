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

🌐 https://sentiment-and-urgency-detector-dqg64ccmtf28dul7pead9m.streamlit.app/

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

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sentiment & Urgency Detector</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: #f8f9fa;
            color: #212529;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }

        .container {
            width: 100%;
            max-width: 700px;
            background: #ffffff;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        }

        h1 {
            font-size: 2rem;
            font-weight: 700;
            color: #1a1e21;
            margin-bottom: 24px;
        }

        .form-group {
            margin-bottom: 20px;
        }

        label {
            display: block;
            font-size: 0.85rem;
            color: #6c757d;
            margin-bottom: 8px;
            font-weight: 500;
        }

        textarea {
            width: 100%;
            height: 120px;
            padding: 16px;
            border: 1px solid #dee2e6;
            border-radius: 8px;
            background-color: #e9ecef; /* Matching the muted blue-gray tone from the image */
            font-family: inherit;
            font-size: 1rem;
            color: #495057;
            resize: vertical;
            outline: none;
            transition: border-color 0.2s ease, background-color 0.2s ease;
        }

        textarea:focus {
            background-color: #f1f3f5;
            border-color: #ced4da;
        }

        button {
            background-color: #f1f3f5;
            color: #495057;
            border: 1px solid #ced4da;
            padding: 10px 24px;
            font-size: 0.95rem;
            border-radius: 20px; /* Rounded pill style matching the image */
            cursor: pointer;
            font-weight: 500;
            transition: all 0.2s ease;
            margin-bottom: 32px;
        }

        button:hover {
            background-color: #e2e6ea;
            border-color: #adb5bd;
        }

        .result-section {
            border-top: 1px solid #e9ecef;
            padding-top: 24px;
        }

        h2 {
            font-size: 1.5rem;
            font-weight: 600;
            color: #212529;
            margin-bottom: 16px;
        }

        .result-item {
            font-size: 1rem;
            margin-bottom: 12px;
            color: #495057;
        }

        .result-value {
            font-weight: 500;
            color: #212529;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Sentiment & Urgency Detector</h1>
    
    <div class="form-group">
        <label for="complaintInput">Enter Customer Complaint</label>
        <textarea id="complaintInput" placeholder="Type customer complaint here...">I am frustrated and nobody helped me</textarea>
    </div>
    
    <button onclick="analyzeSentiment()">Analyze</button>
    
    <div class="result-section">
        <h2>Result</h2>
        <div class="result-item">
            Sentiment: <span id="sentimentResult" class="result-value">Angry / Negative</span>
        </div>
        <div class="result-item">
            Urgency: <span id="urgencyResult" class="result-value">High</span>
        </div>
    </div>
</div>

<script>
    function analyzeSentiment() {
        const text = document.getElementById('complaintInput').value.toLowerCase().trim();
        const sentimentEl = document.getElementById('sentimentResult');
        const urgencyEl = document.getElementById('urgencyResult');

        if (text === "") {
            sentimentEl.textContent = "N/A";
            urgencyEl.textContent = "N/A";
            return;
        }

        // Mock basic client-side analysis logic for interactivity
        if (text.includes('frustrated') || text.includes('angry') || text.includes('nobody helped')) {
            sentimentEl.textContent = "Angry / Negative";
            urgencyEl.textContent = "High";
        } else if (text.includes('broken') || text.includes('urgent') || text.includes('help')) {
            sentimentEl.textContent = "Negative";
            urgencyEl.textContent = "High";
        } else if (text.includes('thanks') || text.includes('good') || text.includes('happy')) {
            sentimentEl.textContent = "Positive";
            urgencyEl.textContent = "Low";
        } else {
            sentimentEl.textContent = "Neutral";
            urgencyEl.textContent = "Medium";
        }
    }
</script>

</body>
</html>

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
