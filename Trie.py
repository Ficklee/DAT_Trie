#coding: utf-8

class Node(object):
	def __init__(self,CurCode):
		self.CurCode=CurCode
		self.Children=[]
		self.ChildrenNum=[]
		self.IsEnd=False
class Trie(object):
	"""docstring for Trie"""
	def __init__(self, rootnode):
		self.root=rootnode(1)
	def Insert_word(self,word):
		uword=word.decode('utf-8')
		
	
