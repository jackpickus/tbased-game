import time
import sys

def print_words(words):
    words = words.split()
    for w in words:
        for c in w:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(' ') # keep in outer loop so only prints spaces between words
    print()

