import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
import math
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score
from sklearn.feature_selection import SelectFromModel
from sklearn.cluster import KMeans

# ================================================================================

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def cost(hypothesis, y):
    if y != 0:
        return math.log(hypothesis)
    return math.log(1 - hypothesis)
    

def gradientDescent(X, Y, Xtest, Ytest, learning_rate = 0.5, num_iterations=100,normal=0, lasso = 0, ridge = 0):

    thetas_temp = np.zeros([1, X.shape[1]])
    testing_examples = Xtest.shape[0]
    thetas = np.zeros([1, X.shape[1]], dtype="float")
    

    accuracy_test_all = []
    accuracy_test = 0

    cost_test_all = []
    cost_test = 0
    
    accuracy_train_all = []
    accuracy_train = 0
    
    cost_train_all = []
    cost_train = 0

    iterations=0
    while iterations<(num_iterations):

        for j in range(X.shape[1]):
            thetas_temp[0][j] = thetas[0][j]
            if (j == 0):
                pass
            else:
                
                if (thetas_temp[0][j] < 0):
                    check1=((-1)*lasso + 2*ridge*thetas[0][j])
                    thetas_temp[0][j] -= check1/(2*X.shape[0])
                else:
                    check2= (1*lasso + 2*ridge*thetas[0][j])
                    thetas_temp[0][j] -= check2/(2*X.shape[0])

        for i in range(X.shape[0]):
            check = np.dot(thetas[0], X[i])
            hypothesis = sigmoid(check)
            for j in range(X.shape[1]):
                thetas_temp[0][j] -= (learning_rate*(hypothesis - Y[i][0])/X.shape[0])*X[i][j]

        for j in range(X.shape[1]):
            thetas[0][j] = thetas_temp[0][j]

        chkrange = testing_examples - 1
        for i in range(chkrange):
            prediction = 1
            if ((sigmoid(np.dot(thetas[0], Xtest[i]))) > 0.5):
                prediction = 1
            else:
                prediction=0
            if (prediction != Ytest[i][0]):
                accuracy_test += 0
            else:
                accuracy_test+=1
            cost_test += cost(hypothesis, Ytest[i][0]) 

        for i in range(training_examples):
            prediction = 1
            if ((sigmoid(np.dot(thetas[0], trainingX[i]))) > 0.5):
                prediction = 1
            else:
                prediction=0
            if (prediction != trainingY[i][0]):
                accuracy_train += 0
            else:
                accuracy_train+=1 
            cost_train += cost(hypothesis, trainingY[i][0]) 

        for j in range(1, X.shape[1]):
            check2=thetas[0][j]
            check3=(ridge*((check2)**2) + lasso*(abs(check2)))
            cost_train += check3/2*X.shape[0]
            check4=(ridge*((thetas[0][j])**2) + lasso*(abs(thetas[0][j])))
            cost_test += check4/2*X.shape[0]

        cost_test /= testing_examples
        accuracy_test /= testing_examples
        accuracy_test *= 100
        cost_train /= X.shape[0]
        accuracy_train /= X.shape[0]
        accuracy_train *= 100
        accuracy_test_all.append(accuracy_test)
        accuracy_train_all.append(accuracy_train)
        cost_test_all.append(-cost_test)
        cost_train_all.append(-cost_train)
        iterations+=1
    return accuracy_train_all, cost_train_all, accuracy_test_all, cost_test_all 



# Reading the training Set from train.csv
df = pd.read_csv("train.csv", sep=", ", header = None, engine='python')
df.columns = ["age","workclass","fnlwgt","education","education-num","marital-status","occupation","relationship","race","sex","capital-gain","capital-loss","hours-per-week","native-country", "salaries"]
#trainingY = df[['salaries']]
trainingY = pd.get_dummies(df['salaries']).drop(['<=50K'], axis=1)
trainingX = df.drop(['salaries'], axis=1)


tf = pd.read_csv("test.csv", sep=", ", header = None, engine='python')
tf.columns = ["age","workclass","fnlwgt","education","education-num","marital-status","occupation","relationship","race","sex","capital-gain","capital-loss","hours-per-week","native-country", "salaries"]
#testingY = tf[['salaries']]
testingY = pd.get_dummies(tf['salaries']).drop(['<=50K.'], axis=1)
testingX = tf.drop(['salaries'], axis=1)


# testingX_examples = testingX.shape[0]

categorical = ["workclass", "education","marital-status","occupation","relationship","race","sex","native-country"]
merged = pd.concat([trainingX, testingX])
for i in range(len(categorical)):
    merged = pd.concat([merged, pd.get_dummies(merged[categorical[i]], prefix=categorical[i])],axis=1)
    merged.drop([categorical[i]], axis=1, inplace=True)

temp1=merged.min()
temp2=merged.max()
merged =(merged-temp1)/(temp2-temp1)
merged = np.array(merged, dtype = "float") 

# Getting training and testing set from merged numpy array
training_examples = trainingX.shape[0]

trainingY = np.array(trainingY, dtype = "float")
trainingX = merged[0: training_examples]
testingY = np.array(testingY, dtype = "float")
testingX = merged[training_examples: ]



trainingX = np.c_[np.ones(trainingX.shape[0]),trainingX]
testingX = np.c_[np.ones(testingX.shape[0]), testingX]

print('1.Normal Logistic Regression 2.Ridge Logistic Regression 3.Lasso Logistic Regression')
choice = input()
if (choice == "1"):
    accuracy_train_all, cost_train_all, accuracy_test_all, cost_test_all = gradientDescent(trainingX, trainingY, testingX, testingY,normal=1)
    iterations = []
    for i in range (len(accuracy_train_all)):
        iterations.append(i + 1)
    
    string1 = 'trainingaccuracy' 
    string2 = 'testingaccuracy'
    df=pd.DataFrame({'x': iterations, string1 : accuracy_train_all, string2: accuracy_test_all})
    plt.plot('x', string1, data=df) 
    plt.plot('x', string2, data=df)
    plt.legend()
    plt.xlabel('Iterations')
    plt.ylabel('Accuracy')
    plt.show()

    string1 = 'trainingcost' 
    string2 = 'testingcost'
    df=pd.DataFrame({'x': iterations, string1 : cost_train_all, string2: cost_test_all})
    plt.plot('x', string1, data=df) 
    plt.plot('x', string2, data=df)
    plt.legend()
    plt.xlabel('Iterations')
    plt.ylabel('Cost')
    plt.show()

elif (choice == "2"):
    accuracy_train_all, cost_train_all, accuracy_test_all, cost_test_all = gradientDescent(trainingX, trainingY, testingX, testingY,normal=0, ridge= 0.5)
    iterations = []
    for i in range (len(accuracy_train_all)):
        iterations.append(i + 1)
    
    string1 = 'trainingaccuracy' 
    string2 = 'testingaccuracy'
    df=pd.DataFrame({'x': iterations, string1 : accuracy_train_all, string2: accuracy_test_all})
    plt.plot('x', string1, data=df) 
    plt.plot('x', string2, data=df)
    plt.legend()
    plt.xlabel('Iterations')
    plt.ylabel('Accuracy')
    plt.show()

    string1 = 'trainingcost' 
    string2 = 'testingcost'
    df=pd.DataFrame({'x': iterations, string1 : cost_train_all, string2: cost_test_all})
    plt.plot('x', string1, data=df) 
    plt.plot('x', string2, data=df)
    plt.legend()
    plt.xlabel('Iterations')
    plt.ylabel('Cost')
    plt.show()
elif (choice == "3"):
    accuracy_train_all, cost_train_all, accuracy_test_all, cost_test_all = gradientDescent(trainingX, trainingY, testingX, testingY, lasso = 0.5)
    iterations = []
    for i in range (len(accuracy_train_all)):
        iterations.append(i + 1)
    
    string1 = 'trainingaccuracy' 
    string2 = 'testingaccuracy'
    df=pd.DataFrame({'x': iterations, string1 : accuracy_train_all, string2: accuracy_test_all})
    plt.plot('x', string1, data=df) 
    plt.plot('x', string2, data=df)
    plt.legend()
    plt.xlabel('Iterations')
    plt.ylabel('Accuracy')
    plt.show()

    string1 = 'trainingcost' 
    string2 = 'testingcost'
    df=pd.DataFrame({'x': iterations, string1 : cost_train_all, string2: cost_test_all})
    plt.plot('x', string1, data=df) 
    plt.plot('x', string2, data=df)
    plt.legend()
    plt.xlabel('Iterations')
    plt.ylabel('Cost')
    plt.show()
else:
    pass
