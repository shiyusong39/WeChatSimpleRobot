from pydub import AudioSegment
import os
import speech_recognition as sr
from os import path


AudioSegment.ffmpeg = os.getcwd()+'\\ffmpeg.exe'
AudioSegment.ffprobe = os.getcwd()+'\\ffprobe.exe'

def dealMp3(filePath,fileName):
    sound = AudioSegment.from_mp3(filePath)
    #获取原始pcm数据
    data=sound._data
    sound_wav = AudioSegment(
        #指定原始pcm文件
        data = data,
        #指定采样深度，可选值1,2,3,4
        # 2 byte (16 bit) samples
        sample_width = 2,
        #指定采样频率
        # 44.1 kHz frame rate
        # 16kHz frame rate
        frame_rate = 16000,
        #指定声道数量
        # stereo or mono
        channels = 1
    )
    #导出wav文件
    sound_wav.export(fileName,format='wav')

    isDeal = os.path.exists(os.getcwd()+'\\'+fileName)

    #如果wav文件生成了就删除mp3文件
    if isDeal:
        #删除mp3文件
        os.remove(filePath)

    return isDeal

#语音转文字
def voice2Text(file_name):

    voice_file = path.join(path.dirname(path.realpath(__file__)), file_name)
    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(voice_file) as source:
        audio = r.record(source)
    try:
        content = r.recognize_google(audio, language='zh-CN')
        # print("Google Speech Recognition:" + content)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Google Speech Recognition error; {0}".format(e))

    return content or '无法翻译'



# def main():
#     voice_file = '190726-142241.mp3'
#     # filePath = os.getcwd()+'\\'+voice_file
#     fileName = voice_file.replace('mp3','wav')
#     # reply = dealMp3(filePath,fileName)
#     #音频文件
#     voice2Text(fileName)
#
#     #如果该py文件作为脚本来执行时，会执行'__mian__'方法，如果作为第三方model被引用，则不会执行
# if __name__ == '__main__':
#     main()