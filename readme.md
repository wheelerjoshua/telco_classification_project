# About this Project
To be updated as progress is achieved.

## Project Goals
The goal of this project is to identify drivers of churn for the benefit of creating a solution to reduce the rate of churn among customers. 


## Project Description
With an unsteady and increasingly competitive market, it is cheaper to retain current customers than to establish new ones. We will observe various details of customer contracts and discover what may be driving them to churn and will use the information to create a model to predict future customer churn and a recommendation in reducing rate of churn.

## Initial Questions

- Are customers with fiber more or less likely to churn?
- Do customers who churn have a higher average monthly spend than those who don't?
- Are customers with dependents less likely to churn than those who don't?
- Are seniors less likely to churn?

## Data Dictionary

| variable      | meaning       |
| ------------- |:-------------:|
|RF|Random Forest modeling algorithm|
|KNN|K-Nearest Neighbors modeling algorithm |
|Logit |Logistic Regression modeling algorithm|
|df|Dataframe of raw telco data from sql server|
|train| training dataset, a major cut from the df|
|validate| validate dataset, used to prevent overfitting|
|test| test dataset, to test the top model on unseen data|
|chi2 | statistical test used to compare churn with various categories|

## Steps to Reproduce
What I did to get here?
- Create Trello Board listing tasks to completion
- Created modules with functions to acquire and clean the data
- Examined the data and came up with 4 questions
- Created visualizations relating to the quesitons
- Ran statistical tests to answer the questions
- Created a baseline model to test baseline accuracy
- Created numerous models to see how various algorithms performed
- Modified algorithms to see how changes affected performance
- Chose the 3 that performed the best and evaluated them on the validate training set
- Decided on a recommendation and next steps

## The Plan

### Wrangle
- acquire.py
Python module with functions defined to retrieve data for use
- prepare.py
Python module with functions defined to clean, tidy, prepare, and split data for use

### Explore
#### Ask Questions
1. Are customers with fiber more or less likely to churn?
2. Do customers who churn have a higher average monthly spend than those who don't?
3. Are customers with dependents less likely to churn than those who don't?
4. Are seniors less likely to churn?

#### Visualizations
- Matplotlib and Seaborn used to create visualizations
#### Statistical Tests
Used .mean() and chi2 test to answer statistical questions
#### Summary
Wrap up all of the testing conclusions
### Modeling
#### Select Evaluation Metric
Decided based on company's needs.
#### Evaluate Baseline
Create series of churn == 0
#### Develop 3 Models
Develop numerous models and asses top 3
#### Evaluate on Train
All models evaluated on train, but top 3 were validated
#### Evaluate on Validate
Ensure no overfitting takes place
#### Evaluate top model on Test
Top model evaluated against test dataset to see how it performed on unknown data.