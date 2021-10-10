import sys
import cv2
import tensorflow
import numpy

def print_awesome():
    print(
        '===================================================\n' \
        '                                                   \n' \
        '    ________                                       \n' \
        '    ___  __ \____  _____   _____   _______         \n' \
        '    __  /_/ /_  / / /_| | / /_| | / /_  _ \        \n' \
        '    _  _, _/ / /_/ / _| |/ / _| |/ / /  __/___     \n' \
        '    /_/ |_|  \__,_/  _|___/  _|___/  \___/ _(_)    \n' \
        '                                                   \n' \
        '                                                   \n' \
        '===================================================\n' \
    )
    print('\n')

    print(
        '                                                \n' \
        '  __   _ ____ ___  __  _  ___  _   _            \n' \
        '  \ \  /| |_ | |_)( (`| |/ / \| |\ |  _         \n' \
        '   \_\/ |_|__|_| \_)_)|_|\_\_/|_| \| (_)        \n' \
        '                                                \n' \
        '                                                \n' \
    )
    print('python ', sys.version)
    print('\nopenCV ', cv2.__version__)
    print('tensorflow ', tensorflow.__version__)
    print('numpy ', numpy.__version__)
    # print('             ')
    print('\n\n\n')