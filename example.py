import sys,os
from gitbot import *
from commit import *
from dicttojson import *
from savetofile import *

data = commit(sys.argv[1],sys.argv[2])
jsondata = dicttojson(data)
print jsondata
print savetofile("mapall.json", jsondata)