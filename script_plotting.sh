#!/bin/sh
python results_plotting2.py EXT true H0
python results_plotting2.py ANN true H0
python results_plotting2.py XGB true H0
python results_plotting2.py SVM true H0

python results_plotting2.py EXT true bvt
python results_plotting2.py ANN true bvt
python results_plotting2.py XGB true bvt
python results_plotting2.py SVM true bvt
