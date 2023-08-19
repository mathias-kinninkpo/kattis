#include <stdio.h>
#include <string.h>

int main() {
    char let[101];
    scanf("%s", let);
    int idx = -1;
    
    for (int i = 0; i < strlen(let) - 1; i++) {
        if (let[i] == 's' && let[i] == let[i+1]) {
            idx = i;
            break;
        }
    }
    
    if (idx != -1) {
        printf("hiss\n");
    } else {
        printf("no hiss\n");
    }
    
    return 0;
}
