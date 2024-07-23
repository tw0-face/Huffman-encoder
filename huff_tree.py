import turtle


class HuffmanTree:
    def __init__(self, data) -> None:
        self.data = data
        self.origin = 0, 250

    def turtle_space(self):
        turtle.penup()
        turtle.forward(20)
        turtle.pendown()

    def down_lt_branch(self, a, length):
        branch_length = length * (length * 6 / 2 ** a)
        turtle.forward(10)
        turtle.right(90)
        turtle.forward(branch_length)
        turtle.left(90)
        turtle.forward(10)
        self.turtle_space()

    def down_rt_branch(self, a, length):
        branch_length = length * (length * 6 / 2 ** a)
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(branch_length)
        turtle.right(90)
        turtle.forward(10)
        self.turtle_space()

    def write_uncircled(self, character, size):
        turtle.penup()
        turtle.left(90)
        turtle.backward(size * 2)
        turtle.pendown()
        turtle.write(character, font=("Arial", 10, "normal"))
        turtle.penup()
        turtle.forward(size * 2)
        turtle.right(90)
        turtle.pendown()

    def write_circled(self, character, size):
        turtle.penup()
        turtle.left(90)
        turtle.backward(size * 3)
        turtle.pendown()
        turtle.write(character, font=("Arial", 10, "normal"))
        turtle.penup()
        turtle.forward(size * 3)
        turtle.pendown()
        turtle.circle(10)
        turtle.right(90)

    def init_turtle_screen(self):
        turtle.title('Huffman Coding Visualization')
        turtle.speed(0)
        turtle.color("black")
        turtle.bgcolor("white")

    def tp(self):
        turtle.penup()
        turtle.goto(self.origin)
        turtle.pendown()

    def tree_info(self, freq, huf):
        frequency, huff = freq, huf
        huff_frequency = [[frequency[symbol], binary] for symbol, binary in huff]
        parent_nodes = []

        huff_frequency.sort(key=lambda x: len(x[1]), reverse=True)

        current_binary_value = huff_frequency[0]

        while len(huff_frequency) > 2:
            for freq, binary in huff_frequency:
                if binary[:-1] == current_binary_value[1][:-1] and binary != current_binary_value[1]:
                    parent_value = freq + current_binary_value[0]
                    huff_frequency.append([parent_value, binary[:-1]])

                    parent_nodes.append([parent_value, binary[:-1]])

                    huff_frequency.remove(current_binary_value)
                    huff_frequency.remove([freq, binary])
            current_binary_value = huff_frequency[0]
            huff_frequency.sort(key=lambda x: len(x[1]), reverse=True)

        huffman_tree_data = huff + parent_nodes

        return huffman_tree_data

    def tree_visualize(self, freq, huf):
        self.init_turtle_screen()
        _, huff = freq, huf

        length = len(huff[len(huff) - 1][1])

        huffman_tree_data = self.tree_info(freq, huff)

        self.tp()
        turtle.right(90)
        self.write_circled(len(self.data), 2)

        for char, binary_code in huffman_tree_data:
            for index, bit in enumerate(binary_code):
                if bit == '0':
                    self.down_lt_branch(index, length)
                else:
                    self.down_rt_branch(index, length)

            if type(char) is str:
                if char == ' ':
                    self.write_uncircled("space", 5)
                self.write_uncircled(char, len(char))
            else:
                self.write_circled(char, len(str(char)))
            self.tp()

        turtle.penup()
        turtle.goto(0, 300)
        turtle.pendown()
        turtle.write(self.data, font=("Arial", 15, "normal"), align='center')

        turtle.hideturtle()
        turtle.mainloop()