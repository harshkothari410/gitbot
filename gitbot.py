import os,sys

def gitdata(path, query):
	data = os.popen('cd ' + path + ' && ' + query).read()
	return data

if __name__ == '__main__':
	data = gitdata(sys.argv[1],sys.argv[2])
	print data