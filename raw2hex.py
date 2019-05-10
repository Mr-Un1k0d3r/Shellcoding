import binascii
import sys
import re

if __name__ == "__main__":
	
	if len(sys.argv) < 2:
		print("Missing file path")
		sys.exit(0)
		
	try:
		data = binascii.b2a_hex(open(sys.argv[1], "rb").read()).decode()
	except:
		print("Error reading %s" % sys.argv[1])
		sys.exit(0)
		
	if "-list" in sys.argv:
		print("0x" + ",0x".join(re.findall("..", data)))
	else:
		print("\\x" + "\\x".join(re.findall("..", data)))
