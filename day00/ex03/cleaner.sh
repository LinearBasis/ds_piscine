#!bin/sh

curl -s https://raw.githubusercontent.com/LinearBasis/ds_piscine/master/day00/cleaner.py > cleaner.py
python3 -m pip install --upgrade pip > /dev/null
pip3 install pandas > /dev/null
python3 cleaner.py > hh_positions.csv
rm cleaner.py