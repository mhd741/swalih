#include <stdio.h>

int main() {
    int a = 10;
    int b = 5;
    int c = 20;
    int d = a + b * c - 30;
    printf("%d\n", d); // Corrected to print d

    int i = 1;
    i = ++i + i++;
    printf("%d\n", i); // Print i

    return 0;
}
