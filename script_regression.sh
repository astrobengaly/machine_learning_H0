# !/bin/sh
python H0_regression.py 100 0.008 20 EXT
python H0_regression.py 100 0.008 30 EXT
python H0_regression.py 100 0.008 50 EXT
python H0_regression.py 100 0.008 80 EXT

python H0_regression.py 100 0.008 20 ANN
python H0_regression.py 100 0.008 30 ANN
python H0_regression.py 100 0.008 50 ANN
python H0_regression.py 100 0.008 80 ANN

python H0_regression.py 100 0.008 20 XGB
python H0_regression.py 100 0.008 30 XGB
python H0_regression.py 100 0.008 50 XGB
python H0_regression.py 100 0.008 80 XGB

python H0_regression.py 100 0.008 20 SVM
python H0_regression.py 100 0.008 30 SVM
python H0_regression.py 100 0.008 50 SVM
python H0_regression.py 100 0.008 80 SVM
