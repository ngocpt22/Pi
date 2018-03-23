import glob2
from datetime import datetime

filenames = glob2.glob('f*.txt')
def merge_files():
    with open('%s.txt' % datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f'), 'w') as fi:
        for i in filenames:
            with open(i) as file:
                content = file.read()
                fi.write(content + '\n')

merge_files()