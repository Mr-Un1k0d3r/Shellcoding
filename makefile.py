import binascii
import sys
import re

if __name__ == "__main__":
	
	if len(sys.argv) < 3:
		print("Usage %s shellcode outfile" % sys.argv[0])
		sys.exit(0)
		
	try:
		data = open("loader32.c", "r").read()
		shellcode = binascii.b2a_hex(open(sys.argv[1], "rb").read()).decode()
	except:
		print("Error reading file")
		sys.exit(0)
		
	shellcode = "0x" + ",0x".join(re.findall("..", shellcode))
		
	data = data.replace("{{SHELLCODE}}", shellcode)
	open(sys.argv[2], "w").write(data)
	
	print("%s was created" % sys.argv[2])
