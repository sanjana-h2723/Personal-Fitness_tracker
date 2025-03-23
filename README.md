# Personal-Fitness_tracker

The Personal Fitness Tracker is a fully web-based application built with Streamlit for enabling end-users to estimate their calorie expenditures based on their physiology and physical activity parameters. The users have to input their age, height, BMI, duration of exercise, heart rate, and some other lifestyle information. Based on all this information, the users get a systematic data-driven prediction of their calories burned.

**Key Features:**
1.An interactive sidebar soothing the user to input parameters is the basis for the application.
2.Calorie expenditure prediction using a Random Forest Regressor.
3.For reference, shows user parameters.
4.Visually depicts the estimated predicted calorie expenditure over time.
5.Comparison with similar data points from the dataset.
6.Analytical views on hydration level, age, exercise duration, heartbeat, and body temperature concerning the other users.

**Usage**
1.Start the Streamlit app:
      streamlit run app.py
2.Open your browser to the shown localhost link.
3.Change the input parameters from the sidebar and know your predicted calorie burn and insight. 

**Dependencies**
It requires these in the project:
   *streamlit
   *pandas
   *plotly
   *scikit-learn

To install them manually, execute:
   pip install streamlit pandas plotly scikit-learn 

**Dataset**
1.The application uses exercise.csv and calories.csv datasets.
2.These datasets have been merged using User_ID, and are pre-processed for training the ML model.

**Machine Learning Model**
1.Uses a Random Forest Regressor with the following parameters :
    *n_estimators=1000
    *max_features=3
    *max_depth=6
2.Model trained on various user parameters and predictor would be calorie expenditure based on input 


**Author**
[Sanjana H]
