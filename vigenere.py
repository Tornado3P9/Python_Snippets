# import sys
# text = sys.argv[1]
# key = sys.argv[2]

alphabet = "abcdefghijklmnopqrstuvwxyz"

text = input("Your text: ")
key  = input(" Your key: ")
option = input(" encrypt 'e' oder decrypt 'd': ")

while len(text) != len(key):
    print(f"Unequal input length! text = {len(text)}, key = {len(key)}")
    text = input("Your text: ")
    key  = input(" Your key: ")

text_index_list = []
for t in text:
    text_index_list.append(alphabet.index(t))

key_index_list = []
for k in key:
    key_index_list.append(alphabet.index(k))

result = []
if option == 'e':
    for i in range(len(text)):
        x = text_index_list[i]
        y = key_index_list[i]
        result.append((x+y)%len(alphabet))
else:
    for i in range(len(text)):
        x = text_index_list[i]
        y = key_index_list[i]
        result.append((x-y)%len(alphabet)) # (x-y+26) mod 26

print( "".join([alphabet[r] for r in result]) )
