import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score,roc_curve
from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler,StandardScaler
# ================================

trainingimages=np.load('trainingimages.npy')
traininglabel=np.load('traininglabel.npy')
testimages=np.load('testingimages.npy')
testlabels=np.load('testinglabels.npy')
print(testlabels)
print(len(testlabels))
scaler = StandardScaler()
scaler.fit(trainingimages)
trainingimages = scaler.transform(trainingimages)
testimages = scaler.transform(testimages)
# model1=LogisticRegression(multi_class='ovr',solver='saga',penalty='l1',max_iter=10)
model2=LogisticRegression(multi_class='ovr',solver='lbfgs',penalty='l2',max_iter=10)
# model1.fit(trainingimages,traininglabel)
model2.fit(trainingimages,traininglabel)

pred2=model2.predict_proba(testimages)
length=testlabels.shape[0]
print(length)
Encoding = np.zeros([length, 10])
for i in range(length):
	Encoding[i][testlabels[i]] = 1
Encoding =Encoding.T;
pred2 = pred2.T

score1=[]
fpr1=[]
tpr1=[]

for i in range (10):
	fpr, tpr, thresholds = roc_curve(Encoding[i], pred2[i])
	print(fpr)
	print(tpr)
	fpr1.append(fpr)
	tpr1.append(tpr)
	plt.plot(fpr, tpr, label=str(i) + ":" + str(roc_auc_score(Encoding[i], pred2[i])))
	score1.append(roc_auc_score(Encoding[i], pred2[i]))
plt.xlabel('False +ve Rate')
plt.ylabel('True +ve Rate')
plt.title('ROC Curve')
plt.legend(loc="lower right")
plt.plot([0, 1], [0, 1])
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.show()


def modelchosen(model,testimages,trainingimages,testlabels,traininglabel):
	
	misclassified_test = 0
	wrongtest = [0]*10
	totaltest = [0]*10
	y_pred_test = model.predict(testimages)
	for i in range(y_pred_test.shape[0]):
		if (y_pred_test[i] != testlabels[i]):
			misclassified_test += 1
			wrongtest[testlabels[i]]=wrongtest[testlabels[i]]+1
		totaltest[testlabels[i]] += 1
		
	for i in range(10):
		print('Class: ',i,'Accuracy: ', 100*((totaltest[i] - wrongtest[i])/totaltest[i]))

	print("Accuracy for test with model:", 100*((y_pred_test.shape[0] - misclassified_test)/y_pred_test.shape[0]))


	misclassified_training = 0
	wrongtrain = [0]*10
	totaltrain = [0]*10
	y_pred_training = model.predict(trainingimages)
	for i in range(y_pred_training.shape[0]):
		if (y_pred_training[i] != traininglabel[i]):
			misclassified_training += 1
			wrongtrain[traininglabel[i]]+=1
		totaltrain[traininglabel[i]]+=1
		
	for i in range(10):
		print('Class: ',i,'Accuracy: ', 100*((totaltrain[i] - wrongtrain[i])/totaltrain[i]))
	print("Accuracy for train with model:", 100*((y_pred_training.shape[0] - misclassified_training)/y_pred_training.shape[0]))
	
print('Check Accuracy for 1.L1 2.L2')
input1=int(input())
if input1==1:
	modelchosen(model1,testimages,trainingimages,testlabels,traininglabel)
else:
	modelchosen(model2,testimages,trainingimages,testlabels,traininglabel)

