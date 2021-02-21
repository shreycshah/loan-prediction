import pickle
import streamlit as st
import time

pickle_in=open('model.pkl','rb')
classifier=pickle.load(pickle_in)

@st.cache

def prediction(Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area):
    
    if Gender=="Male":
        Gender=0
    else:
        Gender=1
    
    if Married=="Yes":
        Married=1
    else:
        Married=0

    if Dependents=="3+":
        Dependents=3

    if Education=="Graduate":
        Education=1
    else:
        Education=0

    if Self_Employed=="Yes":
        Self_Employed=1
    else:
        Self_Employed=0

    if Credit_History=="Unknown":
        Credit_History=2
    elif Credit_History=="Yes":
        Credit_History=1
    else:
        Credit_History=0
    
    if Property_Area=="Urban":
        Property_Area=0
    elif Property_Area=="Rural":
        Property_Area=1
    else:
        Property_Area=2    
        
    Debt_Income_Ratio=(ApplicantIncome+CoapplicantIncome)/LoanAmount
    
    pred=classifier.predict([[Gender, Married, Dependents, Education, Self_Employed,ApplicantIncome, CoapplicantIncome, LoanAmount,Loan_Amount_Term, Credit_History, Property_Area,Debt_Income_Ratio]])

    # if prediction==0:
    #     pred="rejected"
    # else:
    #     pred="aprooved!"
    
    return pred

if __name__=='__main__':

    st.markdown("<h1 style='text-align: center; color: red;'>Loan Eligibility Prediction ML App</h1>", unsafe_allow_html=True)
    
    Gender=st.radio('Gender',("Male","Female"))
    Married=st.radio("Are you married?",("Yes","No"))
    Dependents=st.radio("Number. of Dependents",(0,1,2,"3+"))
    Education=st.radio("Education",("Graduate","Not Graduate"))
    Self_Employed=st.radio("Are you self employed?",("Yes","No"))
    ApplicantIncome=st.number_input("Applicant's Income in INR")
    CoapplicantIncome=st.number_input("Co-Applicant's Income in INR")
    LoanAmount=st.number_input("Loan Amount in thousands")
    Loan_Amount_Term=st.number_input("Term of loan in months")
    Credit_History=st.radio("Does credit history meet guidlines?",("Yes","No","Unknown"))
    Property_Area=st.radio("Area of Owned Property",("Urban","Rural","Semiurban"))

    result=""

    if st.button("Predict"):
        result=prediction(Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area)
        with st.spinner('Processing Request...'):
             time.sleep(1.5)
        if result==1:
            st.balloons()
            st.success("We are glad to inform you that your loan application has been approoved!")
        else:
            st.error("We regret to inform you that your application has been rejected!")
        
    

        