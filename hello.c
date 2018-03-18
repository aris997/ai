#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <time.h>
//#include "hello.h"

#define TRUE 0

int main(){

	srand(time(NULL));

	int i;
	char X[1024], Y[32];
	FILE *DIC;
	DIC = fopen("dictionary.dat", "r");

	sprintf(X, "Ciao");
	fprintf(stdout, "%s\n", X);

	do{
		scanf("%1023s", X);
	
		do{
			fscanf(DIC, "%31s", Y); i++;
			if(Y == NULL) break;		//checking if it's all right
			if(strncmp(X, Y, 3) == 0) break; //exit for when comparision is ok
		} while(TRUE);
	
	//fprintf(stdout, "\rusr said:%s\n", Y);
	


	}
	exit(0);
}