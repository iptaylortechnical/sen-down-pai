import sys
import requests
import shutil

### Hey dad, here's how you use this
### create a file called 'files' (NO EXTENSION)
### put all urls inside that file
### open terminal and run:
### python check.py [path-to-directory] [file format]

fromPath = sys.argv[1]
lel = fromPath + "files"

with open(lel) as p:
	content = p.readlines()

content = [x.strip('\n') for x in content]

print(content)

for c in content:
	path = c

	a = requests.get(path, stream=True)

	if not path.split('.')[len(path.split('.'))-1] == 'jpg':
		name = path.split('/')[len(path.split('/'))-1] + ".jpg"
	else:
		name = path.split('/')[len(path.split('/'))-2] + ".jpg"	

	if a.status_code == 200:
		f = open(fromPath  + name, 'wb')
		a.raw.decode_content = True
		shutil.copyfileobj(a.raw, f)

		f.close()