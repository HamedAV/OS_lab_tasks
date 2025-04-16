#include <pthread.h>
#include <stdio.h>
#include <unistd.h>

void* print_message(void* arg) {
    pid_t pid_t = getpid();
    printf("Main process PID: %d\n", pid_t);
    printf("This is a multi-threaded program.\n");
    sleep(20);
    return NULL;
}

int main() {
    pid_t pid_main = getpid();
    printf("Main process PID: %d\n", pid_main);
    pthread_t thread;

    pthread_create(&thread, NULL, print_message, NULL);
    // printf("%lu", (unsigned long)thread);
    pthread_join(thread, NULL);

    return 0;
}