# CertForge Sentinel Project Plan

## Goal

CertForge Sentinel is a multi-agent certification readiness system for cybersecurity teams. It helps learners and managers understand certification goals, study plans, readiness risks, and next steps using synthetic data and grounded learning materials.

## Challenge Alignment

This project is built for the Microsoft Agents League Hackathon Reasoning Agents track.

It aligns with the challenge by demonstrating:

- Multi-agent system design
- Role-based certification planning
- Grounded learning recommendations
- Synthetic learner and team data
- Readiness assessment
- Manager-level insight generation
- Microsoft Foundry and Foundry IQ integration

## Target Scenario

A cybersecurity team wants to prepare junior analysts and IT professionals for role-relevant certifications while balancing workload, weak topics, and realistic study capacity.

Example learner roles:

- Junior SOC Analyst
- Help Desk Technician transitioning into cybersecurity
- Cloud Security Trainee
- Security Operations Intern

Example certification goals:

- SC-900
- AZ-900
- Security+
- Google Cybersecurity Certificate

## Multi-Agent Architecture

### 1. Learner Profile Agent

Reviews the learner's role, certification goal, study availability, workload, current practice score, and weak topics.

### 2. Learning Path Curator Agent

Maps the learner's role and certification goal to relevant domains, topics, and study priorities.

### 3. Study Plan Generator Agent

Creates a realistic study plan based on available hours, focus time, meeting load, and deadline.

### 4. Assessment Agent

Generates practice questions from approved synthetic learning materials.

### 5. Readiness Evaluator Agent

Determines whether the learner is Ready, Almost Ready, or Not Yet Ready.

### 6. Manager Insights Agent

Summarizes team readiness, risk areas, and recommended support actions.

## Microsoft IQ Layer

CertForge Sentinel is designed to use Foundry IQ as the required Microsoft IQ layer.

Foundry IQ will ground the agent workflow in synthetic certification guidance documents, readiness rubrics, study recommendations, and team learning summaries.

## Synthetic Data

All demo data is synthetic and created only for this hackathon project.

The project will not include:

- Real employee data
- Real customer data
- Personal information
- Credentials
- Confidential company data
- Internal proprietary documents

## MVP Features

The minimum viable version will include:

- Streamlit interface
- Synthetic learner profile selector
- Certification goal selector
- Workload and study availability inputs
- Multi-agent style output sections
- Learning path recommendation
- Study plan
- Practice questions
- Readiness verdict
- Manager insight summary
- Documentation of agent roles and data sources

## Stretch Goals

Potential future improvements include:

- Microsoft Foundry agent integration
- Foundry IQ knowledge source connection
- Cited answers from synthetic knowledge documents
- Team readiness dashboard
- Exportable readiness report
- Evaluation test cases
- Telemetry or trace examples
- Hosted deployment story

## Success Criteria

The project will be successful if it can clearly demonstrate:

- A learner or manager entering certification readiness information
- Multiple specialized agents contributing to the result
- A grounded learning path
- A realistic study plan
- A readiness decision with explanation
- A team-level insight summary
- Safe use of synthetic data only
