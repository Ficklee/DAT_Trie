#coding:utf-8

with open('dic.txt','r') as f:
	a=f.readlines()
for line in a:
	line=line.strip('\n')
	line=line.decode('utf-8')
	print line