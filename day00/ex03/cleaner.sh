#!bin/sh

curl -s https://raw.githubusercontent.com/LinearBasis/ds_piscine/master/day00/cleaner.py > script.py
python3 -m pip install --upgrade pip > /dev/null
pip3 install pandas > /dev/null
python3 script.py > hh_positions.csv