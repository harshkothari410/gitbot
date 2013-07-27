import os, sys
from gitbot import *


def commit(path, directory):
	option = raw_input('If you want to entire commit then press 1 or just want to last commit then press 2 : ')
	files = os.popen('ls ' + path + '/' + directory).read()
	file_list = files.split('\n')
	finalpath = path + '/' + directory
	print file_list[:len(file_list) - 1]
	commit_dict = {}
	keys = ['commit','author','data','message','long_message']
	if option == '1':
		for f in file_list[:len(file_list) - 1]:
			command = 'git log ' + f
			data = gitdata(finalpath,command)
			#datalist = data.count('Author:')
			if data.count('Author:') > 1:
				data = data.split('commit ')
				data.remove('')
				sub_dict = []
				for s in data:
					values = dataExtract(s)
					temp = createDict(keys, values)
					sub_dict.append(temp)
			else:
				values = dataExtract(data)
				sub_dict = createDict(keys, values)
			#print data
			commit_dict[f] = sub_dict
	if option == '2':
		for f in file_list[:len(file_list) - 1]:
			command = 'git log --diff-filter=A -- ' + f
			data = gitdata(finalpath,command)
			values = dataExtract(data)
			sub_dict = createDict(keys, values)
			commit_dict[f] = sub_dict
	#print commit_dict
	return commit_dict

def dataExtract(data):
	datalist = data.split('\n')
	value = []
	count = 0
	for d in datalist:
		d = d.replace('    ','')
		if d == '':
			continue
		if count > 4:
			temp = d
			value[4] = value[4] + ' ' + temp
		else:
			value.append(d)
		count = count + 1
	if value[0].find('commit ') == 0: 
		value[0] = value[0][len('commit '):]
	value[1] = value[1][len('Author: '):]
	value[2] = value[2][len('Date:   '):]
	return value	

def createDict(keys, values):
	return dict(zip(keys, values))

if __name__ == '__main__':
	data = commit(sys.argv[1],sys.argv[2])
	print data