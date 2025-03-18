# Huffman, LZ77, and LZ78 Algorithms

This project contains Python implementations of Huffman, LZ77, and LZ78 compression algorithms. Each algorithm has its own Python file.

## Files and Their Contents

### 1. Huffman Algorithm (`huffman.py`)
This file implements Huffman encoding for text compression and decompression.

**Features:**
- Calculates character frequencies in text files.
- Builds a Huffman tree and generates Huffman codes for characters.
- Compresses data using Huffman codes and creates a compressed file.
- Decompresses the compressed file to restore the original text.
- Supports bit-level compression and decompression.

**Usage:**
```sh
python huffman.py
```

---

### 2. LZ78 Algorithm (`lz78.py`)
This file implements the LZ78 compression and decompression algorithm.

**Features:**
- Compresses text files using the LZ78 algorithm.
- Decompresses compressed data to restore the original content.
- Performs encoding and decoding operations on a file basis.

**Usage:**
```python
encodeLZ('input.txt', 'encoded.txt')
decodeLZ('encoded.txt', 'decoded.txt')
```

---

### 3. LZ77 Algorithm (`LZ77.py`)
This file implements the LZ77 compression and decompression algorithm.

**Features:**
- Uses a sliding window mechanism for data compression.
- Supports file-based compression and decompression.
- Stores compressed data in binary format.

**Usage:**
```python
compressor = LZ77Compressor()
compressor.compress('input.txt', 'compressed.lz77')
compressor.decompress('compressed.lz77', 'output.txt')
```

## Requirements
The following dependencies must be installed for these scripts to work:
```sh
pip install bitarray
```

## License
This project is open-source and has no licensing restrictions.

