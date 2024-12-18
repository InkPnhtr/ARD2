#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <sys/socket.h>

int main() {
    char hostname[1024];
    struct hostent *host_entry;
    char *local_ip;

    // Get the hostname of the system
    if (gethostname(hostname, sizeof(hostname)) == -1) {
        perror("gethostname failed");
        exit(EXIT_FAILURE);
    }

    // Get host entry by hostname
    host_entry = gethostbyname(hostname);
    if (host_entry == NULL) {
        perror("gethostbyname failed");
        exit(EXIT_FAILURE);
    }

    // Convert the first IP address to a string
    local_ip = inet_ntoa(*(struct in_addr *)host_entry->h_addr_list[0]);
    if (local_ip == NULL) {
        perror("inet_ntoa failed");
        exit(EXIT_FAILURE);
    }

    printf("System Local IP: %s\n", local_ip);

    return 0;
}
