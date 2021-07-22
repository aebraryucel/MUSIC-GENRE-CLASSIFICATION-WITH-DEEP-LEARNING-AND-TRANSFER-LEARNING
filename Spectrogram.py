import os
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import splitfolders



def spectrogram():
    directory = r'E:\DATASETS\genres_original\pop'

    for filename in os.listdir(directory):

        os.chdir(r'E:\DATASETS\genres_original\pop')
        if filename.endswith(".wav"):
            audio, sr=librosa.load(filename)
            spect=librosa.stft(audio,hop_length=512,n_fft=2048)
            spect = librosa.amplitude_to_db(np.abs(spect), ref=np.max)
            librosa.display.specshow(spect, sr=sr, hop_length=512)
            os.chdir(r'E:\DATASETS\spectrograms\pop')
            fname=filename+".png"
            plt.savefig(fname)
            plt.clf()




def mel_spectrogram():
    directory = r'E:\DATASETS\genres_original\country'

    for filename in os.listdir(directory):

        os.chdir(r'E:\DATASETS\genres_original\country')
        if filename.endswith(".wav"):
            audio, sr=librosa.load(filename)
            mel_s=librosa.feature.melspectrogram(audio,sr=sr,n_fft=2048,hop_length=512,n_mels=13)
            mel_sp = librosa.amplitude_to_db(np.abs(mel_s), ref=np.max)
            librosa.display.specshow(mel_sp,sr=sr,hop_length=512)
            os.chdir(r'E:\DATASETS\mel_spectrogramss\country')
            fname=filename+".png"
            plt.savefig(fname)
            plt.clf()

            mel_delta1=librosa.feature.delta(mel_sp)
            librosa.display.specshow(mel_delta1,sr=sr,hop_length=512)
            os.chdir(r'E:\DATASETS\mel_spectrograms_delta11\country')
            plt.savefig(fname)
            plt.clf()

            mel_delta2=librosa.feature.delta(mel_sp,order=2)
            librosa.display.specshow(mel_delta2,sr=sr,hop_length=512)
            os.chdir(r'E:\DATASETS\mel_spectrograms_delta22\country')
            plt.savefig(fname)
            plt.clf()




def split_folders():
    splitfolders.ratio("E:\DATASETS\mel_spectrograms", output="E:\DATASETS\mel_spectrograms_split3", seed=1337, ratio=(.9, .0, .1),group_prefix=None)  # default values







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mel_spectrogram()


