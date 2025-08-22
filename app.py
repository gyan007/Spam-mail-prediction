import streamlit as st
import pickle
import os

# Set page title and a brief description
st.set_page_config(page_title="Spam Mail Prediction")
st.title("📧 Spam Mail Prediction App")
st.markdown("Enter the content of the email below:")

# --- Load the Model and Vectorizer ---
# Adjust the paths to your model files if they are not in the same directory
try:
    model_path = os.path.join(os.path.dirname(__file__), 'predict', 'spam_mail_model.pkl')
    vectorizer_path = os.path.join(os.path.dirname(__file__), 'predict', 'vectorizer.pkl')
    
    model = pickle.load(open(model_path, 'rb'))
    vectorizer = pickle.load(open(vectorizer_path, 'rb'))
    
except FileNotFoundError:
    st.error("Error: Model files not found. Please ensure 'spam_mail_model.pkl' and 'vectorizer.pkl' are in the 'predict' folder.")

# --- UI Components and Prediction Logic ---

# Text area for user input
email_content = st.text_area("Email Content", height=200, help="Type the email text here to check if it's spam.")

# Predict button
if st.button("Predict"):
    if email_content:
        with st.spinner("Analyzing email..."):
            # Transform the input using the loaded vectorizer
            transformed_input = vectorizer.transform([email_content])
            
            # Predict using the loaded model
            prediction = model.predict(transformed_input)
            
            # Display the result
            if prediction[0] == 0:
                st.error("🛑 This email is classified as **Spam**.")
            else:
                st.success("✅ This email is **Not Spam**.")
    else:
        st.warning("Please enter some email content to predict.")
