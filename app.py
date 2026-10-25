
import streamlit as st

st.set_page_config(page_title="Learning Path Generator", page_icon="🎯")

st.title("🎯 Learning Path Generator")
st.write("Create your personalized learning roadmap!")

st.subheader("Tell us about your learning goal")

goal = st.text_input("What do you want to learn?", "Python Programming")

level = st.selectbox(
    "Your current skill level",
    ["Beginner", "Intermediate", "Advanced"]
)

hours = st.slider("Study hours per day", 1, 8, 2)

weeks = st.selectbox("Learning duration (weeks)", [2, 4, 6, 8, 12])

if st.button("Generate Learning Path"):
    st.success("Your learning path is ready!")
    st.header(f"Your Roadmap: {goal}")

    topics = [
        "Learn the fundamentals",
        "Understand important concepts",
        "Practise with exercises",
        "Build a mini-project",
        "Review and improve",
        "Complete a final project"
    ]

    for week in range(1, weeks + 1):
        st.subheader(f"Week {week}")
        topic_index = min((week - 1) * len(topics) // weeks, len(topics) - 1)
        st.write(f"**Focus:** {topics[topic_index]}")
        st.write(
            f"Study for {hours} hour(s) daily and practise what you learn."
        )

    st.write(f"**Current level:** {level}")
    st.balloons()
  
