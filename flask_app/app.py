# importing Flask and other modules
from flask import Flask, request, render_template
import subprocess
import os
# Flask constructor
app = Flask(__name__)  
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       first_name = request.form.get("fname")
       #print(os.getcwd())
       #command = "python3 /home/paperspace/ByteTrack/tools/demo_track.py video --path {} -f exps/example/mot/yolox_x_mix_det.py -c pretrained/bytetrack_x_mot17.pth.tar --fp16 --fuse --save_result".format(first_name)
       #command = ["python3","/home/paperspace/ByteTrack/tools/demo_track.py video --path {} -f exps/example/mot/yolox_x_mix_det.py -c pretrained/bytetrack_x_mot17.pth.tar --fp16 --fuse --save_result".format(first_name)]
       command = ["python3", "../tools/demo_track.py", "video", "--path", first_name, "-f", "exps/example/mot/yolox_x_mix_det.py", "-c", "pretrained/bytetrack_x_mot17.pth.tar", "--fp16", "--fuse", "--save_result"]
       p = subprocess.run(command,stdout=subprocess.PIPE).communicate()[0]
       print(p)
       return "Your name is "+first_name
    return render_template("form.html")
if __name__=='__main__':
   app.run(host="0.0.0.0")
