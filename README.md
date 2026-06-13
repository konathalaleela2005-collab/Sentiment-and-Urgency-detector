PROJECT TITLEL: Sentiment and Urgency detector
PROBLEM STATEMENT:
Customer support teams receive large volumes of inbound tickets every day. Critical messages containing anger, frustration, urgency, or churn-risk indicators can be missed, leading to escalations, customer dissatisfaction, and revenue loss.

The Sentiment & Urgency Detector uses an LLM-powered classification service to analyze incoming support tickets, assign sentiment and urgency scores, detect churn-risk language, and automatically notify support teams through Discord when high-risk tickets are identified.
 TEAM MEMBERS:
1. Team Member 1 – 23U41A0526 K.LEELA SRI LAKSHMI
2. Team Member 2 – 23U41A0519 JAVVADI SUNITHA
3. Team Member 3 – 24U45A0413 ADIGARLA MOHAN
4. Team Member 4 – 23U41A4239 MASARAPU LALITHA
FEATURE IMPLEMENTATION:
Core Features:
* Analyze inbound ticket text using an LLM.
* Detect customer sentiment (Positive, Neutral, Negative).
* Calculate urgency score.
* Identify churn-risk language.
* Generate explainable reasons for classification.
* Risk threshold-based alert generation.
* Automatic Discord notifications for critical tickets.
ADDITIONAL FEATURES:
* Confidence scoring.
* JSON-based API response.
* Configurable alert thresholds.
* Ticket audit logging.
* Dashboard-ready output format
ARCHITECHTURE OVERVIEW:
                ┌─────────────────┐
                │ Customer Ticket │
                └────────┬────────┘
                         │
                         ▼
               ┌──────────────────┐
               │ Sentiment Service│
               │   (LLM Model)    │
               └────────┬─────────┘
                        │
        ┌───────────────┼────────────────┐
        ▼               ▼                ▼
 Sentiment Score  Urgency Score   Churn Risk Score
        │               │                │
        └───────┬───────┴────────┬───────┘
                ▼                ▼
         Risk Evaluation Engine
                │
      Above Threshold?
                │
         Yes ───┘
                ▼
      Discord Alert Service
                │
                ▼
      Support Team Notification

TOOLS AND TECHNOLOGIES USED:
 AI/ML:
* OpenAI GPT API (LLM Classifier)
* Prompt Engineering
 Backend:
* Python
* FastAPI / Flask
 Integration:
* Discord Webhooks
 Data Processing:
* JSON
* REST APIs
 Development Tools:
* Git
* GitHub
* VS Code
SETUP INSTRUCTION:
 1. Clone Repository
bash
git clone https://github.com/your-team/sentiment-urgency-detector.git
cd sentiment-urgency-detector
2. Create Virtual Environment
bash
python -m venv venv
 3. Activate Environment
Windows:
bash
venv\Scripts\activate
Linux/Mac:
bash
source venv/bin/activate
 4. Install Dependencies
bash
pip install -r requirements.txt
RUN INSTRUCTIONS:
 Start API Server
bash
python app.py
Test Endpoint
bash
POST /analyze-ticket
Example:
json
{
  "ticket": "I am extremely disappointed. If this issue isn't fixed today, I will cancel my subscription."
}
SAMPLE INPUT:
json
{
  "ticket": "Your service has been down for two days. Nobody is responding. If this is not resolved immediately, I will switch to another provider."
}
SAMPLE OUTPUT:
json
{
  "sentiment": "Negative",
  "sentiment_score": 0.94,
  "urgency_score": 0.91,
  "churn_risk_score": 0.88,
  "overall_risk": "High",
  "flagged": true,
  "reasons": [
    "Strong negative language detected",
    "Immediate resolution requested",
    "Customer threatens to switch provider"
  ]
}
DISCORD ALERT EXAMPLE:
text
🚨 High-Risk Customer Ticket
Risk Level: HIGH
Sentiment Score: 0.94
Urgency Score: 0.91
Churn Risk Score: 0.88
Reasons:
• Strong negative language
• Immediate action requested
• Churn intent detected
Ticket:
"Your service has been down for two days..."
AI CAPABILITY DEMONSTRATED:
 LLM-Based Classification
The system uses a Large Language Model to:
* Classify customer sentiment.
* Detect urgency levels.
* Identify churn-risk indicators.
* Generate human-readable explanations.
* Produce structured JSON outputs.
 Agent-Like Behavior
The solution autonomously:
1. Receives ticket text.
2. Analyzes customer intent.
3. Computes risk scores.
4. Makes escalation decisions.
5. Sends notifications to Discord.

ASSUMPTION AND LIMITATIONS:
Assumptions
* Ticket text is in English.
* Discord webhook is configured correctly.
* OpenAI API is available and accessible.
* Support teams monitor Discord alerts.
 Limitations:
* Accuracy depends on LLM quality.
* Sarcasm and highly ambiguous language may be misclassified.
* Non-English tickets may require translation support.
* Threshold tuning may be required for different businesses.
* LLM API costs increase with ticket volume.
DEMO VIDEO LINK:
Demo Video:
EXPECTED RCO(result of concept)
Input:Customer support ticket text
Processing: LLM evaluates sentiment, urgency, and churn-risk signals
Output:
* Sentiment score
* Urgency score
* Churn-risk score
* Explanation of reasoning
* Automatic Discord alert for high-risk tickets
Business Impact:
* Faster response to critical tickets
* Reduced customer churn
* Improved escalation management
* Better customer satisfaction and retention metrics
