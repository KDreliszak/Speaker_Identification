# import the pyplt and wavfile modules
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Read the wav file
samplingFrequency, signalData = wavfile.read(r'c:\Users\kajet\Desktop\magisterka\testy\Filtered\test2\Babcia_Kozak_0.wav')

# plot amplitude from time
plt.subplot(211)

plt.xlabel('Próbka')
plt.ylabel('Amplituda')

plt.plot(signalData)

# plot frequencies from time
plt.subplot(212)

plt.xlabel('Czas')
plt.ylabel('Częstotliwość')

# choose one channel
y = signalData[:, 0]
plt.specgram(y, Fs=samplingFrequency)

# plt.savefig('specF.png')
plt.tight_layout()
plt.show()
