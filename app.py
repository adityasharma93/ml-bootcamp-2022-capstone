# importing Flask and other modules
from flask import Flask, request, render_template
import subprocess
import torch
import os
import glob
# Flask constructor
app = Flask(__name__)  
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       # getting input in HTML form
       video_name = request.form.get("fname")
       command = ["python3", "tools/demo_track.py", "video", "--path", video_name, "-f", "exps/example/mot/yolox_x_mix_det.py", "-c", "pretrained/bytetrack_x_mot17.pth.tar", "--fp16", "--fuse", "--save_result"]
       p = subprocess.run(command)
       videos_output = "./YOLOX_outputs/yolox_x_mix_det/track_vis/"
       subfolders = [ f.path for f in os.scandir(videos_output) if f.is_dir() ]
       latest_folder = max(subfolders, key=os.path.getctime)
       final_output = latest_folder
       return "Your video is in folder "+final_output
    return render_template("form.html")
if __name__=='__main__':
    os.environ['CUDA_VISIBLE_DEVICES'] = '0'
    print(torch.cuda.is_available()) # true
    app.run(host="0.0.0.0")
