"""Enterprise Customer Support Agent with Memory and Module Intelligence
AI Agents Intensive - Capstone Project
"""

import json
from datetime import datetime
from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class Memory:
    """Manages conversation memory and history"""
    messages: List[Dict] = field(default_factory=list)
    max_history: int = 20
    
    def add(self, role: str, content: str):
        """Add a message to memory"""
        self.messages.append({
            "role": role,
            "content": content,
            "time": datetime.now().isoformat()
        })
        if len(self.messages) > self.max_history:
            self.messages = self.messages[-self.max_history:]
    
    def get_context(self):
        """Get last 5 messages as context"""
        out = ""
        for m in self.messages[-5:]:
            out += f"{m['role']}: {m['content']}\n"
        return out


class IntentAgent:
    """Classifies customer intent and urgency"""
    
    def classify(self, message: str):
        """Classify message intent and urgency"""
        text = message.lower()
        
        if "refund" in text:
            return "refund", "high"
        elif "cancel" in text:
            return "cancellation", "high"
        elif "invoice" in text or "bill" in text:
            return "billing", "medium"
        elif "help" in text:
            return "general_help", "low"
        else:
            return "general", "low"


class ReplyAgent:
    """Generates contextual replies based on intent"""
    
    def create_reply(self, message: str, intent: str, urgency: str):
        """Generate appropriate reply"""
        if intent == "refund":
            return "I understand you want a refund. Please share your order ID so I can assist you further."
        elif intent == "cancellation":
            return "I can help you cancel your subscription. Kindly provide your registered email."
        elif intent == "billing":
            return "It seems you have a billing concern. Please send your invoice number for verification."
        elif intent == "general_help":
            return "Sure, I'm here to help. Could you please share more details?"
        else:
            return "Thank you for your message. How can I assist you today?"


class Coordinator:
    """Orchestrates the customer support agent workflow"""
    
    def __init__(self):
        self.intent_agent = IntentAgent()
        self.reply_agent = ReplyAgent()
        self.memory = Memory()
    
    def ask(self, message: str):
        """Process customer message and return response"""
        # Add user message to memory
        self.memory.add("user", message)
        
        # Classify intent
        intent, urgency = self.intent_agent.classify(message)
        
        # Generate reply
        reply = self.reply_agent.create_reply(message, intent, urgency)
        
        # Store reply in memory
        self.memory.add("agent", reply)
        
        # Return structured output
        return {
            "intent": intent,
            "urgency": urgency,
            "reply": reply
        }
