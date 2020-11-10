import sys

def update_data(data, key, value):
	return data.replace("{%s}" % key.upper(), value)


if len(sys.argv) < 3:
	print("Usage: %s key [shellcode in \\x41\\x41 format]" % sys.argv[0])
	exit()

key = sys.argv[1]
shellcode = sys.argv[2]
template = open("simple-encoder.c", "r").read()

template = update_data(template, "key", str(hex(int(key))))
template = update_data(template, "shellcode", shellcode)
template = update_data(template, "size", str(int(len(shellcode) / 4)))

print(template)
