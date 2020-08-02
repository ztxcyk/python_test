import sys
import os
xx = os.getcwd() + "\\wwmimport\\A"
yy = os.getcwd() + "\\wwmimport\\B"
sys.path.append(xx)
sys.path.append(yy)
from a import test
from b import sum


if __name__ == '__main__':
    test()
    sum()
