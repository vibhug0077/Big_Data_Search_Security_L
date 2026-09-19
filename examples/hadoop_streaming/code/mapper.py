#!/usr/bin/env python3

# Command to execute in mac: cat data.txt | python mapper.py
# Command to execute in windows: type data.txt | python mapper.py
import sys

def mapper():
    for line in sys.stdin:
        line = line.strip()     # remove leading/trailing whitespace
        words = line.split()    # split the line into words - tokenization
        for word in words:
            # print(f"{word}\t1")
            print(word.lower() + "\t1")  # also emit lowercase version

if __name__ == "__main__":
    mapper()