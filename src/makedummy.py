import os

block = 1024
with open('dummy.file', 'wb') as fout:
    for i in range(1024):
        print('.', end='')
        fout.write(os.urandom(block))
