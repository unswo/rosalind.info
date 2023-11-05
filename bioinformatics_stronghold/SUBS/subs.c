#include <stdio.h>
#include <string.h>

int my_strlen(char *s)
{
    int count = 0;

    while (s[count] != '\0')  // Single quotes for single char
        count++;

    return count;
}


int main(void)
{
	FILE *fp;
	FILE *fpsbs;
	char s[1024];
	char sub[1024];
	int count[1024] = {0};
	int counter = 0;
	int linecount = 0;
	int i, j = 0;


	fp = fopen("string.txt", "r");
	fpsbs = fopen("sub.txt", "r");

	while (fgets(s, sizeof s, fp) != NULL) 
		printf("\n", ++linecount, s);

	while (fgets(sub, sizeof sub, fpsbs) != NULL) 
		printf("\n", ++linecount, sub);
	// remove newline	
	sub[strcspn(sub, "\n")] = 0;
	int str_len = my_strlen(s);
	int len = my_strlen(sub);
	//printf("len %d\n", len);

	while (i < (str_len - len)){
		char substr[1024] = {0};
		int k = 0;
		while (k < len){
			//printf("k, %d\n", k);
			substr[k] = s[i+k];
			//printf("%c %c\n", substr[k], s[i+k]);
			k++;
			}
		//printf("%d, %s \n", i, substr, sub);
		int cmp = strcmp(substr, sub);
		//printf("cmp %d\n", cmp);
		if (cmp == 0){
			printf("%d ", i + 1);
		}
		
		i++;
	}
	//printf("counter: %d\n", count[0]);

	fclose(fp);
	fclose(fpsbs);
}
