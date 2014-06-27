#!/bin/sh

echo "beginning performance test";

# test how long it takes for transferDomains.py to run
echo "testing to see how long transferDomains.py takes to run"

time1=`date +%N`
/usr/bin/python ../src/transferDomains.py
if [ $? -eq 0 ]; then
    time2=`date +%N`
fi

diff_time=$(((time2 - time1) / 1000000))

echo "time it took (milliseconds) for transferDomains.py to run:" $diff_time

# test how long it takes for topDomains.py to run
echo "testing to see how long topDomains.py takes to run"

time3=`date +%N`

/usr/bin/python ../src/topDomains.py
if [ $? -eq 0 ]; then
    time4=`date +%N`
fi

diff_time=$(((time4 - time3) / 1000000))

echo "time it took (milliseconds) for topDomains.py to run:" $diff_time
