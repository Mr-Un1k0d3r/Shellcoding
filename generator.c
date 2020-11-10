#include <windows.h>
#include <stdio.h>

int main(int argc, char **argv) {

    DWORD key = atoi(argv[1]);
    HANDLE hFile = CreateFile(argv[2], GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);

    if(hFile == INVALID_HANDLE_VALUE) {
        printf("Failed to open %s\n", argv[2]);
        ExitProcess(0);
    }

    DWORD *current;
    DWORD dwSize = GetFileSize(hFile, NULL);
    DWORD dwRead = 0;
    CHAR *shellcode = GlobalAlloc(GPTR, dwSize);

    ReadFile(hFile, shellcode, dwSize, &dwRead, NULL);

    int i = 0;
    for(i; i < dwSize / 4; i++) {
        current = (DWORD*)shellcode;
        *current = *current ^ key;
        shellcode += 4;
    }
    shellcode -= dwSize;

    printf("Encoded using the following key: 0x%08x (%d)\n", key, key);
    for(i = 0; i < dwSize; i++) {
        printf("\\x%02x", (unsigned char)shellcode[i]);
    }

    CloseHandle(hFile);
    GlobalFree(shellcode);
    return 0;
}
