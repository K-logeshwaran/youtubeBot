import os 
# try:
#     os.system("del /f /s /q character 1>nul")
#     os.system("rmdir /s /q character")
# except :
#     print("Some thing went wrong on")
try:
    os.system("""
        py upload_video.py --file="finalOutputVid.mp4"
                       --title="Anime Quotes That hit different"
                       --description="Had fun surfing in Santa Cruz"
                       --keywords="surfing,Santa Cruz"
                       --category="22"
                       --privacyStatus="private"
    """)
except   Exception as err :
    print("Some thing went wrong on")
    print(err)