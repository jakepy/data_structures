class Node:
	def __init__(self, data, next_node):
		self.data = data
		self.next_node = next_node


class Stack:
	def __init__(self):
		self.head = None

	def peek(self):
		return self.head

	def push(self, data):
		next_node = self.head
		new_head = Node(data, next_node)
		self.head = new_head

	def pop(self):
		if self.head is None:
			return None
		removed = self.head
		self.head = self.head.next_node
		return removed