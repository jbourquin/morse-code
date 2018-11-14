# Morse Code

In this project we will build a morse code audio generator using Python.

## Project Setup

In your developer directory, clone this repository using git:

    cd ~/Developer
    git clone https://github.com/bourqujl/morse-code.git

Change to the morse-code project directory and create a new virtual environment:

    cd morse-code
    mkvirtualenv -a . morse-code

Setup the build environment for your target operating system:

### Mac

Install the xcode command line tools if you don't already have them installed:

    xcode-select --install

### Ubuntu

Install the following developer libraries using apt-get:

    sudo apt-get install -y python3-dev libasound2-dev

### CentOS

Install the following developer libraries using yum:

    sudo yum install alsa-lib-devel

## Python Depedencies

Install the following python modules into your virtual environment using PIP:

```
pip install numpy simpleaudio
```

Test that the install of simpleaudio was successful, open a python intrepreter by typing `python` in your virtual environment console. In the python intrepreter, type the following commands:

```
import simpleaudio.functionchecks as fc
fc.LeftRightCheck.run()
```

You should here a piano note from each of your computer speakers.

## Assignment

Morse code is a method of encoding letters and numbers as a sequence of dots
and dashes. For example, the letter 'S' is represented by three dots '...' 
while an 'O' is represented by three dashes '---' giving you the familiar
sequence of 'S.O.S.': '...---...'

To complete this assignment, you will write two functions. 1) One function
to translate letters into their morse code representation and 2) a second
function to play the necessary audio over your computuer speakers.

### Part 1

Write a function named 'morse_code' that accepts a letter as a positional
argument and returns the morse code representation of that letter as a string
of dots (.) and dashes (-). For example, if I pass the letter 'S' to this 
function I would expect it to return a string with three dots '...':

    mark = morse_code('s')
    mark == '...'

Likewise with the letter 'O', I would expect the function to return a string
with three dashes:

    mark = morse_code('o')
    mark == '---'

In your function use a period (.) to represent dots and a dash/minus (-) to represent dashes.
The function should be case insensitive, meaning that it will return the correct morse code
representation of the letter regardless if I pass it a lower case 'a' or an upper case 'A'.

*Hint: Use the .lower() method on a string to convert your argument to lower case.*

The function should return an empty string for characters other than letters, i.e. numbers or punctuation marks:

    mark = morse_code('1')
    mark == ''

You can use the following website for the morse code representation of each letter:

https://www.military.com/join-armed-forces/guide-to-the-military-phonetic-alphabet.html/amp

### Part 2

For the second part of the assignment, you will complete the 'transmit' function below
to play audio tones.

    def transmit(message):
        time_unit = 0.06  # (secs)
        dot_tone = tone(time_unit)
        dash_tone = tone(3 * time_unit)

        # <-- Your Code Goes Here -->

I will show you later in the tutorial how to play the dot_tone and dash_tone audio.

Morse code is composed of 5 elements:

1. short mark, dot or "dit": "dot duration" is one time unit long
2. longer mark, dash or "dah": three time units long
3. inter-element gap between the dots and dashes within a character: one dot duration or one unit long
4. short gap (between letters): three time units long
5. medium gap (between words): seven time units long

For this assignment the time unit will be 60 milliseconds (0.06 seconds).

So what does this all mean? It means that for a 'dot' the computer should play an audio
tone for 0.06 seconds and for a 'dash' the computer should play the same tone for 0.18
seconds. The gap (silence) between each dot or dash is 0.06 seconds long, the gap between
each letter sequence is 0.18 seconds long, and the gap between each word is 0.42 seconds
long.

The transmit function accepts one positional argument called 'message'. Message is what
it sounds like a string of words (seperated by spaces) that a caller wants converted
to morse code audio tones:

    transmit('hello world')

To complete the function, you will first need to convert the message to an array
of words that you can loop through. This can be accomplished with the '.split()'
method like so:

    message = 'hello world'
    words = message.split()
    words == ['hello', 'world']

Split will return a list of each 'space' seperated word in message allowing you
to iterate through each word in message using a for loop:

    for word in words:
        print(word)

The next step is to iterate through each letter in the word and convert it to
morse code. To do this, use a for loop with 'word' as the thing you
want to iterate through like so:

    for letter in word:
        print(letter)

Python makes it supper easy to iterate through each letter (character) of a string.
Pass each letter in the word to your morse code function you built in step 1, the
function should return a string representing the dots and dashes of the letter.
In this example we will call it the letter's 'marks':

    marks = morse_code(letter)
    print(marks)

Now we have a string of dots and dashes that we would like the computer to convert
to a series of audio tones. Like the previous step, we will iterate through each
character in the 'marks' string and play an audio tone:

    for mark in marks:
        if mark == '.':
            playback = dot_tone.play()
            playback.wait_done()
        elif mark == '-':
            playback = dash_tone.play()
            playback.wait_done()

'dot_tone' and 'dash_tone' are already defined in the transmit function, so use this code to play the audio tone over the computer speakers.

We need one more thing to complete the assignment, a way to insert the silent gap between each morse code element:

- 1 time unit between each dot or dash
- 3 time units between each letter
- 7 time units between each word

To do this we will use the 'time.sleep()' function to pause program execution. The sleep function tells the computer to wait a certain amount of time before going on to the next step. For example:

    print('Hello')
    time.sleep(3)  # Wait 3 seconds
    print('World')

The sleep function accepts 1 argument, the number of seconds to wait before executing the next step. To make the computer wait a fraction of a second, use a floating point number like so:

    print('Hello')
    time.sleep(0.06)  # Wait 60 milliseconds
    print('World')

You will need to use the sleep function at least 3 times in the transmit function to insert the necessary gaps for the morse code audio tones.

## Run

To run the program, pass the file name to the python intrepreter:

    python morse_code.py

The program will prompt you to input a message, type anything you like and hit enter to hear the morse code representation:

    Message: hello world
