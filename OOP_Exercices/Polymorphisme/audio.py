'''
POLYMORPHISME EXAMPLE
all audio files check to ensure that a valid extension was given
observe, that the init method from the parent , are able to access ext class variable on sublcass
'''


class AudioFile:
    def __init__(self, filename):
        if not filename.endswith(self.ext):  #the self.ext, are polymorphic read this attribute on the future subclass
            raise Exception("Invalid file Format")

        self.filename = filename


class MP3File(AudioFile):
    ext = 'mp3'
    def play(self):
        print("playing {} as mp3".format(self.filename))



class WavFile(AudioFile):
    ext = 'wav'
    def play(self):
        print("playing {} as wav".format(self.filename))



class OggFile(AudioFile):
    ext = 'ogg'
    def play(self):
        print("playing {} as ogg".format(self.filename))



ogg = OggFile("myfile.ogg")
ogg.play()

mp3 = MP3File("myfile.mp3")
mp3.play()


not_an_mp3 = MP3File("myfile.nx")
