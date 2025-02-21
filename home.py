import streamlit as st

# Set page title and layout
st.set_page_config(page_title="FitSync AI", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "BMI Calculator", "Hydration Tracker", "Sleep Tracking", "Workout Plan"])

# ------------------------- Home Page -------------------------
if page == "Home":
    st.markdown(
        """
        <style>
            .hero {
                text-align: center;
                background: linear-gradient(135deg, #007bff, #0056b3);
                color: white;
                padding: 60px 20px;
                border-radius: 15px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
            }
            .hero h1 {
                font-size: 3rem;
            }
        </style>
        <div class="hero">
            <h1>Welcome to FitSync AI</h1>
            <p>Your AI-powered fitness and wellness assistant.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### Key Features", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("#### 🏋 Personalized Workouts")
        st.write("AI-driven routines tailored to your fitness level and goals.")
    with col2:
        st.markdown("#### 💧 Hydration Tracking")
        st.write("Track your daily water intake and stay hydrated.")
    with col3:
        st.markdown("#### 😴 Sleep Monitoring")
        st.write("Analyze your sleep data and improve your rest.")

# ------------------------- BMI Calculator -------------------------
elif page == "BMI Calculator":
    st.markdown("## BMI Calculator")
    weight = st.number_input("Weight (kg)", min_value=10.0, max_value=300.0, step=0.1)
    height = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, step=0.1)

    if st.button("Calculate BMI"):
        if height > 0 and weight > 0:
            bmi = weight / ((height / 100) ** 2)
            st.success(f"Your BMI is: {bmi:.2f}")
            if bmi < 18.5:
                st.warning("Underweight")
            elif 18.5 <= bmi < 24.9:
                st.success("Normal weight")
            elif 25 <= bmi < 29.9:
                st.warning("Overweight")
            else:
                st.error("Obese")

# ------------------------- Hydration Tracker -------------------------
elif page == "Hydration Tracker":
    st.markdown("## Hydration Tracker")
    weight = st.number_input("Weight (kg)", min_value=10.0, max_value=300.0, step=0.1)
    activity_level = st.selectbox("Activity Level", ["Low", "Moderate", "High"])
    climate = st.selectbox("Climate", ["Normal", "Hot"])

    if st.button("Calculate Hydration Needs"):
        base_hydration = weight * 0.033
        activity_multiplier = 1.5 if activity_level == "High" else (1.2 if activity_level == "Moderate" else 1)
        climate_multiplier = 1.3 if climate == "Hot" else 1
        total_hydration = base_hydration * activity_multiplier * climate_multiplier
        st.success(f"Recommended Hydration: {total_hydration:.2f} liters/day")

# ------------------------- Sleep Tracking -------------------------
elif page == "Sleep Tracking":
    st.markdown("## Sleep Tracking")
    sleep_hours = st.slider("How many hours did you sleep last night?", 0, 12, 7)
    if st.button("Analyze Sleep"):
        if sleep_hours < 6:
            st.warning("You are not getting enough sleep! Try to improve your sleep routine.")
        elif 6 <= sleep_hours <= 8:
            st.success("You have a good sleep pattern! Keep it up.")
        else:
            st.warning("You might be oversleeping. Aim for 7-8 hours for optimal health.")

# ------------------------- Workout Plan -------------------------
elif page == "Workout Plan":
    st.markdown("## Workout Plan")
    phase = st.selectbox("Select Phase", ["Foundation (Weeks 1-4)", "Progression (Weeks 5-8)", "Optimization (Weeks 9-12)"])
    if phase == "Foundation (Weeks 1-4)":
        st.markdown("#### Foundation Phase")
        st.write("**Focus:** Building a solid foundation of fitness.")
        st.write("**Workout Frequency:** 3 days per week.")
        st.write("**Workout Duration:** 30-45 minutes.")
    elif phase == "Progression (Weeks 5-8)":
        st.markdown("#### Progression Phase")
        st.write("**Focus:** Increasing intensity and building muscle.")
        st.write("**Workout Frequency:** 4 days per week.")
        st.write("**Workout Duration:** 45-60 minutes.")
    else:
        st.markdown("#### Optimization Phase")
        st.write("**Focus:** Reaching specific fitness goals.")
        st.write("**Workout Frequency:** 5-6 days per week.")
        st.write("**Workout Duration:** 60+ minutes.")

# ------------------------- Footer -------------------------
st.markdown(
    """
    <style>
        .footer {
            text-align: center;
            padding: 20px;
            background-color: #007bff;
            color: white;
            border-radius: 5px;
            margin-top: 30px;
        }
    </style>
    <div class="footer">
        <p>&copy; 2024 FitSync AI. All rights reserved.</p>
    </div>
    """,
    unsafe_allow_html=True
)