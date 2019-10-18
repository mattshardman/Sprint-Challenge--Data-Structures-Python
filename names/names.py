import time

start_time = time.time()

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.stack = []

    # Insert the given value into the tree
    def insert(self, value):
        if value <= self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else: 
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self == None:
            return False
        elif self.value == target:
            return True
        elif target < self.value:
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            if not self.right:
                return False
            return self.right.contains(target)

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

def bin_search_names():
    names_2_tree = BinarySearchTree(names_2[0])

    for name in names_2[1:]:
        names_2_tree.insert(name)

    for name_1 in names_1:
        contains = names_2_tree.contains(name_1)
        if contains:
            duplicates.append(name_1)


def bin_search_dict_names():
    names_2_dict = {}

    for name in names_2:
        if not names_2_dict.get(name[0]):
            names_2_dict[name[0]] = BinarySearchTree(name)
        else:
            names_2_dict[name[0]].insert(name) 

    for name_1 in names_1:
        if names_2_dict[name_1[0]]:
            contains = names_2_dict[name_1[0]].contains(name_1)
            if contains:
                duplicates.append(name_1)

def dic_search_names():
    names_2_dict = {}

    for name in names_2:
        names_2_dict[name] = True

    for name_1 in names_1:
        if names_2_dict.get(name_1):
            duplicates.append(name_1)

def embedded_comp_search():
    duplicates = []

    for name_1 in names_1:
        if name_1 in names_2:
            duplicates.append(name_1)

# bin_search_names()
# bin_search_dict_names()
dic_search_names() # quickest
# embedded_comp_search()

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

