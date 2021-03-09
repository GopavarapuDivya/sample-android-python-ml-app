import pandas as pd
from flask import Flask,request,jsonify
from sklearn.preprocessing import StandardScaler  
import pickle
import requests,ssl
from flask_cors import CORS
app=Flask(__name__)
CORS(app)
model = pickle.load(open('model.pkl', 'rb'))
@app.route('/predict',methods=['POST'])
def predict():
    gender=request.json['Gender']
    
    married=request.json['Married']
    
    education=request.json['Education']
    
    self_employed=request.json['Self_Employed']
    
    applicantincome=float(request.json['CoapplicantIncome'])
    
    loanamountterm=float(request.json['Loan_Amount_Term'])
    
    credithistory=float(request.json['Credit_History'])
    
    datavalues=[[gender,married,education,self_employed,applicantincome,loanamountterm,credithistory]]
    
    data=pd.dataframe(datavalues,columns=['Gender','Married','Education','Self_Employed','CoapplicantIncome','Loan_Amount_Term','Credit_History'])
    
    categorical_mod=['Gender','Married','Education','Self_Employed']

    from sklearn.preprocessing import LabelEncoder
    le=LabelEncoder()
    for i in categorical_mod:
        data[i] = le.fit_transform(data[i])
        
    data[['CoapplicantIncome','Loan_Amount_Term','Credit_History']] = StandardScaler().fit_transform(data[['CoapplicantIncome','Loan_Amount_Term','Credit_History']])
    res=model.predict(data)
    return str(res[0])

if __name__=="__main__":
    app.run(debug=True)
    

