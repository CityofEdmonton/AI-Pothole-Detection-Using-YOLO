# Darknet

## Compilation

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

## Usage

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