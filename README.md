# Crowd Counting App

This repository contains a Gradio-based web application for crowd counting. Utilizing the `modelscope` library, the app performs crowd counting from images and displays the total count in an interactive interface.

## Features

- **Crowd Counting**: Upload an image, and the app will count the number of individuals using a pre-trained crowd counting model.
- **Interactive Interface**: Built with Gradio for an intuitive user experience.
- **Reset Functionality**: Allows users to upload another image seamlessly.

## Technologies Used

- **Gradio**: For creating the user interface.
- **Modelscope**: To perform crowd counting.
- **PIL**: For image processing.

## Usage

1. Upload an image using the file uploader.
2. Click "Count Crowd" to get the total number of people detected in the image.
3. Use "Upload Another Image" to clear the input and upload a new image.

## Installation

To run this application locally, follow these steps:

First, clone the repository:

```bash
git clone https://github.com/HussainNasirKhan/Crowd-Counting-App.git
cd Crowd-Counting-App
```

Create a new virtual environment and activate it:
```bash
conda create -n crowdcount python=3.10
conda activate crowdcount
```

Install the required Python packages:
```bash
pip3 install torch torchvision torchaudio
pip install --upgrade tensorflow==2.13.0
pip install modelscope
pip install "modelscope[cv]" -f https://modelscope.oss-cn-beijing.aliyuncs.com/releases/repo.html
pip install gradio
```
Run the Application
```bash
python app.py
```
