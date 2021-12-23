#!/bin/bash


#sed -n '/short test summary info/,$p' test.log > log1
#grep ^"FAILED" log1|awk -F "::" '{print $3}'|awk -F "-" '{print $1}'|awk -F "test_"  '{print $2}' > log2
grep ^"FAILED" log1|awk -F "/" '{print $3}' > log3


