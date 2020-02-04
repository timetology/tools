#!/usr/bin/python
import csv
import pandas as pd
import json
import sys
import argparse
import os

#Output from Office365 UAL export or https://github.com/jrentenaar/Office-365-Extractor
#
#Grep
#cat ../SearchTermsOrUserList | while read item; do echo "Processing $item" && grep -F -i $item * > ../newgreps/$item.UAL.grep.csv; done
#
#Bash loop
#for f in *.csv; do echo "Processing $f file.." && python3 o365-UAL-flatten-json-to-csv.py -f $f > $f.flat.csv; done



parser = argparse.ArgumentParser(description='o365 UAL flatten json to csv.py')
parser.add_argument('-f','--file', help='o365 UAL file input', required=True)
#parser.add_argument('--columnheader', help='Column Header of the AuditData', default=False)
parser.add_argument('-n','--number', help='Column Number of the AuditData', type=int,default=7)
parser.add_argument('-j','--json', help='Output Flattened JSON', action='store_true', default=False)
#parser.add_argument('-c','--csv', help='Output CSV of Flattened JSON', action='store_true', default=True)
args = parser.parse_args()



if (args.file):
	#df = pd.read_csv(args.file, usecols=['AuditData'])
	df = pd.read_csv(args.file, header=None, usecols=[args.number])
	#df = pd.read_csv(args.file)
	#print(df.to_string(header=False, index=False))
	#print(df.to_csv(header=False, index=False))


	#csvfile = df.to_csv(header=False, index=False)
	#csvfile = df.to_string(header=False, index=False)
	#print(df.head(3))

	#For some reason I HAVE to write this to a file.  dumping it to variable from pandas does weird things
	df.to_csv('tempfile.csv',header=False, index=False)
	with open('tempfile.csv') as csvfile:
		#thelist = csv.reader(csvfile,delimiter=',', quotechar='"')
		#print(csvfile)

		#print csvfile
		#for row in csvfile:
		#	print row

		#with open(args.file) as csvfile:
		#df = pd.read_csv(csvfile)
		#saved_column = df.column_name #you can also use df['column_name']



		csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')

		col_keys = []
		csvdata = []
		i = 0
		for row in csvreader:
		#for row in df.AuditData:
		#for row in df.columns[7]:

			csvrow = {}
			col_h = json.loads(row[0])

			for key, value in col_h.items():
				if key == "Parameters":	# break out parameters
					for parm_key in value:
						name = parm_key["Name"]
						value = parm_key["Value"]
						key_name = "Parameters.%s" % name

						if key_name not in col_keys: col_keys.append(key_name)
						csvrow.update({key_name: value})
				else:
					if key not in col_keys: col_keys.append(key)
					csvrow.update({key: value})

			csvdata.append(csvrow)

		if args.json:
			print(json.dumps(csvdata))
		else:
			#myjson = json.dumps(csvdata)
			data = pd.read_json(json.dumps(csvdata))
			print(data.to_csv(header=False, index=False))
			#data.to_csv("output.csv")
#Cleanup temp File
if os.path.exists("tempfile.csv"):
	 os.remove("tempfile.csv")
