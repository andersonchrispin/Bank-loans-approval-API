# Loans prediction
We want to automate the loan eligibility process based on customer details that are provided as online application forms are being filled. You can find the dataset [here](https://drive.google.com/file/d/1h_jl9xqqqHflI5PsuiQd_soNYxzFfjKw/view?usp=sharing). These details concern the customer's Gender, Marital Status, Education, Number of Dependents, Income, Loan Amount, Credit History and other things as well.

## Project/Goals
The project consist on training a Machine Learning algorithm and deploy the result on a server.

## Insights
The subset of applicants that is more likely to have a loan approval is clients having a credit history.
    77.36 % of the applicants have a credit history
    79.58 of clients having a credit history are approuved

The target variable is highly correlated with credit history status. That makes the training of the model kind of difficult with that small dataset. The ML algorithm quikly follow the pattern of credit history. 
I used many other features to decrease the weight of credit history

## Process
1 - Cleaning under the contrainst of not loosing too much data. The data size is small

2 - Select the best combination features

3 - Try a couple of classifier and cross-validate to refine ML hyper parameters

4 - Synthetize all this process into a class

5 - Elabotrate an algorithm for deployment

## Results/Demo
The model was trained with accurancy score:
    1 - Training: 90 %
    2 - Test: 84.83 %
