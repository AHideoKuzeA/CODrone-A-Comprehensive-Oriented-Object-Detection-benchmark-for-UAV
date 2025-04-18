<p align="center">
<!--   <h1 align="center"><img height="100" src="https://github.com/imlixinyang/director3d-page/raw/master/assets/icon.ico"></h1> -->
  <h1 align="center"> <b>GOI</b>: CODrone: A Comprehensive Oriented Object Detection benchmark for UAV</h1>
  <p align="center">
        <a href="https://arxiv.org/abs/2405.17596"><img src='https://img.shields.io/badge/arXiv-GOI-red?logo=arxiv' alt='Paper PDF'></a>
        <a href='https://drive.google.com/file/d/1JunEiWyPNwGprdqXh-D2dTQPFMaRisDz/view?usp=sharing'><img src='https://img.shields.io/badge/Dataset-MipNeRF360 OV-yellow?logo=databricks' alt='MipNeRF360-OV'></a>
  </p>
    
<!-- <img src='assets/pipeline.gif'> -->
**😊 TL;DR**

CODrone is a comprehensive oriented object detection dataset for UAVs that accurately reflects real-world conditions. 

**⭐ Key contributions of CODrone**:


- We proposed a large-scale, high-resolution UAV-oriented object detection dataset, CODrone, which consists of over ten thousand UAV-captured images with precise oriented bounding box annotations.To the best of our knowledge,  CODrone is the first UAV object detection dataset featuring oriented annotations across a wide range of object categories.
- The proposed CODrone dataset considers multiple influential factors, including image acquisition altitude, camera perspective, lighting conditions, and geographic location. These considerations enhance the dataset’s ability to support robust model training and realistic performance evaluation for UAV-based oriented object detection.
- Based on the proposed dataset, we establish a UAV-oriented object detection benchmark and conduct training and evaluation using X representative state-of-the-art methods. 
We identify existing limitations and challenges in the field, which can support future advancements in both algorithm development and practical deployment.

## Characteristics
<div align="center">
  
|     Dataset    | Resolution | Categories | Altitude Gap | Camera Angles | Images | Objects | OBB |
|:--------------:|:----------:|:----------:|:------------:|:-------------:|:------:|:-------:|:---:|
|  VisDrone2019  |  2000×1500 |     10     |       *      |       *       |  10.2k |   54.2k |     |
|      UAVDT     |   1080×540 |      3     |      60m     |       *       |  80.0k |  841.5k |     |
|     AU-AIR     |  1920×1080 |      8     |      25m     |       45      |   3.2k |  132.0k |     |
|      CARPK     |   1280×720 |      1     |       *      |       *       |   1.4k |   89.7k |     |
|     HazyDet    |   1333×800 |      3     |       *      |       *       |  11.6k |  383.0k |  　 |
|  DroneVehicle  |    840×712 |      5     |      40m     |       30      |  56.8k |  953.0k |  ✅  |
|     UAV-ROD    |  1920×1080 |      1     |      50m     |       *       |   1.5k |   30.0k |  ✅  |
| **CODrone (ours)** |  **3840×2160** |     **12**     |      **70m**     |       **60**      |  10.0k |  596.7k |  ✅  |

</div>
We present a comparison between CODrone and other commonly used UAV-based object detection datasets.
It is important to note that datasets designed for more specialized tasks, such as multiview object detection, video-based dynamic object tracking, and other fine-grained UAV applications, are not included in the table, as their objectives and data structures differ significantly from standard image-based object detection tasks.

CODrone significantly expands several key dimensions, including image resolution, object category diversity, and variation in flight altitude and camera angle.
For resolution, CODrone employs a 3840 × 2160 high-resolution onboard camera, aligning with the capabilities of modern UAV hardware.
In terms of object classes, unlike most existing UAV OOD datasets that focus primarily on vehicles, CODrone includes a more diverse range of categories, thereby increasing the difficulty and realism of the detection task.
Furthermore, we explicitly annotate both altitude and camera angle for each image, enabling research into UAV pose-aware perception and related tasks. 
Although we collected a large amount of video data, we manually selected and annotated only 10,004 high-quality images for the OOD task. 
The remaining video resources will be labeled and released in future work to support related tasks such as UAV-based video object tracking and multi-frame detection.

### High resolution brings more high-quality information
<div align="center">

![Description](img/HR.jpg)

</div>

CODrone employs a **3840 × 2160** high-resolution onboard camera, aligning with the capabilities of modern UAV hardware.

### High resolution brings more high-quality information
<div align="center">

![Description](img/HR.jpg)

</div>

CODrone employs a **3840 × 2160** high-resolution onboard camera, aligning with the capabilities of modern UAV hardware.

## Citation

```
@article{goi2024,
    title={GOI: Find 3D Gaussians of Interest with an Optimizable Open-vocabulary Semantic-space Hyperplane},
    author={Qu, Yansong and Dai, Shaohui and Li, Xinyang and Lin, Jianghang and Cao, Liujuan and Zhang, Shengchuan and Ji, Rongrong},
    journal={arXiv preprint arXiv:2405.17596},
    year={2024}
}
```


## License

Licensed under the CC BY-NC-SA 4.0 (Attribution-NonCommercial-ShareAlike 4.0 International)


The code is released for academic research use only. 

If you have any questions, please contact me via [yekai@stu.xmu.edu.cn]. 
