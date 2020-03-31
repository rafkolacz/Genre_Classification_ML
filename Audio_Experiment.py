import matplotlib.pyplot as plt
import librosa
import numpy as np



# Plik do obserwacji, porownywania cech oraz podziwiania wykresow

audio_path = 'Gitzan/genres/genres/blues/blues.00000.wav'
y, sr = librosa.load(audio_path)
S, phase = librosa.magphase(librosa.stft(y=y))
# print(type(x), type(sr))

# Zero crossing
zero_crossing = librosa.feature.zero_crossing_rate(y)
print("Zero_crossing: ", np.mean(zero_crossing))

''' # Wykres widma
plt.figure()
librosa.display.waveplot(y, sr=sr)
plt.show()
'''
# Spectral Centroid
cent = librosa.feature.spectral_centroid(y=y, sr=sr)
print("Spectral Centroid: ", np.mean(cent))

''' Wykres do spectral centroidu
plt.figure()
plt.subplot(2, 1, 1)
plt.semilogy(cent.T, label='Spectral centroid')
plt.ylabel('Hz')
plt.xticks([])
plt.xlim([0, cent.shape[-1]])
plt.legend()
plt.subplot(2, 1, 2)
librosa.display.specshow(librosa.amplitude_to_db(S, ref=np.max), y_axis='log', x_axis='time')
plt.title('log Power spectrogram')
plt.tight_layout()
plt.show()
'''

# Roll off
rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
print("Spectral rolloff: ", np.mean(rolloff))

'''
plt.figure()
plt.subplot(2, 1, 1)
plt.semilogy(rolloff.T, label='Roll-off frequency')
plt.ylabel('Hz')
plt.xticks([])
plt.xlim([0, rolloff.shape[-1]])
plt.legend()
plt.subplot(2, 1, 2)
librosa.display.specshow(librosa.amplitude_to_db(S, ref=np.max),
                         y_axis='log', x_axis='time')
plt.title('log Power spectrogram')
plt.tight_layout()
plt.show()
'''

# Mel-Frequency Cepstral Coefficients
mfcc = librosa.feature.mfcc(y, sr=sr)
x = 1
for e in mfcc:
    print("MFCC: ", np.mean(e))
    print(x)
    x += 1
'''
plt.figure(figsize=(10, 4))
librosa.display.specshow(mfcc, x_axis='time')
plt.colorbar()
plt.title('MFCC')
plt.tight_layout()
plt.show()
'''

# Chroma stft
chroma = librosa.feature.chroma_stft(y=y, sr=sr)
print("Chroma Freq: ", np.mean(chroma))

'''
plt.figure(figsize=(10, 4))
librosa.display.specshow(chroma, y_axis='chroma', x_axis='time')
plt.colorbar()
plt.title('Chromagram')
plt.tight_layout()
plt.show()

'''
# Compute the tempogram
tempo = librosa.feature.tempogram(y=y, sr=sr)
print(np.mean(tempo))

# spectral contrast
contrast = librosa.feature.spectral_contrast(y=y, sr=sr)
print(np.mean(contrast))

# Computes the tonal centroid
tonal = librosa.feature.tonnetz(y=y, sr=sr)
print(np.mean(tonal))

# Flatness
flatness = librosa.feature.spectral_flatness(y=y)
print(np.mean(flatness))

# More data ?