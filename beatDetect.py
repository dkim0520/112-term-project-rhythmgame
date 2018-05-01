###Beat Detection from https://stackoverflow.com/questions/12344951/detect-beat-and-play-wav-file-in-a-synchronised-manner
import pyaudio
import numpy
import wave
import aubio
import pygame

class SimpleBeatDetection(object):
    """
    Simple beat detection algorithm from
    http://archive.gamedev.net/archive/reference/programming/features/beatdetection/index.html
    """
    def __init__(self, history = 43):
        self.local_energy = numpy.zeros(history) # a simple ring buffer
        self.local_energy_index = 0 # the index of the oldest element

    def detect_beat(self, signal):

        samples = signal.astype(numpy.int) # make room for squares
        # optimized sum of squares, i.e faster version of (samples**2).sum()
        instant_energy = numpy.dot(samples, samples) / float(0xffffffff) # normalize

        local_energy_average = self.local_energy.mean()
        local_energy_variance = self.local_energy.var()

        beat_sensibility = (-0.0025714 * local_energy_variance) + 1.15142857
        beat = instant_energy > beat_sensibility * local_energy_average

        self.local_energy[self.local_energy_index] = instant_energy
        self.local_energy_index -= 1
        if self.local_energy_index < 0:
            self.local_energy_index = len(self.local_energy) - 1
        return beat

#skeleton PyAudio code from PyAudio documentation
#wf = wave.open("bach.wav", "rb")
class Record(object):
    def __init__(self):
        self.record = False

    def micPitchVolumeDetect(self, keyDown):
        p = pyaudio.PyAudio()
        FORMAT = pyaudio.paFloat32
        CHANNELS = 2
        RATE = 44100
        CHUNK = 2048
        HOP_SIZE = CHUNK//2
        PERIOD_SIZE_IN_FRAME = HOP_SIZE

        audio = pyaudio.PyAudio()
         
        pitchDetect = aubio.pitch("default", CHUNK, HOP_SIZE*2, RATE)
        pitchDetect.set_unit("midi")
        pitchDetect.set_silence(-40)

        # start Recording
        stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=PERIOD_SIZE_IN_FRAME)

        data = stream.read(HOP_SIZE)
        #beat = SimpleBeatDetection()
        count = 0
        while keyDown(pygame.K_r) and self.record:
            # stream.write(data)
            count += 1
            data = stream.read(PERIOD_SIZE_IN_FRAME)
            # signal = numpy.frombuffer(data, numpy.int16)
            # (beat.detect_beat(signal))

            #volume detection from https://gist.github.com/notalentgeek/48aeab398b6b74e3a9134a61b6b79a36
            samples = numpy.fromstring(data, dtype = aubio.float_type)
            volume = numpy.sum(samples**2)/len(samples)

            volume = "{:6f}".format(volume)
            #print(str(volume))

            #pitch detection from same website as above
            pitch = pitchDetect(samples)[0]
            if count % 5 == 0 and pitch < 100:
                print(pitch)

        stream.stop_stream()
        stream.close()

        p.terminate()


# record = Record()
# record.micPitchVolumeDetect()