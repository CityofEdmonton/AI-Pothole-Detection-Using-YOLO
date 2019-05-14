# AI Pothole Detection Using YOLO

### [YOLO: Real-Time Object Detection](https://pjreddie.com/darknet/yolo/)

# Setup

This project uses [AlexeyDB's fork](https://github.com/AlexeyAB/darknet) of Darknet Yolo that runs on Windows and Linux. This [tutorial](https://timebutt.github.io/static/how-to-train-yolov2-to-detect-custom-objects/) was used as a basis to train the model to detect potholes. I found it beneficial to run through the tutorial completely once before starting on the potholes dataset. The modified files can be found in [this](https://github.com/CityofEdmonton/AI-Pothole-Detection-Using-YOLO) Github repository.

## System Description

A Linux virtual machine was used to run this project.

```
OS: Ubuntu 18.04
GPU: 1GB
```
<!-- TODO: Get more system descriptions -->

## Virtual Machine Communication

An SSH connection was used to connect to the virtual machine used to run the project. [PuTTY](https://www.putty.org/) was used on the local machine (Windows 10) to connect to the VM. Since there was no graphical interface for the VM, [SCP](https://en.wikipedia.org/wiki/Secure_copy) was used to transfer files between the local machine and the VM.

## OpenCV

Follow [this tutorial](https://docs.opencv.org/4.1.0/d7/d9f/tutorial_linux_install.html) to install OpenCV onto a Linux machine.

If you run into any problems, you can check out the *Troubleshooting* section which highlights some of the problems I've encountered while working on this project.

## Saving Weights

You can configure the frequency to save the trained weights in the [`detector.c`](https://github.com/AlexeyAB/darknet/blob/cce34712f6928495f1fbc5d69332162fc23491b9/src/detector.c#L271) file.

## Data Formatting (Custom Objects)

There should be a text file for every JPEG image file describing the positions of the potholes in the specified image. The text file should have the same name and be in the same directory as the image file. What should be included in the text file:

`<object-class> <x_center> <y_center> <width> <height>`

Where: 
  * `<object-class>` - integer object number from `0` to `(classes-1)`
  * `<x_center> <y_center> <width> <height>` - float values **relative** to width and height of image, it can be equal from `(0.0 to 1.0]`
  * for example: `<x> = <absolute_x> / <image_width>` or `<height> = <absolute_height> / <image_height>`
  * attention: `<x_center> <y_center>` - are center of rectangle (are not top-left corner)

For example for `img1.jpg` you will be creating `img1.txt` containing:

```
1 0.716797 0.395833 0.216406 0.147222
0 0.687109 0.379167 0.255469 0.158333
1 0.420312 0.395833 0.140625 0.166667
```

The above information is obtained from [this source](https://github.com/AlexeyAB/darknet#how-to-train-to-detect-your-custom-objects).

*Note*: `<object-class>` should always be `0` in our case since we are only detecting a single `Pothole` class

## Other Requirements

Project requirements can be found [here](https://github.com/AlexeyAB/darknet#requirements).

# Running the Project

The files referenced below can be found in [this repository](https://github.com/CityofEdmonton/AI-Pothole-Detection-Using-YOLO).

1. Fork [this repo](https://github.com/AlexeyAB/darknet) into your Github account and clone it to your local machine.
2. Ensure that the [requirements](https://github.com/AlexeyAB/darknet#requirement) for this project are met.
3. Replace the *Makefile* with the one in the repository specified above or configure the file accordingly:

   - ```MK
     GPU=1
     ```
   - ```MK
     OPENCV=1
     ```
   - ```MK
     NVCC=/usr/local/cuda/bin/nvcc # Or the path to your NVCC
     ```
   - ```MK
     LDFLAGS+= `pkg-config --libs opencv4`
     COMMON+= `pkg-config --cflags opencv4`
     ```

4. Run `make` in the root of the project.
5. If darknet has compiled successfully, running `./darknet` in the root of the project should return:

   ```
   usage: ./darknet <function>
   ```

6. Place the files `obj.data`, `obj.names`, `yolo-pothole-test.cfg`, and `yolo-pothole-train.cfg` in the `cfg/` directory of the project.
7. Import the formatted data with both the JPEG and text files into the ```data/Pothole/``` directory. This directory will have to be created.
8. Place the `train.txt` and `test.txt` files in the `data/Pothole` directory as well.
9. Training requires a set of convolutional weights that can be downloaded from the official YOLO website [here](https://pjreddie.com/media/files/darknet19_448.conv.23). Place these weights in the root of the project.
10. Start the training by running:

    ```
    ./darknet detector train cfg/obj.data cfg/yolo-pothole-train.cfg darknet19_448.conv.23
    ```

    *Note*: The weights save every 100 iterations until the 1000th iteration, after which it saves every 1000 iterations. The program will also save the weights every 100 iterations as a `<training_config>_last.weights` file

11. To resume training using an existing weight, run:

    ```
    ./darknet detector train cfg/obj.data cfg/yolo-pothole-train.cfg <last_weight_file>
    ```

12. You should stop training when the mean average precision (mAP) is the **highest**. To get the mAP of a weight:

    ```
    ./darknet detector map cfg/obj.data cfg/yolo-pothole-train.cfg <weight_file>
    ```

    Read [here](https://github.com/AlexeyAB/darknet#when-should-i-stop-training) for more info.

13. Once the training is complete, you can test the detection by running:
    - For image files:

      ```
      ./darknet detector test cfg/obj.data cfg/yolo-pothole-test.cfg <trained_weight_file> <image_file>
      ```

      *Note*: The image will automatically be saved as `predictions.jpg`

    - For video files:

      ```
      ./darknet detector demo cfg/obj.data cfg/yolo-pothole-test.cfg <trained_weight_file> <video_file> -out_filename <video_output>.avi
      ```
      Here's a [reference](https://github.com/pjreddie/darknet/issues/102#issuecomment-413264294) to the command


Check out the *Troubleshooting* section if you run into any problems.

# Troubleshooting

Here is a description of the problems I encountered while working on this project.

## OpenCV Installation

**Problem:**

```
Package opencv was not found in the pkg-config search path.
```
Compile with additional options:
```
cmake -D CMAKE_BUILD_TYPE=Release -D OPENCV_GENERATE_PKGCONFIG=YES -D CMAKE_INSTALL_PREFIX=/usr/local ..
```
Remember to change the references in darknet's Makefile as well:
```
LDFLAGS+= `pkg-config --libs opencv4`
COMMON+= `pkg-config --cflags opencv4`
```
Solution obtained from [this post](https://github.com/opencv/opencv/issues/13154#issuecomment-456652297).

---

**Problem:**

```
./darknet: error while loading shared libraries: libopencv_highgui.so.4.1: cannot open shared object file: No such file or directory
```
Run this command:
```
sudo /bin/bash -c 'echo "/usr/local/lib" > /etc/ld.so.conf.d/opencv.conf'
sudo ldconfig
```
Solution obtained from [this post](https://github.com/pjreddie/darknet/issues/382#issuecomment-353793523).

## Darknet Compilation

**Problem:**

```
/bin/sh: 1: nvcc: not found
Makefile:152: recipe for target 'obj/convolutional_kernels.o' failed
make: *** [obj/convolutional_kernels.o] Error 127
```
Obtain the correct reference to the CUDA library. For me, it was:
```
NVCC=/usr/local/cuda/bin/nvcc
```
Solution obtained from [this post](https://github.com/pjreddie/darknet/issues/1246#issuecomment-460568326)

## Renaming files

**Problem:**

Transferring JPEG files to the VM from the local machine results in the .jpg file extensions to be changed to .JPG, which prevents the images from being properly read by the program.

Run this command while in the directory of the image files:
```
rename 's/.JPG/.jpg/' *.JPG
```
Solution obtained from [this site](https://www.maketecheasier.com/rename-files-in-linux/).

## Using Darknet

**Problem:**

The project was run on an Azure VM without display capabilities.
```
Gtk-WARNING **: 19:03:05.170: cannot open display:
```
Use the `-dont_show` flag when testing or training:
```
./darknet detector test <object data file> <config file> <weight file> <test image> -dont_show
```
Solution obtained from [this post](https://github.com/pjreddie/darknet/issues/722#issuecomment-383836468).

# Datasets and Files

### Original dataset

Download from [Google Drive](http://goo.gl/Uj38Sf) or their [server](http://staff.ee.sun.ac.za/mjbooysen/Potholes/Slow/).

### YOLOv2 Formatted Dataset

Download from [Google Drive](http://bit.ly/2vZV8Bj).

### Project Files

Project files can be found in [this Github repository]().
<!-- TODO: Include weight files -->

# Results

*Images to be added...*

*Videos to be added...*
<!-- Images and Videos -->
