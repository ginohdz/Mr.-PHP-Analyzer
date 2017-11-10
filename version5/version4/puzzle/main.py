#!/usr/bin/python

import version
import argparse
import files
import report
import csvcreate
import vulnerability
import generateHtml
# -*- coding: utf-8 -*-
__author__="Coronado Gozain Saine, Hernandez Cuecuecha Jorge Alberto"
__copyright__="Copyright 2017, UNAM-CERT"
__license__="UNAM CERT"
__version__="1.0"
__status__="Prototype"
parser = argparse.ArgumentParser(description='Find vulnerabilities in php code')
parser.add_argument('-r' , nargs=1,  help="root")
parser.add_argument('-v' , nargs=1, help="vulnerability")
parser.add_argument('--sos', action="store_true", help="actions list")
option = parser.parse_args()

if option.r and option.v:
	files.get_files(option.r[0])
	v=version.get_version()
	if option.v[0] is "1":
		generateHtml.headerhtml(generateHtml.creareporte())
		report.create_reportlist()
		report.create_re_vulist("1")
		csvcreate.create_report("11")
		generateHtml.footer(generateHtml.creareporte())	
	elif option.v[0] is "2":
		report.create_reportlist()
		report.create_re_vulist("2")
		csvcreate.create_report("11")			
	elif option.v[0] is "3":
		report.create_reportlist()
	        report.create_re_vulist("3")
	        csvcreate.create_report("11")

	elif option.v[0] is "4":
		report.create_reportlist()
		report.create_re_vulist("4")
		csvcreate.create_report("11")

	elif option.v[0] is "5":
		report.create_reportlist()
                report.create_re_vulist("5")
                csvcreate.create_report("11")

	elif option.v[0] is "6":
		report.create_reportlist()
                report.create_re_vulist("6")
                csvcreate.create_report("11")

	elif option.v[0] is "7":
		report.create_reportlist()
                report.create_re_vulist("7")
                csvcreate.create_report("11")
	elif option.v[0] is "9":
		if v is "7":
			print"Didn't find obsolete functions"    	
		else:
        		generateHtml.headerhtml(generateHtml.creareporte())
			report.create_reportlist()
        		report.create_re_funclist()
        		csvcreate.create_report("12")
        		generateHtml.footer(generateHtml.creareporte())	

elif option.r:
	generateHtml.headerhtml(generateHtml.creareporte())
	generateHtml.graphic(generateHtml.creareporte())
	prov=["1","3"]
	files.get_files(option.r[0])
        v=version.get_version()
	report.create_reportlist()
	for o in range(len(prov)):
        	report.create_re_vulist(prov[o])
	if v is "7":
        	print"Didn't find obsolete functions"           
       	else:
		report.create_re_funclist()
	csvcreate.create_report("10")
	generateHtml.footer(generateHtml.creareporte())
			

if option.sos:
        print '''
               	Herzlich willkommen bei Mr.-PHPAnalyzer
		Mr.-PHPAnalyzer find vulnerabilities in php code 

                Options:

		1. SQLi
                2. XSS
		3. SESSION'S COOKIES
		4. SEND SENSIBLE INFORMATION
		5. LFI & RFI
		6. PATH TRAVERSAL
		7. COMMAND INJECTION
		8. SOURCE CODE INJECTION
                9. OBSOLETE FUNCTIONS
		
        '''

