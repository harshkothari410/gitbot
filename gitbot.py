import os,sys

def gitdata(query):
	data = os.popen(query).read()
	return data

if __name__ == '__main__':
	data = gitdata(sys.argv[1])
	print data