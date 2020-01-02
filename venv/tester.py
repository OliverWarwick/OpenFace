import math
from os import listdir
from os.path import isfile, join


import os

# if __name__ == "__main__":
#     print(os.getcwd())
#     mypath = "/Users/student/Desktop/Project/Datasets/VIPeR/cam_b"
#     onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#     print(onlyfiles)


if __name__ =="__main__":
    for a in range(1,100):
        for b in range(1,100):
            if (math.pow(a,b) + 1) % (math.pow(b,a) + 1) == 0:
                print("Values that work: a = " + str(a) + "   b = " + str(b))


