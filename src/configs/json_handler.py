import json
import os

class JSONHandler:
    def __init__(self, filepath):
        self.filepath = filepath

    def load(self):
        """Lädt die JSON-Daten aus der Datei."""
        if not os.path.exists(self.filepath):
            return {}
        with open(self.filepath, 'r') as file:
            return json.load(file)

    def save(self, data):
        """Speichert die JSON-Daten in der Datei."""
        with open(self.filepath, 'w') as file:
            json.dump(data, file, indent=4)

    def read_value(self, key):
        """Liest einen Wert aus den JSON-Daten."""
        data = self.load()
        return data.get(key, None)

    def write_value(self, key, value):
        """Schreibt einen Wert in die JSON-Daten."""
        data = self.load()
        data[key] = value
        self.save(data)

# Beispielverwendung:
filepath = 'settings.json'
json_handler = JSONHandler(filepath)
