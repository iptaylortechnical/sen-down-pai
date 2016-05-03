import sys
import requests
import shutil

### Hey dad, here's how you use this
### create a file called 'files' (NO EXTENSION)
### put all urls inside that file
### open terminal and run:
### python check.py [path-to-directory (WITH TRAILING SLASH)] [default file format]
### files will download to the same directory as your "files" file. this file can be placed anywhere.


### DEBUGGING
### if you're getting an error about files not existing, check your trailing slash and make sure theres no space between it
### check to make sure you have all the parameters on the command line
### cannot handle extensions above 4 characters in length. to change this, see line marked "EXTENSION LENGTH"

fromPath = sys.argv[1]
lel = fromPath + "files"

fileFormat = sys.argv[2]

with open(lel) as p:
	content = p.readlines()

content = [x.strip('\n') for x in content]

print(content)

for c in content:
	path = c

	a = requests.get(path, stream=True)

	if not len(path.split('.')[len(path.split('.'))-1]) < 5'''<-- EXTENSION LENGTH''':
		name = path.split('/')[len(path.split('/'))-1] + "." + fileFormat
	else:
		name = path.split('/')[len(path.split('/'))-1]

	if a.status_code == 200:
		f = open(fromPath  + name, 'wb')
		a.raw.decode_content = True
		shutil.copyfileobj(a.raw, f)

		f.close()