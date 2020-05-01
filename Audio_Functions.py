import librosa
import numpy as np
import pickle
import pandas as pd
from sklearn.decomposition import PCA


# this function abstract all needed features
def audioAnalysis(path):
    y, sr = librosa.load(path)

    zero_crossing = librosa.feature.zero_crossing_rate(y)
    cent = librosa.feature.spectral_centroid(y=y, sr=sr)
    rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
    mfcc = librosa.feature.mfcc(y, sr=sr)
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    rms = librosa.feature.rms(y)
    spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
    tempo = librosa.feature.tempogram(y=y, sr=sr)
    contrast = librosa.feature.spectral_contrast(y=y, sr=sr)
    tonal = librosa.feature.tonnetz(y=y, sr=sr)
    flatness = librosa.feature.spectral_flatness(y=y)
    onset_env = librosa.onset.onset_strength(y, sr=sr)
    #bpm = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)

    data = [np.mean(zero_crossing), np.mean(cent), np.mean(rolloff), np.mean(chroma), np.mean(rms), np.mean(spec_bw),
            np.mean(tempo), np.mean(contrast), np.mean(tonal), np.mean(flatness)]
    for e in mfcc:
        data.append(np.mean(e))
    return data


# uses audioAnalysis to create one var
def fileAnalysis(path):
    feature = audioAnalysis(path)
    return feature


#  returns genre of particular song (specified by path)
def prediction(path):
    # opens out best model
    pickle_in = open("model/genre18.pickle", "rb")
    model = pickle.load(pickle_in)

    # array must match
    toanalyse = pd.read_csv("temp.data")
    # predict = "Genre"
    # toanalyse = np.array(toanalyse.drop([predict], 1))
    # instead of temp we can use for example music9.data
    # temp.data consist features from new songs (not from gitzan)

    # now we extract features of our song
    feature = fileAnalysis(path)

    # ddaing new row, columns must match
    feature = pd.DataFrame([feature], columns=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234'))
    toanalyse = toanalyse.append(feature, ignore_index=True)

    # creating pca model
    pca_model = PCA(n_components=8)  # must be the same value as previous fit
    pca_model.fit(toanalyse)
    toanalyse = pca_model.transform(toanalyse)
    predicted = model.predict(toanalyse)

    # returns last genre
    return predicted[-1]


