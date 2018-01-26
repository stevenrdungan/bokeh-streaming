from random import randint
import time
import os
from datetime import datetime
import sys


def loop():
    ''' simulate streaming data'''
    print("looping")
    try:
        i = 0
        output_file = "output.txt"
        line_limit = 10000
        if not os.path.exists(output_file):
            open(output_file, 'w').close()
        while i < 100:
            lines = []
            i = randint(0,99)
            with open(output_file, 'r') as f:
                lines = f.readlines()
            lines = [str(x).strip() for x in lines if x]
            lines.append(str.format("{0},{1}", datetime.utcnow(), i))
            if len(lines) > line_limit:
                lines = lines[line_limit*-1:]
            output = '\n'.join(lines)
            with open(output_file, 'w') as f:
                f.write(output)
            time.sleep(.1)
    except KeyboardInterrupt:
        print("Stopping")
    finally:
        sys.exit(0)


if __name__ == "__main__":
    loop()
