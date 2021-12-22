import os

# TODO: convert file to image
def convert(path):
	return path

# get spreadsheets
FILES = list(filter(lambda x: x.split('.')[-1] == 'xlsx', os.listdir('.')))
print(FILES)