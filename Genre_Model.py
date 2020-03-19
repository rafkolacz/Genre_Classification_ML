import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as pyplot
from matplotlib import style
from sklearn import linear_model, preprocessing
from sklearn.metrics import confusion_matrix

data = pd.read_csv("music2.data")

predict = "Genre"

X = np.array(data.drop([predict], 1))
Y = np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y, test_size=0.1)

model = KNeighborsClassifier(n_neighbors=5)

model.fit(x_train,y_train)

acc = model.score(x_test,y_test)
print(acc)

predicted = model.predict(x_test)
names = ["blues", "classical", "country", "disco", "hiphop", "jazz", "metal", "pop", "reggae", "rock"]
for x in range(len(predicted)):
    print("Predicted: ", predicted[x], "Actual: ", y_test[x])

conf = confusion_matrix(predicted, y_test, labels=names)
print(conf)

