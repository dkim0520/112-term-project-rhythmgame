###Beat Detection from https://stackoverflow.com/questions/12344951/detect-beat-and-play-wav-file-in-a-synchronised-manner
import pyaudio
import numpy
import wave

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

CHUNK = 1024

wf = wave.open("bach.wav", "rb")

p = pyaudio.PyAudio()

stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True)

data = wf.readframes(CHUNK)
beat = SimpleBeatDetection()
while len(data) > 0:
    # stream.write(data)
    data1 = wf.readframes(CHUNK)
    signal = numpy.frombuffer(data1, numpy.int16)
    print(beat.detect_beat(signal))

stream.stop_stream()
stream.close()

p.terminate()