cd ../../../output/60
svm-scale -s train-data-scale-info train-data > train-data.scale
svm-train -s 3 -b 1 train-data.scale train-model
svm-scale -r train-data-scale-info test-data > test-data.scale
svm-predict -b 1 test-data.scale train-model test-result

