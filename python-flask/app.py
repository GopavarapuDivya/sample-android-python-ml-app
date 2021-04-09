import pandas as pd
from sklearn.preprocessing import StandardScaler  
from sklearn.preprocessing import LabelEncoder
import pickle
from flask_cors import CORS
from flask import Flask,request,render_template
app=Flask(__name__)
CORS(app)
model = pickle.load(open('model.pkl', 'rb'))
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/form')
def form():
    return render_template('form.html')

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
    
    data=pd.DataFrame(datavalues,columns=['Gender','Married','Education','Self_Employed','CoapplicantIncome','Loan_Amount_Term','Credit_History'])
    
    categorical_mod=['Gender','Married','Education','Self_Employed']

    le=LabelEncoder()
    for i in categorical_mod:
        data[i] = le.fit_transform(data[i])
        
    data[['CoapplicantIncome','Loan_Amount_Term','Credit_History']] = StandardScaler().fit_transform(data[['CoapplicantIncome','Loan_Amount_Term','Credit_History']])
    res=model.predict(data)
    output=str(res[0])

    if output==0:
        res_str="Eligible for loan"
    else:
        res_str="Not Eligible for Loan"
        
    return res_str
if __name__=="__main__":
    app.run(debug=True)
    

