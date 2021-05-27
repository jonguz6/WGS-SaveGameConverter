import itertools


def hex_part_reverse(hex_part: str, split_length: int = 2) -> str:
    hex_part = reversed([hex_part[i:i + split_length] for i in range(0, len(hex_part), split_length)])
    hex_part_reversed = ''
    for item in hex_part:
        hex_part_reversed += item
    return hex_part_reversed


def hex_string_reverse(hex_string: str) -> str:
    hex_string = hex_string.replace(' ', '')
    if len(hex_string) != 32:
        raise ValueError("String is not the correct length")
    int32 = hex_string[:8]
    int16_1 = hex_string[8:12]
    int16_2 = hex_string[12:16]
    int16_3 = hex_string[16:20]
    int32 = hex_part_reverse(int32)
    int16_1 = hex_part_reverse(int16_1)
    int16_2 = hex_part_reverse(int16_2)
    int16_3 = hex_part_reverse(int16_3)

    return int32 + int16_1 + int16_2 + int16_3 + hex_string[20:]


def filename_parser(data: str) -> dict:
    data_array = data.split('''000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000''')
    wgs_filename = data_array[1][:32]
    wgs_filename = hex_string_reverse(wgs_filename)
    steam_filename = bytes.fromhex(data_array[0]).decode().replace('\x00', '')
    data_dict = {steam_filename: wgs_filename}
    return data_dict


def data_parser(data: str) -> str:
    data = data.replace('040000000B000000', '')
    data = [data[i:i+2] for i in range(0, len(data), 2)]
    array = []
    idx = 0
    i = 0
    skipping = False

    while i != len(data) - 1:
        prev = data[i - 1] or None
        curr = data[i]
        nxxt = data[i + 1] or None

        if curr == '00' == nxxt:
            skipping = True
            i += 1
            continue

        if curr == '00' == prev:
            i += 1
            continue

        if skipping:
            idx += 1
            i += 1
            skipping = False

        if idx == len(array):
            array.append('')

        array[idx] += curr
        i += 1

    data_dict = {}
    for idx, item in enumerate(array):
        if idx == 0:
            data_dict[item] = 0
        if len(item) > 64:
            filename = item[:32]
            rest = item[64:]







