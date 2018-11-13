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


MORSE_CODE_MARKS = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..'
}


def morse_code(char):
    return MORSE_CODE_MARKS.get(char.lower(), '')


# <-- Complete The Transmit Function -->
def transmit(message):

    # time unit (secs)
    time_unit = 0.06  
    
    # see README.md for use
    dot_tone = tone(time_unit)  
    dash_tone = tone(3 * time_unit)

    # Loop through each word in the message
    for word in words:

        # Loop through each letter in the word
        for letter in word:

            # Convert the letter to morse code marks (dots and dashes)
            marks = morse_code(letter)
            
            # Loop through each mark and play a tone
            for mark in marks:
                
                # Dots are one time unit long
                if mark == '.':
                    playback = dot_tone.play()
                    playback.wait_done()
                
                # Dashes are 3 time units long
                elif mark == '-':
                    playback = dash_tone.play()
                    playback.wait_done()

                # Inter-element gap
                time.sleep(time_unit)

            # Gap between letters
            time.sleep(3 * time_unit)

        # Gap between words
        time.sleep(7 * time_unit)


# <-- Do Not Modify or Move -->
if __name__ == '__main__':
    message = input('Message: ') 
    transmit(message)
