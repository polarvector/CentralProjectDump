#include <stdio.h>
#include <stdlib.h> // Include stdlib for malloc and free
#include <string.h>

char *selection_sort(char ary_old[]);
char *bubble_sort(char ary_old[]);
void print_struct(void);
int factorial(int n);

typedef struct{
    char firstname[7];
    char  lastname[7];
}person; // this is the name of the structure

int main(void) {
    print_struct();
    int n = 10;
    char ary[] = "youreaboyinamansworld";
    //char *sorted = selection_sort(ary); // Call the sort function to sort the array
    //char *sorted = bubble_sort(ary); // Call the sort function to sort the array
    printf("\n   Bubble sorted array is: %s\n", bubble_sort(ary)); // Print the sorted array
    printf("\nSelection sorted array is: %s\n", selection_sort(ary)); // Print the sorted array
    printf("\n%d! = %d\n", n, factorial(n));
return 0;
}

char *selection_sort(char ary_old[]){ // works only for ASCII characters cuz max = 127
    int i=0, j=0, len=0, min = 128, ascii_max = 127, argmin=0; // Initialize variables
    while(ary_old[len] != '\0'){
        len++;
    }

    char *ary_new = malloc((len + 1) * sizeof(char)); // Allocate memory for the new array
    for (i=0; i<len;i++){
        ary_new[i]=ary_old[i]; // Copy the original array to the new array
    } 
    char *sorted_ary = malloc((len + 1) * sizeof(char)); // Allocate memory for the new array
    for (i=0; i<len;i++){
        sorted_ary[i]=0; // Copy the original array to the new array
    } 
    int arg_asc_order [len];

    // main sorting algorithm
    for(i=0; i<len;i++){ // while it's not equal to the NUL terminator. NUL not NULL 'kay? Differentiation
        min=127;
        for(j=0; j<len; j++){
            if (ary_old[j] <= min){
            min = ary_old[j];
            argmin = j;
            }
        }
        ary_old[argmin] = ascii_max;
        arg_asc_order[i] = argmin;
    }

    for(i=0; i<len; i++){
        sorted_ary[i] = ary_new[arg_asc_order[i]]; // Fill the new array with sorted characters
    }
    sorted_ary[len] = '\0'; // Add the null terminator to the end of the new array
    return sorted_ary; 
}

char *bubble_sort(char ary_old[]){
    int len=0;
    while(ary_old[len] != '\0'){
        len++;
    }
    
    for (int j = 0; j < len; j++){
        for(int i = 0; i < len-j-1; i++){  // len-j-1 because we always check the next
            if (ary_old[i] > ary_old[i+1]){// element and for the final iteration, that 
                char temp = ary_old[i];    // checks the NUL character \0 
                ary_old[i] = ary_old[i+1];
                ary_old[i+1] = temp;
            }
        }
    }
    return ary_old;
}

void print_struct(void){
    person people[2]; // Declare an array of 2 person structs
    strcpy(people[0].firstname, "Polarj"); // Assign values to the first person
    strcpy(people[0].lastname , "Sapkota"); // Assign values to the first person

    strcpy(people[1].firstname, "Richa"); // Assign values to the first person
    strcpy(people[1].lastname , "Dragon"); // Assign values to the first person

    char usr_ip[] = "Richa";
    for (int i=0; i<2;i++){
        if (usr_ip[0]==people[i].firstname[0]){
            printf("Full name is %s %s\n", people[i].firstname, people[i].lastname);
            return 0;
        }
    }
    printf("Not found\n");
}

int factorial(int n){
    if (n==0){
        return 1;
    }
    int fact = n*factorial(n-1);
    return fact;
}