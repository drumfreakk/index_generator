#!/usr/bin/python3

import string
from pypdf import PdfReader


w = open("1000-words.txt", "r")
words = w.read().split(',')
w.close()
#print(words)


reader = PdfReader("text.pdf")

parts = []

def visitor_body(text, cm, tm, font_dict, font_size):
	global parts
	parts.append(text)

def get_page(reader, page):
	global parts
	page = reader.pages[page]
	
	parts = []
	
	page.extract_text(visitor_text=visitor_body)
	text_body = "".join(parts)

	return "\n".join(text_body.split("\n")[:-1])

#print(get_page(reader, 12))

index = {}

for i in range(len(reader.pages)):
	for word in get_page(reader, i).split():
		word = word.lower().translate(str.maketrans('','',"!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~”“’‘"))
		if word not in words:
			if word in index:
				index[word].append(i)
			else:
				index[word] = [i]
index = dict(sorted(index.items()))

#print(index)

for i in index:
	print(i)
