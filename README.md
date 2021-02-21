# loan-prediction : Predict Loan Eligibility for Dream Housing Finance company
Analytics Vidhya Hackathon: Loan Predicting Practice Problem

## Overview
Dream Housing Finance company deals in all kinds of home loans. They have presence across all urban, semi urban and rural areas. Customer first applies for home loan and after that company validates the customer eligibility for loan.
Company wants to automate the loan eligibility process (real time) based on customer detail provided while filling online application form. These details are Gender, Marital Status, Education, Number of Dependents, Income, Loan Amount, Credit History and others. To automate this process, they have provided a dataset to identify the customers segments that are eligible for loan amount so that they can specifically target these customers. 

## Data Dictionary
| Variable | Description |
| --- | --- |
|Loan_ID | Unique Loan ID |
| Gender | Male/ Female |
| Married | Applicant married (Y/N) |
| Dependents | Number of dependents |
| Education | Applicant Education (Graduate/ Under Graduate) |
| Self_Employed | Self employed (Y/N) |
| ApplicantIncome | Applicant income |
| CoapplicantIncome | Co-Applicant income |
| LoanAmount | Loan amount in thousands |
| Loan_Amount_Term | Term of loan in months |
| Credit_History | credit history meets guidelines |
| Property_Area | Urban/ Semi Urban/ Rural |
| Loan_Status | (Target) Loan approved (Y/N) |

## Evaluation Metrics
Accuracy

## Add-Ons
Developed a streamlit app what would make predictions for us (refer to app.py)
For downloading streamlit library, use the following command:
```
pip install streamlit
```

And to run a streamlit app (app.py) go to the directory where app.py is present (model.pkl shall also be present in the same folder), and run the following command:
```
streamlit run app.py
```
