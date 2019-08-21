# OpenCV

## Installation

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