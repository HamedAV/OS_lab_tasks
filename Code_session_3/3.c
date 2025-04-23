#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

void* sum_function(void* arg) {
    int n = *((int*)arg); 
    int sum = 0;

    for (int i = 2; i <= n; ++i) {
        sum += i;
    }

    printf("Sum from 2 to %d is: %d\n", n, sum);
    return NULL;
}

int main() {
    int n;
    printf("Enter a number (n): ");
    scanf("%d", &n);

    pthread_t thread;
    pthread_attr_t attr;

    pthread_attr_init(&attr);

    size_t stack_size = 1024 * 1024; 
    pthread_attr_setstacksize(&attr, stack_size);
 
    pthread_create(&thread, &attr, sum_function, &n);


    pthread_join(thread, NULL);

 
    pthread_attr_destroy(&attr);

    return 0;
}