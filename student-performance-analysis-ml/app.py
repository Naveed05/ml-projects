from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the saved model
model = joblib.load('linear_regression_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    math = float(request.form['math'])
    reading = float(request.form['reading'])
    writing = float(request.form['writing'])

    input_features = np.array([[math, reading, writing]])
    prediction = model.predict(input_features)[0]
    
    return render_template('index.html', prediction_text=f'Predicted Score: {prediction:.2f}')

if __name__ == '__main__':
    app.run(debug=True)
