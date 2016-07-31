#coding:utf-8
from Trie import *
Tree1=Trie()
Tree1.Insert_Dic()
dat_01=DAT(Tree1)
dat_01.DAT_Gen()
#dat_01.DAT_SAVE()
print dat_01.DAT_Search("一举")
