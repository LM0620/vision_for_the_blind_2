from vision_for_the_blind_2 import text as txt
import sys
import os


def main():
    """take two arguments, including one optional"""
    # full path of file including the extension
    file_name = sys.argv[1]
    if len(sys.argv) > 3 or len(sys.argv) < 2:
        print('Invalid command')
    elif len(sys.argv) > 2 and sys.argv[2] == 'c':
        print('image capturing...')
        #TODO image capture
    else:
        print('extracting text...')
        full_path = os.path.abspath(file_name)
        # print(full_path)
        output = txt.get_setence(full_path)
        for item in output:
            item = os.linesep.join([s for s in item.splitlines() if s])
            print(item)


if __name__ == '__main__':
    main()
