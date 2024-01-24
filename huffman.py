import Ordered_linked_list
import huffmna_bit_writer


def cnt_freq(filename: str) -> list:
    try:
        file = open(filename, 'r')
        big_string = file.read()
        super_list = [0] * 256
        for i in big_string:
            temp = ord(i)
            super_list[temp] += 1
        file.close()
        return super_list
    except FileNotFoundError:
        raise FileNotFoundError


class HuffmanNode:
    def __init__(self, ascii_val, occurrence_count):
        self.right = None
        self.left = None
        self.ascii_character = chr(ascii_val)
        self.occurrence_count = occurrence_count

    def __lt__(self, other):
        if self.occurrence_count == other.occurrence_count:
            if ord(self.ascii_character) < ord(other.ascii_character):
                return True
            else:
                return False
        if self.occurrence_count < other.occurrence_count:
            return True
        return False


def create_huff_tree(list_of_frequencies: list) -> None or HuffmanNode:
    if list_of_frequencies == [0] * 256:
        return None
    ordered_huff = Ordered_linked_list.OrderedList()
    for i in range(len(list_of_frequencies) - 1):
        if list_of_frequencies[i] != 0:
            ordered_huff.add(HuffmanNode(i, list_of_frequencies[i]))
    if ordered_huff.is_empty():
        return None
    size = ordered_huff.size
    while size > 1:
        if ordered_huff.head.item > ordered_huff.head.next.item: # second item has smaller ASCII value
            new_huff = HuffmanNode(ord(ordered_huff.head.next.item.ascii_character),
                                ordered_huff.head.next.item.occurrence_count + ordered_huff.head.item.occurrence_count)
            new_huff.right = ordered_huff.pop(0)
            new_huff.left = ordered_huff.pop(0)
            ordered_huff.add(new_huff)
            size = ordered_huff.size
        else: # first item has smaller ASCII value
            if ord(ordered_huff.head.next.item.ascii_character) > ord(ordered_huff.head.item.ascii_character):
                new_huff = HuffmanNode(ord(ordered_huff.head.item.ascii_character),
                                ordered_huff.head.next.item.occurrence_count + ordered_huff.head.item.occurrence_count)
            else:
                new_huff = HuffmanNode(ord(ordered_huff.head.next.item.ascii_character),
                                ordered_huff.head.next.item.occurrence_count + ordered_huff.head.item.occurrence_count)
            new_huff.left = ordered_huff.pop(0)
            new_huff.right = ordered_huff.pop(0)
            ordered_huff.add(new_huff)
            size = ordered_huff.size
    return ordered_huff.head.item


def create_code(root_node: HuffmanNode) -> list[str]:
    array = [''] * 256
    if root_node is None:
        return [''] * 256

    def traversal(node, alist: str):
        if node.left is None and node.right is None:
            array[ord(node.ascii_character)] = alist
        else:
            if node.left:
                traversal(node.left, alist + '0')
            if node.right:
                traversal(node.right, alist + '1')
        return array
    return traversal(root_node, '')


def create_header(list_of_freqs: list) -> str:
    if list_of_freqs == [0] * 256 or list_of_freqs is None:
        return ''
    resulting_string = ''
    for index in range(len(list_of_freqs)):
        if list_of_freqs[index] != 0:
            resulting_string += (str(index) + ' ' + str(list_of_freqs[index]) + ' ')
    return resulting_string + '\n'


def huffman_encode(in_file: str, out_file: str):
    try:
        frequencies = cnt_freq(in_file)
        header = create_header(frequencies)
        tree = create_huff_tree(frequencies)
        list_of_strings_of_codes = create_code(tree)
        opened_in_file = open(in_file, 'r')
        contents_infile = opened_in_file.read()
        opened_in_file.close()

        proper_out_file = out_file.replace('.txt', '_compressed.txt')
        bit_written_out_file = huffmna_bit_writer.HuffmanBitWriter(proper_out_file)
        bit_written_out_file.write_str(header)
        string_for_printing = ''
        for item in contents_infile:
            bit_written_out_file.write_code(list_of_strings_of_codes[ord(item)])
            string_for_printing += list_of_strings_of_codes[ord(item)]
        bit_written_out_file.close()
        return string_for_printing
    except FileNotFoundError:
        raise FileNotFoundError
