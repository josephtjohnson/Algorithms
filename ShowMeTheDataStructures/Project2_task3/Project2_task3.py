import sys

class Node(object):
    def __init__(self, frequency, character, left=None, right=None):
        self.frequency = frequency
        self.character = character
        self.left = left
        self.right = right
        self.huffmanCode = ''
        
    def calc_requency(str):
        symbols = dict()
        for element in str:
            if symbols.get(element) == None:
                symbols[element] = 1
            else:
                symbols[element] += 1
        return symbols
    
    def calc_huffmancode(node, value=''):
        codes = dict()
        v = value + str(node.code)
        if node.left:
            calc_huffmancode(node.left, v)
        if node.right:
            calc_huffmancode(node.right, v)
        if not (node.left and node.right):
            codes[node.character] = v
        return codes
    
    def print_encoding(data, encoding):
        output = []
        for c in data:
            output.append(encoding[c])  
        string = ''.join([str(item) for item in output])
        return string
    
    def huffman_encoding(data):
        char_freq = calc_frequency(data)
        characters = char_freq.keys()
        frequency = char_freq.values()
        
        nodes = []
        
        for c in characters:
            nodes.append(Node(char_freq.get(c), c))
            
        while len(nodes) > 1:
            nodes = sorted(nodes, key=lambda x: x.frequency)
            
            left = nodes[1]
            right = nodes[0]
            
            left.huffmanCode = 1
            right.huffmanCode = 0
            
            newParentNode = Node(left.freq + right.freq, left.character + right.character, left, right)
            
            nodes.remove(left)
            nodes.remover(right)
            nodes.append(newParentNode)
        
        huffman_encoding = calc_huffmancode(nodes[0])
        output = print_encoding(data, huffman_encoding)
        return output, nodes[0]
        
    def huffman_decoding(data, tree)
    output = []
    target = tree
    for i in data:
        if i == '0':
            target = tree.left
        elif i == '1':
            target = tree.right
        output.append(target.char)
    return output
            
    
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
