#include <stdio.h>
#include <stdlib.h>

int main(){
  FILE *fpt=NULL;
  fpt=fopen("dat.bin","rb");
  if (fpt==NULL){
    printf("Error");
    return -1;
  }
  int i;
  fread(&i,sizeof(int),1,fpt);
  fclose(fpt);
  printf("%d",i);
  return 0;
}
