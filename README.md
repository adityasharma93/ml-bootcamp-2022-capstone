INTRODUCTION

This is an implementation of ByteTrack, a Multi Object Tracking algorithm that will uniquely detect the different people in a given image/video. This code builds an end to end application and will allow the user to give an input path to the videos and will get back a path to the output videos.

PREREQUISITES

1. The user must have a setup that can use CUDA (This requires an Nvidia GPU)
2. Docker is installed on the setup
3. We have Python installed with a version >= 3.7

SETUP

1. Download the code from the github repository
2. Download the trained models from the Google Drive link(https://drive.google.com/drive/folders/1-ypFOl9yeR20DJOljX6TnNYsoLZrHU5m?usp=share_link) and put it in a folder called pretrained
3. Put all the videos you want to be annotated into the datasets folder in the directory


HOW TO RUN

1. Run the shell_run.sh bash script to spin up a Docker with the application running on it
2. Open a web browser. If you are running this on your local machine, navigate to http://127.0.0.1:5000/ to see the application has started up. If you are running it on a remote machine, navigate to http://public IP of machine:5000/
3. Enter the path of the video in the datasets folder relative to the main directory, and you will see the annotated video path relative to the main directory

ACKNOWLEDGEMENTS

This work is based off of the ByteTrack implementation of Yufi Zhang, author of the paper ByteTrack: Multi-Object Tracking by Associating Every Detection Box.
