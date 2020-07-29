#!/usr/bin/env

import os
import sys
import json

from character import Character

__all__ = [
    "CharacterLoader",
    "LocalCharacterLoader",
]

class CharacterLoader(object):
    def __init__(self, path=None):
        if path:
            self.path = self.set_new_path(path)
        else:
            try:
                with open("config/path_cache.json", "r") as f:
                    self.path = json.load(f)["path"]
            except FileNotFoundError:
                print("ERROR: No directory for Diablo II saves was specified and no cache could be found.")
                sys.exit(1)

        self.characters = None

    def set_new_path(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError("Specified path to save files does not exist")
        with open("config/path_cache.json", "w") as cache:
            json.dump({"path": path}, cache)
        return path

    def load_characters(self):
        pass


class LocalCharacterLoader(CharacterLoader):
    def __init__(self, path=None):
        super().__init__(path)
        self.characters = self.load_characters()

    def get_abs_path(self, file_name):
        return "{}/{}".format(self.path, file_name)

    def load_characters(self):
        char_files = [f for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, f))]
        character_dict = dict()
        for char_file in char_files:
            char_name, ext = char_file.split(".")[0], char_file.split(".")[1]

            try:
                character_dict[char_name].add_file(char_file)
            except KeyError:
                new_char = Character(char_name)
                new_char.add_file(char_file)
                character_dict[char_name] = new_char

            if ext == "key":
                creation_time = os.path.getmtime(self.get_abs_path(char_file))
                character_dict[char_name].set_creation_time(creation_time)
            elif ext == "d2s":
                last_modified = os.path.getmtime(self.get_abs_path(char_file))
                character_dict[char_name].set_last_modified(last_modified)

        return character_dict

    def pretty_print_chars(self):
        print("-"*50)
        print("Found {} Diablo II characters locally".format(len(self.characters)))
        print("-"*50)
        [print(i) for i in self.characters.values()]
        print("-"*50)
