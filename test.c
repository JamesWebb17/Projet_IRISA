#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>


int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <pid>\n", argv[0]);
        return 1;
    }

    int pid = atoi(argv[1]);
    char path[256];
    snprintf(path, sizeof(path), "/proc/%d/stat", pid);

    int fd = openat(AT_FDCWD, path, O_RDONLY);
    if (fd == -1) {
        perror("openat");
        return 1;
    }

    char buffer[1024];
    ssize_t bytesRead = read(fd, buffer, sizeof(buffer) - 1);
    if (bytesRead == -1) {
        perror("read");
        close(fd);
        return 1;
    }

    buffer[bytesRead] = '\0'; // Null-terminate the string

    printf("Contents of /proc/%d/stat:\n%s\n", pid, buffer);

    // Now, let's extract and explain individual fields in the buffer
    long pidValue;
    char comm[1024];
    char state;
    long ppid;
    long pgrp;
    long session;
    int tty_nr;
    long tpgid;
    unsigned int flags;
    unsigned long minflt;
    unsigned long cminflt;
    unsigned long majflt;
    unsigned long cmajflt;
    unsigned long utime;
    unsigned long stime;
    long cutime;
    long cstime;
    long priority;
    long nice;
    long num_threads;
    long itrealvalue;
    unsigned long starttime;

    // Parse the values from the buffer
    sscanf(buffer, "%ld %s %c %ld %ld %ld %d %ld %u %lu %lu %lu %lu %lu %lu %ld %ld %ld %ld %ld %ld %ld %lu",
           &pidValue, comm, &state, &ppid, &pgrp, &session, &tty_nr, &tpgid, &flags, &minflt, &cminflt,
           &majflt, &cmajflt, &utime, &stime, &cutime, &cstime, &priority, &nice, &num_threads,
           &itrealvalue, &starttime);

    // Print explanations for each field
    printf("\nExplanation of fields:\n");
    printf("PID: %ld\n", pidValue);
    printf("Command: %s\n", comm);
    printf("State: %c\n", state);
    printf("Parent PID: %ld\n", ppid);
    printf("Process Group ID: %ld\n", pgrp);
    printf("Session ID: %ld\n", session);
    printf("Terminal Number: %d\n", tty_nr);
    printf("Foreground Process Group ID: %ld\n", tpgid);
    printf("Flags: %u\n", flags);
    printf("Minor Page Faults: %lu\n", minflt);
    printf("Child Minor Page Faults: %lu\n", cminflt);
    printf("Major Page Faults: %lu\n", majflt);
    printf("Child Major Page Faults: %lu\n", cmajflt);
    printf("User Mode CPU Time: %lu\n", utime);
    printf("Kernel Mode CPU Time: %lu\n", stime);
    printf("User Mode CPU Time of Child Processes: %ld\n", cutime);
    printf("Kernel Mode CPU Time of Child Processes: %ld\n", cstime);
    printf("Priority: %ld\n", priority);
    printf("Nice Value: %ld\n", nice);
    printf("Number of Threads: %ld\n", num_threads);
    printf("Real Time Quantum (jiffies): %ld\n", itrealvalue);
    printf("Start Time (jiffies): %lu\n", starttime);

    close(fd);

;
    snprintf(path, sizeof(path), "/proc/%d/status", pid);

    fd = openat(AT_FDCWD, path, O_RDONLY);
    if (fd == -1) {
        perror("openat");
        return 1;
    }

    bytesRead = read(fd, buffer, sizeof(buffer) - 1);
    if (bytesRead == -1) {
        perror("read");
        close(fd);
        return 1;
    }

    buffer[bytesRead] = '\0'; // Null-terminate the string

    // Find and extract the RSS (Resident Set Size) field
    const char *rssLabel = "VmRSS:";
    char *rssPtr = strstr(buffer, rssLabel);

    printf("\nContents of /proc/%d/status:\n%s\n", pid, buffer);

    printf("\nContent : \n%s\n" , buffer);

    if (rssPtr) {
        long rssValue;
        sscanf(rssPtr + strlen(rssLabel), "%ld", &rssValue);
        printf("RSS (Resident Set Size): %ld kB\n", rssValue);
    } else {
        printf("RSS (Resident Set Size) not found in /proc/%d/status.\n", pid);
    }

    close(fd);

    return 0;
}
