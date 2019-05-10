import binascii
import sys
import re

if __name__ == "__main__":
	
	if len(sys.argv) < 3:
		print("Usage %s shellcode outfile" % sys.argv[0])
		sys.exit(0)
		
	try:
		data = open("loader32.c", "r").read()
	except:
		print("Error reading loader32.c")
		sys.exit(0)
		
		
	data = data.replace("{{SHELLCODE}}", sys.argv[1])
	open(sys.argv[2], "w").write(data)
