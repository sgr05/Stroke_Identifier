import joblib
import streamlit as st
from os import path
import pandas as pd

st.title("Am I at risk of having a stroke?")

filename = "stroke_model.pkl"
predictor_model = joblib.load(path.join("model", filename))


def change_format(age, height, weight, work, smoking, glucose, gender, married, residence, hypertension, heart_disease):

    bmi= (weight*10000)/(height*height)

    if hypertension:
        hypertension=1
    else:
        hypertension=0

    if heart_disease:
        heart_disease=1
    else:
        heart_disease=0

    if married:
        married="yes"
    else:
        married="No"

    if (work=="Never Worked"):
        work="Never_worked"
    elif (work=="Children"):
        work="children"
    elif (work=="Goverment Job"):
        work="Govt_job"
    elif (work=="Self Employed"):
        work="Self-employed"

    if (smoking=="Never Smoked"):
        smoking="never smoked"
    elif (smoking=="Formerly Smoked"):
        smoking="formerly smoked"
    elif (smoking=="Smokes"):
        smoking="smokes"

    input_values = [age, glucose, bmi, gender, hypertension, heart_disease, married, work, residence, smoking]
    column_names= ['age', 'avg_glucose_level', 'bmi', 'gender', 'hypertension','heart_disease', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']
    # create DataFrame using the input values.
    input_data = pd.DataFrame([input_values], columns= column_names)

    return input_data

def reset():
    age==None 
    height==None 
    weight==None 
    work==None
    smoking==None 
    glucose==None
    gender==None 
    married==None 
    residence==None
    hypertension==None 
    heart_disease==None


col1, col2 = st.columns(2)

with col1:
    age = st.number_input( "Let us know your age", value=None, placeholder="Enter your age...", label_visibility = "collapsed", min_value=0, max_value=123)
    height = st.number_input( "Let us know your height", value=None, placeholder="Enter your height in cms...", label_visibility = "collapsed", min_value=0, max_value=272)
    weight = st.number_input( "Let us know your weight", value=None, placeholder="Enter your weight in kgs...", label_visibility = "collapsed", min_value=0, max_value=635)
    work = st.selectbox("Let us know your age", ("Never Worked", "Children", "Private","Goverment Job","Self Employed"), index = None, placeholder="Select your work type", label_visibility = "collapsed")
    smoking = st.selectbox("Let us know your smoking habit", ("Never Smoked", "Formerly Smoked", "Smokes", "Unknown"), index = None,placeholder="Select your smoking habit",label_visibility = "collapsed" )
    glucose = st.number_input( "Let us know your sugar level", value=None, placeholder="Enter your average blood sugar", label_visibility = "collapsed", min_value=0, max_value=2656)


with col2:
    gender = st.radio("Select your gender", ["Male", "Female"], horizontal=True, index=None)
    married = st.checkbox("I am/was married")
    residence = st.radio("Select your residence type", ["Rural", "Urban"], horizontal=True, index=None)    
    hypertension = st.checkbox("I have Hypertension")
    heart_disease = st.checkbox("I have a Heart Disease")
    # if st.button("Reset"):            # working on othis feature. 
    #     reset()



if st.button("Predict"):
    if((age==None) or (height==None) or (weight==None) or (work==None) or
       (smoking==None) or (glucose==None) or (gender==None) or (married==None) or
       (residence==None) or (hypertension==None) or (heart_disease==None)):
        st.write("Please fill all the fields.")
    else:
        user_data = change_format(age, height, weight, work, smoking, glucose, gender, married, residence, hypertension, heart_disease)
        # pred = predictor_model.predict(np.array([i_values]))
        pred = predictor_model.predict(user_data)
        #st.write("The flower is :", pred[0])
        if (pred[0]==0):
            st.write("No Risk")
        else:
            st.write("you are at risk.")
        
    
    