#!/usr/bin/env

import os
import sys
import json

class FileLoader(object):
    def __init__(self, path=None, cache=None):
        if path:
            self.path = self.set_new_path(path)
        elif cache:
            with open(cache, "r") as f:
                self.path = json.load(f)["path"]
        else:
            raise ValueError("Specify path or cache for save files")

        self.characters = self.load_characters()

    def set_new_path(self, path):
        if not os.path.exists(path):
            raise ValueError("Specified path to save files does not exist")
        cache_dict = {"path": path}
        with open("path_cache.json", "w") as cache:
            json.dump(cache_dict, cache)
        return path

    def get_abs_path(self, file_name):
        return "{}/{}".format(self.path, file_name)

    def load_characters(self):
        char_files = [f for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, f))]
        character_dict = dict()
        for char_file in char_files:
            character = char_file.split(".")[0]
            if character in character_dict:
                character_dict[character].append((char_file, os.path.getmtime(self.get_abs_path(char_file))))
            else:
                character_dict[character] = [(char_file, os.path.getmtime(self.get_abs_path(char_file)))]
        return character_dict

    # def get_modified_datetime(self, file_name):
    #     return time.asctime(time.gmtime(os.path.getmtime(self.get_abs_path(file_name))))
    #
    # def print_character_files(self):
    #     for char in self.characters.keys():
    #         print("Character: {}".format(char))
    #         [print("\t{}, {}".format(i, self.get_modified_datetime(i))) for i in self.characters[char]]
