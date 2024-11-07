import pygame.mixer as mixer

class SoundManager:
    
    def __init__(self):
        mixer.init()
        self.__sound = None
    
    def play_sound(self, sound_path: str):
        self.__sound = mixer.Sound(sound_path)
        self.__sound.set_volume(0.8)
        self.__sound.play()
    
    def play_music(self, music_path: str):
        mixer.music.load(music_path)
        mixer.music.set_volume(0.4)
        mixer.music.play(loops=-1)
    
    def stop_music(self):
        mixer.music.stop()
    
    def stop_sound(self):
        self.__sound.stop()