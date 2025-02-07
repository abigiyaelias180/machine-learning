from fastapi import FastAPI, HTTPException
import pandas as pd
import joblib
from pydantic import BaseModel

app = FastAPI()

# Load the trained model
model_path = "employee_promotion_model.pkl"
model = joblib.load(model_path)

# Define expected categorical columns
CATEGORICAL_COLUMNS = [
    "department", "education", "gender", "recruitment_channel", "region"
]

# Define possible categorical values (update based on training data)
CATEGORY_MAPPING = {
    "department": ["Finance", "HR", "Legal", "Operations", "Procurement", "R&D", "Sales & Marketing", "Technology"],
    "education": ["Below Secondary", "Bachelor's", "Master's & above"],
    "gender": ["m", "f"],
    "recruitment_channel": ["referred", "sourcing", "other"],
    "region": [f"region_{i}" for i in range(1, 35)]  # Adjust based on dataset
}

class EmployeeData(BaseModel):
    no_of_trainings: int
    age: int
    previous_year_rating: float
    length_of_service: int
    awards_won: int
    avg_training_score: float
    department: str
    education: str
    gender: str
    recruitment_channel: str
    region: str

@app.post("/predict")
def predict(data: EmployeeData):
    try:
        # Convert input to DataFrame
        input_df = pd.DataFrame([data.dict()])
        
        # One-hot encode categorical features
        for col in CATEGORICAL_COLUMNS:
            for category in CATEGORY_MAPPING[col]:
                input_df[f"{col}_{category}"] = int(input_df[col] == category)
        
        # Drop original categorical columns
        input_df.drop(columns=CATEGORICAL_COLUMNS, inplace=True)
        
        # Ensure column alignment with the trained model
        expected_columns = model.feature_names_in_
        input_df = input_df.reindex(columns=expected_columns, fill_value=0)
        
        # Debugging: Print processed input
        print("Processed Input Data:")
        print(input_df)
        
        # Make prediction
        prediction = model.predict(input_df)
        
        return {"promotion_prediction": int(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
