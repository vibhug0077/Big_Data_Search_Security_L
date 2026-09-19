#!/usr/bin/env python3

import sys

current_word = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    word, count = line.split("\t")
    count = int(count)

    if current_word == word:
        current_count += count
    else:
        if current_word is not None:
            # print(f"{current_word}\t{current_count}")
            print(current_word + "\t" + str(current_count))  # emit lowercase version
        current_word = word
        current_count = count

if current_word is not None:
    # print(f"{current_word}\t{current_count}")
    print(current_word + "\t" + str(current_count))  # emit lowercase version

# Command to execute in mac: cat input.txt | python mapper.py | sort | python reducer.py
# Command to execute in windows: type input.txt | python mapper.py | sort | python reducer.py