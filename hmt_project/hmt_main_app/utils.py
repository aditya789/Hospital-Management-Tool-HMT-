import os
from hmt_project.settings import BASE_DIR
import json

def get_defaults():
    defaults_directory = os.path.join(BASE_DIR, 'hmt_main_app/defaults.json')
    json_data = open(defaults_directory)
    defaults = json.load(json_data)  # deserialises it
    json_data.close()
    return defaults
