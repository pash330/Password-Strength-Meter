import streamlit as st
import re

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*()`._-=+{}[]\|;:).")
    
    # Strength Rating
    if score == 4:
        strength = "Strong"
        color = "#023e8a"
    elif score == 3:
        strength = "Moderate"
        color = "#0077b6"
    else:
        strength = "Weak"
        color = "#0096c7"
    
    return strength, score, feedback, color

# Streamlit UI with Background Shading
st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(to bottom, #6c584c, #023e8a);
            color: white;
        }
        .password-input input {
            font-size: 20px;
            text-align: center;
        }
        .suggestions {
            color: white;
            font-weight: bold;
        }
        .strength-text {
            color: white;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🔒 Password Strength Meter")
password = st.text_input("Check Password", type="password", placeholder="Check Password", key="password", help="Enter a secure password")

if password:
    strength, score, feedback, color = check_password_strength(password)
    st.markdown(f"<div class='strength-text'>**Password Strength: {strength}**</div>", unsafe_allow_html=True)
    st.progress(score / 4)
    
    if strength != "Strong":
        st.markdown("<div class='suggestions'>⚠️ Suggestions:</div>", unsafe_allow_html=True)
        for tip in feedback:
            st.markdown(f"<div class='suggestions'>- {tip}</div>", unsafe_allow_html=True)