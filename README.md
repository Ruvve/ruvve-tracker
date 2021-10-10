# Ruvve Tracker

### yolov4-deepsort

Object tracking implemented with YOLOv4, DeepSort, and TensorFlow. YOLOv4 is a state of the art algorithm that uses deep convolutional neural networks to perform object detections. We can take the output of YOLOv4 feed these object detections into Deep SORT (Simple Online and Realtime Tracking with a Deep Association Metric) in order to create a highly accurate object tracker.

<br/>

<p align="center">
<img alt="python-v3.7.0" src="https://img.shields.io/badge/python-v3.7.0-3f72af" />
<img alt="opencv-4.1.1.26" src="https://img.shields.io/badge/opencv-4.1.1.26-green.svg" />
<img alt="Yolo-v4" src="https://img.shields.io/badge/Yolo-v4-aa96da" />

<br/>
<a href="https://github.com/theAIGuysCode/yolov4-deepsort">
<img alt="Origin Repository" src="https://img.shields.io/badge/Origin Repository-grey" />
</a>
<img alt="license" src="https://img.shields.io/github/license/mashape/apistatus.svg" />
</p>
<br/>

<p align="center">
<img alt="mockup" width="60%" src="https://user-images.githubusercontent.com/43839834/135746103-41e41f40-0fbf-415e-9a11-2a5c8ea34cab.png" />
</p>

<br/><br/>

#### Personal Mobility Navigation - Ruvve

 개인형 이동수단을 위한 전용 경로를 찾아 AR화면을 통한 길안내 서비스를 제공합니다. ML을 통한 사물인식 기술을 통해 주행 중 사고 요소를 사전 감지하고 사고를 미연에 방지할 수 있는 안전 서비스를 가지고 있습니다. 장애물 탐지 기능과 AR Navigation이라는 특징이 기존의 Navigation과의 차별점입니다.

<br/>

#### Why Ruvve? 
최근 뉴스 등에서 이슈가 되고 있는 전동 킥보드의 자전거 도로 주행 관련 법 개정에 이 지속적으로 이루어지고 있습니다. 이는 전동 킥보드를 규정에 벗어난 이용하고 있는 사용자들로 인해 많은 시민들의 안전에 위협을 주고 있고 있으며, 사용자 또한 다양한 안전사고에 노출되어 있는 것이 현실입니다. 이러한 사회적 문제해결에 AI와 IoT 기술을 통해 기여를 하고자 합니다.


<!-- <p align="center">
<img alt="mockup" width="80%" src="https://user-images.githubusercontent.com/43839834/135746381-1c6d9f45-3247-4df0-99ad-e21819087553.png" />
</p> -->

<br/><br/>

## Ruvve Architecture
<img alt="Service Architecture" width="100%" src="https://user-images.githubusercontent.com/43839834/135746113-b2428f0c-29fd-4e07-84cf-478fe017a845.png" />

<br/>

<p align="center">
<a href="https://github.com/Ruvve/ruvve-server"><img alt="Ruvve Server" title="Ruvve Server" src="https://img.shields.io/badge/-Ruvve Server-grey?style=for-the-badge&logo=github&logoColor=white"/></a>
<a href="https://github.com/Ruvve/ruvve-server"><img alt="Ruvve iOS" title="Ruvve iOS" src="https://img.shields.io/badge/-Ruvve iOS-grey?style=for-the-badge&logo=github&logoColor=white"/></a>
</p>


<br/><br/><br/><br/>

## Getting Started
To get started, install the proper dependencies either via Anaconda or Pip. I recommend Anaconda route for people using a GPU as it configures CUDA toolkit version for you.

### Conda (Recommended)

```bash
# Tensorflow CPU
conda env create -f conda-cpu.yml
conda activate yolov4-cpu

# Tensorflow GPU
conda env create -f conda-gpu.yml
conda activate yolov4-gpu
```

### Pip
(TensorFlow 2 packages require a pip version >19.0.)
```bash
# TensorFlow CPU
pip install -r requirements.txt

# TensorFlow GPU
pip install -r requirements-gpu.txt
```

<br/>

### Running the Tracker with YOLOv4
To implement the object tracking using YOLOv4, first we convert the .weights into the corresponding TensorFlow model which will be saved to a checkpoints folder. Then all we need to do is run the object_tracker.py script to run our object tracker with YOLOv4, DeepSort and TensorFlow.

```bash
# Convert darknet weights to tensorflow model
python save_model.py --model yolov4 

# Run yolov4 deep sort object tracker on video
python object_tracker.py --video ./data/video/test.mp4 --output ./outputs/demo.avi --model yolov4

# Run yolov4 deep sort object tracker on webcam (set video flag to 0)
python object_tracker.py --video 0 --output ./outputs/webcam.avi --model yolov4
```

<br/>

### Running the Tracker with YOLOv4-Tiny
The following commands will allow you to run yolov4-tiny model. Yolov4-tiny allows you to obtain a higher speed (FPS) for the tracker at a slight cost to accuracy. Make sure that you have downloaded the tiny weights file and added it to the 'data' folder in order for commands to work!
```
# save yolov4-tiny model
python save_model.py --weights ./data/yolov4-tiny.weights --output ./checkpoints/yolov4-tiny-416 --model yolov4 --tiny

# Run yolov4-tiny object tracker
python object_tracker.py --weights ./checkpoints/yolov4-tiny-416 --model yolov4 --video ./data/video/test.mp4 --output ./outputs/tiny.avi --tiny
```

<br/>

### Create Firebase Key File
Create a `firebase-key.json` file.

```json
{
  "API_KEY": "firebase-api-key",
  "TOKEN": "device-token"
}
```

<br/>

### Add Firebase Admin SDK File
Add a `firebase-adminsdk.json` file in the top folder.

<br/>

### Resulting

<p align="center" style="display: flex;align-items: center"> 
<img alt="result capture" width="45%" src="https://user-images.githubusercontent.com/43839834/136698482-e9e9e465-6f43-4449-8116-8d3fc277bb4c.png" />
<img alt="result capture" width="45%" src="https://user-images.githubusercontent.com/43839834/136698048-0cd18a7c-0245-4fc5-bc2c-c70d7723692a.jpg" />
</p>
<p align="center" style="display: flex;justify-content:center; align-items: center"> 
<img alt="result capture" width="20%" style="margin-right: 10px;" src="https://user-images.githubusercontent.com/43839834/136698106-66cb7b57-dc65-489c-9571-a33c98a1d7a5.PNG" />
<img alt="result capture" width="20%" src="https://user-images.githubusercontent.com/43839834/136698107-6fbe4e19-4b6e-424e-9586-b96b60a943ba.PNG" />
</p>


### References  

   Huge shoutout goes to hunglc007 and nwojke for creating the backbones of this repository:
  * [tensorflow-yolov4-tflite](https://github.com/hunglc007/tensorflow-yolov4-tflite)
  * [Deep SORT Repository](https://github.com/nwojke/deep_sort)
