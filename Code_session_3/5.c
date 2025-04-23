#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct thdata {
    int thread_no;
    char message[100];
} thdata;

void* print_message(void* arg) {
    thdata* data = (thdata*) arg;
    printf("Thread #%d: %s\n", data->thread_no, data->message);

    pthread_exit(NULL);
}

int main() {
    pthread_t thread1, thread2;

    thdata data1, data2;
    data1.thread_no = 1;
    strcpy(data1.message, "Hello from Thread 1!");

    data2.thread_no = 2;
    strcpy(data2.message, "Hello from Thread 2!");

    pthread_create(&thread1, NULL, print_message, (void*)&data1);
    pthread_create(&thread2, NULL, print_message, (void*)&data2);

    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);

    return 0;
}