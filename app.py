from flask import Flask, request, jsonify, render_template
import numpy as np
import joblib

app = Flask(__name__)

# Load the trained machine learning model
model = joblib.load('models/wine_quality_model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = [data['fixed_acidity'], data['volatile_acidity'], data['citric_acid'], 
                data['residual_sugar'], data['chlorides'], data['free_sulfur_dioxide'], 
                data['total_sulfur_dioxide'], data['density'], data['pH'], 
                data['sulphates'], data['alcohol']]
    features = np.array(features).reshape(1, -1)
    quality = model.predict(features)[0]
    return jsonify({'quality': int(quality)})

if __name__ == '__main__':
    app.run(debug=True)
