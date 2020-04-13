import pickle
import Audio_Functions as audio
import librosa
from sklearn.decomposition import PCA
from tkinter import *

pickle_in = open("genre12.pickle", "rb")
model = pickle.load(pickle_in)

pickle_in = open("pcaModel.pickle", "rb")
pca_model = pickle.load(pickle_in)

path = 'Test/05.wav'

feature = audio.audioAnalysis(path)
feature2 = audio.audioAnalysis(path)

test = []
test.append(feature)
test.append(feature2)
#test = pca_model.transform(test)

predicted = model.predict(test)

names = ["blues", "classical", "country", "disco", "hiphop", "jazz", "metal", "pop", "reggae", "rock"]
for x in range(len(predicted)):
    print("Predicted: ", predicted[x])
