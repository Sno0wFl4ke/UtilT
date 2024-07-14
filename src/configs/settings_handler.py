from configs.json_handler import json_handler

def load_settings():
    global DOWNLOAD_PATH
    settings = json_handler.load()
    DOWNLOAD_PATH = settings.get('download_path', '')
