#!/usr/bin/env python
import argparse
import os
import time

from file_loader import FileLoader

def parser():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--directory", "-d", required=False, type=str
    )

    return parser.parse_args()

def main():
    args = parser()

    if args.directory:
        files = FileLoader(path=args.directory)
    elif os.path.exists("path_cache.json"):
        files = FileLoader(cache="path_cache.json")
    else:
        raise ValueError("Specify path or cache for save files")

    for char in files.characters.keys():
        print("Character: {}".format(char))
        for file in files.characters[char]:
            print("\t{}, {}".format(file[0], time.asctime(time.gmtime(file[1]))))

if __name__ == '__main__':
    main()
