import json

## File Paths

CONFIGS_PATH = './config.json'
SCORE_FILE_PATH = './score.csv'


## Functions

def cargar_configs(configs_path: str):
    with open(configs_path, 'r') as config:
        configs = json.load(config)
    return configs

def save_score(score_file_path: str, data: str):
    with open(score_file_path, 'a') as score_file:
        score_file.write(data)