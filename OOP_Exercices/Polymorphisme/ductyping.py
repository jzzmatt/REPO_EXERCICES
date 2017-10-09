'''
DUC TYPING
differently to POLYMORPHISME
duc typing, doesnt use any variable class of subclass
'''

class FlacFile:
    def __init__(self, filename):
        if not filename.endswith(".flac"):
            raise Exception("Invalid file Format")

        self.filename = filename


    def play(self):
        print("playing {} as flac".format(self.filename))