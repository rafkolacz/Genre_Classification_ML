import pickle
import Audio_Functions as audio
import librosa
from sklearn.decomposition import PCA
from tkinter import *

pickle_in = open("model/genre18.pickle", "rb")
model = pickle.load(pickle_in)

pickle_in = open("pcamodel/pcaModel18.pickle", "rb")
pca_model = pickle.load(pickle_in)

test = []
for i in range(9):
    path = 'Test/0' + str(i+1) + ".mp3"
    feature = audio.audioAnalysis(path)
    print(feature)
    test.append(feature)
print("------------------------------------------------------")
print(test)
print("------------------------------------------------------")
test = pca_model.transform(test)
predicted = model.predict(test)

print(test)

for x in range(len(predicted)):
    print(str(x+1) + " predicted: ", predicted[x])
