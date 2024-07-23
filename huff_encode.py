from prettytable import PrettyTable
import math
from heapq import *
from collections import *
from huff_tree import HuffmanTree


def huff_encoder(char_freq):
    heap_list = [[wt, [sym, ""]] for sym, wt in char_freq.items()]
    heapify(heap_list)
    while len(heap_list) > 1:
        low = heappop(heap_list)
        high = heappop(heap_list)
        for item in high[1:]:
            item[1] = '1' + item[1]
        for item in low[1:]:
            item[1] = '0' + item[1]
        heappush(heap_list, [low[0] + high[0]] + low[1:] + high[1:])
    return sorted(heappop(heap_list)[1:], key=lambda op: (len(op[-1]), op))


print("\n")

ip_str = input("Input tex to encode: ")
tree_code = str(ip_str)
huffman_tree = HuffmanTree(str(ip_str))
char_freq = defaultdict(int)
for char in ip_str:
    char_freq[char] += 1

huffman_tree = huff_encoder(char_freq)
x = PrettyTable()
len_code = 0
entropy = 0
prob = 0
encoded = {}
ip_len = str(len(ip_str))
x.field_names = ["Letter", "Frequency", "Probability", "Huffman Encoding", "Length"]
for op in huffman_tree:
    prob = ((int)(char_freq[op[0]]) / (len(ip_str)))
    x.add_row([op[0], char_freq[op[0]], (int)(char_freq[op[0]]) / (len(ip_str)), op[1], len(op[1])])
    len_code += prob * len(op[1])
    entropy += prob * (math.log2(1 / prob))
    encoded[op[0]] = str(op[1])

print("\n")
print(x)
print("\nCalculations :-")
print("\nLength of the code: " + str(len_code))
print("\nEntropy: " + str(entropy))
print("\nEfficiency: " + str(entropy / len_code))
print("\nRedundancy: " + str(1 - (entropy / len_code)))

for key, val in encoded.items():
    ip_str = ip_str.replace(key, val)

print("\nRatio: " + str(int(len(str(ip_str)) * 100) / (int(ip_len) * 8)) + "%")
print("\n\033[1;32m Encoded message: " + str(ip_str) + "\n")


huffman_tree = HuffmanTree(tree_code)
huffman_tree.tree_info(char_freq, huff_encoder(char_freq))
huffman_tree.tree_visualize(char_freq, huff_encoder(char_freq))




