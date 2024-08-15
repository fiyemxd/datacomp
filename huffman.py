import heapq
import time
from collections import Counter, defaultdict

class Node:
    def __init__(self, frequency, symbol=None, left=None, right=None):
        self.frequency = frequency
        self.symbol = symbol
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.frequency < other.frequency

def huffman_tree(symbols):
    heap = [Node(freq, sym) for sym, freq in symbols.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(left.frequency + right.frequency, left=left, right=right)
        heapq.heappush(heap, merged)

    return heap[0]

def huffman_codes(tree):
    codes = {}
    
    def generate_codes(node, current_code):
        if node is not None: #node var ise, leafte biter
            if node.symbol is not None:
                codes[node.symbol] = current_code
            generate_codes(node.left, current_code + "0")
            generate_codes(node.right, current_code + "1")
    
    generate_codes(tree, "")
    return codes

def encode(text, codes):
    return ''.join(codes[symbol] for symbol in text)

def decode(encoded_text, tree):
    decoded_text = []
    node = tree
    for bit in encoded_text:
        node = node.left if bit == '0' else node.right
        if node.symbol is not None:
            decoded_text.append(node.symbol)
            node = tree
    return ''.join(decoded_text)

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def calculate_frequencies(file_path):
    counter = Counter()
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            chunk = file.read(1024 * 1024)
            if not chunk:
                break
            counter.update(chunk)
    return counter

def encode_file(input_path, output_path, codes):
    with open(input_path, 'r', encoding='utf-8') as infile, open(output_path, 'w', encoding='utf-8') as outfile:
        while True:
            chunk = infile.read(1024 * 1024)
            if not chunk:
                break
            encoded_chunk = encode(chunk, codes)
            outfile.write(encoded_chunk)

def encode_file_to_bytes(input_path, output_path, codes):
    with open(input_path, 'r', encoding='utf-8') as infile, open(output_path, 'wb') as outfile:
        while True:
            chunk = infile.read(1024 * 1024)
            if not chunk:
                break
            encoded_chunk = encode(chunk, codes)
            byte_data = bits_to_bytes(encoded_chunk)
            outfile.write(byte_data)

def decode_file(encoded_path, output_path, tree):
    with open(encoded_path, 'r', encoding='utf-8') as infile, open(output_path, 'w', encoding='utf-8') as outfile:
        encoded_text = infile.read()
        decoded_text = decode(encoded_text, tree)
        outfile.write(decoded_text)

def bits_to_bytes(bits):
    byte_arr = bytearray()
    for i in range(0, len(bits), 8):
        byte = bits[i:i + 8]
        if len(byte) < 8:
            byte += '0' * (8 - len(byte))
        byte_arr.append(int(byte, 2))
    return byte_arr

def save_bytes_to_file(byte_data, file_path):
    with open(file_path, 'wb') as file:
        file.write(byte_data)

def bytes_to_bits(byte_arr):
    bits = ''.join(format(byte, '08b') for byte in byte_arr)
    return bits

def read_encoded_bits(bin_path, output_path):
    
    with open(bin_path, 'rb') as infile, open (output_path, 'w', encoding='utf-8') as outfile:
        while True:
            chunk = infile.read(1024 * 1024)
            if not chunk:
                break
            bits = bytes_to_bits(chunk)
            outfile.write(bits)
    return bits

def main():
    input_file = 'pg11.txt'
    encoded_file = 'encoded.txt'
    encoded_bytes_file = 'encoded_bytes.bin'
    decoded_file = 'decoded.txt'
    bin_to_encoded_file = 'bin_to_encoded.txt'
    decoded_from_bin = 'decoded2.txt'

    start = time.time()
    symbols = calculate_frequencies(input_file)
    tree = huffman_tree(symbols)
    codes = huffman_codes(tree)

    encode_file(input_file, encoded_file, codes)
    encode_file_to_bytes(input_file, encoded_bytes_file, codes)
    end = time.time()


    decode_file(encoded_file, decoded_file, tree)

    print("Huffman Codes:", codes)

    with open(input_file, 'r', encoding='utf-8') as file:
        original_text = file.read()

    with open(decoded_file, 'r', encoding='utf-8') as file:
        decoded_text = file.read()

    assert original_text == decoded_text
    print("Metin başarıyla kodlandı ve çözüldü.")

    read_encoded_bits('encoded_bytes.bin',bin_to_encoded_file)
    decode_file(bin_to_encoded_file,decoded_from_bin,tree)
    print("elapsed time: " + str(end-start) + " seconds")
    print("a")
   

if __name__ == "__main__":
    main()
