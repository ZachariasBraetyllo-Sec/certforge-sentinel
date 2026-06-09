# CertForge Sentinel Architecture

## Overview

CertForge Sentinel is designed as a multi-agent cybersecurity certification readiness system.

The system helps cybersecurity learners and managers understand certification goals, study plans, readiness risks, and support needs using synthetic learner data and synthetic knowledge sources.

## High-Level Flow

Learner Profile Input  
↓  
Learner Profile Agent  
↓  
Learning Path Curator Agent  
↓  
Study Plan Generator Agent  
↓  
Assessment Agent  
↓  
Readiness Evaluator Agent  
↓  
Manager Insights Agent  
↓  
Final Certification Readiness Report

## Agent Responsibilities

### Learner Profile Agent

The Learner Profile Agent reviews the learner's role, certification goal, current practice score, hours studied, meeting load, focus hours, preferred learning slot, and weak topics.

Primary responsibilities:

- Summarize learner context
- Identify readiness factors
- Identify workload constraints
- Surface missing or unclear information

### Learning Path Curator Agent

The Learning Path Curator Agent maps the learner's role and certification goal to relevant learning domains.

Primary responsibilities:

- Recommend certification domains
- Prioritize weak topics
- Use synthetic certification guidance
- Explain why topics were selected

### Study Plan Generator Agent

The Study Plan Generator Agent converts the learner's readiness profile into a practical study plan.

Primary responsibilities:

- Create a short-term study schedule
- Account for workload and focus time
- Emphasize weak topics
- Include review checkpoints

### Assessment Agent

The Assessment Agent generates practice questions based on the learner's certification goal and weak topics.

Primary responsibilities:

- Generate topic-aligned practice questions
- Connect questions to weak domains
- Support readiness review
- Avoid unsupported or overly specific claims

### Readiness Evaluator Agent

The Readiness Evaluator Agent determines whether the learner is Ready, Almost Ready, or Not Yet Ready.

Primary responsibilities:

- Apply the synthetic readiness rubric
- Evaluate practice score
- Evaluate study hours
- Evaluate weak topics
- Explain the readiness verdict
- Recommend the next step

### Manager Insights Agent

The Manager Insights Agent provides team-level support guidance using synthetic team data.

Primary responsibilities:

- Summarize readiness risk
- Identify workload concerns
- Recommend manager support actions
- Highlight focus time needs
- Keep insights privacy-conscious

## Microsoft IQ Integration Plan

CertForge Sentinel is designed to use Foundry IQ as its grounding layer.

Foundry IQ will be used to retrieve information from synthetic knowledge sources, including:

- Cybersecurity certification guide
- Certification readiness rubric
- Team learning report
- Synthetic learner data

The goal is to ground learning recommendations, practice questions, and readiness explanations in approved synthetic documentation.

## Current Prototype Architecture

The current prototype uses Streamlit and local synthetic data to demonstrate the workflow.

Streamlit UI  
↓  
Synthetic learner JSON data  
↓  
Rule-based prototype logic  
↓  
Multi-agent style output sections

## Planned Foundry Architecture

The planned Foundry-enabled version will use Microsoft Foundry and Foundry IQ to support agent reasoning and grounded retrieval.

Streamlit UI  
↓  
Microsoft Foundry Agent Workflow  
↓  
Foundry IQ Knowledge Sources  
↓  
Specialized Agent Outputs  
↓  
Final Readiness Report

## Data Sources

All data sources are synthetic and created for demonstration only.

Current data sources:

- `data/synthetic_team_data.json`
- `docs/knowledge_base/cybersecurity_certification_guide.md`
- `docs/knowledge_base/readiness_rubric.md`
- `docs/knowledge_base/team_learning_report.md`

## Safety and Responsible AI

CertForge Sentinel follows these safety principles:

- Use synthetic data only
- Do not use real employee or customer data
- Do not include credentials or confidential information
- Clearly communicate readiness as guidance, not a final authority
- Include human oversight for certification and workforce decisions
- Avoid overstating certainty
- Explain reasoning and assumptions
