#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <time.h>
//#include "hello.h"
//#include "dictionary.h"
int main(){

	char X[1024];

	sprintf(X, "Ciao, sto imparando, sii clemente (non Smarra)");

	fprintf(stdout, "%s\n", X);

	scanf("%1023s", X);
	fprintf(stdout, "%s\n", X);

	exit(0);
}