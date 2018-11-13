import time
import numpy as np 
import simpleaudio as sa 

# This function generates the audio tone by creating a 650hz SIN wave
def tone(duration, frequency=650, sampling_rate=44100):
    """
    Generates a simple audio wave object from a specified frequency and duration.
    """
    samples = np.sin(2*np.pi*np.arange(sampling_rate*duration)*frequency/sampling_rate)
    samples *= 32767 / np.max(np.abs(samples))  # Normalize to 16 bit range
    samples = samples.astype(np.int16)
    wave = sa.WaveObject(samples, 1, 2, sampling_rate)
    return wave


# <-- Write Your Morse Code Function Here -->


# <-- Complete The Transmit Function -->
def transmit(message):

    # time unit (secs)
    time_unit = 0.06  
    
    # see README.md for use
    dot_tone = tone(time_unit)  
    dash_tone = tone(3 * time_unit)

    # <-- Your Code Goes Here -->


# <-- Do Not Modify or Move -->
if __name__ == '__main__':
    message = input('Message: ') 
    transmit(message)
