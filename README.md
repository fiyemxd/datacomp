# Text Compression Algortihms
 
# Huffman, LZ77 ve LZ78 Algoritmaları

Bu proje, veri sıkıştırma tekniklerinden Huffman, LZ77 ve LZ78 algoritmalarını içeren Python kodlarını içerir. Her algoritma için ilgili Python dosyaları mevcuttur.

## Dosyalar ve İçerikleri

### 1. Huffman Algoritması (`huffman.py`)
Bu dosya, Huffman kodlamasını kullanarak metin sıkıştırma ve açma işlemlerini gerçekleştirir.

**Özellikler:**
- Metin dosyalarındaki karakter frekanslarını hesaplar.
- Huffman ağacını oluşturur ve karakterler için Huffman kodlarını belirler.
- Veriyi Huffman kodlarıyla sıkıştırır ve sıkıştırılmış dosyayı oluşturur.
- Sıkıştırılmış dosyayı açarak orijinal metni geri getirir.
- Bit seviyesinde dosya sıkıştırma ve açma işlemleri de desteklenir.

**Kullanım:**
```sh
python huffman.py
```

---

### 2. LZ78 Algoritması (`lz78.py`)
Bu dosya, LZ78 algoritmasını kullanarak veri sıkıştırma ve açma işlemlerini yapar.

**Özellikler:**
- Metin dosyalarını LZ78 algoritması ile sıkıştırır.
- Sıkıştırılmış veriyi çözerek orijinal içeriği geri yükler.
- Kodlama ve kod çözme işlemlerini dosya bazlı gerçekleştirir.

**Kullanım:**
```python
encodeLZ('input.txt', 'encoded.txt')
decodeLZ('encoded.txt', 'decoded.txt')
```

---

### 3. LZ77 Algoritması (`LZ77.py`)
Bu dosya, LZ77 algoritmasını kullanarak veri sıkıştırma ve açma işlemlerini gerçekleştirir.

**Özellikler:**
- Sliding window (kaydırmalı pencere) mekanizması ile veri sıkıştırma yapar.
- Dosya bazlı sıkıştırma ve açma işlemlerini destekler.
- Sıkıştırılmış veriyi ikili formatta saklar.

**Kullanım:**
```python
compressor = LZ77Compressor()
compressor.compress('input.txt', 'compressed.lz77')
compressor.decompress('compressed.lz77', 'output.txt')
```

## Gereksinimler
Bu kodların çalışması için aşağıdaki bağımlılıkların yüklenmiş olması gerekmektedir:
```sh
pip install bitarray
```

## Lisans
Bu proje açık kaynaklıdır ve herhangi bir lisans kısıtlaması bulunmamaktadır.


