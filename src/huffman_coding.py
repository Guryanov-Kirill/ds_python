import heapq
from collections import Counter

class Node:
    def __init__(self, char, freq):
        self.char = char      # Символ
        self.freq = freq      # Сколько раз встречается
        self.left = None      # Левый узел
        self.right = None     # Правый узел
    
    def __lt__(self, other):
        return self.freq < other.freq  # Сравниваем по частоте

def build_huffman_tree(text):
    if not text:
        return None
    
    # Считаем частоту символов
    frequency = Counter(text)
    # Создаем узлы для каждого символа
    priority_queue = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)  # Упорядочиваем по частоте
    
    # Строим дерево, объединяя узлы
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)  # Берем узел с наименьшей частотой
        right = heapq.heappop(priority_queue)
        
        # Создаем главный узел
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        
        heapq.heappush(priority_queue, merged)  # Добавляем обратно
    
    return priority_queue[0]  # Возвращаем корень дерева

def build_codes(node, current_code, codes):
    if node is None:
        return
    
    if node.char is not None:
        codes[node.char] = current_code
        return
    
    # Идем влево добавляем 0
    build_codes(node.left, current_code + "0", codes)
    # Идем вправо добавляем 1
    build_codes(node.right, current_code + "1", codes)

def encode(msg: str) -> tuple[str, dict[str, str]]:
    if not msg:
        return "", {}
    
    # Строим дерево и коды
    root = build_huffman_tree(msg)
    codes = {}
    build_codes(root, "", codes)
    
    # Кодируем сообщение
    encoded_msg = ""
    for char in msg:
        encoded_msg += codes[char]   # Добавляем код
    
    # Создаем таблицу для декодирования
    decode_table = {code: char for char, code in codes.items()}
    
    return encoded_msg, decode_table
    
def decode(encoded_msg: str, decode_table: dict[str, str]) -> str:
    if not encoded_msg or not decode_table:
        return ""
    
    decoded_msg = ""
    current_code = ""  # Накапливаем биты кода
    
    # Идём по битам и добавляем в current_code
    for bit in encoded_msg:
        current_code += bit
        # Если код найден в таблице
        if current_code in decode_table:
            decoded_msg += decode_table[current_code]
            current_code = ""
    
    return decoded_msg