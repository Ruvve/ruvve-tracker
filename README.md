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
<img alt="Service Architecture" width="100%" src="https://user-images.githubusercontent.com/43839834/135746113-b2428f0c-29fd-4e07-84cf-478fe017a845.png
" />

<p align="center">
<a href="https://github.com/Ruvve/ruvve-server"><img alt="Ruvve Server" title="Ruvve Server" src="https://img.shields.io/badge/-Ruvve Server-grey?style=for-the-badge&logo=github&logoColor=white"/></a>
<a href="https://github.com/Ruvve/ruvve-server"><img alt="Ruvve Server" title="Ruvve Server" src="https://img.shields.io/badge/-Ruvve iOS-grey?style=for-the-badge&logo=github&logoColor=white"/></a>
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

### References  

   Huge shoutout goes to hunglc007 and nwojke for creating the backbones of this repository:
  * [tensorflow-yolov4-tflite](https://github.com/hunglc007/tensorflow-yolov4-tflite)
  * [Deep SORT Repository](https://github.com/nwojke/deep_sort)
