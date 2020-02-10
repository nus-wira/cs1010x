/*****************************************
 * CS1010X --- Programming Methodology  *
 *                                       *
 *   Mission 16, Question 3 Template     *
 *****************************************/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define DST_SIZE 100

void copy_odd(char *dst, char *src, int *count) {
    /************
     *  Task 1  *
     ************

     Parameters:
        dst   - Pointer to a char array
        src   - Pointer to a char array (with a valid string in it)
        count - Count of characters copied

     Copy all ODD characters from the source to the destination char array and
     return the number of characters copied through the "count" pointer.

     The destination must be a valid string regardless of the number of
     characters copied. You may assume that the destination array will have
     sufficient space to hold all the odd characters.

     !!IMPORTANT!!: YOU ARE NOT ALLOWED TO DEFINE ANY ADDITIONAL VARIABLES
                    NOR CALL/IMPORT/DEFINE ANY HELPER FUNCTIONS.
                    Two marks will be deducted for every extra variable or
                    function call.
    */
    *count = 0;
    dst[*count] = '\0';
    if (src[0] == '\0') return;

    //every ith element of dst will = to every 2ith element of src
    while (src[2*(*count)] != '\0'){
        dst[*count] = src[2*(*count)];
        (*count)++;
        if (src[2*(*count) - 1] == '\0') break;
    }
    //set dst to end after last character copied
    dst[*count] = '\0';
}

void test_copy_odd(char *input) {
    char output[DST_SIZE];
    int count;
    memset(output, '*', DST_SIZE);
    output[DST_SIZE - 1] = 0;
    copy_odd(output, input, &count);
    printf("\"%s\" --(copied %d)--> \"%s\"\n", input, count, output);
}

int main(void) {
    test_copy_odd("");
    test_copy_odd("C");
    test_copy_odd("123");
    test_copy_odd("hello world");
    return 0;
}

/*
 EXPECTED OUTPUT:

    "" --(copied 0)--> ""
    "C" --(copied 1)--> "C"
    "123" --(copied 2)--> "13"
    "hello world" --(copied 6)--> "hlowrd"
*/
