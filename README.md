# 💡 HiDF: A Human-Indistinguishable Deepfake Dataset

<p align="center">
  <img src="thumbnail.png" alt="Sample deepfake images of HiDF" style="width:90%;">
  <br>
  <b>[Deepfake image samples of HiDF]</b>
</p>

<br>

$HiDF$ is a high-quality, **human-indistinguishable deepfake dataset** comprising 30K images and 4K videos, curated to include diverse subjects and undergo rigorous quality checks. It addresses the limitations of existing datasets by providing more realistic and undetectable deepfakes. This makes HiDF an invaluable benchmark for advancing deepfake detection research, with data and code publicly available for future studies. You can find HiDF's deepfake images and videos in the **_samples_** folder. It includes 100 deepfake images and 10 deepfake videos. For access to the entire dataset, please refer to [Request for HiDF](https://github.com/DSAIL-SKKU/HiDF#-request-for-hidf) below.

<br>


## 💡 News

* **[05/16/2025] Our paper on the HiDF dataset has been accepted to KDD 2025 (Datasets & Benchmarks Track)!**
  - With this acceptance, the dataset is now officially available for research use.
  - Please refer to the [Request for HiDF](https://github.com/DSAIL-SKKU/HiDF#-request-for-hidf) section below for access instructions.
  - Presentation video: [https://youtu.be/PLVaHbYCnNg?si=Ztpwpcg1IKLkI310](https://youtu.be/PLVaHbYCnNg?si=Ztpwpcg1IKLkI310)

<br>


## 💡 Quantitative comparison of HiDF and existing deepfake datasets

|   Dataset   |    # Real    |    # Fake     |    # Total    |       # Subject       |            DType             |   Tool  |  Quality  |
| :---------: | :----------: | :-----------: | :-----------: | :-------------------: | :--------------------------: | :-----: | :-------: |
|     FF++    |    1,000     |     4,000     |     5,000     |           N/A         |   Image, Video (w/o audio)   |    X    |    N/A    |
|     DFDC    |    23,654    |    104,500    |    128,154    |           960         |        Video (w/ audio)      |    X    |    N/A    |
|     KoDF    |    62,166    |    175,776    |    237,942    |           403         |        Video (w/ audio)      |    X    |     Q     |
| FakeAVCeleb |     500      |    19,500     |     20,000    |           500         |        Video (w/ audio)      |    X    |    N/A    |
|     DFGC    |    2,019     |     3,270     |     5,289     |           40          |        Video (w/ audio)      |    O    |    N/A    |
|   **HiDF**  |  **35,611**  |  **35,611**   |   **71,222**  |  **6,127 + &alpha;**  |  **Image, Video (w/ audio)** |  **O**  |  **QQ**   |

Quantitative comparison of HiDF and existing deepfake datasets. Real, Fake, and Total for HiDF represent the combined count of images and videos. Tool indicates whether commercial tools were used for generating the deepfake data, and Quality denotes whether a quality assessment of the dataset was performed. Q: Quantitative (using evaluation metrics such as FID, PSNR, SSIM) only, QQ: Both Quantitative and Qualitative (including pilot studies such as human surveys), N/A: Not applicable.

<br>


## 💡 Data Description

HiDF provides high-quality deepfake images and videos, along with the corresponding real data. The detailed quantities are as follows.

- **Image**
  - \# of Real: **30,250**
  - \# of Fake: **30,250**
- **Video**
  - \# of Real: **4,241**
  - \# of Fake: **4,241**

<br>

When swapping the face of image A with that of image B, we refer to image A as the base image and the image to be swapped (i.e., image B) as the target image. 
The filenames of HiDF deepfake images follow the format **(base_image_id)_(target_image_id).jpg**. Similarly, the filenames of deepfake videos follow the format **(base_video_id)_(target_image_id).mp4**.

<br>

In our commitment to supporting comprehensive deepfake detection research, we provide detailed information on the race, gender, and age of the synthesized individuals in the generated deepfake images and videos. This comprehensive information is included in the **_HiDF_metadata.csv_** file, structured as follows. For detailed annotation procedures regarding race, gender, and age, please refer to the paper 'HiDF: A Human-Indistinguishable Deepfake Dataset.'

<br>

- **Configuration of HiDF_metadata.csv**

|   Image ID   |   Race    |  Gender  |   Age   |
| :----------: | :-------: | :------: | :-----: |
|    c01213    |   white   |  female  |  child  |
|    f00105    |   Asian   |   male   |  Adult  |
|      ...     |    ...    |    ...   |   ...   |

  - **Image ID**
    - This column refers to the unique ID of the image. Each ID consists of one letter and five digits. The letters 'c' and 'f' indicate the source dataset from which the image was extracted (i.e., CelebA-HQ and FFHQ, respectively).
  - **Race**
    - This column indicates the race of the individuals appearing in the image. Race is divided into five categories: White, Black, Asian, Latino, and Indian.
  - **Gender**
    - This column indicates the gender of the individuals appearing in the image.
  - **Age**
    - This column indicates the age group of the individuals appearing in the image, divided into three categories: child, middle-aged adult, and elderly.

<br>


## 💡 Evaluation

### 1. Installation

```
git clone https://github.com/DSAIL-SKKU/HiDF.git
cd HiDF/Code/AVAD
```
Install the requirements file:
```
pip install -r requirements.txt
```

### 2. Inference

Steps to run the python code directly:
```
python detect_implementation_code.py --input_dir /SampleData/HiDF/Fake --output_dir ./save
```
You can download checkpoint `sync_model.pth` from [here](https://drive.google.com/file/d/1BxaPiZmpiOJDsbbq8ZIDHJU7--RJE7Br/view) and place it in the folder where the code resides.

`input_dir` should contain the path to the directory of evaluation data, and `output_dir` should contain the path to the `save` folder created in the `./AVAD` directory.

In the end, there would be `{evaluation data}_{Real/Fake}_score.csv' file under output_dir generated to record scores for all the testing videos.

### 3. Performance evaluation

Finally, you can evaluate performance by running the following command:
```
python APnAUC.py
# Average Precision (AP): 0.xxxx
# Area Under the Curve (AUC): 0.xxxx
```
If there are multiple CSV files in the `save` folder, you need to specify which Real and Fake you want within the `APnAUC.py` script.

___
### Acknowledgments

Our code is borrowed from [AVAD](https://github.com/cfeng16/audio-visual-forensics). Thanks for their sharing codes and models.

<br>

## 💡 Request for $HiDF$

To access the HiDF dataset, please visit the following link.
* https://zenodo.org/records/16140829

The HiDF dataset is available under the [Creative Commons Attribution-NonCommercial 4.0 International Public License](https://creativecommons.org/licenses/by-nc/4.0/). Any violation of this license agreement may result in legal action. By downloading the HiDF, the user agrees to the terms of the CC BY-NC 4.0 license.

<br>


## 💡 Maintenance
This repository is maintained by [Chaewon Kang](https://sites.google.com/view/chaewon-kang/) and Seoyoon Jeong. Any feedback, extensions & suggestions are welcome! Please send an email to codnjs3@g.skku.edu.

<br>

## 💡 License
The HiDF dataset is available under the Creative Commons Attribution-NonCommercial 4.0 International Public License: [https://creativecommons.org/licenses/by-nc/4.0/](https://creativecommons.org/licenses/by-nc/4.0/). The code is released under the MIT license.

