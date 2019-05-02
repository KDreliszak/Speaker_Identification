import os
import wave
import numpy as np
from GMM_UBM import training_model


def filter_cataloges(src, dst):
    for folder in os.listdir(src):
        folder_path = src + folder + '\\'

        if not os.path.isdir(dst+folder):
            os.mkdir(dst + folder)

        for wave_file in os.listdir(folder_path):
            wr = wave.open(folder_path+wave_file, 'r')
            par = list(wr.getparams())  # Get the parameters from the input.
            par[3] = 0  # The secber of samples will be set by writeframes.

            # Open the output file
            ww = wave.open(dst+folder+'\\'+wave_file, 'w')
            ww.setparams(tuple(par))  # Use the same parameters as the input file.

            lowpass = 300  # Remove lower frequencies.
            highpass = 3500  # Remove higher frequencies.

            framerate = wr.getframerate()  # Read and process 1 second at a time.
            length = int(wr.getnframes() / framerate)  # whole file

            for sec in range(length+1):
                try:
                    da = np.frombuffer(wr.readframes(framerate), dtype=np.int16)
                    if len(da) % 2 != 0:
                        da = np.delete(da, -1)
                    # print('Processing {}/{} s'.format(sec + 1, length))
                    left, right = da[0::2], da[1::2]  # left and right channel
                    lf, rf = np.fft.rfft(left), np.fft.rfft(right)
                    lf[:lowpass], rf[:lowpass] = 0, 0  # low pass filter
                    # lf[55:66], rf[55:66] = 0, 0  # line noise ZBADAĆ TO
                    lf[highpass:], rf[highpass:] = 0, 0  # high pass filter
                    nl, nr = np.fft.irfft(lf), np.fft.irfft(rf)
                    ns = np.column_stack((nl, nr)).ravel().astype(np.int16)
                    ww.writeframes(ns.tostring())
                except:
                    print(folder)
            # Close the files.
            wr.close()
            ww.close()


def filter_files(src, dst):

    for wave_file in os.listdir(src):
        wr = wave.open(src+wave_file, 'r')

        par = list(wr.getparams())  # Get the parameters from the input.
        par[3] = 0  # The secber of samples will be set by writeframes.

        # Open the output file
        ww = wave.open(dst+wave_file, 'w')
        ww.setparams(tuple(par))  # Use the same parameters as the input file.

        lowpass = 300  # Remove lower frequencies.
        highpass = 3500  # Remove higher frequencies.

        framerate = wr.getframerate()  # Read and process 1 second at a time.

        length = int(wr.getnframes() / framerate)  # whole file

        for sec in range(length+1):
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


def create_models_for_all(src, dst):
    for catalog in os.listdir(src):
        print(catalog)
        training_model(src + catalog + '\\', dst)


# filter_files(r'c:\Users\kajet\Desktop\magisterka\dane\Audio\Oryginalne\new\uczace\test''\\', r'c:\Users\kajet\Desktop\magisterka\dane\Audio\Oryginalne\new\uczace_f''\\')

# filter_cataloges(r'c:\Users\kajet\Desktop\magisterka\dane\Audio\Oryginalne\new\testowe''\\', r'c:\Users\kajet\Desktop\magisterka\dane\Audio\Oryginalne\new\testowe_f''\\')

# create_models_for_all(r'c:\Users\kajet\Desktop\magisterka\dane\Audio\Filtrowane\Uczace''\\', r'c:\Users\kajet\Desktop\magisterka\dane\Modele\All''\\')
