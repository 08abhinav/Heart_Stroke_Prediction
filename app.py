from flask import Flask, render_template, request, jsonify
from mlModel import predict_stroke_risk
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict')
def pedict():
    return render_template('predict.html')

@app.route('/predict-stroke', methods=['POST'])
def predict():
    try:
        user_data = {
            'age': float(request.form['age']),
            'avg_glucose_level': float(request.form['avg_glucose_level']),
            'bmi': float(request.form['bmi']),
            'hypertension': int(request.form['hypertension']),
            'heart_disease': int(request.form['heart_disease']),
            'smoking_status': int(request.form['smoking_status'])
        }
        
        risk_category, risk_percent = predict_stroke_risk(user_data)
        return jsonify({
            'risk_category': risk_category,
            'risk_percent': round(risk_percent, 2)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
