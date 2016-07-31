#coding: utf-8
from struct import pack
class Node(object):
	def __init__(self,CurCode):
		self.CurCode=CurCode
		self.Children=[]
		self.ChildrenNum=[]
		self.IsEnd=False
		self.SearchCode=0
class Trie(object):
	"""docstring for Trie"""
	def __init__(self):
		self.root=Node(1)
		self.root.SearchCode=1
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
			self.Insert_word(S1)


class DAT(object):
	def __init__(self,trie_base):
		self.base=[0]*2
		self.base[1]=1
		self.check=[0]*2
		self.trie_base=trie_base
	def BaseValue(self,s0,pointer):
		value=1
		listnum=pointer.ChildrenNum
		while True:
			Screwed_up=0
			lst01=[k+value for k in listnum]
			Longnum=max(lst01)
			if Longnum>=len(self.base):
				addleng=Longnum-len(self.base)+1
				self.base.extend([0]*addleng)
				self.check.extend([0]*addleng)
			Check_list=[self.check[NUM] for NUM in lst01]
			for data in Check_list:
				if data!=0 and data!=s0:
					Screwed_up=1
					break
			if Screwed_up==0:
				for idx in listnum:
					new_idx=idx+value
					self.check[new_idx]=s0
					pointer.Children[pointer.ChildrenNum.index(idx)].SearchCode=new_idx
				return value
			else:
				value+=1
	def DAT_Gen(self):
		pointer1=self.trie_base.root
		s=1
		Queue=[pointer1]
		while True:
			if pointer1.Children==[]:
				self.base[s]=-s
			else:
				self.base[s]=self.BaseValue(s,pointer1)
				if pointer1.IsEnd==True:
					self.base[s]*=-1
			Queue=Queue+pointer1.Children
			Queue.pop(0)
			if Queue==[]:
				break
			else:
				pointer1=Queue[0]
				s=pointer1.SearchCode
	def DAT_Search(self,the_word):
		search_p=1
		word_unc=the_word.decode('utf-8')
		word_ulist=list(word_unc)
		for w in xrange(len(word_ulist)):
			Charnum=ord(word_ulist[w])
			if self.base[search_p]==-search_p:
				return False
			else:
				if self.base[search_p]<0:
					tempid=-self.base[search_p]
				else:
					tempid=self.base[search_p]
				t=Charnum+tempid
				if self.check[t]!=search_p:
					return False
			search_p=t
			if w==len(word_ulist)-1 and self.base[search_p]>0:
				return False
		return True
	def DAT_SAVE(self):
		ListLength=len(self.base)
		BinLength=pack('i',ListLength)
		with open('dat.bin', 'wb') as fdat:
			fdat.write(BinLength)
			for num_B in self.base:
				fdat.write(pack('i',num_B))
			for num_C in self.check:
				fdat.write(pack('i',num_C))
