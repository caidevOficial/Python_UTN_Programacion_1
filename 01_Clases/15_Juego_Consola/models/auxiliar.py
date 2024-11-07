import json

## File Paths

CONFIGS_PATH = './config.json'
SCORE_FILE_PATH = './score.csv'

## Sound Paths

SUCCESS_SOUND = './assets/sound/success.mp3'
LOSE_SOUND = './assets/sound/lose.mp3'
END_LEVEL_SOUND = './assets/sound/end_level.mp3'
MUSIC_SOUND_L1 = './assets/music/level_1.mp3'
MUSIC_SOUND_L2 = './assets/music/level_2.mp3'
MUSIC_SOUND_L3 = './assets/music/level_3.mp3'

## Functions

def cargar_configs(configs_path: str):
    with open(configs_path, 'r') as config:
        configs = json.load(config)
    return configs

def save_score(score_file_path: str, data: str):
    with open(score_file_path, 'a') as score_file:
        score_file.write(data)