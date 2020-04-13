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
    rms = librosa.feature.rms(y)
    spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
    tempo = librosa.feature.tempogram(y=y, sr=sr)
    contrast = librosa.feature.spectral_contrast(y=y, sr=sr)
    tonal = librosa.feature.tonnetz(y=y, sr=sr)
    flatness = librosa.feature.spectral_flatness(y=y)
    onset_env = librosa.onset.onset_strength(y, sr=sr)
    bpm = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)
    # data = [np.mean(zero_crossing), np.mean(cent), np.mean(rolloff), np.mean(chroma), np.mean(rms),  np.mean(spec_bw)]
    data = [np.mean(zero_crossing), np.mean(cent), np.mean(rolloff), np.mean(chroma),np.mean(rms),  np.mean(spec_bw),np.mean(tempo),np.mean(contrast),np.mean(tonal),np.mean(flatness),int(bpm[0])]
    for e in mfcc:
       data.append(np.mean(e))
    return data


dataset = []
genres = ["blues", "classical", "country", "disco", "hiphop", "jazz", "metal", "pop", "reggae", "rock"]
#genres = ["blues", "classical", "country", "X", "X", "X", "X", "X", "reggae", "X"]

count = 0   # just flag for better performance
for genre in range(10):
    for songs in range(100):
        data = feature_Extraction(genre, songs)
        data.append(genres[genre])
        dataset.append(data)
        print(count)
        count += 1


#columns = ["Zero crossing", "Centroid", "Rolloff", "Chroma Freq", "Tempo", "Contrast", "Tonal", "Flatness"]
columns = ["Zero crossing", "Centroid", "Rolloff", "Chroma Freq", "RMS", "Spectral Bandwidth", "Tempo", "Contrast", "Tonal", "Flatness", "BPM"]
for i in range(20):
    columns.append("MFCC " + str(i + 1))
columns.append("Genre")

df = pd.DataFrame(dataset, columns=columns)
df.to_csv("musicDivision.data", index=False)
