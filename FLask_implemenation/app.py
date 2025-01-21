from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the trained model
with open('stroke_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Extract input values
            age = float(request.form['age'])
            avg_glucose_level = float(request.form['avg_glucose_level'])
            bmi = float(request.form['bmi'])
            gender = request.form['gender']
            hypertension = int(request.form['hypertension'])
            heart_disease = int(request.form['heart_disease'])
            ever_married = request.form['ever_married']
            work_type = request.form['work_type']
            residence_type = request.form['residence_type']
            smoking_status = request.form['smoking_status']

            # Organize input for the model as a DataFrame
            input_data = pd.DataFrame([[
                age, avg_glucose_level, bmi, gender, hypertension, 
                heart_disease, ever_married, work_type, residence_type, smoking_status
            ]], columns=['age', 'avg_glucose_level', 'bmi', 'gender', 'hypertension',
                          'heart_disease', 'ever_married', 'work_type', 'Residence_type', 'smoking_status'])

            # Make prediction
            prediction = model.predict(input_data)[0]
            prediction_text = "Stroke Risk: Yes" if prediction == 1 else "Stroke Risk: No"

            return render_template('index.html', prediction_text=prediction_text)
        except Exception as e:
            return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
