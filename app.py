import json
from pathlib import Path

import streamlit as st


DATA_PATH = Path("data/synthetic_team_data.json")


def load_learners():
    with DATA_PATH.open("r", encoding="utf-8") as file:
        return json.load(file)


def get_readiness_status(practice_score, hours_studied, weak_topics, focus_hours):
    weak_topic_count = len(weak_topics)

    if practice_score >= 80 and hours_studied >= 20 and weak_topic_count <= 1:
        return "Ready", "The learner appears ready for a final review or certification attempt."

    if practice_score >= 70 and hours_studied >= 12 and weak_topic_count <= 3:
        return "Almost Ready", "The learner is close, but should complete targeted review before attempting the exam."

    return "Not Yet Ready", "The learner needs more structured study time and foundational review before attempting the exam."


def get_risk_level(practice_score, hours_studied, meeting_hours, focus_hours, weak_topics):
    risk_points = 0

    if practice_score < 70:
        risk_points += 2
    elif practice_score < 80:
        risk_points += 1

    if hours_studied < 12:
        risk_points += 2
    elif hours_studied < 20:
        risk_points += 1

    if meeting_hours > 18:
        risk_points += 1

    if focus_hours < 10:
        risk_points += 1

    if len(weak_topics) > 2:
        risk_points += 1

    if risk_points >= 5:
        return "High"
    if risk_points >= 3:
        return "Medium"
    return "Low"


def build_study_plan(learner):
    weak_topics = learner["weak_topics"]
    preferred_slot = learner["preferred_learning_slot"]

    plan = [
        f"Day 1: Review core concepts for {learner['certification_goal']} during the {preferred_slot.lower()}.",
        f"Day 2: Focus on weak topic: {weak_topics[0] if weak_topics else 'general review'}.",
        "Day 3: Complete short practice question set and review missed answers.",
        f"Day 4: Focus on weak topic: {weak_topics[1] if len(weak_topics) > 1 else 'scenario-based practice'}.",
        "Day 5: Complete a timed practice assessment.",
        "Day 6: Review incorrect answers and summarize weak concepts in your own words.",
        "Day 7: Complete final readiness check and decide whether to schedule the exam or continue review.",
    ]

    return plan


def generate_practice_questions(certification_goal, weak_topics):
    primary_topic = weak_topics[0] if weak_topics else "security fundamentals"

    return [
        f"What is one key concept a learner should understand about {primary_topic} for {certification_goal}?",
        f"How would you apply {primary_topic} in a realistic cybersecurity workplace scenario?",
        f"What mistake might a learner make when studying {primary_topic}, and how should they correct it?",
    ]


st.set_page_config(
    page_title="CertForge Sentinel",
    page_icon="🛡️",
    layout="wide",
)

st.title("CertForge Sentinel 🛡️")
st.subheader("Multi-agent cybersecurity certification readiness system")

st.write(
    "CertForge Sentinel uses a multi-agent workflow to help cybersecurity learners and managers "
    "plan certification study paths, assess readiness, and identify support needs using synthetic data."
)

st.divider()

learners = load_learners()
learner_options = {
    f"{learner['learner_id']} - {learner['role']} preparing for {learner['certification_goal']}": learner
    for learner in learners
}

selected_label = st.selectbox("Choose a synthetic learner profile", list(learner_options.keys()))
selected_learner = learner_options[selected_label]

st.header("Learner Profile Agent")

col1, col2 = st.columns(2)

with col1:
    role = st.text_input("Role", selected_learner["role"])
    certification_goal = st.text_input("Certification Goal", selected_learner["certification_goal"])
    practice_score = st.slider("Practice Score Average", 0, 100, selected_learner["practice_score_avg"])
    hours_studied = st.slider("Hours Studied", 0, 40, selected_learner["hours_studied"])

with col2:
    meeting_hours = st.slider("Meeting Hours Per Week", 0, 40, selected_learner["meeting_hours_per_week"])
    focus_hours = st.slider("Focus Hours Per Week", 0, 40, selected_learner["focus_hours_per_week"])
    preferred_slot = st.selectbox(
        "Preferred Learning Slot",
        ["Morning", "Afternoon", "Evening"],
        index=["Morning", "Afternoon", "Evening"].index(selected_learner["preferred_learning_slot"]),
    )
    weak_topics_input = st.text_input(
        "Weak Topics",
        ", ".join(selected_learner["weak_topics"]),
    )

weak_topics = [topic.strip() for topic in weak_topics_input.split(",") if topic.strip()]

run_button = st.button("Run Multi-Agent Readiness Review")

if run_button:
    learner = {
        "role": role,
        "certification_goal": certification_goal,
        "practice_score_avg": practice_score,
        "hours_studied": hours_studied,
        "meeting_hours_per_week": meeting_hours,
        "focus_hours_per_week": focus_hours,
        "preferred_learning_slot": preferred_slot,
        "weak_topics": weak_topics,
    }

    readiness_status, readiness_reason = get_readiness_status(
        practice_score,
        hours_studied,
        weak_topics,
        focus_hours,
    )

    risk_level = get_risk_level(
        practice_score,
        hours_studied,
        meeting_hours,
        focus_hours,
        weak_topics,
    )

    study_plan = build_study_plan(learner)
    practice_questions = generate_practice_questions(certification_goal, weak_topics)

    st.success("Multi-agent readiness review complete.")

    st.header("Agent Workflow Output")

    st.subheader("1. Learning Path Curator Agent")
    st.write(
        f"For a {role} preparing for {certification_goal}, the priority learning areas are: "
        f"{', '.join(weak_topics) if weak_topics else 'core certification domains'}."
    )

    st.subheader("2. Study Plan Generator Agent")
    for item in study_plan:
        st.markdown(f"- {item}")

    st.subheader("3. Assessment Agent")
    for question in practice_questions:
        st.markdown(f"- {question}")

    st.subheader("4. Readiness Evaluator Agent")
    st.metric("Readiness Verdict", readiness_status)
    st.write(readiness_reason)

    st.subheader("5. Manager Insights Agent")
    st.metric("Readiness Risk Level", risk_level)
    st.write(
        f"This learner has {meeting_hours} meeting hours and {focus_hours} focus hours per week. "
        "Managers should protect focus time and prioritize support for weak domains."
    )

    st.subheader("Foundry IQ Grounding Plan")
    st.info(
        "This prototype is designed to connect to Foundry IQ using synthetic certification guides, "
        "readiness rubrics, and team learning reports as grounded knowledge sources."
    )

st.divider()

st.header("Microsoft Foundry Integration Status")

st.markdown(
    """
    CertForge Sentinel is configured with a Microsoft Foundry agent named **CertForge-Sentinel**.

    The project also includes a Foundry IQ knowledge base created from synthetic project files:

    - Cybersecurity certification guide
    - Certification readiness rubric
    - Team learning report
    - Synthetic learner/team data

    During testing, the Foundry agent worked successfully with the deployed model. The Foundry IQ knowledge base was successfully created and processed, but its direct attachment to the agent produced an invalid-parameter error with the available model configuration. For stable demo purposes, the local Streamlit prototype mirrors the same multi-agent workflow using synthetic data and rule-based logic.
    """
)

st.info(
    "All learner profiles, team data, and knowledge sources in this project are synthetic and created for demonstration only."
)