line="011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110"
braille_key = [line[i:i+6] for i in range(0, len(line), 6)]

string = "the quick brown fox jumps over the lazy dog"

letter_dict={string[x]:braille_key[x] for x in range(len(braille_key))}

def solution(s):
  braille = ""
  for letter in s:
    if letter in letter_dict.keys():
      braille+=letter_dict[letter]
    else:
      braille+="000001"
      braille+=letter_dict[letter.lower()]
  return braille