# coding:utf-8
# 一元线性回归分析例子

from sklearn import linear_model
import pandas as pd

#Function to get data
def get_data(file_name):
    data = pd.read_csv(file_name)
    X = []
    Y = []
    for time, city in zip(data['时间'], data['北京']):
        X.append([float(time)])
        Y.append(float(city))
    return X, Y

#Function for linear model
def linear_model_main(X_parameters, Y_parameters, predict_value):
    regr = linear_model.LinearRegression()
    regr.fit(X_parameters, Y_parameters)
    predict = regr.predict(predict_value)
    predictions = {}
    predictions['intercept'] = regr.intercept_   #截距
    predictions['coefficient'] = regr.coef_   #回归系数
    predictions['predicted_value'] = predict
    return predictions

X, Y = get_data('test1.csv')
print X
print Y

predict_time = 2014
result = linear_model_main(X, Y, predict_time)
print "Intercept value ", result['intercept']
print "coefficient", result['coefficient']
print "Predicted value: ", result['predicted_value']