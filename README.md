# Shellcoding
Bunch of stuff I used that are related to shellcoding

# loader.c

A simple shellcode loader in C. This shellcode loader is not storing the shellcode in the data section. It store it directly in the text section to new to do shady memory allocation to call your shellcode.

The ASM syntax is for GCC compiler it can be adapted for VC too

# raw2hex.py

Convert raw shellcode into something else

```
raw2hex.py rawshellcodefile -list
0x90, 0x90

raw2hex.py rawshellcodefile
\x90\x90
```

# makefile.py

Generate the final C code

```
makefile.py 0x90,0x90,0x90 output.c
```

# Credit
Mr.Un1k0d3r RingZer0 Team
