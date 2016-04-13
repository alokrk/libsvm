# libsvm
IoT Homework 4

csv - have converted present and absent to 1 and -1 in initial data set

otherwise decent results for 1000 random samples


1. Converted all present and absent values to 1 and -1 in CSV datasets
2. Converted combined data set to libsvm format
3. Train model on complete data set
4. Prediction done on test data set
5. Test has initial value 1 for all 1000 entries.(as suggested in README for libsvm/python)
6. Predicted values are converted to present/absent and stored in CSV
7. Create executable

##Work remaining

finalise parameters - current set to param = svm_parameter('-s 0 -t 2 -c 2')

create executable - going thru PyInstaller
