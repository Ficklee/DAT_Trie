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
	def Insert_Dic(self,dicname="dic.txt"):
		with open(dicname,'r') as fDic:
			word_c=fDic.readlines()
		for dic_word in word_c:
			S1=dic_word.strip('\n')
			print S1
			self.Insert_word(S1)
Tree1=Trie()
Tree1.Insert_Dic()
print Tree1.word_search("一")
print Tree1.word_search("一名")
print Tree1.word_search("一举")
print Tree1.word_search("一举一动")
print Tree1.word_search("一举成名")
print Tree1.word_search("一举夺魁")

class DAT(object):
	def __init__(self,trie_base):
		self.base=[0]*400000
		self.base[1]=1
		self.check=[0]*400000
		self.trie_base=trie_base()
	def BaseValue(self,s,listnum):
		value=1
		while True:
			Screwed_up=0
			Check_list=[self.check[NUM] for NUM in [k+value for k in listnum]]
			for data in Check_list:
				if data!=0 and data!=s:
					Screwed_up=1
					break
			if Screwed_up==0:
				return value
			else:
				value+=1

	def DAT_Gen(self):
		pointer1=self.trie_base.root
		s=1
		Queue=[pointer1]
		while True:
			Queue=Queue+pointer1.Children
			
			



		
