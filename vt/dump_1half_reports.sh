#!/bin/bash

for filename in x01 x02 x03 x04
do
    echo "processing $filename ..."
    ./dump_vt_reports.sh $filename > vt_reports_$filename.txt
    sleep 2
done
