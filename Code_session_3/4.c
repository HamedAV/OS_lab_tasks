#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

void* print_hello_world(void* arg) {
    printf("Hello World from thread!\n");
    pthread_exit(NULL); 
}

int main() {
    pthread_t threads[5];  


    for (int i = 0; i < 5; i++) {
        if (pthread_create(&threads[i], NULL, print_hello_world, NULL) != 0) {
            perror("Failed to create thread");
            exit(1);
        }
    }

    
    for (int i = 0; i < 5; i++) {
        pthread_join(threads[i], NULL);
    }

    return 0;
}
