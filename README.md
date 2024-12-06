# Dog Breed Classifier

This project is part of the Udacity AI Programming with Python Nanodegree program. It uses pre-trained convolutional neural networks (CNNs) to classify images of dogs according to their breed, comparing the performance of different architectures (ResNet, AlexNet, and VGG).

## Setup

```bash
# Create and activate conda environment
conda env create -f environment.yml
conda activate dog
```

## Run

```bash
python check_images.py --dir pet_images/ --arch [resnet, alexnet, or vgg] --dogfile dognames.txt
```

Parameters:
- `--dir`: Image directory (default: pet_images/)
- `--arch`: Model architecture (default: vgg)
- `--dogfile`: Dog names file (default: dognames.txt)