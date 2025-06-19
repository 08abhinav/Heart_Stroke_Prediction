# Model thresholds and weights from notebook
thresholds = {
    'age': 72.0,
    'avg_glucose_level': 106.58,
    'bmi': 28.2,
    'hypertension': 1,
    'heart_disease': 1,
    'smoking_status': 1
}

feature_weights = {
    'age': 0.3,
    'avg_glucose_level': 0.3,
    'bmi': 0.15,
    'hypertension': 0.15,
    'heart_disease': 0.05,
    'smoking_status': 0.05
}

def predict_stroke_risk(user_data, thresholds, feature_weights):
    score = 0
    max_score = sum(feature_weights.values())
    for feature in thresholds:
        if feature in ['age', 'avg_glucose_level', 'bmi']:
            if user_data[feature] >= thresholds[feature]:
                score += feature_weights[feature]
        else:
            if user_data[feature] == thresholds[feature]:
                score += feature_weights[feature]
    risk_percent = (score / max_score) * 100
    if risk_percent >= 35:
        return "High Risk", risk_percent
    elif 30 <= risk_percent < 35:
        return "Moderate Risk", risk_percent
    else:
        return "Low Risk", risk_percent
