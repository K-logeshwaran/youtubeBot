from bing_image_downloader import downloader
import os 

def download_image(query):
    downloader.download(query, limit=1,  output_dir='character', 
    adult_filter_off=True, force_replace=False, timeout=60)
    location = f"{os.getcwd()}/character/{query}"
    cr_loc = location.replace("\\","/")
    lst =os.listdir(cr_loc)
    ext_pth = cr_loc+"/"+lst[0]
    return ext_pth