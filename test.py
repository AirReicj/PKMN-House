import codecs
from flask import Flask, render_template
import os

end_res = ""
data = 0
hex = ""

species=0
exp=0
ability=0
nature=0
stat_nature=0
gender=0
hp_ev=0
att_ev=0
def_ev=0
speed_ev=0
sp_att_ev=0
sp_def_ev=0
height=0
weight=0
name=""
move1=0
move2=0
move3=0
move4=0
friendship=0
date_met=0
location_met=0
version_met=0
level=0

app = Flask(__name__)
@app.route("/")
def hello_world():
    global end_res
    global data
    global hex
    slugma_path = os.getcwd()+"\Slugma.pk9"
    end_res = ""
    slugma = open(slugma_path, "rb")
    hex = slugma.read().hex()

    decode_all_stats()
    
    slugma.close()
    return render_template(
        "base.html",
        text= end_res,
        temp = hp_ev
    )

def decode_stat(stat_name, start, size):
    global end_res
    global data
    global hex

    end_res += str(stat_name) + ":<br>"
    data = int(hex[start:start+size],16)

    if size == 2:
        end_res += str(data) + "<br>"
    else:
        end_res += str(int("0x" +codecs.encode(codecs.decode(hex[start:start+size], 'hex')[::-1], 'hex').decode(),0)) + "<br>"
    end_res += "<br>"

def decode_all_stats():
    global end_res 
    global data
    global hex
    global hp_ev

    decode_stat("Species Number",16,4)
    decode_stat("EXP",32,8)
    decode_stat("Ability",44,4)
    decode_stat("Nature",64,2)
    decode_stat("Stat Nature",66,2)
    end_res += "Gender:<br>"
    data = int(hex[68:70],16)
    if data == 0 or data == 1:
        end_res += "Male<br>"
    elif data == 2 or data == 3:
        end_res += "Female<br>"
    elif data == 4 or data == 5:
        end_res += "Sexless<br>"
    end_res += "<br>"
    decode_stat("Health EV",76,2)
    decode_stat("Attack EV",78,2)
    decode_stat("Defense EV",80,2)
    decode_stat("Speed EV",82,2)
    decode_stat("Special Attack EV",84,2)
    decode_stat("Special Defense EV",86,2)
    decode_stat("Height",144,2)
    decode_stat("Weight",146,2)
    end_res += "Name:<br>"
    nick = ""
    for i in range(0,24):
        if i % 2 == 0:
            data = int(hex[176+i*2:178+i*2],16)
            nick += chr(data)
    end_res += str(nick) + "<br>"
    end_res += "<br>"
    decode_stat("Move 1", 228,4)
    decode_stat("Move 2", 232,4)
    decode_stat("Move 3", 236,4)
    decode_stat("Move 4", 240,4)
    decode_stat("Friendship",548,2)
    decode_stat("Year",568,2)
    decode_stat("Month",570,2)
    decode_stat("Day",572,2)
    decode_stat("Location Met",580,4)
    decode_stat("Version",448,2)
    decode_stat("Level", 656,2)

    #IVS
    hp_ev = bin(int("0x" +codecs.encode(codecs.decode(hex[280:288], 'hex')[::-1], 'hex').decode(),0))[2:]
    hp_ev = hp_ev[len(hp_ev)-15:][:-10]
    #first nº after len is the bit shift, the second is the bitshift +5


