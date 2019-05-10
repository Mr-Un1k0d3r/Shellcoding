#include <Windows.h>

int main() {
    asm("call code\n\t"
        ".byte {{SHELLCODE}}\n\t" 
        "code:\n\t"
        "ret\n\t");

	return 0;
}
