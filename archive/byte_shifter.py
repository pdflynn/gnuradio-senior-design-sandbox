from bitstring import ConstBitStream
import copy

# Read bytes and attempt to decode
for i in range(0, 16):
    b = ConstBitStream(filename='barebones_out.txt')
    thrown_out = b.read(i)
    valid_bits = b.read(8)
    valid_bits_str = str(valid_bits)
    valid_bits_binary = valid_bits.read('bin:8')
    valid_bits_int = int(valid_bits_binary, 2)
    valid_bits_char = chr(valid_bits_int)
    print("Shifted by", str(i), ": ", valid_bits_str,
          "| Binary: ", valid_bits_binary, "| Integer: ", str(valid_bits_int), "| Char: ", valid_bits_char)

# Save a new file and throw out n bits
b = ConstBitStream(filename='barebones_out.txt')
throw_away = b.read(3)

f = open('shifted_file.txt', 'wb')

while b.peek(8):
    print(str(b.peek(8)))
    f.write(b.read(8).tobytes())
