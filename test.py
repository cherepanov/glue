#!/usr/bin/env python

import os
from optparse import OptionParser

def main():

    parser = OptionParser()

    (options, args) = parser.parse_args()

    target_dir = args[0]

    items = dict()

    for root, dirs, files in os.walk(target_dir):
        #print os.path.basename(root).startswith('.')
#        if not os.path.basename(root).startswith('.'):
        class_name = root.replace(target_dir, '').replace(os.path.sep, '-')
        if class_name not in files:
            items[class_name] = list()

        for f in files:
            items[class_name].append(f)

        print class_name

    print items

if __name__ == "__main__":
    main()
