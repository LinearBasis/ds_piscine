#!bin/bash


cd ../ex03
sh cleaner.sh
cd ../ex05

curl -s -o partitioner.py -G https://gist.githubusercontent.com/LinearBasis/c9db53068d2b54dc8e7fc8c30bc6fb78/raw/b1e0113852575f91086e72234c97faa8ed8052c4/gistfile1.txt
mkdir -p parted
python3 partitioner.py
rm partitioner.py