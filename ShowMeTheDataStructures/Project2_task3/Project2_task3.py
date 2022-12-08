import sys

class Node(object):
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right
        self.huff = ''

    def get_left(self):
        return self.left

    def set_left_child(self, left):
        self.left = left

    def has_left_child(self):
        return self.left == True

    def get_right(self):
        return self.right

    def set_right_child(self, right):
        self.right = right

    def has_right_child(self):
        return self.right == True



def huffman_encoding(words,data):
    result = ''
    
    for i in range(0,len(words),1):
        result = result + data[words[i]]

    return result

def huffman_decoding(data,tree):
    result = ''
    dataLength = len(data)
    counter = 0
    while counter < dataLength:
        n = tree
        while n.get_left() != None and n.right != None:
            
            if data[counter] == 0:
                n.get_left_child()

            else:
                n.get_right_child()

            counter += 1
        result = n.value
    return result

def huffmancode(node,codes={},val=''):
    newVal = val + str(node.huff)
    if(node.get_left()):
        huffmancode(node.get_left(),codes, newVal)
    if(node.get_right()):
        huffmancode(node.get_right(),codes, newVal)
    if(not node.get_left() and not node.get_right()):
        codes[node.value] = newVal
    return codes

def saperate(data):
    frequency = {}
    for i in range(len(data)):
        if data[i] in frequency:
            frequency[data[i]]+=1
        else:
            frequency[data[i]]=1
    sort_order = sorted(frequency.items(), key=lambda x: x[1],reverse=False)
    return sort_order

def creation(a_great_sentence):
    frequency = saperate(a_great_sentence)
    char = []
    freq = []
    chars = []
    for values in frequency:
        char.append(values[0])
        freq.append(values[1])
    for cha in char:
        chars.append(Node(cha))
    tyu = 0
    while len(freq) != 1:
        index1 = freq.index(min(freq))
        freq1 = freq.pop(index1)
        index2 = freq.index(min(freq))
        freq2 = freq.pop(index2)
        char1 = chars.pop(index1)
        char2 = chars.pop(index2)
        newNode = Node(freq1+freq2)
        newNode.set_left_child(char1)
        newNode.set_right_child(char2)
        char1.huff = 0
        char2.huff = 1
        chars.insert(0,newNode)
        freq.insert(0, newNode.value)
    return newNode

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1

# Test Case 2

# Test Case 3
