import sklearn
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot
from matplotlib import style
from sklearn.metrics import confusion_matrix
from sklearn import linear_model, preprocessing
from sklearn.decomposition import PCA
import Audio_Functions as audio
from sklearn.neighbors import KNeighborsClassifier as knn

data = pd.read_csv("Data/music9.data")

predict = "Genre"

X = np.array(data.drop([predict], 1))
Y = np.array(data[predict])

# le = preprocessing.LabelEncoder()
# Y = le.fit_transform(Y)
scaler = preprocessing.MinMaxScaler()
X = scaler.fit_transform(X)

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y, test_size=0.1)


pca_model = PCA(n_components=7)
pca_model.fit(x_train)
x_train = pca_model.transform(x_train)
x_test = pca_model.transform(x_test)

model = KNeighborsClassifier(n_neighbors=9)

model.fit(x_train,y_train)

acc = model.score(x_test, y_test)
print(acc)
predicted = model.predict(x_test)

for x in range(len(predicted)):
    print("Predicted: ", predicted[x], "Actual: ", y_test[x])

names = ["blues", "classical", "country", "disco", "hiphop", "jazz", "metal", "pop", "reggae", "rock"]
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

test = []
for i in range(7):
    path = 'Test/0' + str(i+1) + ".wav"
    feature = audio.audioAnalysis(path)
    test.append(feature)
    print(feature)

pca_model = PCA(n_components=7)
pca_model.fit(test)
test = pca_model.transform(test)
print(test)
predict = model.predict(test)

for x in range(len(predict)):
    print(str(x+1) + " predicted: ", predict[x])
