import codecs
slugma = open('Slugma.pk9', "rb")
hex = slugma.read().hex()

def decode_stat(stat_name, start, size):
    print(stat_name + ":")
    data = int(hex[start:start+size],16)

    if size == 2:
        print(data)
    else:
        print(int("0x" +codecs.encode(codecs.decode(hex[start:start+size], 'hex')[::-1], 'hex').decode(),0))
    print("")

decode_stat("Species Number",16,4)
decode_stat("EXP",32,8)
decode_stat("Ability",44,4)
decode_stat("Nature",64,2)
decode_stat("Stat Nature",66,2)
print("Gender:")
data = int(hex[68:70],16)
if data == 0 or data == 1:
    print("Male")
elif data == 2 or data == 3:
    print("Female")
elif data == 4 or data == 5:
    print("Sexless")
print("")
decode_stat("Health EV",76,2)
decode_stat("Attack EV",78,2)
decode_stat("Defense EV",80,2)
decode_stat("Speed EV",82,2)
decode_stat("Special Attack EV",84,2)
decode_stat("Special Defense EV",86,2)
decode_stat("Height",144,2)
decode_stat("Weight",146,2)
decode_stat("Scale",148,2)
print("Nickname:")
nick = ""
for i in range(0,24):
    if i % 2 == 0:
        data = int(hex[176+i*2:178+i*2],16)
        nick += chr(data)
print(nick)
print("")
decode_stat("Move 1", 228,4)
decode_stat("Move 2", 232,4)
decode_stat("Move 3", 236,4)
decode_stat("Move 4", 240,4)
#IVS

slugma.close()