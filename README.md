🚀 Employee Promotion Prediction
⭐️ Overview
This project predicts employee promotions using machine learning. It aims to assist HR departments in making data-driven and fair promotion decisions.

📌 Features
🔍 Predict promotions based on employee attributes.
🛠 Data preprocessing to handle missing values and encode categories.
🤖 Multiple ML models tested for best performance.
📊 Evaluation using accuracy, precision, recall, and F1-score.
🌐 Optional API Deployment for real-world integration.
🧪 Testing Phase
The testing phase of the Employee Promotion Prediction project involves evaluating the trained models with real employee data and ensuring that predictions are accurate and fair. Here are the steps and results from the testing process:

Testing Steps
Test Data Preparation
The test data consists of employee attributes that were not part of the training set. The model uses the following features for prediction:

Number of trainings (no_of_trainings)
Age (age)
Previous year rating (previous_year_rating)
Length of service (length_of_service)
Awards won (awards_won)
Average training score (avg_training_score)
Department (department)
Education (education)
Gender (gender)
Recruitment channel (recruitment_channel)
Region (region)
Test Predictions
The model is tested with different sets of employee data to predict whether they will be promoted or not (output 0 or 1). Below are some examples:

Input JSON 1
json
Copy
Edit
{
  "no_of_trainings": 1,
  "age": 22,
  "previous_year_rating": 2,
  "length_of_service": 1,
  "awards_won": 0,
  "avg_training_score": 50,
  "department": "Sales",
  "education": "Bachelor's",
  "gender": "f",
  "recruitment_channel": "other",
  "region": "region_5"
}
Predicted Output

json
Copy
Edit
{
  "Predicted_Study_Efficiency_Score": 0
}
Input JSON 2
json
Copy
Edit
{
  "no_of_trainings": 5,
  "age": 35,
  "previous_year_rating": 5.0,
  "length_of_service": 10,
  "awards_won": 1,
  "avg_training_score": 90,
  "department": "R&D",
  "education": "Master's & above",
  "gender": "m",
  "recruitment_channel": "sourcing",
  "region": "region_10"
}
Predicted Output

json
Copy
Edit
{
  "Predicted_Study_Efficiency_Score": 1
}
Evaluation
The model's predictions are evaluated using several metrics such as:

Accuracy: The percentage of correct predictions.
Precision: The accuracy of positive predictions.
Recall: The ability of the model to correctly identify positive samples.
F1-Score: The harmonic mean of precision and recall, providing a balance between the two.
Testing Results
Best model achieved X% accuracy, Y precision, Z recall, W F1-score.
Top influencing factors in the predictions: previous_year_rating, avg_training_score, length_of_service.
Testing Conclusion
The model is able to predict employee promotions effectively, with good performance on both precision and recall. Further testing on larger, more diverse datasets can improve generalization and fairness.

⚙️ Installation
Clone the repository:
git clone https://github.com/abigiyaelias180/machine-learning.git

Install dependencies:
pip install -r requirements.txt

Run the Jupyter Notebook for analysis or execute app.py to deploy the API.

🚀 Usage
Train Model: Run the notebook to preprocess data and train models.

Evaluate Model: Compare different algorithms and metrics.

Deploy API (Optional):
python app.py

Live Deployment: Access the deployed API here.

📈 Results
🏆 Best model: X% accuracy, Y precision, Z recall, W F1-score.
🔑 Top influencing factors: previous_year_rating, avg_training_score, length_of_service.
🔮 Future Scope
⚖️ Improve fairness in predictions.
📂 Expand dataset for better generalization.
📊 Create a dashboard for visualization.
📩 Contact
For queries, email 📧 abigiyaelias180@gmail.com or open an issue.

