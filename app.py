from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

# Load the trained model and vectorizer (make sure these files are in the correct directory)
model = pickle.load(open('./predict/spam_mail_model.pkl', 'rb'))
vectorizer = pickle.load(open('./predict/vectorizer.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    email_content = data['content']
    
    # Transform the input using the loaded vectorizer
    transformed_input = vectorizer.transform([email_content])
    
    # Predict using the loaded model
    prediction = model.predict(transformed_input)
    
    # Return the result ('Spam' or 'Not Spam')
    result = 'Spam' if prediction[0] == 0 else 'Not Spam'
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)
