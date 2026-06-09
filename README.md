# CertForge Sentinel 🛡️

**A multi-agent cybersecurity certification readiness system built for the Microsoft Agents League Hackathon.**

CertForge Sentinel helps cybersecurity teams plan, track, and assess certification readiness using a multi-agent workflow. The system is designed for junior SOC analysts, help desk professionals transitioning into security, and cloud/security learners preparing for certifications such as SC-900, AZ-900, Security+, or cybersecurity fundamentals programs.

## Hackathon Track

**Reasoning Agents**

This project is designed for the Microsoft Agents League Hackathon Reasoning Agents track. It focuses on multi-step reasoning, agent collaboration, grounded learning recommendations, synthetic data, and clear certification readiness decisions.

## Project Goal

Organizations often need to help employees prepare for role-relevant certifications while balancing real workloads, skill gaps, and team readiness goals.

CertForge Sentinel turns learner profiles and synthetic team data into:

* Role-based learning paths
* Practical study schedules
* Grounded practice questions
* Readiness assessments
* Manager-level team insights
* Clear next-step recommendations

## Multi-Agent Workflow

CertForge Sentinel uses a multi-agent design with specialized responsibilities:

1. **Learner Profile Agent**
   Reviews the learner's role, target certification, available study time, current practice score, and weak topics.

2. **Learning Path Curator Agent**
   Maps the learner's goal to relevant certification domains and study topics using approved synthetic knowledge sources.

3. **Study Plan Generator Agent**
   Creates a realistic study schedule based on workload, focus time, and deadline.

4. **Assessment Agent**
   Generates practice questions grounded in approved synthetic certification materials.

5. **Readiness Evaluator Agent**
   Determines whether the learner is Ready, Almost Ready, or Not Yet Ready based on practice score, study time, and topic confidence.

6. **Manager Insights Agent**
   Summarizes team-level readiness, risk areas, and recommended support actions using synthetic team data.

## Microsoft IQ Integration

This project is designed to integrate **Foundry IQ** as the grounding layer for certification guidance, study materials, readiness rubrics, and practice questions.

All knowledge sources and demo data are synthetic and created for hackathon demonstration purposes only.

## Planned Tech Stack

* Microsoft Foundry
* Foundry IQ
* Python
* Streamlit
* GitHub
* GitHub Copilot

## Synthetic Data Notice

This project uses synthetic learner profiles, synthetic team workload signals, and synthetic certification guidance documents. It does not use real employee data, customer data, confidential information, credentials, or personally identifiable information.

## Disclaimer

CertForge Sentinel is an educational hackathon project. It is intended to demonstrate multi-agent reasoning and certification readiness planning. It does not replace official certification guidance, employer training policies, or professional judgment.
