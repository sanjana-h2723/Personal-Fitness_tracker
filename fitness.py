import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import time
import warnings
import logging

# Configure logging
logging.basicConfig(level=logging.CRITICAL)

# Suppress warnings
warnings.filterwarnings('ignore')


st.markdown("<div class='background left-align'><h2>Personal Fitness Tracker</h2></div>", unsafe_allow_html=True)
st.markdown("<div class='background left-align'>In this WebApp you will be able to observe your predicted calories burned in your body. Pass your parameters such as `Age`, `Gender`, `BMI`, etc., into this WebApp and then you will see the predicted value of kilocalories burned.</div>", unsafe_allow_html=True)

st.sidebar.header("User Input Parameters: ")

def user_input_features():
    user_age = st.sidebar.slider("Age: ", 10, 100, 30)
    user_height = st.sidebar.slider("Height (cm): ", 100, 220, 170)
    user_bmi = st.sidebar.slider("BMI: ", 15, 40, 20)
    duration = st.sidebar.slider("Duration (min): ", 0, 35, 15)
    heart_rate = st.sidebar.slider("Heart Rate: ", 60, 130, 80)
    body_temp = st.sidebar.slider("Body Temperature (C): ", 36, 42, 38)
    gender_selection = st.sidebar.radio("Gender: ", ("Male", "Female"))
    activity_type = st.sidebar.selectbox("Activity Type: ", ["Running", "Cycling", "Swimming", "Walking"]) 
    fitness_level = st.sidebar.selectbox("Fitness Level: ", ["Beginner", "Intermediate", "Advanced"])  
    hydration_level = st.sidebar.slider("Hydration Level (liters): ", 0.0, 5.0, 2.0)  
    sleep_quality = st.sidebar.slider("Sleep Quality (1-10): ", 1, 10, 7)  
    stress_level = st.sidebar.slider("Stress Level (1-10): ", 1, 10, 5)  
    exercise_intensity = st.sidebar.slider("Exercise Intensity (1-10): ", 1, 10, 5)
    diet_quality = st.sidebar.slider("Diet Quality (1-10): ", 1, 10, 7)
    step_count = st.sidebar.slider("Step Count: ", 0, 30000, 10000)

    gender = 1 if gender_selection == "Male" else 0

    # Use column names to match the training data
    data_model = {
        "Age": user_age,
        "Height": user_height,
        "BMI": user_bmi,
        "Duration": duration,
        "Heart_Rate": heart_rate,
        "Body_Temp": body_temp,
        "Gender_male": gender,
        "Activity_Type": activity_type,
        "Fitness_Level": fitness_level,
        "Hydration_Level": hydration_level,
        "Sleep_Quality": sleep_quality,
        "Stress_Level": stress_level,
        "Exercise_Intensity": exercise_intensity,
        "Diet_Quality": diet_quality,
        "Step_Count": step_count
    }

    features = pd.DataFrame(data_model, index=[0])
    return features

user_data = user_input_features()

st.write("---")
st.header("Your Parameters: ")
progress_text = st.empty()
bar_indicator = st.progress(0)
for i in range(100):
    bar_indicator.progress(i + 1)
    time.sleep(0.01)
st.write(user_data)

# Load and preprocess data
calories_data = pd.read_csv("calories.csv")
exercise_data = pd.read_csv("exercise.csv")

exercise_u_data = exercise_data.merge(calories_data, on="User_ID")
exercise_u_data.drop(columns="User_ID", inplace=True)

train_d, test_d = train_test_split(exercise_u_data, test_size=0.2, random_state=1)

# Add BMI column to both training and test sets
for data in [train_d, test_d]:
    data["BMI"] = data["Weight"] / ((data["Height"] / 100) ** 2)
    data["BMI"] = round(data["BMI"], 2)

# Prepare the training and testing sets
required_col = ["Gender", "Age", "Height", "BMI", "Duration", "Heart_Rate", "Body_Temp", "Calories", "Activity_Type", "Fitness_Level", "Hydration_Level", "Sleep_Quality", "Stress_Level", "Exercise_Intensity", "Diet_Quality", "Step_Count"]
missing_col = [col for col in required_col if col not in train_d.columns]

if missing_col:
    st.write("Missing columns: ", missing_col)
else:
    train_d = train_d[required_col]
    test_d = test_d[required_col]

    train_d = pd.get_dummies(train_d, drop_first=True)
    test_d = pd.get_dummies(test_d, drop_first=True)

    # Separate features and labels
    X_train = train_d.drop("Calories", axis=1)
    y_train = train_d["Calories"]

    X_test = test_d.drop("Calories", axis=1)
    y_test = test_d["Calories"]

    # Train the model
    random_r = RandomForestRegressor(n_estimators=1000, max_features=3, max_depth=6)
    random_r.fit(X_train, y_train)

    # Align prediction data columns with training data
    user_data = user_data.reindex(columns=X_train.columns, fill_value=0)

    # Make prediction
    calorie_prediction = random_r.predict(user_data)

    st.write("---")
    st.header("Prediction: ")
    progress_text = st.empty()
    bar_indicator = st.progress(0)
    for i in range(100):
        bar_indicator.progress(i + 1)
        time.sleep(0.01)
    
    st.write(f"{round(calorie_prediction[0], 2)} **kilocalories**")

    # Create a line graph of predicted calories over time
    calories_over_time = pd.DataFrame({
        "Time": range(1, 11),
        "Predicted Calories": [calorie_prediction[0] + (i * 0.5) for i in range(1, 11)]  # Example data
    })

    figure = px.line(calories_over_time, x="Time", y="Predicted Calories", title="Predicted Calories Burned Over Time")
    st.plotly_chart(figure)

    st.write("---")
    st.header("Similar Results: ")
    progress_text = st.empty()
    bar_indicator = st.progress(0)
    for i in range(100):
        bar_indicator.progress(i + 1)
        time.sleep(0.01)

    # Find similar results based on predicted calories
    calorie_range = [calorie_prediction[0] - 10, calorie_prediction[0] + 10]
    matching_data = exercise_u_data[(exercise_u_data["Calories"] >= calorie_range[0]) & (exercise_u_data["Calories"] <= calorie_range[1])]
    st.write(matching_data.sample(5))

    st.write("---")
    st.header("General Information: ")

    boolean_hydration = (exercise_u_data["Hydration_Level"] < user_data["Hydration_Level"].values[0]).tolist()
    st.write("You have a higher hydration level than", round(sum(boolean_hydration) / len(boolean_hydration), 2) * 100, "% of other people.")

    # Boolean logic for age, duration, etc., compared to the user's input
    bool_age = (exercise_u_data["Age"] < user_data["Age"].values[0]).tolist()
    bool_duration = (exercise_u_data["Duration"] < user_data["Duration"].values[0]).tolist()
    bool_body_temp = (exercise_u_data["Body_Temp"] < user_data["Body_Temp"].values[0]).tolist()
    bool_heart_rate = (exercise_u_data["Heart_Rate"] < user_data["Heart_Rate"].values[0]).tolist()

    st.write("You are older than", round(sum(bool_age) / len(bool_age), 2) * 100, "% of other people.")
    st.write("Your exercise duration is higher than", round(sum(bool_duration) / len(bool_duration), 2) * 100, "% of other people.")
    st.write("You have a higher heart rate than", round(sum(bool_heart_rate) / len(bool_heart_rate), 2) * 100, "% of other people during exercise.")
    st.write("You have a higher body temperature than", round(sum(bool_body_temp) / len(bool_body_temp), 2) * 100, "% of other people during exercise.")