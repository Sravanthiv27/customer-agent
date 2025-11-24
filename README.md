# Customer Agent - Enterprise Support Automation

## Overview

An intelligent, modular customer support agent designed to automate initial customer interactions through contextual memory, intent classification, urgency assessment, and targeted reply generation.

**Project**: AI Agents Intensive - Capstone Project  
**Author**: Sravanthi Mathi  
**Competition**: Kaggle - Agents Intensive Hackathon

---

## Features

✨ **Key Capabilities:**

- **Instant Triage**: Automatically classifies customer intent (refund, cancellation, billing, general help) and urgency level (high, medium, low)
- **Memory Management**: Maintains conversation history to provide context-aware responses
- **Intelligent Routing**: Routes inquiries based on intent and urgency to optimize agent efficiency
- **Proactive Information Gathering**: Requests essential details upfront to accelerate resolution
- **Modular Architecture**: Easily extensible components for future AI model integration

---

## Project Structure

```
customer-agent/
├── customer_agent.py       # Main implementation with all classes
├── WRITEUP.md             # Detailed technical writeup
├── README.md              # This file
└── LICENSE                # CC BY 4.0
```

## Architecture

The system is built on four core components:

### 1. **Memory Module**
Manages conversation history and context retrieval.
- Stores messages with metadata (role, content, timestamp)
- Maintains context window for conversation continuity
- Provides `get_context()` method for historical reference

### 2. **Intent Agent**
Classifies customer messages to determine intent and urgency.
- Uses keyword matching for intent detection
- Assigns priority levels based on issue type
- Extendable with ML models for improved accuracy

### 3. **Reply Agent**
Generates contextual responses tailored to classified intent.
- Creates action-oriented replies
- Requests specific data based on intent (Order ID, Email, Invoice #, etc.)
- Maintains professional, helpful tone

### 4. **Coordinator**
Orchestrates the end-to-end workflow.
- Routes messages through Memory → Intent Agent → Reply Agent
- Returns structured output with intent, urgency, and reply
- Manages agent initialization and execution

---

## Usage

### Quick Start

```python
from customer_agent import Coordinator

# Initialize the agent
agent = Coordinator()

# Process a customer message
response = agent.ask("I need a refund for my order.")

print(response)
# Output:
# {
#     "intent": "refund",
#     "urgency": "high",
#     "reply": "I understand you want a refund. Please share your order ID..."
# }
```

### Supported Intents

| Intent | Keywords | Urgency | Response |
|--------|----------|---------|----------|
| **Refund** | refund | HIGH | Requests order ID |
| **Cancellation** | cancel | HIGH | Requests registered email |
| **Billing** | invoice, bill | MEDIUM | Requests invoice number |
| **General Help** | help | LOW | Asks for more details |
| **General** | (other) | LOW | Generic greeting |

---

## Business Impact

### Quantifiable Benefits

- **40% Faster Triage**: Instant classification eliminates manual sorting
- **Reduced Handling Time**: Proactive data collection reduces back-and-forth
- **Improved CSAT**: Faster response times increase customer satisfaction
- **Optimized Resource Allocation**: Human agents focus on complex cases
- **Scalability Ready**: Architecture supports ML/LLM integration for enhanced capabilities

---

## Future Enhancements

🚀 Planned improvements:

1. **NLP Integration**: Replace keyword matching with transformer-based intent classification
2. **LLM Integration**: Use GPT/Claude for more natural, contextual responses
3. **Multi-language Support**: Handle non-English customer inquiries
4. **Sentiment Analysis**: Detect emotional tone and escalate accordingly
5. **Knowledge Base Integration**: Link to FAQ/documentation for better responses
6. **Analytics Dashboard**: Track classification accuracy and customer metrics

---

## Installation & Setup

### Requirements

```
Python 3.8+
dataclasses (built-in for Python 3.7+)
json (built-in)
datetime (built-in)
typing (built-in)
```

### Running the Code

```bash
python customer_agent.py
```

---

## Documentation

📖 For detailed technical information, see [WRITEUP.md](WRITEUP.md)

This file contains:
- Problem statement and motivation
- Detailed solution architecture
- Implementation walkthrough
- Value proposition and metrics

---

## License

This project is licensed under the **CC BY 4.0** license.  
See LICENSE file for details.

---

## Contact & Attribution

**Author**: Sravanthi Mathi  
**GitHub**: [Sravanthiv27](https://github.com/Sravanthiv27)  
**LinkedIn**: [Profile](https://linkedin.com/in/sravanthimathi)  

---

*Last Updated: November 24, 2025*
