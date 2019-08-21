# Preparing the Data - Data Formatting for Custom Objects

### **You can skip the steps below by downloading the annotated dataset from [this](http://bit.ly/2vZV8Bj) link.**

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

## Next Step: > [Running the Project](/documentation/RUNNING_THE_PROJECT.md)