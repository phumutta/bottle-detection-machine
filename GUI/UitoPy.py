import os
from PyQt5 import uic
SRC="D:/os_guiv"
DEST="basic.ui"


if __name__ =='__main__':
    uic.compileUiDir(SRC,map=lambda src,name :(DEST,name))
