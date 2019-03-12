<p align="center"><img src="https://i.imgur.com/NXgkPSs.png" width="100" /></p>
<p align="center"><img src="https://travis-ci.org/dwyl/esta.svg?branch=master" width="100" /></p>


<h2>Drishti</h2>
Drishti uses automated malaria screening using DL techniques could, therefore, serve as an effective diagnostic aid

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
  <li><p >Caffee<a href="#" ><img src="https://img.shields.io/badge/api-reference-blue.svg" width="100" align="right" /></a></p></li>
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
