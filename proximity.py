import sys

class Node:

	left = None
	right = None

	def __init__(self, data, value):
		self.data = data
		self.value = value
		self.left = None
		self.right = None

	def __str__(self):
		if self == None:
			return "None"
		else:
			return "Data: "+format(self.data)+" | Value: "+format(self.value)



# BST
class Tree:
	root = None

	def __init__(self, data):
		self.root = Node(data, self.getStringValue(data))


	def insert(self, data):
		# passing "string" and ASCII sum of string
		s_value = self.getStringValue(data)

		self.insertAction(self.root, Node(data, s_value))

		print("String "+format(data)+" successfully inserted with value "+format(s_value))


	# to_insert is a Node object, initialised with from insert function
	def insertAction(self, root, to_insert):
		if root == None:
			root = to_insert

			return True
		else:
			if root.value > to_insert.value:
				if root.left == None:
					root.left = to_insert
				else:
					self.insertAction(root.left, to_insert)
				return True
			elif root.value < to_insert.value:
				if root.right == None:
					root.right = to_insert
				else:
					self.insertAction(root.right, to_insert)
				return True
			else:
				print("Duplicate")


	# Search operation initiator
	# Converts string into value and passes it on to searchWithValue function for search
	def search(self, data_to_search):
		value = self.getStringValue(data_to_search)

		return self.searchWithValue(self.root, self.getStringValue(data_to_search))


	def searchWithValue(self, root, value_to_search):
		if root is None or root.value == value_to_search:
			return root

		if root.value < value_to_search:
			return self.searchWithValue(root.right, value_to_search)
		else:
			return self.searchWithValue(root.left, value_to_search)


	def getStringValue(self, s):
		values = [ord(c) for c in s]

		return sum(values)


def parseCsv(name):
	result = []
    
	with open(name) as f:
		lis=[line.strip().split(",") for line in f]
		for x in lis:
			if(len(x) > 1):
				for i in x:
					result.append(i)

	return result


def getClosest(root, data, n):
	if root == None:
		print("Root is empty")
		exit()

	focus_node = t.search(data)

	list_all_levels(focus_node, n)

	# # Can't figure out how to do the below process
	# # Need to add in recursion somehow I think
	# # But still a simple Binary Search doesn't seem to be the answer
	# while(n != 0):
	# 	if left_flag:
	# 		to_print = format(to_print) + format(left_offset.data)
	# 		left_offset = left_offset.left
	# 	else:
	# 		to_print = format(to_print) + format(right_offset.data)
	# 		right_offset = right_offset.left

	# print(to_print)



def breadth_search(node, counter, n, level=None):
	if node == None:
		return
	elif level == 1:
		counter+=1

		if counter+1 == n:
			print(node.data)
			return
		else:
			print(node.data, end=", ")
	else:
		breadth_search(node.left, counter, n, level-1)
		breadth_search(node.right, counter, n, level-1)

def getHeight(node):
	if node==None:
		return 1

	l_height = getHeight(node.left)
	r_height = getHeight(node.right)

	return max(l_height,r_height)+1

# Traversing level-wise
def list_all_levels(node, n):
	# print("Node is "+format(node.data))
	counter = 0

	height = getHeight(node)
	# print("Height is "+format(height))
	# exit()

	print("\nThe closest "+format(n)+" items for "+format(node.data)+" is ", end="")

	for i in range(1, height):
		breadth_search(node, counter, n, i)
		# print("Next level")



if(len(sys.argv) < 3):
    print("Invalid number of arguments\n")
    exit(0)

# to_process = parseCsv("sample.csv")
to_process = parseCsv(sys.argv[1])
n = sys.argv[2]


# Initialising tree
t = Tree(to_process[0])

for i in range(1, len(to_process)):
	t.insert(to_process[i])


# s_result = t.search("3")

# if s_result is None:
# 	print("No results found")
# else:
# 	print(s_result)


for i in to_process:
	getClosest(t.root, i, n)
