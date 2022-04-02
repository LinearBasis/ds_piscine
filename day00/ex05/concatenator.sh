#!bin/bash


dir="./parted"

file1=($(ls $dir));
files=$(ls $dir);

head -n 1 < ./parted/$file1 > hh_positions.csv

for file in $files
do
tail -n +2 ./parted/$file >> hh_positions.csv
done;

