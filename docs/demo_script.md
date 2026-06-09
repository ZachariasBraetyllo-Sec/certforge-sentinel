# CertForge Sentinel Demo Script

## Demo Goal

Show how CertForge Sentinel uses a multi-agent workflow to help cybersecurity teams plan certification study paths, assess readiness, and generate manager-level insights using synthetic data.

## Opening

CertForge Sentinel is a multi-agent cybersecurity certification readiness system built for the Microsoft Agents League Hackathon Reasoning Agents track.

It helps learners and managers answer a practical question:

"Is this learner ready for their certification goal, and what should they do next?"

## Demo Flow

### 1. Open the App

Open the CertForge Sentinel Streamlit interface.

Point out that the app uses synthetic learner profiles and synthetic knowledge sources only.

### 2. Select a Learner

Choose one synthetic learner profile.

Recommended demo profile:

L-1001 - Junior SOC Analyst preparing for Security+

This learner has:

- A practice score below 70
- Limited study hours
- Several weak topics
- Moderate meeting load
- Low focus time

### 3. Run the Multi-Agent Readiness Review

Click:

Run Multi-Agent Readiness Review

### 4. Walk Through the Agent Outputs

Highlight each output section:

#### Learning Path Curator Agent

Explain that this agent identifies the learner's priority certification topics and weak areas.

#### Study Plan Generator Agent

Explain that this agent creates a short-term study plan based on workload, focus time, and weak topics.

#### Assessment Agent

Explain that this agent generates practice questions connected to the learner's weak domains.

#### Readiness Evaluator Agent

Explain the readiness verdict: Ready, Almost Ready, or Not Yet Ready.

#### Manager Insights Agent

Explain how the manager insight summarizes workload risk and recommended support actions.

### 5. Show a Contrasting Learner

Switch to a stronger learner profile.

Recommended demo profile:

L-1003 - Cloud Security Trainee preparing for AZ-900

Run the review again and show how the readiness verdict, risk level, and recommendations change.

## Microsoft IQ Explanation

CertForge Sentinel is designed to use Foundry IQ as the grounding layer.

The planned Foundry IQ knowledge sources are:

- Cybersecurity certification guide
- Certification readiness rubric
- Team learning report
- Synthetic learner data

Foundry IQ grounds learning recommendations, practice questions, and readiness explanations in approved synthetic documentation.

## Safety Explanation

All data is synthetic.

The project does not use:

- Real employee data
- Customer data
- Personal information
- Credentials
- Confidential documents

Readiness recommendations are guidance only and should include human oversight.

## Closing

CertForge Sentinel demonstrates how multi-agent reasoning can support cybersecurity certification planning by coordinating learner profiling, study planning, assessment generation, readiness evaluation, and manager insights in one workflow.
