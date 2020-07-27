#!/usr/bin/env python
import argparse
import os
import time

from character_loaders import LocalCharacterLoader

def parser():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--directory", "-d", required=False, type=str
    )

    return parser.parse_args()

def main():
    args = parser()

    if args.directory:
        files = LocalCharacterLoader(path=args.directory)
    elif os.path.exists("path_cache.json"):
        files = LocalCharacterLoader(cache="path_cache.json")
    else:
        raise ValueError("No file specified and no cache could be found.")

    files.pretty_print_chars()

if __name__ == '__main__':
    main()
