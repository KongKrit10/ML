# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 11:23:45 2026

@author: Lab
"""
import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#load model 
loan_model = pickle.load(open('loan_model.sav','rb'))
ridingmower_model = pickle.load(open('RidingMowers_model.sav','rb'))


with st.sidebar:
    selected = option_menu(
        'Classification',
        ['Loan', "RidingMower"])
    
if(selected == 'RidingMower'):
    st.title('RidingMower Predict')
    
    Income = st.text_input('Income')
    LotSize = st.text_input('LotSize')
    ridingmower_predict = ''
    
    if st.button('Predict'):
        ridingmower_predict = ridingmower_model.predict([[
            float(Income),
            float(LotSize)
            ]])
        if ridingmower_predict[0] == 0:
            ridingmower_predict='Non Owner'
        else:
            ridingmower_predict = 'Owner'
                                 
    st.success(ridingmower_predict)
    
if(selected == 'Loan') :
    st.title('Loan Predict')
      

    person_age = st.text_input('person age')
    person_gender = st.text_input('person gender')
    person_education = st.text_input('person education')
    person_income = st.text_input('person income')
    person_emp_exp = st.text_input('person employment experience')
    person_home_ownership = st.text_input('person home ownership')
    loan_amnt = st.text_input('loan amount')
    loan_intent = st.text_input('loan intent')
    loan_int_rate = st.text_input('loan interest rate')
    loan_percent_income = st.text_input('loan percent income')

    cb_person_cred_hist_length = st.text_input('credit history length')
    credit_score = st.text_input('credit score')
    previous_loan_defaults_on_file = st.text_input('previous loan defaults on file')

    loan_predict = ''
        
        
    if st.button('Predict'):
        loan_predict = loan_model.predict([[
             
         
                    float(person_age),
                    float(person_gender),
                    float(person_education),
                    float(person_income),
                    float(person_emp_exp),
                    float(person_home_ownership),
                    float(loan_amnt),
                    float(loan_intent),
                    float(loan_int_rate),
                    float(loan_percent_income),
                    float(cb_person_cred_hist_length),
                    float(credit_score),
                    float(previous_loan_defaults_on_file)
            ]])
        if loan_predict[0] == 0:
            loan_predict='Not Accept'
        else:
                loan_predict = 'Accept'
                    
             
    st.success(loan_predict) 
            
        
