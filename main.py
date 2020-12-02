print('Welcome to File Organizer v0.0.1')
print('Loading...')
print()

import inputs
import organize

path = input('Enter PATH of Direcctory which you want to Organize: ')
files = organize.basic_work(path)
inputs.menu()

user_choice = input('Enter Task Number: ')
organize.organize(path, files, user_choice)
print('Organized!!')
