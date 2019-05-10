#include <Windows.h>

int main() {
    printf("Running shellcode\n");
    
    // Shellcode format is 0x90, 0x90
    asm("call code\n\t"
        ".byte {{SHELLCODE}}\n\t" 
        "code:\n\t"
        "ret\n\t");

	return 0;
}
