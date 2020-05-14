
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import warnings

warnings.filterwarnings("ignore")


# ---------- IMPORTANT!!! ----------

# The variables must maintain the following order:
# AYE, BIG, BAR, IND, DWF, PST, CPB, REC, SUR, CDA, INC, MLB

# example = np.reshape(np.array([0,0,1,1,2,0,1,0,1,0,1,0]),(1,12))


def get_classification(array):

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


