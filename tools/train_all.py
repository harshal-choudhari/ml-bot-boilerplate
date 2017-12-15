#!/usr/bin/python

import os
import sys


def train():
    os.system("python tools/train_nlu.py")
    os.system("sleep 5")
    os.system("python tools/train_core.py")
    os.system("sleep 5")


def test():
    os.system('python tools/test_core.py')


def main(todo=None):
    if (todo == 't'):
        train()
    elif (todo == 'tt'):
        train()
        test()
    elif (todo == 'test'):
        test()

if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except:
        print("""Usage: {} <options>\n\toptions
            -\n\t\tt\ttrain\n\t\ttt\ttrain and
            test""".format(sys.argv[0]))
