#!/bin/bash

for filename in x06 x07 x08 x09
do
    echo "processing $filename ..."
    ./dump_vt_reports.sh $filename > vt_reports_$filename.txt
    sleep 2
done
