"""

"""

import time
import numpy as np 
import simpleaudio as sa 

def tone(frequency, duration, fs=44100):
    """
    Generates a simple audio wave object from a specified frequency and duration.
    """
    samples = np.sin(2*np.pi*np.arange(fs*duration)*frequency/fs)
    samples *= 32767 / np.max(np.abs(samples))  # Normalize to 16 bit range
    samples = samples.astype(np.int16)
    wave = sa.WaveObject(samples, 1, 2, fs)
    return wave


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

def transmit(message, frequency=650):
    """
    International Morse Code Elements:
    1. short mark, dot or "dit": "dot duration" is one time unit long
    2. longer mark, dash or "dah": three time units long
    3. inter-element gap between the dots and dashes within a character: one dot duration or one unit long
    4. short gap (between letters): three time units long
    5. medium gap (between words): seven time units long

    Assuming 20 WPM and PARIS as the standard word, the time unit is 60 milliseconds.
    """
    time_unit = 0.06  # time unit (secs)
    dot_tone = tone(frequency, time_unit)
    dash_tone = tone(frequency, 3 * time_unit)

    # split the message into words
    words = message.split()

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


if __name__ == '__main__':
    message = input('Message: ') 
    transmit(message)
