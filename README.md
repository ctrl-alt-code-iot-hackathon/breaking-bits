<p align="center"><img src="https://i.imgur.com/NXgkPSs.png" width="100" /></p>
<p align="center"><img src="https://travis-ci.org/dwyl/esta.svg?branch=master" width="100" /></p>


<h2>Drishti</h2>
Drishti uses an automated malaria screening technique on the blood samples using our Deep Learning model which serves as an effective diagnostic aid for the infected people.

## Malaria
Diagnosis of malaria involves identification of malaria parasite or its antigens/products in the blood of the patient. Although this seems simple, the efficacy of the diagnosis is subject to many factors. The different forms of the four malaria species; the different stages of erythrocytic schizogony; the endemicity of different species; the population movements.

The diagnosis of malaria is confirmed by blood tests and can be divided into microscopic and non-microscopic tests.

## Flaws in RDTs of Malaria
1) Cross-reactions with autoantibodies
2) Sensitivity
3) False Positivity
4) Cross reactions between Plasmodia species and problems in identifying non-falciparum species

## Dependencies
<ul>
  <li><p >TensorFlow<a href="#" ><img src="https://img.shields.io/badge/api-reference-blue.svg" width="100" align="right" /></a></p></li>
 <li><p >OpenCV<a href="#" ><img src="https://img.shields.io/badge/api-reference-blue.svg" width="100" align="right" /></a></p></li>
 <li><p >NumPy<a href="#" ><img src="https://img.shields.io/badge/api-reference-blue.svg" width="100" align="right" /></a></p></li>
 <li><p >Matplotlib<a href="#" ><img src="https://img.shields.io/badge/api-reference-blue.svg" width="100" align="right" /></a></p></li>
 <li><p >Protobuf<a href="#" ><img src="https://img.shields.io/badge/api-reference-blue.svg" width="100" align="right" /></a></p></li>
 <li><p >Jupyter notebook<a href="#" ><img src="https://img.shields.io/badge/api-reference-blue.svg" width="100" align="right" /></a></p></li>
 
</ul>

## Our Model
<p align="center"><img src="https://static1.squarespace.com/static/54856bade4b0c4cdfb17e3c0/t/58278379f7e0ab81d3e68c5a/1478984571373/" width="500" /></p>

* The dataset consists of 27,558 cell images with equal instances of parasitized and uninfected cells.
* Positive samples contained Plasmodium and negative samples contained no Plasmodium.
* The proposed CNN has two convolutional layers and two fully connected layers.
* The input to the model constitutes segmented cells of 128 × 128 × 3 pixel resolution.
* The first convolutional layers use 3 × 3 filters with 2 pixel strides then we perform max pooling with a pooling window of 2 × 2 and 2 pixel strides.
* The second convolutional layers also use 3 × 3 filters with 2 pixel strides then we perform max pooling with a pooling window of 2 × 2 and 2 pixel strides.
* Both the Convolution layer have 64 filters.
* Now, we flatten the layer that have 28800 units.
* we apply Relu activation function on this flatten layer and make a dense layer of 128 units.
* we apply sigmoid activation function on the dense layer to predict the presence of malaria or not.

## Images dataset

<h2>Uninfected thin blood smear images</h2>
<a href="https://imgur.com/RQF7ncr"><img src="https://i.imgur.com/RQF7ncr.png" title="source: imgur.com" /></a>
<a href="https://imgur.com/ZPPcCch"><img src="https://i.imgur.com/ZPPcCch.png" title="source: imgur.com" /></a>
<a href="https://imgur.com/CprSslG"><img src="https://i.imgur.com/CprSslG.png" title="source: imgur.com" /></a>

<h2>Infected thin blood smear images</h2>
<a href="https://imgur.com/veyBS97"><img src="https://i.imgur.com/veyBS97.png" title="source: imgur.com" /></a>
<a href="https://imgur.com/YkDTGJz"><img src="https://i.imgur.com/YkDTGJz.png" title="source: imgur.com" /></a>
<a href="https://imgur.com/8JYV6cG"><img src="https://i.imgur.com/8JYV6cG.png" title="source: imgur.com" /></a>

## Working
<a href="https://imgur.com/3pRpsJS"><img src="https://i.imgur.com/3pRpsJS.png" title="source: imgur.com" /></a>
<a href="https://imgur.com/SSERQGQ"><img src="https://i.imgur.com/SSERQGQ.png" title="source: imgur.com" /></a>

## Video Link

Youtube Link: https://youtu.be/wflByqpDdA0

