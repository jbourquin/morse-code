# Morse Code

In this project we will build a morse code audio generator using Python.

## Project Setup

In your developer directory, clone this repository using git:

```
cd ~/Developer
git clone git@github.com:bourqujl/morse-code.git
```

Change to the morse-code project directory and create a new virtual environment:

```
cd morse-code
mkvirtualenv -a . morse-code
```

Setup the build environment for your target operating system:

### Mac

Install the xcode command line tools if you don't already have them installed:

```
xcode-select --install
```

### Ubuntu

Install the following developer libraries using apt-get:

```
sudo apt-get install -y python3-dev libasound2-dev
```

### CentOS

```

```

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

## Source Code

Open morse-code.py in your editor and follow the instructions in the comment section to complete the assignment.