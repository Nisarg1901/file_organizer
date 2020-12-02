import os
import sys
import shutil
import subprocess

PDF = ['pdf', 'enc', 'epub']
WORD = ['docx', 'doc', 'Docx']
IMAGE = ['jpg', 'jpeg', 'png', 'gif', 'tiff', 'raw', 'PNG']
AUDIO = ['mp3', 'aac', 'ogg', 'wav', 'aiff', 'm4a', 'wma', ]
PROGRAM = ['py', 'c', 'cpp', 'java', 'php', 'js', ]
EXECUTABLES = ['exe',]

def get_extention_list(choice):
    '''
    Returns list of possible extentions according to the choice.

    :param choice: User's Choice According to the Menu.
    :return: list of possible extentions.
    '''
    if (choice == '1'):
        return PDF
    elif (choice == '2'):
        return WORD
    elif (choice == '3'):
        return IMAGE
    elif (choice == '4'):
        return AUDIO
    elif (choice == '5'):
        return PROGRAM
    elif (choice == '6'):
        return EXECUTABLES
    elif (choice == '7'):
        return PDF + WORD + IMAGE + AUDIO + PROGRAM + EXECUTABLES
    else:
        print('Invalid Choice')
        print('Terminating...')
        sys.exit(0)


def basic_work(path):
    '''
    Changes current working directory to specified path.
    returns the list of files at specified path.

    :param path: Absolute path of the directory.
    :return: List of files at given path
    '''
    try:
        os.chdir(path)
        return os.listdir(path)
    except:
        print('Folder doesn\'t exists.')
        print('Terminating...')
        sys.exit(0)

def get_extention(file):
    '''
    extracts the extention from the file.

    :param file: Name of the file.
    :return: length of parts of file splitted by (.),       extention of file
    '''
    temp = file.split('.')
    return len(temp), temp[-1]


def get_folder_name(extention):
    '''
    Returns Folder name according to the extention.

    :param extention: Extention of the file
    :return: Name of the folder, 'Others' otherwise
    '''
    if extention in PDF:
        return 'PDFs'
    elif extention in WORD:
        return 'Word Document'
    elif extention in IMAGE:
        return 'Images'
    elif extention in AUDIO:
        return 'Audio Files'
    elif extention in PROGRAM:
        return 'Program Files'
    elif extention in EXECUTABLES:
        return 'exe files'
    else:
        return 'Others'


def move_file(path, file, extention):
    '''
    Moves specified file from the path to new path.

    :param path: Current path of the file
    :param file: Name of the file
    :param extention: extention of the file 
    :return: None
    '''
    current_path = os.path.join(path, file)
    future_path = os.path.join(path, get_folder_name(extention), file)

    shutil.move(current_path, future_path)


def organize(path, files, choice):
    '''
    Groups files by their extention.

    :param path: Absolute path of the directory
    :param files: list of files in that directory
    :param choice: User's Choice
    :return: None
    '''
    extentions_to_be_organized = get_extention_list(choice)

    for file in files:
        length, extention = get_extention(file)
        if extention in extentions_to_be_organized:
            if length >= 2:
                try:
                    move_file(path, file, extention)
                except:
                    os.mkdir(os.path.join(path, get_folder_name(extention)))
                    move_file(path, file, extention)
            else:
                continue
        else:
            continue
