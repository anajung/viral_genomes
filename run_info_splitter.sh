#!/bin/bash

# Run Info_splitter 

for i in *.snpEFF.ann.tsv; do

    F='basename $i .snpEFF.ann.tsv';

    python3 /home/ajung/info_splitter.py $i "$F".snpEFF.ann.split.xlsx;

done