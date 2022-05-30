#!/usr/bin/env bash

clear
rm -rf log_reduced_perses.txt

root_path="./CI_Perses"
cd ${root_path}

rm -rf perses_test_original.java perses_test_reduced.java
rm -rf perses_test_original.java.*.orig PersesTempRoot_*
rm -rf tmp/ __pycache__/

mkdir -p tmp/
touch tmp/perses_result_original.txt
touch tmp/perses_result_reduced.txt

chmod u+x perses_test_script.sh
python3 run_perses.py

rm -rf perses_test_original.java perses_test_reduced.java
rm -rf perses_test_original.java.*.orig PersesTempRoot_*
rm -rf tmp/ __pycache__/

cd ../
