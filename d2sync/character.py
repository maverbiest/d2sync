#!/usr/bin/env python

import os
import time

__all__ = [
    "Character",
]

class Character(object):
    def __init__(self, char_name):
        self.name = char_name
        self.creation_time = None
        self.last_modified = None
        self.files = None

    def get_name(self):
        return self.name

    def set_creation_time(self, creation_time):
        if self.creation_time:
            raise AttributeError("Character '{}' already has a creation time!".format(self.name))
        self.creation_time = creation_time

    def get_creation_time(self):
        return self.creation_time

    def set_last_modified(self, last_modified):
        if self.last_modified:
            raise AttributeError("Character '{}' already has a last modief time!".format(self.name))
        self.last_modified = last_modified

    def get_last_modified(self):
        return self.last_modified

    def add_file(self, new_file):
        if not self.files:
            self.files = [new_file]
        elif not new_file in self.files:
            self.files.append(new_file)

    def epoch_to_local(self, epoch_time):
        return time.asctime(time.localtime(epoch_time))

    def __str__(self):
        return "Name: {}\n\tcreated: {}\n\tlast modified: {}".format(
            self.get_name(),
            self.epoch_to_local(self.get_creation_time()),
            self.epoch_to_local(self.get_last_modified())
        )

    def __key(self):
        return (self.name, self.creation_time)

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if not isinstance(other, Character):
            return False
        if not self.creation_time:
            raise ValueError("Character '{}' is not complete".format(self.name))
        return self.__key() == other.__key()

    def __ne__(self, other):
        return not self.eq(other)
