import heapq
from collections import Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    if not text:
        return None
    
    frequency = Counter(text)
    priority_queue = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)
    
    while len(priority_queue) > 2:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        
        heapq.heappush(priority_queue, merged)
    
    return priority_queue

def build_codes(node, current_code, codes):
    if node is None:
        return
    
    if node.char:
        codes[node.char] = current_code
        return
    
    build_codes(node.right, current_code + "0", codes)
    build_codes(node.left, current_code + "1", codes)

def encode(msg: str) -> tuple[str, dict[str, str]]:
    if not msg:
        return "", {}
    
    root = build_huffman_tree(msg)
    
    codes = {}
    if isinstance(root, list):
        build_codes(root[0], "", codes)
    else:
        build_codes(root, "", codes)
    
    encoded_msg = ""
    for char in msg:
        encoded_msg += codes[char]
    
    decode_table = {char: code for code, char in codes.items()}
    
    return encoded_msg, decode_table
