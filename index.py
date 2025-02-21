import streamlit as st

# Set page title
st.set_page_config(page_title="FitSync AI - Your Fitness Journey", layout="wide")

# Hero Section
st.markdown(
    """
    <style>
        .hero {
            text-align: center;
            background: linear-gradient(135deg, #007bff, #0056b3);
            color: white;
            padding: 50px 20px;
            border-radius: 10px;
        }
        .hero a {
            display: inline-block;
            padding: 10px 20px;
            background: white;
            color: #007bff;
            text-decoration: none;
            border-radius: 5px;
            font-weight: bold;
            margin-top: 10px;
        }
        .hero a:hover {
            background: #e0e0e0;
        }
    </style>
    <div class="hero">
        <h1>Transform Your Body, Empower Your Life</h1>
        <p>AI-powered fitness and nutrition plans designed for you.</p>
        <a href="#">Start Your Journey</a>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# About Section
st.header("About FitSync AI")
st.write("We leverage cutting-edge AI to personalize your fitness experience, helping you achieve your goals faster and more efficiently.")

st.markdown("---")

# Features Section
st.header("Key Features")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🏋 Personalized Workouts")
    st.write("AI-driven routines tailored to your fitness level and goals.")

with col2:
    st.markdown("### 🍎 Smart Nutrition")
    st.write("Custom meal plans designed to support your health and fitness journey.")

with col3:
    st.markdown("### 📊 Progress Tracking")
    st.write("Monitor your achievements and stay motivated with our AI assistant.")

st.markdown("---")

# Contact Form
st.header("Get In Touch")
st.write("For inquiries, support, or partnership opportunities, please reach out to our team.")

with st.form(key="contact_form"):
    name = st.text_input("Name", "").strip()
    email = st.text_input("Email", "").strip()
    message = st.text_area("Message", "").strip()
    submit = st.form_submit_button("Submit")

    if submit:
        if name and email and message:
            st.success(f"Thank you {name}! Your message has been received.")
        else:
            st.error("Please fill in all the fields before submitting.")

st.markdown("---")

# Footer
st.markdown(
    """
    <style>
        .footer {
            text-align: center;
            padding: 20px;
            background-color: #343a40;
            color: white;
            border-radius: 5px;
        }
    </style>
    <div class="footer">
        <p>&copy; 2024 FitSync AI. All rights reserved.</p>
    </div>
    """,
    unsafe_allow_html=True
)