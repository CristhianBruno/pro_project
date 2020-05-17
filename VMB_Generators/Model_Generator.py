""" ## Programing - Final Project - UNIL - MSc. in Finance - May 2020
### Group members: Valeria Medinaceli, Martin Ruilova, and Bruno Ayllon.
---

This scripts is designed run the prediction algorithm of the VMB Model.

"""


# Import the external dependencies:
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import warnings

warnings.filterwarnings("ignore")


# Create the classification function:
def get_classification(array):
    """ This function returns the prediction using a Random Forest model with a hyper parameter tuning.

    :param array: The function requires 12 variables (to be presented below).
    The keys of the features are obtained in the platform which convert them into the required values
    to be used in the model. For this process each variable counts with an own dictionary.

    ---------- IMPORTANT! ----------
    The variables must maintain the following order, and must be displayed as a np.array with shape (1,12):
    AYE, BIG, BAR, IND, DWF, PST, CPB, REC, SUR, CDA, INC, MLB

    example = np.reshape(np.array([0,0,1,1,2,0,1,0,1,0,1,0]),(1,12))

    :return:
    y_predicted: The prediction returns 0 or 1.
    - If y_predicted = 0 the company is likely to not be successful given its current features.
    - If y_predicted = 1 the company is likely to be successful given its current features.
    precision: The precision is 0.880796. This value was obtained by our team through a separated project of
    Advanced Data Analytics.
    """

    X = np.array(pd.read_csv('PROG_CAX_Features_Selection.csv'))
    y = np.array(pd.read_csv('PROG_CAX_Preprocessed_Target_ADA.csv'))
    data = np.concatenate((X, y), axis=1)

    train_data, test_data = train_test_split(data, test_size=0.2, random_state=42, stratify=y)

    train_X = train_data[:, 0:12]
    test_X = array
    train_y = np.reshape(train_data[:, 12], (377, 1))

    precision = 0.880796

    rf = RandomForestClassifier(criterion='gini', max_depth=4, max_features=2)
    rf.fit(train_X, train_y)
    y_predicted = int(rf.predict(test_X))

    return y_predicted, precision


