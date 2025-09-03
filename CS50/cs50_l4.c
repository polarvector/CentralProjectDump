#include <stdio.h>
#include "strlen.c"
#include <stdlib.h>

typedef char* string; // So string is just a pointer to the first of a bunch of chars
int strcmp(char * s1, char* s2);
void copy(char* copier, char* s);

int main(void) {
    char* s = "Cena, you're a boy, in a man's world!"; // Declare a string variable and assign it a value
    printf("%s\n", s); // Print the string variable
    printf("%p\n", s); // Print the string variable

    // Notes:
    // syntax very subtle. To correctly print string as above, don't dereference pointer
    // dereferencing pointer would access just the address and prints the first character
    // of the specified string. 
    
    char* s1 = "phrase";
    char* s2 = "phrasey";
    int is_same_string = strcmp(s1, s2);
    
    char* t = malloc( (strlen(s)+1) * sizeof(char) );
    copy(t, s);
    printf("%s\n", t); // Print the string variable
    free(t);

    return 0;
} // End of the program

int strcmp(char * s1, char* s2){
    int i=0;
    while(*(s1+i) != '\0' || *(s2+i) != '\0' ){
        if( *(s1+i) != *(s2+i) ){
            printf("The strings are different\n");
            return 1;
        }
        i++;
    }
    printf("The strings are same\n");
    return 0;
}

void copy(char* copier, char* s){
    int i = 0;
    int len = strlen(s);

    while(i <= len ){
        *(copier+i) = *(s+i);
        i++;
    }
}