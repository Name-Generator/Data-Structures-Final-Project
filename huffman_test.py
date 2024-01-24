import unittest
import huffman


class TestProject3(unittest.TestCase):
    def test_counter_with_example(self):
        f = huffman.cnt_freq('frequency_file.txt')
        self.assertEqual(f[32], 3)
        self.assertEqual(f[97:101], [4, 3, 2, 1])

    def test_counter_with_empty(self):
        f = huffman.cnt_freq('empty.txt')
        self.assertEqual(f, [0] * 256)

    def test_create_huff_with_example(self):
        f = huffman.cnt_freq('frequency_file.txt')
        tree = huffman.create_huff_tree(f)
        self.assertEqual(tree.ascii_character, ' ')
        self.assertEqual(tree.occurrence_count, 13)

    def test_create_huff_with_empty(self):
        f = huffman.cnt_freq('empty.txt')
        self.assertEqual(huffman.create_huff_tree(f), None)

    def test_create_code_with_example(self):
        f = huffman.cnt_freq('frequency_file.txt')
        tree = huffman.create_huff_tree(f)
        self.assertEqual(huffman.create_code(tree)[32], '00')
        self.assertEqual(huffman.create_code(tree)[97:101], ['11', '01', '101', '100'])

    def test_create_code_with_empty(self):
        f = huffman.cnt_freq('empty.txt')
        tree = huffman.create_huff_tree(f)
        self.assertEqual(huffman.create_code(tree), [''] * 256)

    def test_create_header_with_example(self):
        f = huffman.cnt_freq('frequency_file.txt')
        self.assertEqual(huffman.create_header(f), '32 3 97 4 98 3 99 2 100 1 \n')

    def test_create_header_with_empty(self):
        f = huffman.cnt_freq('empty.txt')
        tree = huffman.create_header(f)
        self.assertEqual(tree, '')

    def test_encode_with_example(self):
        self.assertEqual(huffman.huffman_encode('frequency_file.txt', 'resultant_example.txt'), '11011011000011011010011010011')

    def test_encode_with_empty(self):
        self.assertEqual(huffman.huffman_encode('empty.txt', 'resulting_empty.txt'), '')

    def test_encode_with_one_letter(self):
        self.assertEqual(huffman.huffman_encode('all_one_letter.txt', 'resultant.txt'), '')

    def test_encode_with_keyboard_smash(self):
        self.assertEqual(huffman.huffman_encode('keyboard_smash.txt', 'resultant.txt'), '011010010011010111000110101110111111011100011111011101100010110111000010100101001101000000101101001110111111011100011111011101100010110101111110001110101001100110100111110110110001101011101110000101000100101000111011010000001011010011101110001111101110110001011010000010100000111010101110100111111001111110011111100111111101000111010000110111110110001110100010110111110111011101010101011110101001000101111000111100101101111000001110001000110011110100111100001110100110111000110010100001111111010101000010001011010000001011010011101111110101010010111010100110010111100110000000100011010100')


if __name__ == "__main__":
    unittest.main()
