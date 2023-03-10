# Import required libraries
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import random
import pickle

random.seed(20)


def rf_testing(variables):
    # Shuffle dataset now then split
    random.shuffle(np.c_[variables.data])

    # split dataset into X and y
    X = np.c_[variables.data[['Name', 'Position', 'Year', 'Month',
                              'Date', 'Team', 'Location', 'Opp']]]
    y = np.c_[variables.data[['Minutes Played', 'FGM', 'FGA',
                              '3PM', '3PA', 'FTM',
                              'FTA', 'ORB', 'DRB',
                              'TRB', 'AST', 'STL',
                              'BLK', 'TOV', 'PTS']]]

    X_train = X[:int(len(X) * 0.80)]
    y_train = y[:int(len(y) * 0.80)]
    X_test = X[int(len(X) * 0.80):]
    y_test = y[int(len(y) * 0.80):]

    # create model with RandomForestRegressor
    svm_model = RandomForestRegressor(n_estimators=1000, random_state=20)
    svm_model.fit(X_train, y_train)

    # Running Predictions
    predictions = svm_model.predict(X_test)
    # accuracy = [predictions[index][0] - y_test[index][0] for index in range(len(y_test))]
    return predictions


def rf(variables, input):


    # split dataset into X and y
    X = np.c_[variables.data[['Name', 'Position', 'Year', 'Month',
                              'Date', 'Team', 'Location', 'Opp']]]
    y = np.c_[variables.data[['Minutes Played', 'FGM', 'FGA',
                              '3PM', '3PA', 'FTM',
                              'FTA', 'ORB', 'DRB',
                              'TRB', 'AST', 'STL',
                              'BLK', 'TOV', 'PTS']]]

    # create model with RandomForestRegressor
    rf_model = RandomForestRegressor(n_estimators=100, random_state=20)
    rf_model.fit(X, y)

    pickle.dump(rf_model, open('rf_model.sav', 'wb'))

    # Running Predictions
    predictions = rf_model.predict(input)
    # accuracy = [predictions[index][0] - y_test[index][0] for index in range(len(y_test))]

    return predictions


