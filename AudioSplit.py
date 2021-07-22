from pydub import AudioSegment
import os


def splitter():
    directory = r'E:\DATASETS\genres_original\rock'
    os.chdir(r'E:\DATASETS\genres_original\rock')

    for filename in os.listdir(directory):
        if filename.endswith(".wav"):


            newAudio = AudioSegment.from_wav(filename)

            first = newAudio[0:6000]
            second = newAudio[6000:12000]
            third = newAudio[12000:18000]
            fourth = newAudio[18000:24000]
            fifth = newAudio[24000:30000]

            firststr= filename[0:10] + "_1" + filename[-4:]
            secondstr= filename[0:10] + "_2" + filename[-4:]
            thirdstr= filename[0:10] + "_3" + filename[-4:]
            fourthstr= filename[0:10] + "_4" + filename[-4:]
            fifthstr= filename[0:10] + "_5" + filename[-4:]

            first.export(firststr, format="wav")
            second.export(secondstr, format="wav")
            third.export(thirdstr, format="wav")
            fourth.export(fourthstr, format="wav")
            fifth.export(fifthstr, format="wav")

            os.remove(filename)

        else:
            continue


if __name__ == "__main__":
    splitter()
