#!bin/sh

cd ../ex02
sh sorter.sh
cd ../ex03

curl -s -o cleaner.py -G https://gist.githubusercontent.com/LinearBasis/d1f96ab3a5c7338cc32498b488a3d7dd/raw/e75c229ce0d165883e651f0a3119629f3176d22d/gistfile1.txt
python3 -m pip install --upgrade pip > /dev/null
pip3 install pandas > /dev/null
python3 cleaner.py > hh_positions.csv
rm cleaner.py