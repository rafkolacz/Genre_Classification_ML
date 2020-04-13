import sklearn
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot
from matplotlib import style
from sklearn.metrics import confusion_matrix
from sklearn import linear_model, preprocessing
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier as knn

data = pd.read_csv("Data/music3.data")

predict = "Genre"

X = np.array(data.drop([predict], 1))
Y = np.array(data[predict])

# le = preprocessing.LabelEncoder()
# Y = le.fit_transform(Y)

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y, test_size=0.1)

pca_model = PCA(n_components=4)
pca_model.fit(x_train)
x_train = pca_model.transform(x_train)
x_test = pca_model.transform(x_test)

model = KNeighborsClassifier(n_neighbors=9)

model.fit(x_train,y_train)

acc = model.score(x_test,y_test)
print(acc)

predicted = model.predict(x_test)
names = ["blues", "classical", "country", "disco", "hiphop", "jazz", "metal", "pop", "reggae", "rock"]
for x in range(len(predicted)):
    print("Predicted: ", predicted[x], "Actual: ", y_test[x])

conf = confusion_matrix(predicted, y_test, labels=names)
print(conf)


'''
# data plots
label = ["Zero crossing", "Centroid", "Rolloff", "MFCC", "Chroma Freq", "Tempo", "Contrast", "Tonal" ,"Flatness"]
for x in label:
    p = 'Genre'
    style.use("ggplot")
    pyplot.scatter(data[p], data[x])
    pyplot.xlabel(p)
    pyplot.ylabel(x)
    pyplot.show()
'''
