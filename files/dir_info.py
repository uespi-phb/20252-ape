
import os, sys
from datetime import datetime

ERR_OK = 0
ERR_INV_PARAMS = -1
ERR_DIR_NOT_EXISTS = -2


def main():
    argc = len(sys.argv)
    if argc != 2:
        fname = sys.argv[0]
        print(f'usage: {fname} DIR')
        exit(ERR_INV_PARAMS)

    dir_name = sys.argv[1]
    if not os.path.exists(dir_name):
        print(f'Directory not exists: {dir_name}')
        exit(ERR_DIR_NOT_EXISTS)

    dir_entries = os.listdir(dir_name)
    for entry_name in dir_entries:
        entry_path = f'{dir_name}/{entry_name}'
        entry_size = os.path.getsize(entry_path)
        entry_time = datetime.fromtimestamp(os.path.getmtime(entry_path))
        entry_date = entry_time.strftime('%d/%m/%Y %H:%M')
        
        if os.path.isdir(entry_path):
            entry_name += '/'
        
        print(f'{entry_name:<20} {entry_size:>8} {entry_date}')

if __name__ == '__main__':
    main()
