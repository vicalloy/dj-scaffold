#!/usr/bin/env python
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..'))

def main():
    from dj_scaffold.startproject import start_project
    start_project()


if __name__ == '__main__':
    main()
