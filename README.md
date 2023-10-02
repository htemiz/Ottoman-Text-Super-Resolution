Repository for supporting files and outcomes for my paper entitled ___"Enhancing the Resolution of Historical Ottoman Texts Using Deep Learning-Based SuperResolution Techniques"___  published in the journal ___Traitement du Signal ( ISSN: 0765-0019 (print);  1958-5608 (online) )___


Please cite the paper as follows:


*Temiz, H. (2023). Enhancing the resolution of historical Ottoman texts using deep learning-based super-resolution techniques. Traitement du Signal, Vol. 40, No. 3, pp. 1075-1082* 
[https://doi.org/10.18280/ts.400323](https://doi.org/10.18280/ts.400323)



&nbsp;

## Overview
The following deep learning algorithms are exploited to obtain super-resolved 
images of Ottoman texts:

* DECUSR
* SRCNN
* VDSR
* RED-Net 
 
The pre-trained weights of the algorithms are stored in the **weights** folder.
The implementations of the algorithms can be found in the **models** folder.

The entire study was conducted with
[DeepSR](https://www.sciencedirect.com/science/article/pii/S2352711022001790) framework that
provides an integrated development environment for image super-resolution studies.
It is an open source software. PLease visit the [Github page](https://github.com/htemiz/DeepSR) for the source code
and [PyPI](https://pypi.org/project/DeepSR/) repository to download. To install the program:

`pip install DeepSR`

## How To Run
Each model files is of DeepSR-fashion file. They can be re-trained by issuing similar command as below:
(e.g., re-train DECUSR for 2x scale with pre-trained weights)
`python -m DeepSR.DeepSR --modelfile models/DECUSR.py --train --scale 2 
--weightpath weights/DECUSR_2x.h5 `

To test the algorithms, remove `--train` command parameter and include

`--testpath <path to your test files>` 

PLease use the appropriate weights for a particular scale. 

Much more explanations and samples on how to use **DeepSR** can be found its [Github page](https://github.com/htemiz/DeepSR). 

## Dataset
The dataset consists of 966 text images with of very large dimensions
(several thousand pixels in both width and height). It is not served in this page as this paltform is not
dedicated for such purposes. However any requests for the data are welcommed. Please contact me via
[htemiz@artvin.edu.tr](mailto:htemiz@artvin.edu.tr)  

<table style="border-style:hidden;">
 <caption align='center'>Two example images of historical Ottoman texts</caption>
 <tr><td width=350 > <img src="./images/image009.jpg"> </td>
  <td width=350 > <img src="./images/image010.jpg"> </td>
 </tr>
</table>


&nbsp;

## Training

&nbsp;


<table style="border:0 solid white; text-align:center;">
 <caption><b>Training Performances of the Algorithms</b></caption>
 <tr>
    <td><img src="images/training_performances_2x.png"> </td>
    <td><img src="images/training_performances_3x.png"> </td>
    <td><img src="images/training_performances_4x.png"> </td>
 </tr>
  <tr>
    <td><span>2x-Scale</span></td>
    <td><span>3x-Scale</span></td>
    <td><span>3x-Scale</span></td>
 </tr>
</table>


&nbsp;



## Results


&nbsp;


<table style="border:0px solid white; text-align:center;">
 <caption><b>Sample Outputs From A Text Image</b></caption>
 <tr>
  <td></td> <td></td> <td>DECUSR</td> <td>SRCNN</td> <td>VDSR</td> <td>RED-Net</td>
 </tr>
 <tr>
    <td style="width:150px;" rowspan=3><img src="images/img_01_ground_truth.png" alt="Reference image">
        </br><span>Reference image</span></td>
    <td style="width:20px;">2x</td>
    <td><img src="images/decusr_img_01_2x.png"> </td>
    <td><img src="images/srcnn_img_01_2x.png"> </td>
    <td><img src="images/vdsr_img_01_2x.png"> </td>
    <td><img src="images/rednet_img_01_2x.png"> </td>
 </tr>
  <tr>
    <td><img >3x </td>
    <td><img src="images/decusr_img_01_3x.png"> </td>
    <td><img src="images/srcnn_img_01_3x.png"> </td>
    <td><img src="images/vdsr_img_01_3x.png"> </td>
    <td><img src="images/rednet_img_01_3x.png"> </td>
 </tr>
  <tr>
    <td>4x </td>
    <td><img src="images/decusr_img_01_4x.png"> </td>
    <td><img src="images/srcnn_img_01_4x.png"> </td>
    <td><img src="images/vdsr_img_01_4x.png"> </td>
    <td><img src="images/rednet_img_01_4x.png"> </td>
 </tr>
 
</table>


&nbsp;



<table style="border:0px solid white; text-align:center;">
 <caption><b>Sample Outputs From Another Text Image</b></caption>
 <tr>
  <td></td> <td></td> <td>DECUSR</td> <td>SRCNN</td> <td>VDSR</td> <td>RED-Net</td>
 </tr>
 <tr>
    <td style="width:150px;" rowspan=3><img src="images/img_02_ground_truth.png" alt="Reference image">
        </br><span>Reference image</span></td>
    <td style="width:20px;">2x</td>
    <td><img src="images/decusr_img_02_2x.png"> </td>
    <td><img src="images/srcnn_img_02_2x.png"> </td>
    <td><img src="images/vdsr_img_02_2x.png"> </td>
    <td><img src="images/rednet_img_02_2x.png"> </td>
 </tr>
  <tr>
    <td><img >3x </td>
    <td><img src="images/decusr_img_02_3x.png"> </td>
    <td><img src="images/srcnn_img_02_3x.png"> </td>
    <td><img src="images/vdsr_img_02_3x.png"> </td>
    <td><img src="images/rednet_img_02_3x.png"> </td>
 </tr>
  <tr>
    <td>4x </td>
    <td><img src="images/decusr_img_02_4x.png"> </td>
    <td><img src="images/srcnn_img_02_4x.png"> </td>
    <td><img src="images/vdsr_img_02_4x.png"> </td>
    <td><img src="images/rednet_img_02_4x.png"> </td>
 </tr>

</table>



<!--

<style>
.divTable
{
display: table;
width:auto;
background-color:#eee;
border:1px solid #666666;
border-spacing:1px;
}
.divRow
{
width:auto;
display:table-row;
}
.divCell
{
width:150px;
float:left;
display:table-column;
background-color: rgb(212, 209, 209);
}
</style>


<div class="divTable">
<div class="headerRow">
    <div class="divCell">&nbsp;</div>
    <div class="divCell">DECUSR</div>
    <div class="divCell">SRCNN</div>
    <div class="divCell">VDSR</div>
    <div class="divCell">REDNET</div>

</div>
<div class="divRow">
    <div class="divCell">&nbsp;</div>
    <div class="divCell"><img src="images/decusr_img_02_2x.png"></div>
    <div class="divCell"><img src="images/srcnn_img_02_2x.png"></div>
    <div class="divCell"><img src="images/vdsr_img_02_2x.png"></div>
    <div class="divCell"><img src="images/rednet_img_02_2x.png"></div>
</div>
<div class="divRow">
    <div class="divCell"><img src="images/img_02_ground_truth.png" alt="Reference image">
        </br><span>Reference image</span></div>
    <div class="divCell"><img src="images/decusr_img_02_3x.png"></div>
    <div class="divCell"><img src="images/srcnn_img_02_3x.png"></div>
    <div class="divCell"><img src="images/vdsr_img_02_3x.png"></div>
    <div class="divCell"><img src="images/rednet_img_02_3x.png"></div>
</div>
<div class="divRow">
    <div class="divCell">&nbsp;</div>
    <div class="divCell"><img src="images/decusr_img_02_4x.png"></div>
    <div class="divCell"><img src="images/srcnn_img_02_4x.png"></div>
    <div class="divCell"><img src="images/vdsr_img_02_4x.png"></div>
    <div class="divCell"><img src="images/rednet_img_02_4x.png"></div>
</div>
</div>
-->