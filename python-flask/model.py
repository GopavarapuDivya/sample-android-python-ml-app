import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler  
import seaborn as sns
from scipy import stats
from sklearn.ensemble import RandomForestClassifier
import pickle

df=pd.read_csv('train.csv')
del df['LoanAmount']
categorical=['Gender','Married','Dependents','Education','Self_Employed','Property_Area','Loan_Status']
numerical=['ApplicantIncome','CoapplicantIncome','Loan_Amount_Term','Credit_History']
#chi-square test
for i in range(len(categorical)):
    chi_square=stats.chi2_contingency(pd.crosstab(df[categorical[i]],df.Loan_Status))
    res=stats.chi2.pdf(3.84,chi_square[2])
    if res>0.05:
        del df[categorical[i]]
del df['Loan_ID']
#filling missing values with mode
missing=['Gender','Married','Education','Self_Employed','Loan_Amount_Term','Credit_History']
for i in missing:
    df[i]=df[i].fillna(df[i].dropna().mode()[0])
categorical_mod=['Gender','Married','Education','Self_Employed','Loan_Status']

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
for i in categorical_mod:
    df[i] = le.fit_transform(df[i])
#heat map generation
#plt.figure(figsize=(10,5))

del df['ApplicantIncome']
sns.heatmap(df.corr(),annot=True)
train=df.iloc[:,0:7]
test=df.iloc[:,-1]

#standard scaler
df[['CoapplicantIncome','Loan_Amount_Term','Credit_History']] = StandardScaler().fit_transform(df[['CoapplicantIncome','Loan_Amount_Term','Credit_History']])
df.info()
X_train,X_test,y_train,y_test=train_test_split(train.values,test.values,test_size=0.2,random_state=0)


classifier = RandomForestClassifier()
#Fitting model with trainig data
classifier.fit(X_train,y_train)
# Saving model to disk
pickle.dump(classifier, open('model.pkl','wb'))
# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
#print(model.predict([[2,3,4,5,6,7,8,9]]))


