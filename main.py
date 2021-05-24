def hex_part_reverse(hex_part: str, split_length: int = 2) -> str:
    hex_part = [hex_part[i:i+split_length] for i in range(0, len(hex_part), split_length)]
    hex_part.reverse()
    hex_part_reversed = ''
    for item in hex_part:
        hex_part_reversed += item
    return hex_part_reversed


def hex_string_reverse(hex_string: str) -> str:
    pass