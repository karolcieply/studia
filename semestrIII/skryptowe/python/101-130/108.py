def code_shannon_fano(data, code_table):
    if len(data) == 1:
        return data[0]
    else:
        mid = len(data) // 2
        left = code_shannon_fano(data[:mid], code_table)
        right = code_shannon_fano(data[mid:], code_table)
        return (left, right)


def decode_shannon_fano(data, code_table):
    if isinstance(data, tuple):
        return decode_shannon_fano(data[0], code_table) + decode_shannon_fano(
            data[1], code_table
        )
    else:
        return code_table[data]
