import time
from pygame import mixer
import keyboard
def on_key_press(event):
    if event.event_type == keyboard.KEY_DOWN:
        mixer.init()
        mixer.music.load("spongebob-squarepants-mr.mp3")
        mixer.music.play()
keyboard.on_press(on_key_press)
keyboard.wait()