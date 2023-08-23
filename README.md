# Human_face_generator
In this project, we will try to build a GAN from scratch that can generate human faces with TensorFlow then import the trained model and generate an image using the model.
### Setup
Used Libraries:
-  patrol
- os
- glob
- matplotlib
- PIL / Pillow
- NumPy
- TensorFlow
- Flask
### Dataset CelebA
The dataset used is the CelebA https://www.kaggle.com/datasets/jessicali9530/celeba-dataset. It contains over 200,000 celebrity images. we extracted the dataset using patoolib.
### Data Preprocessing
To get some better results and decrease training time, we will crop the images, so that only the faces are showing. We will also standardize the images so that their values are in a range from 0 to 1. At last, we are going to downscale the images to 64x64 after that.
### Model
#### Discriminator network
The discriminator tries to distinguish between real and fake images. It's a convolutional neural network. The discriminator network consists of four convolutional layers. For every layer of the network, we are going to perform a convolution, then we are going to perform batch normalization to make training of artificial neural networks faster and more stable and finally, we are going to perform a Leaky ReLu.
#### Generator network
The generator goes the other way: It tries to fool the discriminator. This network consists of four deconvolutional layers. In here, we are doing the same as in the discriminator, just in the other direction. First, we take our input, called noise_shape, and feed it into our first deconvolutional layer. Each deconvolutional layer performs a deconvolution and then performs batch normalization and a leaky ReLu as well.
