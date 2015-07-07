#!/usr/bin/env python
#print ("Hello World!")
f = open('hello.py','r');
#print ("Hello World!")
#print (f.read())
#print ("Hello World!")

for line in f:
	print(line, end='')
