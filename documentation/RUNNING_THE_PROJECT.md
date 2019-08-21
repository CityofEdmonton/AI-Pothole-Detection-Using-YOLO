# Running the Project

The files referenced below can be found in [this repository](https://github.com/CityofEdmonton/AI-Pothole-Detection-Using-YOLO).

1. Fork [this repo](https://github.com/AlexeyAB/darknet) into your Github account and clone it to your local machine.
0. Ensure that the [requirements](https://github.com/AlexeyAB/darknet#requirements) for this project are met. Visit the [Setup](/documentation/RUNNING_THE_PROJECT.md) page for information on setting up your environment.
0. Replace the [*Makefile*](https://github.com/AlexeyAB/darknet/blob/master/Makefile) with the one in the repository specified above or configure the file accordingly:

   - ```MK
     GPU=1 # (Line 1)
     ```
   - ```MK
     OPENCV=1 # (Line 4)
     ```
   - ```MK
     NVCC=/usr/local/cuda/bin/nvcc # Or the path to your NVCC - (Line 57)
     ```
   - ```MK
     LDFLAGS+= `pkg-config --libs opencv4` # (Line 79)
     COMMON+= `pkg-config --cflags opencv4` # (Line 80)
     ```

0. Run `make` in the root of the project.
0. If darknet has compiled successfully, running `./darknet` in the root of the project should return:

   ```
   usage: ./darknet <function>
   ```

0. Label the images in the potholes dataset. The dataset provided in [this link](http://bit.ly/2vZV8Bj) already has the images labelled. Each image should be accompanied by a text file that describes the bounding boxes of the pothole(s) in the image. You can learn more about the format of these labelling files [here](/documentation/PREPARING_THE_DATA.md).

    The directory holding your formatted data should look like this after creating the text files:

    ![Formatted Data](/media/images/formatted-data.png?raw=true)

0. Place the files `obj.data`, `obj.names`, `yolo-pothole-test.cfg`, and `yolo-pothole-train.cfg` in the `cfg/` directory of the project.
0. Import the formatted data with both the JPEG and text files into the ```data/Pothole/``` directory. This directory will have to be created.
0. Place the `train.txt` and `test.txt` files in the `data/Pothole/` directory as well.
0. Training requires a set of convolutional weights that can be downloaded from the official YOLO website [here](https://pjreddie.com/media/files/darknet19_448.conv.23). Place these weights in the root of the project.
0. Start the training by running:

    ```
    ./darknet detector train cfg/obj.data cfg/yolo-pothole-train.cfg darknet19_448.conv.23
    ```

    *Note*: The weights save every 100 iterations until the 1000th iteration, after which it saves every 1000 iterations. The program will also save the weights every 100 iterations as a `<training_config>_last.weights` file

    The output from the training should look something like this:

    ![Command Line Output](/media/images/command-line-output.png?raw=true)

0. To resume training using an existing weight, run:

    ```
    ./darknet detector train cfg/obj.data cfg/yolo-pothole-train.cfg <last_weight_file>
    ```

0. You should stop training when the mean average precision (mAP) is the **highest**. To get the mAP of a weight:

    ```
    ./darknet detector map cfg/obj.data cfg/yolo-pothole-train.cfg <weight_file>
    ```

    Read [here](https://github.com/AlexeyAB/darknet#when-should-i-stop-training) for more info.

0. Once the training is complete, you can test the detection by running:
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


Check out the [*Troubleshooting*](/documentation/troubleshooting/TROUBLESHOOTING.md) section if you run into any problems.