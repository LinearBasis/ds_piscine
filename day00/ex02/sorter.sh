#!bin/sh

cd ../ex01
sh json_to_csv.sh
cd ../ex02

head -n 1 > hh_sorted.csv < ../ex01/hh.csv
tail -n +2 < ../ex01/hh.csv | sort -t "," -k2,2 -k1,1 >> hh_sorted.csv
