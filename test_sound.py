import pygame
from gpiozero import Button
#must have pygame and gpiozero installed already
#I haven't got pygame to work on python3 yet

pygame.mixer.pre_init(44100)#44100 is freq of sound files
pygame.init()

#create variables to contain sounds using pygame module
#obviously the files need to be at the path you specify
a_c = pygame.mixer.Sound("/home/pi/Omnichord/16bit_samples/Omnichord/a/a-chord.wav")
a0 = pygame.mixer.Sound("/home/pi/Omnichord/16bit_samples/Omnichord/a/a0.wav")
a1 = pygame.mixer.Sound("/home/pi/Omnichord/16bit_samples/Omnichord/a/a1.wav")

#create buttons for the gpio pins you are using
btn_a_c = Button(17)
btn_a0 = Button(27)
btn_a1 = Button(22)

#define functions to play each sound and output status
def a_chord():
    a_c.play()
    print("a chord")

def a0_note():
    a0.play()
    print("a 0")

def a1_note():
    a1.play()
    print("a 1")

#define triggers for functions (link buttons to functions)
btn_a_c.when_pressed = a_chord
btn_a0.when_pressed = a0_note
btn_a1.when_pressed = a1_note

#pygame.time.wait(1000) #need this wait statement to play the sound if not using buttons
                        #otherwise the program will move on before playing anything

#pygame.quit()
