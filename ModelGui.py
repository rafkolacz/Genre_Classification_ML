import pickle
import Audio_Functions as audio
import librosa
from sklearn.decomposition import PCA
from tkinter import *
'''
pickle_in = open("model/genre18.pickle", "rb")
model = pickle.load(pickle_in)

#pickle_in = open("pcamodel/pcaModel18.pickle", "rb")
#pca_model = pickle.load(pickle_in)

test = []
for i in range(9):
    path = 'Test/0' + str(i+1) + ".wav"
    #feature = audio.audioAnalysis(path)
    feature = audio.fileAnalysis(path)
    test.append(feature)
    print(i)

#pca_model = PCA(n_components=8)
#pca_model.fit(test)
#test = pca_model.transform(test)
predicted = model.predict(test)


for x in range(len(predicted)):
    print(str(x+1) + " predicted: ", predicted[x])

'''
print(audio.prediction("Test/07.wav"))
'''
x = audio.fileAnalysis("Test/07.wav")
print("Done")
y = audio.fileAnalysis("Test/08.wav")
test = []
test.append(x)
test.append(y)
prediction = model.predict(test)
'''