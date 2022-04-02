#!bin/sh

cd ../ex03
sh cleaner.sh
cd ../ex04

curl -s -o counter.py -G https://gist.githubusercontent.com/LinearBasis/ab987e24ddf7ec31c88435afb10fb8e1/raw/00507041efdd93c7d073f6e0932377aece149e0f/gistfile1.txt
python3 -m pip install --upgrade pip > /dev/null
pip3 install pandas > /dev/null
python3 counter.py > hh_uniq_positions.csv
rm counter.py