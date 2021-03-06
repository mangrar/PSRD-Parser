import os
import glob

def char_replace(instr):
	instr = instr.replace(' ', '_')
	for char in ['(', ')', '[', ']', ',', '/', "'", ":", ";", "&"]:
		instr = instr.replace(char, '')
	return instr.lower()

def makedirs(output, book, localdir):
	bookdir = os.path.abspath(output + "/" + char_replace(book) + "/")
	if not os.path.exists(bookdir):
		os.makedirs(bookdir)
	if not os.path.exists(bookdir + "/rules/"):
		os.makedirs(bookdir + "/rules/")
	if not os.path.exists(bookdir + "/" + localdir + "/"):
		os.makedirs(bookdir + "/" + localdir + "/")

def locate_other_dbs(filename, sep):
	parts = filename.split(sep)
	parts.pop()
	search = sep.join(parts) + "*.db"
	files = glob.glob(search)
	files.remove(filename)
	return files

