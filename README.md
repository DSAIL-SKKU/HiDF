# 💡 HiDF: A Human-Indistinguishable Deepfake Dataset

<p align="center">
  <img src="thumbnail.png" alt="Sample deepfake images of HiDF" style="width:90%;">
  <br>
  <b>[Deepfake image samples of HiDF]</b>
</p>

<br>

$HiDF$ is a high-quality, **human-indistinguishable deepfake dataset** comprising 30K images and 4K videos, curated to include diverse subjects and undergo rigorous quality checks. It addresses the limitations of existing datasets by providing more realistic and undetectable deepfakes. This makes HiDF an invaluable benchmark for advancing deepfake detection research, with data and code publicly available for future studies. You can find HiDF's deepfake images and videos in the **_samples_** folder. It includes 100 deepfake images and 10 deepfake videos. For access to the entire dataset, please refer to [Request for $HiDF$](#-request-for-hidf-) below.

<br>


## 💡 Quantitative comparison of HiDF and existing deepfake datasets

|   Dataset   |    # Real    |    # Fake     |    # Total    |       # Subject       |            DType             |   Tool  |  Quality  |
| :---------: | :----------: | :-----------: | :-----------: | :-------------------: | :--------------------------: | :-----: | :-------: |
|     FF++    |    1,000     |     4,000     |     5,000     |           N/A         |   Image, Video (w/o audio)   |    X    |    N/A    |
|     DFDC    |    23,654    |    104,500    |    128,154    |           960         |        Video (w/ audio)      |    X    |    N/A    |
|     KoDF    |    62,166    |    175,776    |    237,942    |           403         |        Video (w/ audio)      |    X    |     Q     |
| FakeAVCeleb |     500      |    19,500     |     20,000    |           500         |        Video (w/ audio)      |    X    |    N/A    |
|     DFGC    |    2,019     |     3,270     |     5,289     |           40          |        Video (w/ audio)      |    O    |    N/A    |
|   **HiDF**  |  **34,491**  |  **34,491**   |   **68,982**  |  **6,127 + &alpha;**  |  **Image, Video (w/ audio)** |  **O**  |  **QQ**   |

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

### 1. Environment Setting

```
git clone https://github.com/DSAIL-SKKU/HiDF.git
cd HiDF
pip install -r requirements.txt
```


<br>

-----
## 💡 Request for $HiDF$

To access the HiDF dataset, please complete the form below. We collect minimal information to verify the identity of dataset users to prevent misuse of HiDF; this information will not be used for any other purposes. The HiDF dataset is available under the [Creative Commons Attribution-NonCommercial 4.0 International Public License](https://creativecommons.org/licenses/by-nc/4.0/). Any violation of this license agreement may result in legal action. To gain access to HiDF, complete the form and email it to codnjs3@g.skku.edu, preferably using your institutional or company email address. By submitting the form, the user agrees to the terms of the CC BY-NC 4.0 license. If you are still waiting to receive feedback within 7 days, please contact jsyoon0503@g.sku.edu.

* Name : 
* Lab / Department / Affiliation :
* Principal Investigator/Advisor's Name :
* Principal Investigator/Advisor's Email Address :
* Short description of research purpose or project description :

<br>


## 💡 Maintenance
This repository is maintained by [Chaewon Kang](https://sites.google.com/view/chaewon-kang/) and Seoyoon Jeong. Any feedback, extensions & suggestions are welcome! Please send an email to codnjs3@g.skku.edu.

<br>

## 💡 License
The HiDF dataset is available under the Creative Commons Attribution-NonCommercial 4.0 International Public License: [https://creativecommons.org/licenses/by-nc/4.0/](https://creativecommons.org/licenses/by-nc/4.0/). The code is released under the MIT license.

