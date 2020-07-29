#!/usr/bin/env python
import argparse
import os
import time

from character_loaders import LocalCharacterLoader
from build_service import ServiceBuilder

def parser():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--directory", "-d", required=False, type=str
    )

    return parser.parse_args()

def main():
    args = parser()

    files = LocalCharacterLoader(path=args.directory)
    files.pretty_print_chars()

    builder = ServiceBuilder()
    service = builder.build_service()

    results = service.files().list(
        pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))

if __name__ == '__main__':
    main()
