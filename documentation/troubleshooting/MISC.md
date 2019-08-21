## Renaming files

**Problem:**

Transferring JPEG files to the VM from the local machine results in the .jpg file extensions to be changed to .JPG, which prevents the images from being properly read by the program.

Run this command while in the directory of the image files:
```
rename 's/.JPG/.jpg/' *.JPG
```
Solution obtained from [this site](https://www.maketecheasier.com/rename-files-in-linux/).