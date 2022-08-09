import subprocess
import os
import sys

image_path = sys.argv[1]
class_file_path = sys.argv[2]

image_path_file_count = os.listdir(image_path)
qwer = image_path_file_count
original_file = ''

# print(qwer)
os.chdir(class_file_path)

with open('app_images.dart', 'w') as f:
    f.write('import \'package:flutter/material.dart\';')
    f.write('class AppImages {')
    f.write('static const root = \'assets/images/\';')
    f.write('static const splash = \'${root}splash_image.png\';')
    f.write('static final bottomNavigationbar = _BottomNavigationBar();}')
    f.write('class _BottomNavigationBar {')

for file in image_path_file_count :
    if file.__contains__('.png') :
        init, *temp = file.split('_')
        temp[-1] = temp[-1].replace('.png', '')
        res = ''.join([init.lower(), *map(str.title, temp)])

        with open('app_images.dart', 'r') as f:
            original_file = f.read()
            f.close()
            print(original_file)

        with open('app_images.dart', 'w') as f:
            f.write(original_file)
            f.write(f'Image {res}() => const Image(')
            f.write(f'image: AssetImage(''')
            f.write(f''''${{AppImages.root}}{file}'),);''')
            f.write('\n')
            f.close()

with open('app_images.dart', 'r') as f:
    original_file = f.read()
    f.close()
    print(original_file)

with open('app_images.dart', 'w') as f:
    f.write(original_file)
    f.write('}')
