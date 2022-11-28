from moviepy.editor import *

bg = ImageClip("assets/Image_10.jpg").set_duration("30")
bg.write_videofile("assets/bgVid2.mp4",fps=30)

# bgVid = VideoFileClip("bgVid.mp4")
# bgVid =bgVid.subclip(0,30)
# bg_audio = AudioFileClip("bgm.mpeg").subclip(0,30)
# finalclip = bgVid.set_audio(bg_audio)
# finalclip.write_videofile("finalBgClip.mp4", fps=30)
