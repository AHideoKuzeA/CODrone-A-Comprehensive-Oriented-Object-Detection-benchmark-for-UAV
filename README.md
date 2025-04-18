<p align="center">
<!--   <h1 align="center"><img height="100" src="https://github.com/imlixinyang/director3d-page/raw/master/assets/icon.ico"></h1> -->
  <h1 align="center"> <b>GOI</b>: CODrone: A Comprehensive Oriented Object Detection benchmark for UAV</h1>
  <p align="center">
        <a href="https://arxiv.org/abs/2405.17596"><img src='https://img.shields.io/badge/arXiv-GOI-red?logo=arxiv' alt='Paper PDF'></a>
        <a href='https://drive.google.com/file/d/1JunEiWyPNwGprdqXh-D2dTQPFMaRisDz/view?usp=sharing'><img src='https://img.shields.io/badge/Dataset-MipNeRF360 OV-yellow?logo=databricks' alt='MipNeRF360-OV'></a>
  </p>
    
<!-- <img src='assets/pipeline.gif'> -->
**😊 TL;DR**

GOI can locate 3D gaussians of interests as directed by open-vocabulary prompts.

**⭐ Key components of GOI**:


- A Trainable Feature Clustering Codebook effciently condense noisy high-dimensional semantic features into compact, low-dimensional vectores, ensuring well-defined segmentation boundaries.
- Finetuning Semantic-space Hyperplane, initiallized by text query embedding, to better locate target area.
- An open-vocabulary dataset is proposed, named MipNeRF360-OV.





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
