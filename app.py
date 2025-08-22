import streamlit as st
import requests

st.set_page_config(page_title="Spam Mail Prediction")

# --- UI Components ---
st.title("📧 Spam Mail Prediction App")
st.markdown("Enter the content of the email below:")

# Text area for user input
email_content = st.text_area("Email Content", height=200)

# Button to trigger prediction
if st.button("Predict"):
    if email_content:
        # --- API Call to Flask Backend ---
        # Note: The backend is still a Flask app, but the frontend is now Streamlit.
        try:
            # Replace with your deployed Flask API URL
            API_URL = "https://your-flask-app-url.onrender.com/predict" 
            
            response = requests.post(
                API_URL, 
                json={"content": email_content}
            )

            # --- Displaying the Prediction ---
            if response.status_code == 200:
                result = response.json().get('prediction')
                if result == "Spam":
                    st.error("🛑 This email is classified as **Spam**.")
                else:
                    st.success("✅ This email is **Not Spam**.")
            else:
                st.error("Prediction failed. Check the backend API.")
                st.json(response.json())
        except requests.exceptions.ConnectionError:
            st.error("Failed to connect to the backend. Please ensure the API is running.")
    else:
        st.warning("Please enter some email content to predict.")
