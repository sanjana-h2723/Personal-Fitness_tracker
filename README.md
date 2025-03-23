# Personal-Fitness_tracker

The Personal Fitness Tracker is a fully web-based application built with Streamlit for enabling end-users to estimate their calorie expenditures based on their physiology and physical activity parameters. The users have to input their age, height, BMI, duration of exercise, heart rate, and some other lifestyle information. Based on all this information, the users get a systematic data-driven prediction of their calories burned.

<br>**Key Features:**
<br>1.An interactive sidebar soothing the user to input parameters is the basis for the application.
<br>2.Calorie expenditure prediction using a Random Forest Regressor.
<br>3.For reference, shows user parameters.
<br>4.Visually depicts the estimated predicted calorie expenditure over time.
<br>5.Comparison with similar data points from the dataset.
<br>6.Analytical views on hydration level, age, exercise duration, heartbeat, and body temperature concerning the other users.

<br>**Usage**
<br>1.Start the Streamlit app:
      <br>streamlit run app.py
<br>2.Open your browser to the shown localhost link.
<br>3.Change the input parameters from the sidebar and know your predicted calorie burn and insight. 

<br>**Dependencies**
<br>It requires these in the project:
  <br> *streamlit
   <br>*pandas
  <br> *plotly
  <br> *scikit-learn

<br>To install them manually, execute:
   <br>pip install streamlit pandas plotly scikit-learn 

<br>**Dataset**
<br>1.The application uses exercise.csv and calories.csv datasets.
<br>2.These datasets have been merged using User_ID, and are pre-processed for training the ML model.

<br>**Machine Learning Model**
<br>1.Uses a Random Forest Regressor with the following parameters :
    <br>*n_estimators=1000
    <br>*max_features=3
    <br>*max_depth=6
<br>2.Model trained on various user parameters and predictor would be calorie expenditure based on input 
<br>

<br>**Author**
<br>[Sanjana H]
