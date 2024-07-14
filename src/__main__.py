import sys
import os
from module_registry import register, get_registered_functions
from configs.json_handler import json_handler
from configs.settings_handler import load_settings

DOWNLOAD_PATH = ''

# Module hier registrieren
def register_modules():
    register('funcmodules.downloader', 'download', 'Download Videos from YT, Insta or TikTok')

def display_menu(functions_dict):
    print("Bitte wählen Sie eine Funktion aus:")
    option_number = 1
    function_mapping = {}
    
    for display_name, func in functions_dict.items():
        print(f"{option_number}: {display_name}")
        function_mapping[option_number] = func
        option_number += 1
    print(f"{option_number}: Beenden")
    return function_mapping, option_number

def main():

    print("Loading settings...")
    load_settings()
    print(f"Settings loaded successfully. Download Path: {DOWNLOAD_PATH}")
    print("Loading functions...")
    register_modules()
    print("Functions loaded successfully")
    os.system('cls||clear')
    functions_dict = get_registered_functions()

    while True:
        function_mapping, exit_option = display_menu(functions_dict)
        choice = input("Geben Sie die Nummer der Funktion ein, die Sie ausführen möchten: ")

        try:
            choice_num = int(choice)
            if choice_num == exit_option:
                print("Programm beendet.")
                sys.exit()
            
            selected_func = function_mapping.get(choice_num)
            
            if selected_func:
                selected_func()
            else:
                print("Ungültige Auswahl. Bitte versuchen Sie es erneut.")

        except ValueError:
            print("Ungültige Auswahl. Bitte geben Sie eine Zahl ein.")

if __name__ == '__main__':
    main()
