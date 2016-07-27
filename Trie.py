#coding: utf-8

class Node(object):
	def __init__(self,CurCode):
		self.CurCode=CurCode
		self.Children=[]
		self.ChildrenNum=[]
		self.IsEnd=False
class Trie(object):
	"""docstring for Trie"""
	def __init__(self):
		self.root=Node(1)
	def Insert_word(self,word):
		uword=word.decode('utf-8')
		word_list=list(uword)
		WordNUM_list=[]
		for u_hanja in word_list:
			WordNUM_list.append(ord(u_hanja))
		p0=self.root
		wordlen=len(word_list)
		for x in xrange(wordlen):
			if WordNUM_list[x] not in p0.ChildrenNum:
				newnode=Node(WordNUM_list[x])
				p0.ChildrenNum.append(WordNUM_list[x])
				p0.Children.append(newnode)
				p0=newnode
			else:
				p0=p0.Children[p0.ChildrenNum.index(WordNUM_list[x])]
			if x==wordlen-1:
				p0.IsEnd=True
	def Insert_Dic(self,dicname="dic.txt"):
		with open(dicname,'r') as fDic:
			word_c=fDic.realdines()
	def word_search(self,s_word):
		word_u=s_word.decode('utf-8')
		word_u_list=list(word_u)
		p_search=self.root
		for U_zi in word_u_list:
			num=ord(U_zi)
			if num not in p_search.ChildrenNum:
				return False
			else:
				p_search=p_search.Children[p_search.ChildrenNum.index(num)]
				if U_zi==word_u_list[-1]:
					return p_search.IsEnd
Tree1=Trie()
Tree1.Insert_word("一")
Tree1.Insert_word("一举")
Tree1.Insert_word("一举一动")
Tree1.Insert_word("一举成名")
Tree1.Insert_word("二")
Tree1.Insert_word("三心二意")
Tree1.Insert_word("七上八下")
print Tree1.word_search("一")
print Tree1.word_search("一名")
print Tree1.word_search("一举")
print Tree1.word_search("一举一动")
print Tree1.word_search("一举成名")
print Tree1.word_search("一举夺魁")
