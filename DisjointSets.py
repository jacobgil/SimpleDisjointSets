from collections import namedtuple

class DisjointSets:
	def __init__(self):
		self.Sets = {}
		self.itemToSetIndex = {}
		self.counter = 1

	def make_set(self, item):
		Set = namedtuple("DisjointSet", ["head", "Set"])
		self.itemToSetIndex[item] = self.counter
		self.counter = self.counter + 1
		self.Sets[self.itemToSetIndex[item]] = (Set(head = item, Set = [item]))
		
	def find(self, item):
		if item not in self.itemToSetIndex:
			return None
		return self.Sets[self.itemToSetIndex[item]].head

	def union(self, a, b):
		a_index, b_index = self.itemToSetIndex[a], self.itemToSetIndex[b]
		if a_index == b_index:
			return
		if len(self.Sets[b_index].Set) > len(self.Sets[a_index].Set):
			a_index, b_index = b_index, a_index
			a, b= b, a
			
		self.itemToSetIndex[b] = a_index
		for i in self.Sets[b_index].Set:
			self.itemToSetIndex[i] = a_index
			self.Sets[a_index].Set.append(i)

		del self.Sets[b_index]

	def __str__(self):
		return " ".join(map(str, self.Sets.values()))
