from BTree import BTree

if __name__ == '__main__':
    b_tree = BTree(4)
    array = [8, 11, 6, 7, 15, 12, 13, 4, 34, 10]
    for num in array:
        b_tree.insert(num)
    b_tree.traverse(b_tree.root)
