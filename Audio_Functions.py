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


#
def prediction(path):
    pickle_in = open("model/genre18.pickle", "rb")
    model = pickle.load(pickle_in)
    toanalyse = pd.read_csv("Data/music9.data")
    predict = "Genre"

    toanalyse = np.array(toanalyse.drop([predict], 1))
    #toanalyse =[[0.08304482066898686, 1784.165849538755, 3805.8396058403423, 0.35008812970487335, 0.13022792, 2002.4490601176963, 0.1522905701561464, 20.526698693370026, 0.001626518606774716, 0.0044983495, -113.57065006014841, 121.57179828375645, -19.168141830786567, 42.36641931081864, -6.364662969610004, 18.62349792464524, -13.704889705913923, 15.343149555432882, -12.27410844121361, 10.976570552258794, -8.326572193800242, 8.803791231568432, -3.672299421905254, 5.7479945471953755, -5.162881230931701, 0.7527385539353071, -1.6902141675534033, -0.4089800418536765, -2.3035220174566478, 1.2212897403748306]]
    #feature = fileAnalysis(path)
    #np.append([toanalyse,feature], axis = 0)
    #pca_model = PCA(n_components=1)
    #pca_model.fit(toanalyse)
    #toanalyse = pca_model.transform(toanalyse)
    print(toanalyse)
    predicted = model.predict(toanalyse)
    return predicted


