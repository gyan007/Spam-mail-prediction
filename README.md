# Spam Mail Prediction API

This is a simple Flask-based web application that predicts whether an email is **Spam** or **Not Spam (Ham)**. The app uses a pre-trained machine learning model to classify email content based on the text entered by the user.

## Project Structure

spam_mail_prediction/
│
├── app.py # Main Flask application (backend)
├── templates/
│ └── index.html # The HTML file for the frontend
├── predict/
│ ├── spam_mail_model.pkl # Trained spam detection model
│ └── vectorizer.pkl # Vectorizer used for transforming email content
├── requirements.txt # List of Python dependencies (Flask, scikit-learn, etc.)
└── README.md # Project documentation

## Features

- **Spam Classification**: Classifies email content as either **Spam** or **Not Spam** using a machine learning model.
- **User-friendly Interface**: A simple web page where users can input email content and receive predictions.
- **API**: A POST API to process email content and return the prediction (Spam/Not Spam).

## Installation

To get started, clone this repository and install the necessary dependencies:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/spam-mail-prediction.git
    cd spam-mail-prediction
    ```

2. **Install the required dependencies**:
    - First, create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
    - Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. **Place the trained model and vectorizer files**:
    Ensure the `spam_mail_model.pkl` and `vectorizer.pkl` files are placed in the `predict/` folder.

## Usage

1. **Run the Flask app**:
    - Start the Flask server by running the following command:
    ```bash
    python app.py
    ```

2. **Access the application**:
    - Open your web browser and go to `http://127.0.0.1:5000/` to access the web interface.
    - Enter the email content in the text box and click **Predict** to see if the email is **Spam** or **Not Spam**.

3. **API Usage**:
    - The `/predict` route accepts a **POST** request with JSON data containing the `content` field (email text).
    - Example request:
    ```json
    {
        "content": "Congratulations, you've won a $1,000,000 prize! Click here to claim it."
    }
    ```
    - The response will contain the prediction:
    ```json
    {
        "prediction": "Spam"
    }
    ```

## Dependencies

- **Flask**: A micro web framework for Python used to serve the application.
- **scikit-learn**: A machine learning library used for training the spam detection model and vectorizer.
- **Other dependencies**: Install all required libraries by running `pip install -r requirements.txt`.

## Model

The spam detection model used in this project is a machine learning model that has been trained on a dataset of labeled emails (spam vs. not spam). It uses text vectorization (via `CountVectorizer` or `TfidfVectorizer`) and a classification algorithm (such as Naive Bayes or Logistic Regression) to predict the category of the email.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to fork this project, open issues, or submit pull requests for any improvements or bug fixes.

## Contact

For any questions or inquiries, please feel free to contact Gyan Thakur at gyanthakurthakur@gmail.com.

