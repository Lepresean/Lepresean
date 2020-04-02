# Lepresean
Raspberry Pi Omnichord

The goal is to use a Raspberry Pi to run a real time digital musical instrument inspired by the Suzuki Omnichord.
Working on figuring out how to do that.
Can't be that hard right?

Updates to follow unless I get bored.

%%%%%%%%%%%% Notes %%%%%%%%%%%%%%%%%%%%
need some kind of music player library like pygame or omxplayer to play the sound files

sound files .wav must be Signed 16 bit Little Endian (S16_LE) or 8-bit (U8) to play with aplay from bash prompt or with pygame
conversion with ffmpeg is not difficult:
in windows cmd in directory with .wav files in 32 bit to convert to 16 bit .wav (need ffmpeg.exe in folder):
>ffmpeg -i input.wav -acodec pcm_s16le output.wav
or use ffmpeg batch AV converter (open source on interweb)

pygame only working on python 2 it seems, maybe just a syntax issue?

I needed to install python-gpiozero for raspberry pi (must have internet connection)
in bash terminal on Pi:
>sudo apt-get install python-gpiozero
might want to update everything first: >sudo apt-get install update

wiring should go ground to button, button side 2 to gpio pin
point to gpiopin in python using Button(gpio pin #) command
gpio pin layout shown in gpio-pinout-diagram.png
don't ever connect wire from voltage gpio pins to other ones without some resistor or something, it is bad
gpio pins have 2 numbers to confuse you - pay attention to the ones on the outside labels in the picture, not the numbers that are written on the pins themselves

all the button does is momentarily complete the circuit when pressed, so it is possible to just tap the two wires together without using a button at all. This is what I am doing for now in lieu of a breadboard or soldering.