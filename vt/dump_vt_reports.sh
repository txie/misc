#!/bin/bash

filename="$1"
START=$(date +%s);
cat $filename | while read LINE
do
#echo "dumping VT result for $LINE"
python pe_vt_verif.py $LINE
done
END=$(date +%s);
echo $((END-START)) | awk '{print int($1/60)":"int($1%60)}'
