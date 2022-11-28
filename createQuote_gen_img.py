import requests
import json
from moviepy.editor import *
from downloadChar import download_image

# def getQuote():
#     # global i 
#     # i+=1
#     req = requests.get("https://animechan.vercel.app/api/random/")
#     data = json.loads(req.content)
#     data["location"] = [f"quote{i}.png",f"charName{i}.png"]
#     return data

def createAssets():
    global i 
    i=0
    def getQuote():
        global i 
        i+=1
        req = requests.get("https://animechan.vercel.app/api/random/")
        data = json.loads(req.content)
        data["location"] = [f"quote{i}.png",f"charName{i}.png"]
        return data
    datas =[] 
    for j in range(3):
        datas.append(getQuote())

    datum = []
    for data in datas:

        txtClip = TextClip(  data["quote"],
                                color='black',
                                font="Forte",
                                # kerning = 5,
                                fontsize=45,
                                size=(600,450),
                                # print_cmd=True,
                                method="caption",
                                transparent=True
                                )
        txtClip.save_frame(data["location"][0])

        anime = data["anime"].replace(":",'-')
        loc =download_image(f'{data["character"]} from {anime}  image transparent background')
        data["charBgImg"]=loc
        print()
        print(data["character"])
        print()
        txtClip = TextClip(data["character"],
                                color='white',
                                font="Forte",
                                # kerning = 5,
                                fontsize=70,
                                size=(600,150),
                                # print_cmd=True,
                                transparent=True
                                )

        txtClip.save_frame(data["location"][1])
        datum.append(data)
    i=0
    print(datum)
    return datum 

