import re
import files
import sqlite3


# -*- coding: utf-8 -*-
__author__="Coronado Gozain Saine, Hernandez Cuecuecha Jorge Alberto"
__copyright__="Copyright 2017, UNAM-CERT"
__license__="UNAM CERT"
__version__="1.0"
__status__="Prototype"
class function_version:
        pass

def get_function (version):
        table=[]
        expression=[]
	function=[]
	alternative=[]
	funcob=[]
	functionlist=[]
	fl=[]
	fil=[]
	flfil=[]
	linex=[]
	fileslist=files.get_listfiles()
        connection= sqlite3.connect("../base/Fraudatanalyzer.db")
        cursor= connection.cursor()
	if version is "4":
        	for e in cursor.execute("SELECT  expression FROM functions WHERE versionob = '%s'" %version):
                        c=list(e)
                        expression.append(c[0])
	if version is "5":
		for e in cursor.execute("SELECT  expression FROM functions"):
                        c=list(e)
                        expression.append(c[0])
	for file in fileslist:
        	with open(file,"r") as f:
                	 for line in f.readlines():
                         	line = line.strip()
                                if re.match(r'^\s*$', line): continue #If line is empty, continue with the next one
                                if line[0] == '#': continue
                                if re.match(r'^(\/\*(\s*|.*?))|((\s*|.*?)\*\/)|(\/\/.*)$',line): continue
                                for x in range(len(expression)):
                                	if re.match(expression[x] , line):
                                        	fl.append(line)
						fil.append(file)
			          		table.append(expression[x])

	for f, l in zip(fl, fil):
                flfil.append("%s\n%s" % (f, l))
	linex.append(flfil)
	function=list(set(table))
	for f in range(len(function)):
		for e in cursor.execute("SELECT  function, alternative FROM functions WHERE expression = '%s'" %function[f]):
			c=list(e)
			funcob.append(c[0])
			alternative.append(c[1])
	for fc, al in zip(funcob, alternative):
		print("Tienes la funcion %s que es obsoleta, mejor cambiala por: %s." % (fc, al))
	linex.append(funcob)
	#print linex
	return linex
#get_function("5")
							
