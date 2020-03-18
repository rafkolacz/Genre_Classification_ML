import matplotlib.pyplot as plt
import librosa
import numpy as np
import pandas as pd

# extracting features from samples and saving to file
def feature_Extraction(genre, number):
    genres = ["blues", "classical", "country", "disco", "hiphop", "jazz", "metal", "pop", "reggae", "rock"]
    if number < 10:
        audio_path = 'Gitzan/genres/genres/' + genres[genre] + "/" + genres[genre] + ".0000" + str(number) + ".wav"
    else:
        audio_path = 'Gitzan/genres/genres/' + genres[genre] + "/" + genres[genre] + ".000" + str(number) + ".wav"
    y, sr = librosa.load(audio_path)

    zero_crossing = librosa.feature.zero_crossing_rate(y)
    cent = librosa.feature.spectral_centroid(y=y, sr=sr)
    rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
    mfcc = librosa.feature.mfcc(y, sr=sr)
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)

    data = [np.sum(zero_crossing), np.sum(cent), np.sum(rolloff), np.sum(mfcc), np.sum(chroma)]
    return data


dataset = []
genres = ["blues", "classical", "country", "disco", "hiphop", "jazz", "metal", "pop", "reggae", "rock"]
for genre in range(10):
    for songs in range(100):
        data = feature_Extraction(genre, songs)
        data.append(genres[genre])
        dataset.append(data)

df = pd.DataFrame(dataset, columns=["Zero crossing", "Centroid", "Rolloff", "MFCC", "Chroma Freq", "Genre"])
df.to_csv("music.data", index=False)
