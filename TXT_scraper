'''
This script extracts and saves information from similarly formatted txt files.
Because each file will have a very different format, this is simply an example
of how to set up txt extraction.
'''

import os, glob, time, re
import cPickle as pickle

print 'Starting at '+time.strftime("%H:%M:%S", time.localtime())+'.'

# create function to pull out data from txt files
def text_scrape(txt_file):
	# read in file
	full_text=open(txt_file, "r")

	# create list of each line of file
	text=list(full_text)
	full_text.close()

    ## ADJUST THE NAMES OF VALUES TO BE SCRAPED
	# pull out date, name, alfa, bravo, charlie
	coord_line=""
	coord_count=0
	for line in range(len(text)):
		upp_line=text[line].upper()
		if "DATE" in upp_line:
			coord_line=upp_line
			coord_count=line
			break
				
    coordinates={}
    coordinates['date']=coord_line.index('DATE')
    coordinates['name']=coord_line.index('NAME')
    coordinates['alfa']=coord_line.index('ALFA')
    coordinates['bravo']=coord_line.index('BRAVO')
    coordinates['charlie']=coord_line.index('CHARLIE')

	# Create dictionary
	file={}
	
	positions=[]
	line=coord_count+2
    # Switch turns off scraping once blank lines are found
	switch=True
	switch_count=0
	while switch==True:
		if len(text[line]) >=20:
			obs={}
			obs['date']=text[line][:coordinates['date']].strip()
			obs['name']=text[line][coordinates['date']: coordinates['name']].strip()
			obs['alfa']=text[line][coordinates['name']:coordinates['alfa']].strip()
			obs['bravo']=text[line][coordinates['alfa']:coordinates['bravo']].strip()
			obs['charlie']=text[line][coordinates['bravo']:coordinates['charlie']].strip()
			
			positions.append(obs)
		elif len(text[line])<20:
			switch=False
		line+=1
	file['positions']=positions
		
	return file

# create empty list for files
all_files=[]

# set directory
os.chdir("C:/Users/atalbot/Documents/TXT")

# create list of all txt files
txt_files=[]
for x in glob.glob("*.txt"):
	txt_files.append(x)
	
# loop over and scrape all pdfs
for x in txt_files:
	all_files.append(text_scrape(x))

# save out files	
pickle.dump(all_files, open("Output/Data from PDFs pickle.p", 'wb'))
	
print 'Finished at '+time.strftime("%H:%M:%S", time.localtime())+'.'



#              |    |    |
#             )_)  )_)  )_)
#            )___))___))___)/
#           )____)____)_____)//
#         _____|____|____|____///__
#---------/                   /---------
#  ^^^^^ ^^^^^^^^^^^^^^^^^^^^^
#    ^^^^      ^^^^     ^^^    ^^
#         ^^^^      ^^^

