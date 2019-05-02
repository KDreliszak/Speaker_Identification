import pyaudio
import wave
import numpy as np


def audio_sample(file_name, record_time):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 16000 #44100
    RECORD_SECONDS = record_time
    wave_output = 'no_F_' + file_name

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, output=True)

    frames = []
    print("*recording")
    # !!!!!!!!!!!!!!!!!NAGRYWANIE!!!!!!!!!!!!!!!!!!!!!!
    # wzór birate przy nagrywaniu birate = (RATE/BUFFOR)*RECORD_SECOND
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("* done recording *")

    # !!!!!!!!!!!!!!!ZAPIS DO PLIKU!!!!!!!!!!!!!!!
    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(wave_output, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    # Łączenie znaków w całość
    wf.writeframes(b''.join(frames))
    wf.close()

    noise_reduction(wave_output)


def noise_reduction(wave_file):
    wr = wave.open(wave_file, 'r')

    par = list(wr.getparams())  # Get the parameters from the input.
    par[3] = 0  # The secber of samples will be set by writeframes.

    # Open the output file
    ww = wave.open(wave_file, 'w')
    ww.setparams(tuple(par))  # Use the same parameters as the input file.

    lowpass = 300  # Remove lower frequencies.
    highpass = 3500  # Remove higher frequencies.

    framerate = wr.getframerate()  # Read and process 1 second at a time.

    length = int(wr.getnframes() / framerate)  # whole file

    for sec in range(length + 1):
        try:
            # print('Processing {}/{} s'.format(sec, length))
            da = np.frombuffer(wr.readframes(framerate), dtype=np.int16)
            if len(da) % 2 != 0:
                da = np.delete(da, -1)
            left, right = da[0::2], da[1::2]  # left and right channel
            lf, rf = np.fft.rfft(left), np.fft.rfft(right)
            lf[:lowpass], rf[:lowpass] = 0, 0  # low pass filter
            # lf[55:66], rf[55:66] = 0, 0  # line noise
            lf[highpass:], rf[highpass:] = 0, 0  # high pass filter
            nl, nr = np.fft.irfft(lf), np.fft.irfft(rf)
            ns = np.column_stack((nl, nr)).ravel().astype(np.int16)
            ww.writeframes(ns.tostring())
        except:
            print(wave_file)
    # Close the files.
    wr.close()
    ww.close()

    return


# audio_sample('k')

# noise_reduction('test.wav', 'filtered-test.wav')

