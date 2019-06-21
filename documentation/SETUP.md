# Setup

## System Description

A Linux virtual machine was used to run this project.

```
OS: Ubuntu 18.04
GPU: 1GB
```

## Virtual Machine Communication

An SSH connection was used to connect to the virtual machine used to run the project. [PuTTY](https://www.putty.org/) was used on the local machine (Windows 10) to connect to the VM. Since there was no graphical interface for the VM, [SCP](https://en.wikipedia.org/wiki/Secure_copy) was used to transfer files between the local machine and the VM.

## OpenCV

Follow [this tutorial](https://docs.opencv.org/4.1.0/d7/d9f/tutorial_linux_install.html) to install OpenCV onto a Linux machine.

If you run into any problems, you can check out the [*Troubleshooting*]() section which highlights some of the problems I've encountered while working on this project.

## Saving Weights

You can configure the frequency to save the trained weights in the [`detector.c`](https://github.com/AlexeyAB/darknet/blob/cce34712f6928495f1fbc5d69332162fc23491b9/src/detector.c#L271) file.

## Other Requirements

Project requirements can be found [here](https://github.com/AlexeyAB/darknet#requirements).