import streamlit as st

st.set_page_config(page_title="Strength Training Challenge", layout="wide")

st.title("💪 30-Day Strength Training Challenge")
st.write("Choose your level and follow the plan. Remember to consult your doctor before starting any new exercise program.")

levels = ["Beginner", "Intermediate", "Advanced"]
level = st.radio("Select Difficulty Level", levels)

if level == "Beginner":
    st.subheader("Beginner Plan")
    st.table([
        ["Day 1", "Squats", "3", "10"],
        ["Day 1", "Push-ups", "3", "AMRAP"],
        ["Day 1", "Plank", "3", "30 sec"],
        ["Day 2", "Rest", "-", "-"],
    ])
elif level == "Intermediate":
    st.subheader("Intermediate Plan")
    st.table([
        ["Day 1", "Squats", "3", "12"],
        ["Day 1", "Push-ups", "3", "10"],
        ["Day 1", "Dumbbell Rows", "3", "10"],
        ["Day 2", "Rest / Light Cardio", "-", "-"],
    ])
else:
    st.subheader("Advanced Plan")
    st.table([
        ["Day 1", "Barbell Squats", "4", "8"],
        ["Day 1", "Bench Press", "4", "8"],
        ["Day 1", "Deadlifts", "3", "5"],
        ["Day 2", "Rest / Active Recovery", "-", "-"],
    ])

st.success("Good luck! Stay consistent and keep pushing! 💪")
