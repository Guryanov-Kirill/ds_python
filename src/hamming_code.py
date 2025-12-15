def parity_bit(bits, indices):
    return sum(bits[i - 1] for i in indices) % 2

def encryption(data):
    if len(data) != 4:
        raise ValueError("неверные входные данные")

    d1, d2, d3, d4 = data
    p1 = (d1 + d2 + d4) % 2
    p2 = (d1 + d3 + d4) % 2
    p3 = (d2 + d3 + d4) % 2
    
    encoded = [p1, p2, d1, p3, d2, d3, d4]
    return "".join(map(str, encoded))

def decryption(decryption_data):
    if len(decryption_data) != 7:
        raise ValueError("в строке должно быть 7 бит")
    bits = [int(i) for i in decryption_data]
    s1 = parity_bit(bits, [1, 3, 5, 7])
    s2 = parity_bit(bits, [2, 3, 6, 7])
    s4 = parity_bit(bits, [4, 5, 6, 7])

    pos = s4 * 4 + s2 * 2 + s1
    if pos == 0:
        return -1
    else:
        return pos