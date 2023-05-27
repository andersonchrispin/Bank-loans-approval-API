# Mini-project IV

### [Assignment](assignment.md)

## Project/Goals
The project consist on training a Machine Learning algorithm and deploy the result on a server.

## Hypothesis
The subset of applicants that is most likely to have a loan aproval is clients having a credit history.
    77.36 % of the applicants have a credit history
    79.58 of clients having a credit history are approuved

## EDA 
The target variable is highly correlated with credit history status. That makes the training of the model kind of difficult with that small dataset. The ML algorithm quikly follow the pattern of credit history. 
I used many other features to decrease the weight of credit history

## Process
    1 - Explore the dataset to have better insight on its statistics and variable distribution
    
    2 - Cleaning under the contrainst of not loosing too much fata. The data size is small

    3 - Select the best combination features

    4 - Try a couple of classifier and cross-validate to refine ML hyper parameters

    5 - Synthetize all this process into a class

    6 - Elabotrate an algorithm for deployment

## Results/Demo
The model was trained with accurancy score:
    1 - Training: 90 %
    2 - Test: 84.83 %

## Challanges 
The biggest challenge was to sink all those new concepts and tools in a narrow range of time.

## Future Goals
I would elaborate a web interface to interact with the API.
I do not think the model is too reliable. The small size of the dataset and the high weight of credit history in this dataset may cause issues.