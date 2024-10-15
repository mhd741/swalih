#include <stdio.h>

// Function to calculate factorial
unsigned long long factorial(int n) {
    if (n < 0) {
        return 0; // Factorial is not defined for negative numbers
    }
    if (n == 0 || n == 1) {
        return 1; // Factorial of 0 and 1 is 1
    }
    unsigned long long result = 1;
    for (int i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

int main() {
    int number;
    
    printf("Enter a positive integer: ");
    scanf("%d", &number);
    
    unsigned long long result = factorial(number);
    
    if (result == 0) {
        printf("Factorial is not defined for negative numbers.\n");
    } else {
        printf("Factorial of %d = %llu\n", number, result);
    }
    
    return 0;
}
