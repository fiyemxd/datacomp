def encodeLZ(FileIn, FileOut):
    chunk_size = 1024  # 1 KB
    dict_of_codes = {}
    code = 1

    with open(FileIn, 'r', encoding='utf-8') as input_file, open(FileOut, 'w', encoding='utf-8') as encoded_file:
        while True:
            text_from_file = input_file.read(chunk_size)
            if not text_from_file:
                break  # Dosyanın sonuna ulaşıldı
            
            combination = ''
            for char in text_from_file:
                combination += char
                if combination not in dict_of_codes:
                    dict_of_codes[combination] = str(code)
                    if len(combination) == 1:
                        encoded_file.write('0' + combination)
                    else:
                        encoded_file.write(dict_of_codes[combination[:-1]] + combination[-1])
                    code += 1
                    combination = ''  # Reset combination
            print("a")

    return True


def decodeLZ(FileIn, FileOut):
    coded_file = open(FileIn, 'r', encoding = 'utf-8')
    decoded_file = open(FileOut, 'w', encoding = 'utf-8')
    text_from_file = coded_file.read()
    dict_of_codes = {'0': '', '1': text_from_file[1]}
    decoded_file.write(dict_of_codes['1'])
    text_from_file = text_from_file[2:]
    combination = ''
    code = 2
    for char in text_from_file:
        if char in '1234567890':
            combination += char
        else:
            dict_of_codes[str(code)] = dict_of_codes[combination] + char
            decoded_file.write(dict_of_codes[combination] + char)
            combination = ''
            code += 1
    coded_file.close()
    decoded_file.close()


# Test Kodları:
encodeLZ(
    'C:\\Users\\lenovo\\programmin\\python\\data comp\\datacomp\\pg11.txt', 
    'C:\\Users\\lenovo\\programmin\\python\\data comp\\datacomp\\lz78\\encoded.txt'
)
decodeLZ(
    'C:\\Users\\lenovo\\programmin\\python\\data comp\\datacomp\\lz78\\encoded.txt', 
    'C:\\Users\\lenovo\\programmin\\python\\data comp\\datacomp\\lz78\\decoded.txt'
)
