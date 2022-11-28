from moviepy.editor import *
from createQuote_gen_img import createAssets
import random
import os 

AUDIOCLIPS = ["C:/Users/Logeshwaran K/OneDrive/Desktop/youtubeBot/finalDraft/assets/bgm.mpeg","C:/Users/Logeshwaran K/OneDrive/Desktop/youtubeBot/finalDraft/assets/bgm2.mpeg"]
BGVID =["C:/Users/Logeshwaran K/OneDrive/Desktop/youtubeBot/finalDraft/assets/bgVid.mp4","C:/Users/Logeshwaran K/OneDrive/Desktop/youtubeBot/finalDraft/assets/bgVid2.mp4"]
INTROCLIPS =["C:/Users/Logeshwaran K/OneDrive/Desktop/youtubeBot/finalDraft/assets/vid1.mp4","C:/Users/Logeshwaran K/OneDrive/Desktop/youtubeBot/finalDraft/assets/intro.mp4"]

audio_loc = random.choice(AUDIOCLIPS)
bgv_loc = random.choice(BGVID)
intro_loc =random.choice(INTROCLIPS)


def getBgLoc(D):
    locs =[]
    for d in D:
        locs.append(d["charBgImg"])
    return locs


data = createAssets()
locations = {"quote":["quote1.png","quote2.png","quote3.png",],"charName":["charName1.png","charName2.png","charName3.png",],"bgImg":getBgLoc(data)}

for i in range(3):
    
    #previous
    # major_clip = VideoFileClip("C:/Users/Logeshwaran K/OneDrive/Desktop/youtubeBot/finalDraft/assets/bgVid.mp4").subclip(0,6)

    major_clip = VideoFileClip(bgv_loc).subclip(0,6)
    quote = ImageClip(f"{locations['quote'][i]}").set_duration(6)
    char = ImageClip(f"{locations['charName'][i]}").set_duration(6)
    loc =f"{locations['bgImg'][i]}"
    charImg = ImageClip(loc).set_duration(6).resize((620,500))
    video = CompositeVideoClip([major_clip, quote.set_position((0.1,0.03),relative=True),charImg.set_position((0.1,0.45), relative=True),char.set_position((0.1,0.85),relative=True)]) 
    video.write_videofile(f"finalOut{i}.mp4", fps=30)


#previous
# intro = VideoFileClip("C:/Users/Logeshwaran K/OneDrive/Desktop/youtubeBot/finalDraft/assets/vid1.mp4").subclip(0,2).resize((740,1000))

if intro_loc == INTROCLIPS[0]:
    intro = VideoFileClip(intro_loc).subclip(0,2).resize((740,1000))
    major_clip = major_clip.subclip(0,2)
else:    
    intro = VideoFileClip(intro_loc).subclip(0,6).resize((900,900))
    major_clip = major_clip.subclip(0,6)

video = CompositeVideoClip([major_clip, intro.set_position((0,0.05), relative=True)]) 
clp1 = VideoFileClip("finalOut0.mp4")
clp2 = VideoFileClip("finalOut1.mp4")
clp3 = VideoFileClip("finalOut2.mp4")

merged_clip = concatenate_videoclips([video,clp1,clp2,clp3])
# merged_clip.write_videofile("mergedClip.mp4",fps=30)
bg_audio = AudioFileClip("C:/Users/Logeshwaran K/OneDrive/Desktop/youtubeBot/finalDraft/assets/bgm.mpeg").subclip(0,24)
finalOutputVid = merged_clip.set_audio(bg_audio)
finalOutputVid.write_videofile("./final_cut/finalOutputVid.mp4",fps=30)

try:
    os.system("del /f /s /q character 1>nul")
    os.system("rmdir /s /q character")
    for i in range(3):
        os.system(f"del /f finalOut{i}.mp4")
        os.system(f"del /f quote{i+1}.png")
        os.system(f"del /f charName{i+1}.png")
        
    print("Delection Success")
except :
    print("Some thing went wrong on")

# try:
#     os.system(f'py upload_video.py --file="finalOutputVid.mp4" --title="Anime Quotes That hit different" --description="Anime Quotes That hit different Motivation" --keywords="motivation,anime quotes,anime anime shorts,quotes,naruto,dbs,dbz quotes,one piece " --category="22"')
# except   Exception as err :
#     print("Some thing went wrong on")
#     print(err)