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

## Citation
|     Dataset    | Resolution |   |      | Categories | Altitude Gap | Camera Angles | Images |   | Objects |   | OBB |
|:--------------:|:----------:|:-:|:----:|:----------:|:------------:|:-------------:|:------:|:-:|:-------:|:-:|:---:|
|  VisDrone2019  |       2000 | × | 1500 |     10     |       *      |       *       |   10.2 | k |    54.2 | k |     |
|      UAVDT     |       1080 | × | 540  |      3     |      60m     |       *       |   80.0 | k |   841.5 | k |     |
|     AU-AIR     |       1920 | × | 1080 |      8     |      25m     |       45      |    3.2 | k |   132.0 | k |     |
|      CARPK     |       1280 | × | 720  |      1     |       *      |       *       |    1.4 | k |    89.7 | k |     |
|     HazyDet    |       1333 | × | 800  |      3     |       *      |       *       |   11.6 | k |   383.0 | k |  　 |
|  DroneVehicle  |        840 | × | 712  |      5     |      40m     |       30      |   56.8 | k |   953.0 | k |  1  |
|     UAV-ROD    |       1920 | × | 1080 |      1     |      50m     |       *       |    1.5 | k |    30.0 | k |  1  |
| CODrone (ours) |       3840 | × | 2160 |     12     |      70m     |       60      |   10.0 | k |   596.7 | k |  1  |
![Description](img/HR.jpg)


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
