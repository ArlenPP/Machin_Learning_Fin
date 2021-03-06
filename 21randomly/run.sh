python train_and_test.py
cat train-data-raw test-data-raw > merge
shuf merge > rand_tmp
head -n 500 rand_tmp > train-data
tail -n +501 rand_tmp > test-data
cp train-data test-data ../../../output/21
cd ../../../output/21
svm-scale -s train-data-scale-info train-data > train-data.scale
svm-train -b 1 train-data.scale train-model
svm-scale -r train-data-scale-info test-data > test-data.scale
svm-predict -b 1 test-data.scale train-model test-result

