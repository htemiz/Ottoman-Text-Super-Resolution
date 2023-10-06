
Repository for supporting files and outcomes for my paper entitled 
["Enhancing the Resolution of Historical Ottoman Texts Using Deep Learning-Based SuperResolution Techniques"](https://iieta.org/journals/ts/paper/10.18280/ts.400323) published in the journal
[Traitement du Signal ( ISSN: 0765-0019 (print);  1958-5608 (online) )](https://iieta.org/journals/ts/paper/10.18280/ts.400323)


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

<table >
 <caption><strong>The number of parameters and training times of the algorithms</strong></caption>
 <tbody><tr >
  <td rowspan="2"  >
  <p ><b><span>Models<o:p></o:p></span></b></p>
  </td>
  <td  rowspan="2" >
  <p ><b ><span >Parameters<o:p></o:p></span></b></p>
  </td>
  <td colspan="3">
  <p ><b ><span >Training Time (hours)<o:p></o:p></span></b></p>
  </td>
 </tr>
 <tr >
  
  <td >
  <p ><span >Scale-2<o:p></o:p></span></p>
  </td>
  <td >
  <p ><span >Scale-3<o:p></o:p></span></p>
  </td>
  <td >
  <p ><span>Scale-4<o:p></o:p></span></p>
  </td>
 </tr>
 <tr >
  <td>
  <p ><span >DECUSR<o:p></o:p></span></p>
  </td>
  <td >
  <p><span >40,995<o:p></o:p></span></p>
  </td>
  <td >
  <p ><span >27.839<o:p></o:p></span></p>
  </td>
  <td >
  <p ><span >22.790<o:p></o:p></span></p>
  </td>
  <td>
  <p ><span >21.822<o:p></o:p></span></p>
  </td>
 </tr>
 <tr >
  <td >
  <p ><span >SRCNN<o:p></o:p></span></p>
  </td>
  <td >
  <p ><span >20,099<o:p></o:p></span></p>
  </td>
  <td >
  <p ><span l>40.234<o:p></o:p></span></p>
  </td>
  <td >
  <p ><span l>42.607<o:p></o:p></span></p>
  </td>
  <td >
  <p ><span >41.801 <o:p></o:p></span></p>
  </td>
 </tr>
 <tr >
  <td >
  <p ><span >VDSR<o:p></o:p></span></p>
  </td>
  <td >
  <p ><span >668,227<o:p></o:p></span></p>
  </td>
  <td >
  <p ><span >26.303<o:p></o:p></span></p>
  </td>
  <td >
  <p ><span >40.605<o:p></o:p></span></p>
  </td>
  <td >
  <p ><span >40.147<o:p></o:p></span></p>
  </td>
 </tr>
 <tr >
  <td >
  <p ><span >RED-Net<o:p></o:p></span></p>
  </td>
  <td >
  <p ><span >1,037,507<o:p></o:p></span></p>
  </td>
  <td >
  <p ><span >90.047<o:p></o:p></span></p>
  </td>
  <td >
  <p ><span >89.099<o:p></o:p></span></p>
  </td>
  <td >
  <p ><span >91.0284<o:p></o:p></span></p>
  </td>
 </tr>
</tbody></table>
 

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
    <td><span>4x-Scale</span></td>
 </tr>
</table>


&nbsp;
 


## Results

<table class="MsoNormalTable" border="0" cellspacing="0" cellpadding="0" width="320" style="width:239.65pt;border-collapse:collapse;mso-yfti-tbllook:1184;
 mso-padding-alt:0cm 3.5pt 0cm 3.5pt;mso-prop-change:msi 20230228T1428;
 width:228.3pt !msorm;border-collapse:collapse !msorm;mso-yfti-tbllook:1184 !msorm;
 mso-padding-alt:0cm 3.5pt 0cm 3.5pt !msorm">
 <caption><strong>Performances of the algorithms</strong></caption>
 <tbody><tr style="mso-yfti-irow:0;mso-yfti-firstrow:yes;height:14.15pt;mso-prop-change:
  msi 20230228T1428">
  <td width="36" style="width:27.0pt;width:1.0cm !msorm;border-top:solid windowtext 1.0pt;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:none;
  mso-border-top-alt:solid windowtext .5pt;mso-border-bottom-alt:solid windowtext .5pt;
  padding:0cm 3.5pt 0cm 3.5pt;border-top:solid windowtext 1.0pt !msorm;
  border-left:none !msorm;border-bottom:solid windowtext 1.0pt !msorm;
  border-right:none !msorm;mso-border-top-alt:solid windowtext .5pt !msorm;
  mso-border-bottom-alt:solid windowtext .5pt !msorm;padding:0cm 3.5pt 0cm 3.5pt !msorm;
  height:14.15pt">
  <p class="MsoNormal" style="margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal"><b style="mso-bidi-font-weight:normal"><i style="mso-bidi-font-style:
  normal"><span lang="EN-US" style="font-size:9.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-ansi-language:EN-US">Scale<o:p></o:p></span></i></b></p>
  </td>
  <td width="57" nowrap="" style="width:42.55pt;width:39.7pt !msorm;border-top:solid windowtext 1.0pt;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:none;
  mso-border-top-alt:solid windowtext .5pt;mso-border-bottom-alt:solid windowtext .5pt;
  padding:0cm 3.5pt 0cm 3.5pt;border-top:solid windowtext 1.0pt !msorm;
  border-left:none !msorm;border-bottom:solid windowtext 1.0pt !msorm;
  border-right:none !msorm;mso-border-top-alt:solid windowtext .5pt !msorm;
  mso-border-bottom-alt:solid windowtext .5pt !msorm;padding:0cm 3.5pt 0cm 3.5pt !msorm;
  height:14.15pt">
  <p class="MsoNormal" style="margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal"><b style="mso-bidi-font-weight:normal"><i style="mso-bidi-font-style:
  normal"><span lang="EN-US" style="font-size:9.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-ansi-language:EN-US">Model<o:p></o:p></span></i></b></p>
  </td>
  <td width="68" nowrap="" style="width:51.0pt;width:41.15pt !msorm;border-top:solid windowtext 1.0pt;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:none;
  mso-border-top-alt:solid windowtext .5pt;mso-border-bottom-alt:solid windowtext .5pt;
  padding:0cm 3.5pt 0cm 3.5pt;border-top:solid windowtext 1.0pt !msorm;
  border-left:none !msorm;border-bottom:solid windowtext 1.0pt !msorm;
  border-right:none !msorm;mso-border-top-alt:solid windowtext .5pt !msorm;
  mso-border-bottom-alt:solid windowtext .5pt !msorm;padding:0cm 3.5pt 0cm 3.5pt !msorm;
  height:14.15pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><b style="mso-bidi-font-weight:normal"><i style="mso-bidi-font-style:normal"><span lang="EN-US" style="font-size:9.0pt;
  font-family:&quot;Times New Roman&quot;,serif;mso-ansi-language:EN-US">PSNR<span class="msoIns"><ins cite="mailto:msi" datetime="2023-02-28T14:28"> <span style="background:windowtext !msorm;mso-highlight:windowtext !msorm"><span style="background:yellow;mso-highlight:yellow"><span style="mso-prop-change:
  msi 20230228T1428">(dB)</span></span></span></ins></span><o:p></o:p></span></i></b></p>
  </td>
  <td width="53" nowrap="" style="width:39.7pt;border-top:solid windowtext 1.0pt;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:none;
  mso-border-top-alt:solid windowtext .5pt;mso-border-bottom-alt:solid windowtext .5pt;
  padding:0cm 3.5pt 0cm 3.5pt;border-top:solid windowtext 1.0pt !msorm;
  border-left:none !msorm;border-bottom:solid windowtext 1.0pt !msorm;
  border-right:none !msorm;mso-border-top-alt:solid windowtext .5pt !msorm;
  mso-border-bottom-alt:solid windowtext .5pt !msorm;padding:0cm 3.5pt 0cm 3.5pt !msorm;
  height:14.15pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><b style="mso-bidi-font-weight:normal"><i style="mso-bidi-font-style:normal"><span lang="EN-US" style="font-size:9.0pt;
  font-family:&quot;Times New Roman&quot;,serif;mso-ansi-language:EN-US">SCC<o:p></o:p></span></i></b></p>
  </td>
  <td width="53" nowrap="" style="width:39.7pt;border-top:solid windowtext 1.0pt;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:none;
  mso-border-top-alt:solid windowtext .5pt;mso-border-bottom-alt:solid windowtext .5pt;
  padding:0cm 3.5pt 0cm 3.5pt;border-top:solid windowtext 1.0pt !msorm;
  border-left:none !msorm;border-bottom:solid windowtext 1.0pt !msorm;
  border-right:none !msorm;mso-border-top-alt:solid windowtext .5pt !msorm;
  mso-border-bottom-alt:solid windowtext .5pt !msorm;padding:0cm 3.5pt 0cm 3.5pt !msorm;
  height:14.15pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><b style="mso-bidi-font-weight:normal"><i style="mso-bidi-font-style:normal"><span lang="EN-US" style="font-size:9.0pt;
  font-family:&quot;Times New Roman&quot;,serif;mso-ansi-language:EN-US">SSIM<o:p></o:p></span></i></b></p>
  </td>
  <td width="53" nowrap="" style="width:39.7pt;border-top:solid windowtext 1.0pt;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:none;
  mso-border-top-alt:solid windowtext .5pt;mso-border-bottom-alt:solid windowtext .5pt;
  padding:0cm 3.5pt 0cm 3.5pt;border-top:solid windowtext 1.0pt !msorm;
  border-left:none !msorm;border-bottom:solid windowtext 1.0pt !msorm;
  border-right:none !msorm;mso-border-top-alt:solid windowtext .5pt !msorm;
  mso-border-bottom-alt:solid windowtext .5pt !msorm;padding:0cm 3.5pt 0cm 3.5pt !msorm;
  height:14.15pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><b style="mso-bidi-font-weight:normal"><i style="mso-bidi-font-style:normal"><span lang="EN-US" style="font-size:9.0pt;
  font-family:&quot;Times New Roman&quot;,serif;mso-ansi-language:EN-US">VIF<o:p></o:p></span></i></b></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:1;height:14.15pt;mso-prop-change:msi 20230228T1428">
  <td width="36" rowspan="4" valign="top" style="width:27.0pt;width:1.0cm !msorm;
  border:none;mso-border-top-alt:solid windowtext .5pt;padding:0cm 3.5pt 0cm 3.5pt;
  border:none !msorm;mso-border-top-alt:solid windowtext .5pt !msorm;
  padding:0cm 3.5pt 0cm 3.5pt !msorm;height:14.15pt">
  <p class="MsoNormal" align="right" style="margin-top:5.0pt;margin-right:0cm;
  margin-bottom:0cm;margin-left:0cm;margin-bottom:.0001pt;text-align:right;
  line-height:normal"><span lang="EN-US" style="font-size:9.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-ansi-language:EN-US">2x<o:p></o:p></span></p>
  </td>
  <td width="57" nowrap="" valign="bottom" style="width:42.55pt;width:39.7pt !msorm;
  border:none;mso-border-top-alt:solid windowtext .5pt;padding:0cm 3.5pt 0cm 3.5pt;
  border:none !msorm;mso-border-top-alt:solid windowtext .5pt !msorm;
  padding:0cm 3.5pt 0cm 3.5pt !msorm;height:14.15pt">
  <p class="MsoNormal" style="margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal"><span lang="EN-US" style="font-size:9.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-ansi-language:EN-US">DECUSR<o:p></o:p></span></p>
  </td>
  <td width="68" nowrap="" valign="bottom" style="width:51.0pt;width:41.15pt !msorm;
  border:none;mso-border-top-alt:solid windowtext .5pt;padding:0cm 3.5pt 0cm 3.5pt;
  border:none !msorm;mso-border-top-alt:solid windowtext .5pt !msorm;
  padding:0cm 3.5pt 0cm 3.5pt !msorm;height:14.15pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><b style="mso-bidi-font-weight:normal"><span lang="EN-US" style="font-size:9.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-ansi-language:EN-US">35.3151<o:p></o:p></span></b></p>
  </td>
  <td width="53" nowrap="" valign="bottom" style="width:39.7pt;border:none;mso-border-top-alt:
  solid windowtext .5pt;padding:0cm 3.5pt 0cm 3.5pt;border:none !msorm;
  mso-border-top-alt:solid windowtext .5pt !msorm;padding:0cm 3.5pt 0cm 3.5pt !msorm;
  height:14.15pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><span lang="EN-US" style="font-size:9.0pt;
  font-family:&quot;Times New Roman&quot;,serif;mso-ansi-language:EN-US">*0.6216<o:p></o:p></span></p>
  </td>
  <td width="53" nowrap="" valign="bottom" style="width:39.7pt;border:none;mso-border-top-alt:
  solid windowtext .5pt;padding:0cm 3.5pt 0cm 3.5pt;border:none !msorm;
  mso-border-top-alt:solid windowtext .5pt !msorm;padding:0cm 3.5pt 0cm 3.5pt !msorm;
  height:14.15pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><b style="mso-bidi-font-weight:normal"><span lang="EN-US" style="font-size:9.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-ansi-language:EN-US">0.9553<o:p></o:p></span></b></p>
  </td>
  <td width="53" nowrap="" valign="bottom" style="width:39.7pt;border:none;mso-border-top-alt:
  solid windowtext .5pt;padding:0cm 3.5pt 0cm 3.5pt;border:none !msorm;
  mso-border-top-alt:solid windowtext .5pt !msorm;padding:0cm 3.5pt 0cm 3.5pt !msorm;
  height:14.15pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><b style="mso-bidi-font-weight:normal"><span lang="EN-US" style="font-size:9.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-ansi-language:EN-US">0.6535<o:p></o:p></span></b></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:2;height:11.35pt;mso-prop-change:msi 20230228T1428">
  <td width="57" nowrap="" valign="bottom" style="width:42.55pt;width:39.7pt !msorm;
  padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;height:11.35pt">
  <p class="MsoNormal" style="margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal"><span lang="EN-US" style="font-size:9.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-ansi-language:EN-US">SRCNN<o:p></o:p></span></p>
  </td>
  <td width="68" nowrap="" valign="bottom" style="width:51.0pt;width:41.15pt !msorm;
  padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;height:11.35pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><span lang="EN-US" style="font-size:9.0pt;
  font-family:&quot;Times New Roman&quot;,serif;mso-ansi-language:EN-US">34.1752<o:p></o:p></span></p>
  </td>
  <td width="53" nowrap="" valign="bottom" style="width:39.7pt;padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;
  height:11.35pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><span lang="EN-US" style="font-size:9.0pt;
  font-family:&quot;Times New Roman&quot;,serif;mso-ansi-language:EN-US">0.5629<o:p></o:p></span></p>
  </td>
  <td width="53" nowrap="" valign="bottom" style="width:39.7pt;padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;
  height:11.35pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><span lang="EN-US" style="font-size:9.0pt;
  font-family:&quot;Times New Roman&quot;,serif;mso-ansi-language:EN-US">0.9391<o:p></o:p></span></p>
  </td>
  <td width="53" nowrap="" valign="bottom" style="width:39.7pt;padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;
  height:11.35pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><span lang="EN-US" style="font-size:9.0pt;
  font-family:&quot;Times New Roman&quot;,serif;mso-ansi-language:EN-US">0.5921<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:3;height:11.35pt;mso-prop-change:msi 20230228T1428">
  <td width="57" nowrap="" valign="bottom" style="width:42.55pt;width:39.7pt !msorm;
  padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;height:11.35pt">
  <p class="MsoNormal" style="margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal"><span lang="EN-US" style="font-size:9.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-ansi-language:EN-US">VDSR<o:p></o:p></span></p>
  </td>
  <td width="68" nowrap="" valign="bottom" style="width:51.0pt;width:41.15pt !msorm;
  padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;height:11.35pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><span lang="EN-US" style="font-size:9.0pt;
  font-family:&quot;Times New Roman&quot;,serif;mso-ansi-language:EN-US">30.3865<o:p></o:p></span></p>
  </td>
  <td width="53" nowrap="" valign="bottom" style="width:39.7pt;padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;
  height:11.35pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><span lang="EN-US" style="font-size:9.0pt;
  font-family:&quot;Times New Roman&quot;,serif;mso-ansi-language:EN-US">0.5859<o:p></o:p></span></p>
  </td>
  <td width="53" nowrap="" valign="bottom" style="width:39.7pt;padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;
  height:11.35pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><span lang="EN-US" style="font-size:9.0pt;
  font-family:&quot;Times New Roman&quot;,serif;mso-ansi-language:EN-US">0.9406<o:p></o:p></span></p>
  </td>
  <td width="53" nowrap="" valign="bottom" style="width:39.7pt;padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;
  height:11.35pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><span lang="EN-US" style="font-size:9.0pt;
  font-family:&quot;Times New Roman&quot;,serif;mso-ansi-language:EN-US">0.6159<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:4;height:11.35pt;mso-prop-change:msi 20230228T1428">

  <td width="57" nowrap="" valign="bottom" style="width:42.55pt;width:39.7pt !msorm;
  padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;height:11.35pt">
  <p class="MsoNormal" style="margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal"><span lang="EN-US" style="font-size:9.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-ansi-language:EN-US">RED-Net<o:p></o:p></span></p>
  </td>
  <td width="68" nowrap="" valign="bottom" style="width:51.0pt;width:41.15pt !msorm;
  padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;height:11.35pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><span lang="EN-US" style="font-size:9.0pt;
  font-family:&quot;Times New Roman&quot;,serif;mso-ansi-language:EN-US">*34.2038<o:p></o:p></span></p>
  </td>
  <td width="53" nowrap="" valign="bottom" style="width:39.7pt;padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;
  height:11.35pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><b style="mso-bidi-font-weight:normal"><span lang="EN-US" style="font-size:9.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-ansi-language:EN-US">0.6415<o:p></o:p></span></b></p>
  </td>
  <td width="53" nowrap="" valign="bottom" style="width:39.7pt;padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;
  height:11.35pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><span lang="EN-US" style="font-size:9.0pt;
  font-family:&quot;Times New Roman&quot;,serif;mso-ansi-language:EN-US">*0.9522<o:p></o:p></span></p>
  </td>
  <td width="53" nowrap="" valign="bottom" style="width:39.7pt;padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;
  height:11.35pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><span lang="EN-US" style="font-size:9.0pt;
  font-family:&quot;Times New Roman&quot;,serif;mso-ansi-language:EN-US">*0.6480<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:5;height:14.15pt;mso-prop-change:msi 20230228T1428">
  <td width="36" rowspan="4" valign="top" style="width:27.0pt;width:1.0cm !msorm;
  padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;height:14.15pt">
  <p class="MsoNormal" align="right" style="margin-top:5.0pt;margin-right:0cm;
  margin-bottom:0cm;margin-left:0cm;margin-bottom:.0001pt;text-align:right;
  line-height:normal"><span lang="EN-US" style="font-size:9.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-ansi-language:EN-US">3x<o:p></o:p></span></p>
  </td>
  <td width="57" nowrap="" valign="bottom" style="width:42.55pt;width:39.7pt !msorm;
  padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;height:14.15pt">
  <p class="MsoNormal" style="margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal"><span lang="EN-US" style="font-size:9.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-ansi-language:EN-US">DECUSR<o:p></o:p></span></p>
  </td>
  <td width="68" nowrap="" valign="bottom" style="width:51.0pt;width:41.15pt !msorm;
  padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;height:14.15pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><b style="mso-bidi-font-weight:normal"><span lang="EN-US" style="font-size:9.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-ansi-language:EN-US">32.7401<o:p></o:p></span></b></p>
  </td>
  <td width="53" nowrap="" valign="bottom" style="width:39.7pt;padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;
  height:14.15pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><span lang="EN-US" style="font-size:9.0pt;
  font-family:&quot;Times New Roman&quot;,serif;mso-ansi-language:EN-US">*0.3847<o:p></o:p></span></p>
  </td>
  <td width="53" nowrap="" valign="bottom" style="width:39.7pt;padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;
  height:14.15pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><span lang="EN-US" style="font-size:9.0pt;
  font-family:&quot;Times New Roman&quot;,serif;mso-ansi-language:EN-US">*0.9072<o:p></o:p></span></p>
  </td>
  <td width="53" nowrap="" valign="bottom" style="width:39.7pt;padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;
  height:14.15pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><span lang="EN-US" style="font-size:9.0pt;
  font-family:&quot;Times New Roman&quot;,serif;mso-ansi-language:EN-US">*0.5245<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:6;height:11.35pt;mso-prop-change:msi 20230228T1428">
  <td width="57" nowrap="" valign="bottom" style="width:42.55pt;width:39.7pt !msorm;
  padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;height:11.35pt">
  <p class="MsoNormal" style="margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal"><span lang="EN-US" style="font-size:9.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-ansi-language:EN-US">SRCNN<o:p></o:p></span></p>
  </td>
  <td width="68" nowrap="" valign="bottom" style="width:51.0pt;width:41.15pt !msorm;
  padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;height:11.35pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><span lang="EN-US" style="font-size:9.0pt;
  font-family:&quot;Times New Roman&quot;,serif;mso-ansi-language:EN-US">31.2075<o:p></o:p></span></p>
  </td>
  <td width="53" nowrap="" valign="bottom" style="width:39.7pt;padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;
  height:11.35pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><span lang="EN-US" style="font-size:9.0pt;
  font-family:&quot;Times New Roman&quot;,serif;mso-ansi-language:EN-US">0.3150<o:p></o:p></span></p>
  </td>
  <td width="53" nowrap="" valign="bottom" style="width:39.7pt;padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;
  height:11.35pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><span lang="EN-US" style="font-size:9.0pt;
  font-family:&quot;Times New Roman&quot;,serif;mso-ansi-language:EN-US">0.8882<o:p></o:p></span></p>
  </td>
  <td width="53" nowrap="" valign="bottom" style="width:39.7pt;padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;
  height:11.35pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><span lang="EN-US" style="font-size:9.0pt;
  font-family:&quot;Times New Roman&quot;,serif;mso-ansi-language:EN-US">0.4777<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:7;height:11.35pt;mso-prop-change:msi 20230228T1428">
  <td width="57" nowrap="" valign="bottom" style="width:42.55pt;width:39.7pt !msorm;
  padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;height:11.35pt">
  <p class="MsoNormal" style="margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal"><span lang="EN-US" style="font-size:9.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-ansi-language:EN-US">VDSR<o:p></o:p></span></p>
  </td>
  <td width="68" nowrap="" valign="bottom" style="width:51.0pt;width:41.15pt !msorm;
  padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;height:11.35pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><span lang="EN-US" style="font-size:9.0pt;
  font-family:&quot;Times New Roman&quot;,serif;mso-ansi-language:EN-US">32.2727<o:p></o:p></span></p>
  </td>
  <td width="53" nowrap="" valign="bottom" style="width:39.7pt;padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;
  height:11.35pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><span lang="EN-US" style="font-size:9.0pt;
  font-family:&quot;Times New Roman&quot;,serif;mso-ansi-language:EN-US">0.3799<o:p></o:p></span></p>
  </td>
  <td width="53" nowrap="" valign="bottom" style="width:39.7pt;padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;
  height:11.35pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><span lang="EN-US" style="font-size:9.0pt;
  font-family:&quot;Times New Roman&quot;,serif;mso-ansi-language:EN-US">0.9046<o:p></o:p></span></p>
  </td>
  <td width="53" nowrap="" valign="bottom" style="width:39.7pt;padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;
  height:11.35pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><span lang="EN-US" style="font-size:9.0pt;
  font-family:&quot;Times New Roman&quot;,serif;mso-ansi-language:EN-US">0.5175<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:8;height:11.35pt;mso-prop-change:msi 20230228T1428">
 
  <td width="57" nowrap="" valign="bottom" style="width:42.55pt;width:39.7pt !msorm;
  padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;height:11.35pt">
  <p class="MsoNormal" style="margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal"><span lang="EN-US" style="font-size:9.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-ansi-language:EN-US">RED-Net<o:p></o:p></span></p>
  </td>
  <td width="68" nowrap="" valign="bottom" style="width:51.0pt;width:41.15pt !msorm;
  padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;height:11.35pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><span lang="EN-US" style="font-size:9.0pt;
  font-family:&quot;Times New Roman&quot;,serif;mso-ansi-language:EN-US">*32,6412<o:p></o:p></span></p>
  </td>
  <td width="53" nowrap="" valign="bottom" style="width:39.7pt;padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;
  height:11.35pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><b style="mso-bidi-font-weight:normal"><span lang="EN-US" style="font-size:9.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-ansi-language:EN-US">0.3876<o:p></o:p></span></b></p>
  </td>
  <td width="53" nowrap="" valign="bottom" style="width:39.7pt;padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;
  height:11.35pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><b style="mso-bidi-font-weight:normal"><span lang="EN-US" style="font-size:9.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-ansi-language:EN-US">0.9094<o:p></o:p></span></b></p>
  </td>
  <td width="53" nowrap="" valign="bottom" style="width:39.7pt;padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;
  height:11.35pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><b style="mso-bidi-font-weight:normal"><span lang="EN-US" style="font-size:9.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-ansi-language:EN-US">0.5340<o:p></o:p></span></b></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:9;height:14.15pt;mso-prop-change:msi 20230228T1428">
  <td width="36" rowspan="4" valign="top" style="width:27.0pt;width:1.0cm !msorm;
  padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;height:14.15pt">
  <p class="MsoNormal" align="right" style="margin-top:5.0pt;margin-right:0cm;
  margin-bottom:0cm;margin-left:0cm;margin-bottom:.0001pt;text-align:right;
  line-height:normal"><span lang="EN-US" style="font-size:9.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-ansi-language:EN-US">4x<o:p></o:p></span></p>
  </td>
  <td width="57" nowrap="" valign="bottom" style="width:42.55pt;width:39.7pt !msorm;
  padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;height:14.15pt">
  <p class="MsoNormal" style="margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal"><span lang="EN-US" style="font-size:9.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-ansi-language:EN-US">DECUSR<o:p></o:p></span></p>
  </td>
  <td width="68" nowrap="" valign="bottom" style="width:51.0pt;width:41.15pt !msorm;
  padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;height:14.15pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><span lang="EN-US" style="font-size:9.0pt;
  font-family:&quot;Times New Roman&quot;,serif;mso-ansi-language:EN-US">*30.7326<o:p></o:p></span></p>
  </td>
  <td width="53" nowrap="" valign="bottom" style="width:39.7pt;padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;
  height:14.15pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><span lang="EN-US" style="font-size:9.0pt;
  font-family:&quot;Times New Roman&quot;,serif;mso-ansi-language:EN-US">*0.2571<o:p></o:p></span></p>
  </td>
  <td width="53" nowrap="" valign="bottom" style="width:39.7pt;padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;
  height:14.15pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><span lang="EN-US" style="font-size:9.0pt;
  font-family:&quot;Times New Roman&quot;,serif;mso-ansi-language:EN-US">*0.8603<o:p></o:p></span></p>
  </td>
  <td width="53" nowrap="" valign="bottom" style="width:39.7pt;padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;
  height:14.15pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><span lang="EN-US" style="font-size:9.0pt;
  font-family:&quot;Times New Roman&quot;,serif;mso-ansi-language:EN-US">*0.4374<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:10;height:11.35pt;mso-prop-change:msi 20230228T1428">
  <td width="57" nowrap="" valign="bottom" style="width:42.55pt;width:39.7pt !msorm;
  padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;height:11.35pt">
  <p class="MsoNormal" style="margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal"><span lang="EN-US" style="font-size:9.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-ansi-language:EN-US">SRCNN<o:p></o:p></span></p>
  </td>
  <td width="68" nowrap="" style="width:51.0pt;width:41.15pt !msorm;padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;
  height:11.35pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><span lang="EN-US" style="font-size:9.0pt;
  font-family:&quot;Times New Roman&quot;,serif;mso-ansi-language:EN-US">28.7886<o:p></o:p></span></p>
  </td>
  <td width="53" nowrap="" style="width:39.7pt;padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;
  height:11.35pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><span lang="EN-US" style="font-size:9.0pt;
  font-family:&quot;Times New Roman&quot;,serif;mso-ansi-language:EN-US">0.1970<o:p></o:p></span></p>
  </td>
  <td width="53" nowrap="" style="width:39.7pt;padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;
  height:11.35pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><span lang="EN-US" style="font-size:9.0pt;
  font-family:&quot;Times New Roman&quot;,serif;mso-ansi-language:EN-US">0.8342<o:p></o:p></span></p>
  </td>
  <td width="53" nowrap="" style="width:39.7pt;padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;
  height:11.35pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><span lang="EN-US" style="font-size:9.0pt;
  font-family:&quot;Times New Roman&quot;,serif;mso-ansi-language:EN-US">0.3862<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:11;height:11.35pt;mso-prop-change:msi 20230228T1428">
  <td width="57" nowrap="" valign="bottom" style="width:42.55pt;width:39.7pt !msorm;
  padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;height:11.35pt">
  <p class="MsoNormal" style="margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal"><span lang="EN-US" style="font-size:9.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-ansi-language:EN-US">VDSR<o:p></o:p></span></p>
  </td>
  <td width="68" nowrap="" style="width:51.0pt;width:41.15pt !msorm;padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;
  height:11.35pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><span lang="EN-US" style="font-size:9.0pt;
  font-family:&quot;Times New Roman&quot;,serif;mso-ansi-language:EN-US">30.0878<o:p></o:p></span></p>
  </td>
  <td width="53" nowrap="" style="width:39.7pt;padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;
  height:11.35pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><span lang="EN-US" style="font-size:9.0pt;
  font-family:&quot;Times New Roman&quot;,serif;mso-ansi-language:EN-US">0.2549<o:p></o:p></span></p>
  </td>
  <td width="53" nowrap="" style="width:39.7pt;padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;
  height:11.35pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><span lang="EN-US" style="font-size:9.0pt;
  font-family:&quot;Times New Roman&quot;,serif;mso-ansi-language:EN-US">0.8569<o:p></o:p></span></p>
  </td>
  <td width="53" nowrap="" style="width:39.7pt;padding:0cm 3.5pt 0cm 3.5pt 0cm 3.5pt 0cm 3.5pt !msorm;
  height:11.35pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><span lang="EN-US" style="font-size:9.0pt;
  font-family:&quot;Times New Roman&quot;,serif;mso-ansi-language:EN-US">0.4267<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:12;mso-yfti-lastrow:yes;height:11.35pt;mso-prop-change:
  msi 20230228T1428">
 
  <td width="57" nowrap="" valign="bottom" style="width:42.55pt;width:39.7pt !msorm;
  border:none;border-bottom:solid windowtext 1.0pt;mso-border-bottom-alt:solid windowtext .5pt;
  padding:0cm 3.5pt 0cm 3.5pt;border:none !msorm;border-bottom:solid windowtext 1.0pt !msorm;
  mso-border-bottom-alt:solid windowtext .5pt !msorm;padding:0cm 3.5pt 0cm 3.5pt !msorm;
  height:11.35pt">
  <p class="MsoNormal" style="margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal"><span lang="EN-US" style="font-size:9.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-ansi-language:EN-US">RED-Net<o:p></o:p></span></p>
  </td>
  <td width="68" nowrap="" style="width:51.0pt;width:41.15pt !msorm;border:none;
  border-bottom:solid windowtext 1.0pt;mso-border-bottom-alt:solid windowtext .5pt;
  padding:0cm 3.5pt 0cm 3.5pt;border:none !msorm;border-bottom:solid windowtext 1.0pt !msorm;
  mso-border-bottom-alt:solid windowtext .5pt !msorm;padding:0cm 3.5pt 0cm 3.5pt !msorm;
  height:11.35pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><b style="mso-bidi-font-weight:normal"><span lang="EN-US" style="font-size:9.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-ansi-language:EN-US">31.0851<o:p></o:p></span></b></p>
  </td>
  <td width="53" nowrap="" style="width:39.7pt;border:none;border-bottom:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;padding:0cm 3.5pt 0cm 3.5pt;
  border:none !msorm;border-bottom:solid windowtext 1.0pt !msorm;mso-border-bottom-alt:
  solid windowtext .5pt !msorm;padding:0cm 3.5pt 0cm 3.5pt !msorm;height:11.35pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><b style="mso-bidi-font-weight:normal"><span lang="EN-US" style="font-size:9.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-ansi-language:EN-US">0.2689<o:p></o:p></span></b></p>
  </td>
  <td width="53" nowrap="" style="width:39.7pt;border:none;border-bottom:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;padding:0cm 3.5pt 0cm 3.5pt;
  border:none !msorm;border-bottom:solid windowtext 1.0pt !msorm;mso-border-bottom-alt:
  solid windowtext .5pt !msorm;padding:0cm 3.5pt 0cm 3.5pt !msorm;height:11.35pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><b style="mso-bidi-font-weight:normal"><span lang="EN-US" style="font-size:9.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-ansi-language:EN-US">0.8680<o:p></o:p></span></b></p>
  </td>
  <td width="53" nowrap="" style="width:39.7pt;border:none;border-bottom:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;padding:0cm 3.5pt 0cm 3.5pt;
  border:none !msorm;border-bottom:solid windowtext 1.0pt !msorm;mso-border-bottom-alt:
  solid windowtext .5pt !msorm;padding:0cm 3.5pt 0cm 3.5pt !msorm;height:11.35pt">
  <p class="MsoNormal" align="right" style="margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal"><b style="mso-bidi-font-weight:normal"><span lang="EN-US" style="font-size:9.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-ansi-language:EN-US">0.4574<o:p></o:p></span></b></p>
  </td>
 </tr>
</tbody></table>


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
 <caption><b>Sample Outputs of Another Text Image</b></caption>
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

&nbsp;

Please feel free to contact me at [htemiz@artvin.edu.tr](mailto:htemiz@artvin.edu.tr) for any further information.