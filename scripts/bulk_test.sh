#~/bin/bash

# Place this file in the root of your darknet project folder

if [ $# -ne 2 ]
  then
    echo "Incorrect arguments supplied"
    echo "args: <weight file> <save folder/zip name>"
    exit
fi

weights_regex='^.+\.weights'
if ! [[ $1 =~ $weights_regex ]]
then
	echo "Not a weight file"
	exit
fi

mkdir bulk_test_tmp

# TODO: make this part variable (different file names and number of files)
for i in {1..18}
do
	./darknet detector test cfg/obj.data cfg/yolo-obj.cfg $1 data/Pothole_Test_Images/pothole$i.jpg -dont_show
	cp predictions.jpg bulk_test_tmp/results_$i.jpg
done

zip -r $2.zip bulk_test_tmp/
rm -rf bulk_test_tmp
