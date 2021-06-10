#!/bin/bash

# Run Info_splitter 

for i in *.snpEFF.ann.tsv; do

    F=${i%.tsv};
    echo "$F";

    python3 /Users/anajung/Documents/HandleyLab_Code/info_splitter.py $i "$F".split.xlsx;

done