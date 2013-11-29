''' This script pulls data from PDFs into TXT files for further extraction '''

import os, glob, time, subprocess
import cPickle as pickle

print 'Starting at '+time.strftime("%H:%M:%S", time.localtime())+'.'

# create pdftotext function
def scrape(file, folder):
        ## This should be the folder with PDF_scraper.py and pdftotext
        os.chdir(base_dir + "Analysis of folder")
        ## This should be the location for the new txt files to be saved
        new_file=base_dir + "Analysis of folder/TXT/" + file[0:len(file)-3]+"txt"
        path='pdftotext -layout "../' + folder+ '/' + file + '" "' + new_file + '"'
        subprocess.call(path)

# Loop through various folders
## ADD FOLDER NAMES FOR RELEVANT PDFs
folders=['Folder1', 'Folder2', 'Folder3', 'Folder4', 'Folder5'] 
## ADJUST PATH FOR BASE DIRECTORY
base_dir="C:/Users/atalbot/Documents/"
for f in folders:
	# set directory
	os.chdir(base_dir + f)

	# create list of all pdf files
	pdfs=[]
	for x in glob.glob("*.pdf"):
		pdfs.append(x)

	# loop over and scrape all pdfs
	for x in pdfs:
		scrape(x, f)

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
