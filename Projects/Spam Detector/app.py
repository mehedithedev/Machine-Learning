from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

app = Flask(__name__)

# Sample dataset creation
data = pd.DataFrame({
    'text': [
        'Win money now!', 'Hi, how are you?', 'Claim your prize', 'Important meeting tomorrow',
        'Get a loan now', 'Can we catch up later?', 'Free vacation, click here!',
        'Your account has been compromised', 'Congratulations, you won!', 'Please find the report attached'
    ],
    'label': ['spam', 'ham', 'spam', 'ham', 'spam', 'ham', 'spam', 'ham', 'spam', 'ham']
})

# Convert labels to binary (1 for spam, 0 for ham)
data['label'] = data['label'].map({'spam': 1, 'ham': 0})

# Vectorize text
vectorizer = CountVectorizer(stop_words='english')
X = vectorizer.fit_transform(data['text'])
y = data['label']

# Train Naive Bayes model
nb_model = MultinomialNB()
nb_model.fit(X, y)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the text from the form
    email_text = request.form['email_text']
    
    # Vectorize the user input
    email_vec = vectorizer.transform([email_text])
    
    # Predict using the trained model
    prediction = nb_model.predict(email_vec)[0]
    
    # Convert prediction to human-readable format
    result = 'Spam' if prediction == 1 else 'Not Spam'
    
    return render_template('index.html', email_text=email_text, prediction=result)

if __name__ == '__main__':
    app.run(debug=True)