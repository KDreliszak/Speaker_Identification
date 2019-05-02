import numpy as np
import os
from sklearn import preprocessing
import python_speech_features as mfcc
import pickle
from scipy.io.wavfile import read
from sklearn.mixture import GaussianMixture
import time
import warnings
warnings.filterwarnings("ignore")


def calculate_delta(array, again=False):
    """Calculate and returns the delta of given feature vector matrix"""

    rows, cols = array.shape
    deltas = np.zeros((rows, 20))
    N = 2
    for i in range(rows):
        index = []
        j = 1
        while j <= N:
            if i - j < 0:
                first = 0
            else:
                first = i - j
            if i + j > rows - 1:
                second = rows - 1
            else:
                second = i + j
            index.append((second, first))
            j += 1
        deltas[i] = (array[index[0][0]] - array[index[0][1]] + (2 * (array[index[1][0]] - array[index[1][1]]))) / 10
    if again:
        delta_delta = calculate_delta(deltas)
        combined = np.hstack((deltas, delta_delta))
        return combined
    else:
        return deltas


def extract_features(audio, rate):
    """extract 20 dim mfcc features from an audio, performs CMS and combines
    delta and delt-delta to make it 60 dim feature vector"""

    window_length_samples = 0.025 * rate
    nfft = 1
    while nfft < window_length_samples:
        nfft *= 2

    mfcc_feat = mfcc.mfcc(audio, rate, 0.025, 0.01, 20, appendEnergy=True, nfft=nfft)
    mfcc_feat = preprocessing.scale(mfcc_feat)

    delta = calculate_delta(mfcc_feat, True)
    combined = np.hstack((mfcc_feat, delta))

    return combined


def training_model(train_path, models_path):
    # Extracting features for each speaker (5 files per speakers)
    features = np.asarray(())

    for audio_file in os.listdir(train_path):
        # read the audio
        sr, audio = read(os.path.join(train_path, audio_file))
        # print(sr)
        # extract 40 dimensional MFCC & delta MFCC features
        vector = extract_features(audio, sr)

        if features.size == 0:
            features = vector
        else:
            features = np.vstack((features, vector))

    gmm = GaussianMixture(n_components=10, covariance_type='diag', max_iter=200, n_init=3)
    gmm.fit(features)

    # dumping the trained gaussian model
    picklefile = train_path.split('\\')[-2] + ".gmm"
    pickle.dump(gmm, open(models_path + picklefile, 'wb'))
    #print('+ modeling completed for speaker:', picklefile, " with data point = ", features.shape)


def comparing_models(models_path, UBM_path, file_to_test, limit=99):
    models = []
    speakers_names = []

    for model in os.listdir(models_path):
        models.append(pickle.load(open(os.path.join(models_path, model), 'rb')))
        speakers_names.append(model.split('.')[0])

    sr, audio = read(file_to_test)
    vector = extract_features(audio, sr)

    log_likelihood = np.zeros(len(models))

    for i in range(len(models)):
        gmm = models[i]  # checking with each model one by one
        scores = np.array(gmm.score(vector))
        log_likelihood[i] = scores.sum()
        # print(speakers_names[i], log_likelihood[i])

    ubm_model = pickle.load(open(UBM_path, 'rb'))
    gmm = ubm_model

    ubm_log_likelihood = np.array(gmm.score(vector))
    # print(ubm_log_likelihood)

    # sorted_log = log_likelihood.argsort()
    # print(sorted_log)
    # for index in sorted_log[-5:]:
    #     print(speakers_names[index], log_likelihood[index])

    winner = np.argmax(log_likelihood)

    # if log_likelihood[winner] > ubm_log_likelihood:
    #     # print(log_likelihood[winner], ubm_log_likelihood)
    #     return speakers_names[int(winner)]
    # else:
    #     return 'brak mowcy'

    # print(speakers_names[int(winner)], log_likelihood[winner])
    if limit == 99:
        score = log_likelihood[winner]/ubm_log_likelihood
        # print(score)

        if score < limit:
            return speakers_names[int(winner)]
        else:
            # print('UBM', ubm_log_likelikehood)
            # print(speakers_names[int(winner)], log_likelihood[winner])
            # print(score)
            return 'brak mowcy'

    else:
        if log_likelihood[winner] > ubm_log_likelihood:
            # print(ubm_log_likelihood)
            # print(speakers_names[int(winner)])
            return speakers_names[int(winner)]
        else:
            # print(ubm_log_likelihood)
            return 'brak mowcy'


def UBM(path, models_path):
    # Extracting features for each speaker (5 files per speakers)
    features = np.asarray(())

    for directory in os.listdir(path):
        print('Processing: ', os.listdir(path).index(directory)+1, '/', len(os.listdir(path)))

        audio_directory = os.path.join(path, directory)
        for audio_file in os.listdir(audio_directory):
            # read the audio
            sr, audio = read(os.path.join(audio_directory, audio_file))

            # extract 40 dimensional MFCC & delta MFCC features
            vector = extract_features(audio, sr)

            if features.size == 0:
                features = vector
            else:
                features = np.vstack((features, vector))

    print('Creating UBM model')
    gmm = GaussianMixture(n_components=10, covariance_type='diag', max_iter=200, n_init=3)
    gmm.fit(features)

    # dumping the trained gaussian model
    picklefile = "UBM.gmm"
    pickle.dump(gmm, open(models_path + picklefile, 'wb'))


# training_model(r'c:\Users\kajet\Desktop\magisterka\dane\Audio\Filtered\bonzer''\\', r'C:\Users\kajet\Desktop\magisterka\dane\Modele\All''\\')
# comparing_models(r'C:\Users\kajet\Desktop\magisterka\dane\Modele\All''\\', r'C:\Users\kajet\Desktop\magisterka\dane\Modele\UBM.gmm', r'c:\Users\kajet\Desktop\magisterka\dane\Audio\Testy_filtered\anthonyschaller.wav')

# UBM(r'c:\Users\kajet\Desktop\magisterka\dane\Audio\Filtrowane\Uczace''\\', r'C:\Users\kajet\Desktop\magisterka\dane\Modele''\\')
