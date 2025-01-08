#!/usr/bin/python3

f_in = open("more_manual.txt")

f_out = open("more_manual_up_1.txt", "w")

for line in f_in.readlines():
	out = line.split()[0] + "\t"
	for i in line.split()[1].split(","):
		out += str(int(i) + 1) + ','
	f_out.write(out[:-1] + "\n")	

f_out.close()
f_in.close()
