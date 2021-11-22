import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# import splitting and imputing functions
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

# turn off pink boxes
import warnings
warnings.filterwarnings("ignore")

# import our own acquire module
import acquire


# def impute_mode(train, validate, test):
#     '''
#     Takes in train, validate, and test, and uses train to identify the best value to replace nulls in column
#     Imputes that value into all three sets and returns all three sets.
#     '''
#     imputer = SimpleImputer(missing_values = np.nan, strategy = 'most_frequent')
#     train[[col]] = imputer.fit_transform(train[[col]])
#     validate[[col]] = imputer.transform(validate[[col]])
#     test[[col]] = imputer.transform(test[[col]])
#     return train, validate, test

##### TELCO
def prep_telco(df):
    '''
    Takes in titanic dataframe and returns prepared version of the dataframe
    '''
    # Drop duplicates
    df.drop_duplicates(inplace = True)
    ####### Change total_charges to float #######
    df.total_charges = df.total_charges.str.strip()
    df = df[df.total_charges != ""]
    df.total_charges = df.total_charges.astype(float)
    #############################################
    dummy_df = pd.get_dummies(df[['gender','partner','dependents','multiple_lines', 'streaming_tv','streaming_movies','paperless_billing','churn',]], dummy_na = False, drop_first = [True, True])
    df = pd.concat([df, dummy_df], axis = 1)
    # Drop unecessary columns
    df.drop(columns = ['streaming_tv_No internet service','streaming_movies_No internet service','customer_id', 'online_security', 'online_backup', 'device_protection', 'tech_support', 'internet_service_type', 'payment_type','contract_type'], inplace = True)


    return df


##### SPLIT DATA

def split_telco(df):
    '''
    Takes in a dataframe and stratify variable, returns train, validate, test subset dataframes. 
    '''
    train, test = train_test_split(df, test_size = .2, stratify = df.churn)
    train, validate = train_test_split(train, test_size = .3, stratify = train.churn)
    return train, validate, test