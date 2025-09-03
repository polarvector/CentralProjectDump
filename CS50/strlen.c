#include <stdio.h>

int strlen(char* string){
    int len = 0;
    while( *(string+len) != '\0'){
        len++;
    }
    return len;
}
    