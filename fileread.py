'''
8import os

file = 'out.csv'

time = os.path.getmtime(file)

print(time)


conv = time / 86400

print(conv)
'''

import os
import datetime
file = 'out.csv'

def modification_date(filename):
    file = 'out.csv'
    t = os.path.getmtime(filename)
    print(datetime.datetime.fromtimestamp(t))
    return datetime.datetime.fromtimestamp(t)

date = modification_date(file)
print(date)

'''
import os
import platform

def creation_date(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    if platform.system() == 'Windows':
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime
'''