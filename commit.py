import os, sys
from gitbot import *


def commit(path, directory):
	option = raw_input('If you want to entire commit then press 1 or just want to last commit then press 2 : ')
	files = os.popen('ls ' + path + '/' + directory).read()
	file_list = files.split('\n')
	finalpath = path + '/' + directory
	print file_list[:len(file_list) - 1]
	commit_dict = {}
	if option == '1':
		for f in file_list[:len(file_list) - 1]:
			command = 'git log ' + f
			data = gitdata(finalpath,command)
			commit_dict[f] = data
	if option == '2':
		for f in file_list[:len(file_list) - 1]:
			command = 'git log --diff-filter=A -- ' + f
			#print command
			data = gitdata(finalpath,command)
			commit_dict[f] = data
	return commit_dict

if __name__ == '__main__':
	data = commit(sys.argv[1],sys.argv[2])
	print data