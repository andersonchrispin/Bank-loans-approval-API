from sklearn.metrics import PrecisionRecallDisplay,f1_score, confusion_matrix
import pandas as pd
import numpy as np
from collections import Counter

def test_function(model, X_test, y_test, name, X_train=[], y_train=[]):
    #model score
    if ((list(X_train) != []) & (list(y_train) != [])):
        print('Model score on training data:', model.score(X_train, y_train))
    print('Model score on testing data:', model.score(X_test, y_test))

    #F1 score
    y_pred = model.predict(X_test)
    print('Model F1 score:\n', f1_score(y_test, y_pred, average='binary'))

    #balance of classes
    print('Balance of classes:\n', Counter(y_test))

    print('\nPercentage True:', Counter(y_test)[True]/len(y_test))
    
    #confusion matrix
    print('\nConfusion matrix:\n', confusion_matrix(y_test, y_pred, labels=[True, False]))
    
    #precision-recall graph
    graph = PrecisionRecallDisplay.from_estimator(model, X_test, y_test,
                                                    name=name)
    _ = graph.ax_.set_title("2-class Precision-Recall curve")
        
class prepare_feat:
    def __init__(self):
        self.__tab = pd.DataFrame()
            
    def fit(self, __tab1, y=None):
        self.__tab = __tab1 
        self.__tab['Total_Income'] = self.__tab['ApplicantIncome'] + self.__tab['CoapplicantIncome']
        self.__tab['LoanAmount'] = np.log(self.__tab['LoanAmount'])
        self.__tab['Loan_Status'] = self.__tab.Loan_Status.map({'Y':0, 'N':1})
             
        return self.__tab[['Loan_Status', 'Credit_History','Total_Income', 'LoanAmount']]
    
    def transform(self, X, y=None):
        pass
    
    def fit_transform(self, X, y=None):
        pass