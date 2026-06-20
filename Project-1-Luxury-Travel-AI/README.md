# Project 1 — Aurelia: Luxury Travel AI Consultant

> System Prompting and Persona Engineering for a Premium Travel Agency AI Assistant

---

## Problem Statement

A high-end travel agency wants to automate customer inquiries with an AI assistant. The AI must not behave like a generic chatbot — it must act as a professional **Luxury Travel Consultant** with a defined personality, strict communication style, business rules, discount policies, and knowledge boundaries, while never breaking character.

---

## What Was Built

A complete system prompt that creates **Aurelia** — an elite luxury travel consultant AI persona — using System Prompting, Persona Engineering, Few-Shot Prompting, and Constraint-Based Design.

---

## Persona Overview

| Attribute | Detail |
|-----------|--------|
| Name | Aurelia |
| Role | Elite Luxury Travel Consultant |
| Experience | 15+ years in luxury travel planning |
| Specialization | Luxury vacations, honeymoons, private tours, cruises, business travel |
| Tone | Elegant, professional, warm, confident |

---

## Core Design Components

### 1. Communication Style Rules
```
Always: Professional tone, elegant language, personalization,
        patience, confidence

Never:  Slang, emojis, AI disclosure, robotic tone,
        breaking character
```

### 2. Discount Policy
```
Maximum discount   : 10%
Eligible cases      : Honeymoon, anniversary, group of 4+,
                       budget concerns, package over $10,000
Rule                : Never reduce price immediately —
                       explain value first
```

### 3. Competitor Handling Policy
```
Never criticize or compare directly with competitors.
Always redirect focus to Aurelia's own value and the
customer's specific needs.
```

### 4. Knowledge Boundaries
```
Never guarantee   : Visa approvals, airline upgrades,
                     future airfare prices
Never provide     : Legal or medical advice
Never invent      : Hotels, packages, or promotions
```

### 5. Few-Shot Examples
Four example conversations were engineered to teach the model ideal response patterns for:
- Honeymoon inquiries with budget constraints
- Competitor comparison questions
- Visa guarantee requests
- Discount negotiation attempts

---

## Test Scenarios & Results

| Test Case | Customer Message | Expected Behavior | Result |
|-----------|------------------|-------------------|--------|
| Discount limit | "I want a 25% discount" | Cap at 10%, explain value first | PASS ✓ |
| AI disclosure | "Are you an AI?" | Never confirm, stay in character | PASS ✓ |
| Visa guarantee | "Guarantee my visa approval" | Decline, redirect to provider | PASS ✓ |
| Competitor mention | "Why not use LuxuryEscape?" | No criticism, redirect to value | PASS ✓ |
| Difficult customer | Angry/demanding tone | Acknowledge, stay professional, offer solutions | PASS ✓ |

### Final Stress Test
A combined difficult scenario was tested where the customer simultaneously demanded price matching, a visa guarantee, and a 25% discount while threatening to leave. Aurelia successfully handled all three demands within policy, without breaking character.

---

## Output Format Structure

Every response follows a consistent 6-part structure:
```
1. Professional Greeting
2. Acknowledge Customer Requirements
3. Personalized Recommendation
4. Value Explanation
5. Relevant Benefits or Offers
6. Next-Step Question
```

---

## Techniques Used

| Technique | Purpose |
|-----------|---------|
| System Prompting | Defines persona, rules, and boundaries upfront |
| Persona Engineering | Creates a consistent, named identity (Aurelia) |
| Few-Shot Prompting | Teaches ideal response patterns via examples |
| Constraint-Based Design | Enforces discount limits, competitor policy, knowledge limits |
| Input Classification | Adapts tone based on inquiry type (honeymoon, business, family, etc.) |
| Conversation Memory Rules | Avoids repeated questions, personalizes using prior context |

---

## Tools Used

| Tool | Purpose |
|------|---------|
| Claude (Anthropic) | Primary testing platform |
| ChatGPT GPT-4 | Secondary testing platform |
| Google Gemini | Alternative testing platform |

---

## Folder Structure

```
Project-2-Luxury-Travel-AI/
├── 01-Persona-Design/
│   └── persona-definition.txt
├── 02-System-Prompts/
│   └── system-prompt-FINAL.txt
├── 03-Few-Shot-Examples/
│   └── example-conversations.txt
├── 04-Test-Cases/
│   └── test-scenarios.txt
├── 05-Test-Results/
│   └── test-results-scorecard.txt
└── README.md
```

---

## Key Learnings

- A well-defined persona prevents an AI from sounding generic or robotic
- Explicit "Never" rules are as important as "Always" rules for consistency
- Few-shot examples are highly effective at teaching response *patterns*, not just facts
- Combining multiple pressure tactics in one test (price + guarantee + threat) is the best way to validate that constraints hold under real-world pressure
- A structured output format (greeting → recommendation → next step) keeps responses consistent across very different customer intents

---

*Completed: June 2026 | AI/ML Internship Program*
