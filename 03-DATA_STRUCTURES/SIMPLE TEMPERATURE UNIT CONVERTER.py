#include <stdio.h>

int main() {
    int choice;
    float temp, converted;

    printf("--- Temperature Converter ---\n");
    printf("1. Celsius to Fahrenheit\n");
    printf("2. Fahrenheit to Celsius\n");
    printf("3. Celsius to Kelvin\n");
    printf("Enter your choice (1-3): ");
    scanf("%d", &choice);

    switch (choice) {
        case 1:
            printf("Enter temperature in Celsius: ");
            scanf("%f", &temp);
            converted = (temp * 9.0 / 5.0) + 32;
            printf("%.2f Celsius = %.2f Fahrenheit\n", temp, converted);
            break;
        case 2:
            printf("Enter temperature in Fahrenheit: ");
            scanf("%f", &temp);
            converted = (temp - 32) * 5.0 / 9.0;
            printf("%.2f Fahrenheit = %.2f Celsius\n", temp, converted);
            break;
        case 3:
            printf("Enter temperature in Celsius: ");
            scanf("%f", &temp);
            converted = temp + 273.15;
            printf("%.2f Celsius = %.2f Kelvin\n", temp, converted);
            break;
        default:
            printf("Invalid choice! Please select 1, 2, or 3.\n");
    }

    return 0;
}
