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
    gender = request.json['Gender']
    
    if gender == 'Male':
        gender_int=1
    else:
        gender_int=0
    
    married = request.json['Married']
    
    if married == 'Yes':
        married_int = 1
    else:
        married_int = 0
    
    education = request.json['Education']
    
    if education == 'Graduate':
        education_int = 1
    else:
        education_int = 0
    
    self_employed = request.json['Self_Employed']
    
    if self_employed == 'Yes':
        self_employed_int = 1
    else:
        self_employed_int = 0
    #print(request.json.values())
    applicantincome = request.json['CoapplicantIncome']
    
    loanamountterm = request.json['Loan_Amount_Term']
    
    credithistory = request.json['Credit_History']
    
    datavalues = [[gender_int,married_int,education_int,self_employed_int,applicantincome,loanamountterm,credithistory]]
    
    data = pd.DataFrame(datavalues,columns=['Gender','Married','Education','Self_Employed','CoapplicantIncome','Loan_Amount_Term','Credit_History'])   
#   data[['CoapplicantIncome','Loan_Amount_Term','Credit_History']] = StandardScaler().fit_transform(data[['CoapplicantIncome','Loan_Amount_Term','Credit_History']])    
    res = model.predict(data)
    output = str(res[0])

    if output == "1":
        res_str = "Eligible for loan"
    else:
        res_str = "Not Eligible for Loan"        
    return res_str

if __name__=="__main__":
    app.run(debug=True)
    

