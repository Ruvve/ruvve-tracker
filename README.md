# Ruvve Tracker

### yolov4-deepsort

Object tracking implemented with YOLOv4, DeepSort, and TensorFlow. YOLOv4 is a state of the art algorithm that uses deep convolutional neural networks to perform object detections. We can take the output of YOLOv4 feed these object detections into Deep SORT (Simple Online and Realtime Tracking with a Deep Association Metric) in order to create a highly accurate object tracker.

<br/>

<p align="center">
<img alt="python-v3.7.0" src="https://img.shields.io/badge/python-v3.7.0-3f72af" />
<img alt="opencv-4.1.1.26" src="https://img.shields.io/badge/opencv-4.1.1.26-green.svg" />
<img alt="Yolo-v4" src="https://img.shields.io/badge/Yolo-v4-aa96da" />

<br/>
<img alt="Origin Repository" src="https://img.shields.io/badge/Origin Repository-grey" />
<img alt="license" src="https://img.shields.io/github/license/mashape/apistatus.svg" />
</p>
<br/>

<p align="center">
<img alt="mockup" width="60%" src="https://user-images.githubusercontent.com/43839834/135746103-41e41f40-0fbf-415e-9a11-2a5c8ea34cab.png" />
</p>

<br/><br/>

## Ruvve Architecture
<img alt="Service Architecture" width="100%" src="https://user-images.githubusercontent.com/43839834/135746113-b2428f0c-29fd-4e07-84cf-478fe017a845.png
" />

<p align="center">
<a href="https://github.com/Ruvve/ruvve-server"><img alt="Ruvve Server" title="Ruvve Server" src="https://img.shields.io/badge/-Ruvve Server-grey?style=for-the-badge&logo=github&logoColor=white"/></a>
<a href="https://github.com/Ruvve/ruvve-server"><img alt="Ruvve Server" title="Ruvve Server" src="https://img.shields.io/badge/-Ruvve iOS-grey?style=for-the-badge&logo=github&logoColor=white"/></a>
</p>


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
