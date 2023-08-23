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
The dataset used is the CelebA https://www.kaggle.com/datasets/jessicali9530/celeba-dataset. It contains over 200,000 celebrity images. We extracted the dataset using patoolib.
### Data Preprocessing
To get some better results and decrease training time, we will crop the images, so that only the faces are showing. We are going to downscale the images to 64x64. At last, we  will also standardize the images so that their values are in the range of 0 to 1
### Model
#### Discriminator network
The discriminator tries to distinguish between real and fake images. It's a convolutional neural network. The discriminator network consists of four convolutional layers. For every layer of the network, we are going to perform a convolution, then we are going to perform batch normalization to make training of artificial neural networks faster and more stable and finally, we are going to perform a Leaky ReLu.
#### Generator network
The generator goes the other way: It tries to fool the discriminator. This network consists of four deconvolutional layers. In here, we are doing the same as in the discriminator, just in the other direction. First, we take our input, called noise_shape, and feed it into our first deconvolutional layer. Each deconvolutional layer performs a deconvolution and then performs batch normalization and a leaky ReLu as well.
### Training and Generating Images
The final step is to train the models for 300 epochs.  We have used only five epochs for the following train and saved an image at an interval of 100. The Gradient Tape function will automatically compile both models accordingly. Once our training procedure is complete, we can proceed to save the GAN model in the same directory.
###  Import the model and generate an image using the model
To do that, we start by creating a virtual environment Venv. Then, we install the necessary requirements to execute the model. 
