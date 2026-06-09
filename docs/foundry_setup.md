# Microsoft Foundry Setup

## Overview

CertForge Sentinel uses Microsoft Foundry to define and test a reasoning agent for cybersecurity certification readiness planning.

The Foundry project includes:

- A Microsoft Foundry resource
- A Foundry project named `certforge-sentinel`
- An agent named `CertForge-Sentinel`
- A deployed model: `gpt-oss-120b`
- A deployed embedding model: `text-embedding-3-small`
- A Foundry IQ knowledge base created from synthetic project files

## Agent Configuration

The Foundry agent is configured with instructions for a multi-agent workflow.

Specialized agent roles include:

1. Learner Profile Agent
2. Learning Path Curator Agent
3. Study Plan Generator Agent
4. Assessment Agent
5. Readiness Evaluator Agent
6. Manager Insights Agent

The agent is instructed to use synthetic data only, avoid confidential information, avoid real employee data, and clearly communicate that readiness recommendations are guidance requiring human oversight.

## Foundry IQ Knowledge Base

A Foundry IQ knowledge base was created using the following synthetic project files:

- `docs/knowledge_base/cybersecurity_certification_guide.md`
- `docs/knowledge_base/readiness_rubric.md`
- `docs/knowledge_base/team_learning_report.md`
- `data/synthetic_team_data.json`

These files are synthetic and contain no real employee data, customer data, credentials, confidential information, or personally identifiable information.

## Current Integration Status

The Foundry IQ knowledge base was successfully created and processed.

During testing, the agent returned an invalid parameter error when the knowledge base was attached directly to the agent using the available model deployment. The same model deployment worked successfully in the direct model playground, and the agent worked successfully after the knowledge base was detached.

Current working configuration:

- Foundry agent instructions: active
- Model deployment: active
- Foundry IQ knowledge base: created and processed
- Knowledge base attachment to agent: detached for stable live testing
- Streamlit prototype: uses the same synthetic data and knowledge structure locally

## Design Intent

The intended architecture is:

User input  
↓  
CertForge Sentinel Foundry Agent  
↓  
Foundry IQ synthetic knowledge base  
↓  
Multi-agent readiness reasoning  
↓  
Certification readiness report

The current prototype demonstrates this architecture through:

- Foundry agent configuration
- Synthetic knowledge base creation
- Local Streamlit workflow
- Documented multi-agent responsibilities
- Synthetic data and safety controls

## Safety Controls

CertForge Sentinel follows these guardrails:

- Use synthetic data only
- Do not use real employee or customer data
- Do not include credentials or confidential information
- Do not invent official exam versions, official exam weights, or proprietary materials
- Do not invent team-level insights unless team data is provided
- Clearly state assumptions
- Treat readiness recommendations as guidance, not final authority
