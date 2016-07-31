#include <stdio.h>
#include <stdlib.h>
int Readin(){
  FILE *ptr_file=NULL;
  long SZFile;
  int SiZfile;
  ptr_file=fopen("dat.bin","rb");
  if (NULL==ptr_file) {
    return -1;
  }
  fseek(ptr_file,0L,SEEK_END);
  SZFile=ftell(ptr_file);
  SiZfile=int(SZFile);
  int NumArr=(SiZfile-sizeof(int))/2;
  rewind(ptr_file);
  int i;
  fread
  int *buff=(int *)malloc(SiZfile*sizeof(int));
}
int main(){
  printf("hello world");
  return 0;
}
