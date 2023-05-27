from flask import request, jsonify, Flask
import flask
import numpy as np
import traceback
import pickle
import pandas as pd

app = Flask(__name__)

@app.route('/')
def welcome():
   return "Welcome! Please enter your information to ensure your loan approval."

@app.route('/predict', methods=['POST','GET'])
def predict():
   with open('./loan_predict.pickle', 'rb') as f:
      model = pickle.load(f)
    
   model_columns = ['Credit_History', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
                     'Education', 'Self_Employed', 'Gender', 'Married', 'Dependents', 
                     'Property_Area','Loan_Amount_Term'] 
    
   if flask.request.method == 'GET':
      return "Prediction page. Try using post with params to get specific prediction."

   if flask.request.method == 'POST':
      try:
         json_ = request.get_json() 
         query_ = pd.DataFrame(json_)
         query = query_.reindex(columns = model_columns, fill_value=0)
            
         query['CoapplicantIncome'] = query.CoapplicantIncome.astype('int')
         query['ApplicantIncome'] = query.ApplicantIncome.astype('int')
         query['Total_Income'] = query['ApplicantIncome'] + query['CoapplicantIncome']
         query['Total_Income'] = np.log(query['Total_Income'])
         query['LoanAmount'] = np.log(query['LoanAmount'])
         query['Education'] = query.Education.map({'Graduate':0, 'Not Graduate':1})
         query['Self_Employed'] = query.Self_Employed.map({'Yes':0, 'No':1})
         query['Property_Area'] = query.Property_Area.map({'Urban':0, 'Rural':1, 'Semiurban':2})
         query['Credit_History'] = query.Credit_History.astype('int64')
         query = query[['Credit_History', 'Self_Employed', 'Total_Income', 
                        'LoanAmount' , 'Property_Area', 'Education']]
            
         prediction = list(model.predict(query))
         if prediction[0] == 0:
            prediction = "Rejected"
         if prediction[0] == 1:
            prediction = "Approved"
         return jsonify({
               "Request": prediction
               })
                
      except:
         return jsonify({
               "trace": traceback.format_exc()
               })

if __name__ == "__main__":
   app.run()