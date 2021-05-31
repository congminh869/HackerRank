#https://www.hackerrank.com/challenges/predicting-office-space-price/problem?fbclid=IwAR07Vd94NDPMupwGVJgRyBKp8kpTlFykkliL-aHwsua6ovgm14Isofkps3Q
#https://www.javatpoint.com/machine-learning-polynomial-regression 
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

F, N = map(int, input().split(" "))
data_train = input()
T = int(input())
data_test = input()

data = np.reshape(np.array(data_train.split(' '), float), (N,F+1))
X_test = np.reshape(np.array(data_test.split(' '), float), (T,F))
X_train = data[:,:-1]
y_train = data[:,-1]


poly_regs = PolynomialFeatures(degree=3) 
X_train_poly = poly_regs.fit_transform(X_train)
x_test_poly = poly_regs.fit_transform(X_test)
lin_reg_3 = LinearRegression()
lin_reg_3.fit(X_train_poly, y_train)
results = lin_reg_3.predict(x_test_poly)
for i in range(len(results)):
    print(round(results[i],2))
