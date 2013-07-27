import sys

def savetofile(filename,jsondata):
	fopen = open(filename,'w')
	fopen.write(jsondata)
	return 'File successfully created'

if __name__ == '__main__':
	data = savetofile(sys.argv[1],sys.argv[2])
	print data
	