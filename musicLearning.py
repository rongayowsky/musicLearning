#!/usr/bin/env python3

import argparse
# import errno
# import os
# from os import path

# Define argument parser
help_description =  """
                        Store and manage links and file paths of learning material for songs!
                        Material can be recalled based on song name.
                    """
parser = argparse.ArgumentParser(description=help_description)
## Action flags, only one can be used at a time
command = parser.add_mutually_exclusive_group(required=True)
command.add_argument('--add', action='store_true', help='Mutually exclusive flag to add a new song')
command.add_argument('--edit', action='store_true', help='Mutually exclusive flag to edit an existing song.')
command.add_argument('--remove', action='store_true', help='Mutually exclusive flag to remove an existing song')
command.add_argument('--display', action='store_true', help='Mutually exclusive flag to display all stored songs')
command.add_argument('--learn', action='store_true', help='Mutually exclusive flag to open stored media for a song')
## Specific arguments to detail songs, files, paths
parser.add_argument('-s', '--song', type=str, required=False, nargs='?',
                    help='The song to be affected')
parser.add_argument('-a', '--artist', type=str, required=False, nargs='?',
                    help='The artist of the song. Optional.')
parser.add_argument('-l', '--link', type=str, required=False, nargs='?',
                    help='A link to material on the internet. Optional.')
parser.add_argument('-f', '--file', type=str, required=False, nargs='?',
                    help='A filepath to material on your local machine. Optional.')
args = parser.parse_args()

# Validate user input, select which function will be run.
def main():
    if args.display:
        display_songs()
    elif not args.song:
        print('A song argument must be provided for this operation.')
    elif args.add:
        add()
    elif args.edit:
        edit()
    elif args.remove:
        remove()
    elif args.learn:
        display_material()

# Add a song into the storage medium
def add():
    print("I will add a song to the storage medium!")

# Edit a song from the storage medium
def edit():
    print("I will edit a song from the storage medium!")

# Remove a song from the storage medium
def remove():
    print("I will remove a song from the storage medium!")

# List all the songs stored in the storage medium
def display_songs():
    print("I will display existing songs in the storage medium!")

# Open the webpages and files stored for a song
def display_material():
    print("I will display the stored media so you can practice a song.")

if __name__ == "__main__":
    main()