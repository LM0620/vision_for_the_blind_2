from vision_for_the_blind_2 import text as txt
from vision_for_the_blind_2 import caption_generator as capture
import sys
import os


def main():
    """take two arguments, including one optional"""
    # full path of file including the extension
    try:
        file_name = sys.argv[1]
        if len(sys.argv) > 3 or len(sys.argv) < 2:
            print('Invalid command')
        elif len(sys.argv) > 2 and sys.argv[2] == 'c':
            print('image capturing...')
            output = capture.capture_image(file_name)
            print(output)
        else:
            print('extracting text...')
            output = txt.get_setence(file_name)
            for item in output:
                item = os.linesep.join([s for s in item.splitlines() if s])
                print(item)
    except Exception as e:
        print('something wrong...')


if __name__ == '__main__':
    main()
