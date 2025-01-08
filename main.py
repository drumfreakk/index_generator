#!/usr/bin/python3

import string
from pypdf import PdfReader
# Previous versions contain a thing to read directly from a pdf, but it didnt work very well


w = open("1000-words.txt", "r")
words = w.read().split(',')
w.close()

w = open("banned-words.txt")
words += w.read().split()
w.close()

#print(words)

index = {}


page_no = 0#int(input("Starting page no"))
had_words = []

f = open("input.txt")
text = f.read()
f.close()

def fix_first_break(text):
	for i in range(len(text)-1):
		if text[i] == "-" and text[i+1] == "\n":
			return text[:i] + text[i+2:]
	return text

text_old = ""

while text_old != text:
	text_old = text
	text = fix_first_break(text)

text = text.replace("↵", "ff")

allowed_chars = "abcdefghijklmnopqrstuvwxyz0123456789αβγδεζηθμνπφω"


for word in text.split():
	if word == "PAGE":
		had_words = []
		page_no += 1

	word = word.lower().translate(str.maketrans('','',"!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~”“’‘"))
	if (word not in words) and (word not in had_words) and (len(word) > 1) \
		and not word.isdigit() and all(c in allowed_chars for c in word):
		if word in index:
			index[word].append(page_no)
		else:
			index[word] = [page_no]
		had_words.append(word)

index = dict(sorted(index.items()))


#print(index)

for key,val in index.items():
	out = key + '\t'
	for i in val:
		out += str(i) + ','
	print(out[:-1])
