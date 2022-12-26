import time
import os

row = int(input("Enter size of Star:")) + 1
numloading = int(input("Enter number loading:"))
time.sleep(1.5)

while numloading:
    os.system("cls")
    numloading -= 1
     ## Right Up Triangle
    for i in range(1,row):
        print("\x1b[%d;%dH" % (4+i, 1),end="")
        for j in range(i):
            print("*",end="")
        print("")
    time.sleep(1)

    ## Inverted Mirrored Right UP Triangle
    for i in range(1,row):
        for j in range(i,row):
            print("\x1b[%d;%dH" % (4+i, 2+j),end="")
            print("*",end="")
        print("")
    time.sleep(1)

    ## Inverted Right UP Triangle
    for i in range(1,row):
        print("\x1b[%d;%dH" % (4+i, row+3),end="")
        for j in range(1,row-i+1):
            print("*",end="")
        print("")
    time.sleep(1)

    ## Mirrored Right UP Triangle
    for i in range(1,row):
        for j in range(i):
            print("\x1b[%d;%dH" % (4+i, (row*2)+3-j),end="")
            print("*",end="")
        print("")

    time.sleep(1)

    ## Inverted Mirrored Right Triangle
    for i in range(1,row):
        for j in range(i,row):
            print("\x1b[%d;%dH" % (4+row+i-1, (row+2)+j+2),end="")
            print("*",end="")
        print("")

    time.sleep(1)

    ## Right Down Triangle
    for i in range(1,row):
        for j in range(i):
            print("\x1b[%d;%dH" % (4+row+i-1, (row+2)+j+1),end="")
            print("*",end="")
        print("")

    time.sleep(1)

    ## Mirrored Right Down Triangle
    for i in range(1,row):
        for j in range(i):
            print("\x1b[%d;%dH" % (4+row+i-1, (row+2)-j-1),end="")
            print("*",end="")
        print("")

    time.sleep(1)

    ## Inverted Right Down Triangle
    for i in range(1,row):
        for j in range(0,row-i):
            print("\x1b[%d;%dH" % (4+row+i-1, 1+j),end="")
            print("*",end="")
        print("")
    
    time.sleep(1)