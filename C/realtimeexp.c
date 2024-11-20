#include <stdio.h>
int main(){
    int items = 10;
    float cost_of_each = 9.99;
    float total_cost = items * cost_of_each;
    char currency = '$';

    printf("No of items: %d\n", items);
    printf("Total cost: %c%.2f\n",currency,total_cost);
    return 0;
}