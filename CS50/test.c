#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *sort(char ary_old[]);

int main(void) {
    char ary[] = "youreaboyinamansworld!";  // Input string
    char *sorted = sort(ary);  // Call the sort function to sort the array
    printf("\nThe sorted array is: %s\n", sorted);  // Print the sorted array
    free(sorted);  // Free the allocated memory
    return 0;  // Return 0 to indicate successful completion
}

char *sort(char ary_old[]) {
    int len = 0;
    // Calculate the length of the input array
    while (ary_old[len] != '\0') {
        len++;
    }

    // Allocate memory for the sorted array
    char *sorted_ary = malloc((len + 1) * sizeof(char));
    if (sorted_ary == NULL) {
        return NULL;  // Check if malloc failed
    }

    // Copy the original array into sorted_ary
    for (int i = 0; i < len; i++) {
        sorted_ary[i] = ary_old[i];
    }

    // Selection sort algorithm to sort the array in ascending order
    for (int i = 0; i < len - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < len; j++) {
            if (sorted_ary[j] < sorted_ary[min_idx]) {
                min_idx = j;
            }
        }

        // Swap the elements
        char temp = sorted_ary[min_idx];
        sorted_ary[min_idx] = sorted_ary[i];
        sorted_ary[i] = temp;
    }

    sorted_ary[len] = '\0';  // Add the null terminator to the end of the sorted array
    return sorted_ary;
}
