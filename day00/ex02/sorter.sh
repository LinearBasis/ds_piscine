#!bin/sh


head -n 1 > hh_sorted.csv < ../ex01/hh.csv
tail -n 20 < ../ex01/hh.csv | sort -t "," -k2,2 -k1 >> hh_sorted.csv
