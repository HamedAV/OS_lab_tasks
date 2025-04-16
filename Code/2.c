#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int global_var = 10;

void *child(void *arg) {
    int local_var;

    printf("Thread %ld, pid %d, addresses: &global: %p, &local: %p\n",
           pthread_self(), getpid(), &global_var, &local_var);

    global_var++;

    printf("Thread %ld, pid %d, incremented global var = %d\n",
           pthread_self(), getpid(), global_var);

    pthread_exit(0);
}

int main() {
    pthread_t tid1, tid2;

    printf("Main thread: initial global_var = %d\n", global_var);

    pthread_create(&tid1, NULL, child, NULL);
    pthread_create(&tid2, NULL, child, NULL);

    pthread_join(tid1, NULL);
    pthread_join(tid2, NULL);

    printf("Main thread: final global_var = %d\n", global_var);

    return 0;
}