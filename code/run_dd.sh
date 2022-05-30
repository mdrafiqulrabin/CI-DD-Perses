#!/usr/bin/env bash

clear
rm -rf log_reduced_dd.txt

root_path="./CI_DD"
cd ${root_path}

rm -rf tmp/ __pycache__/

python3 run_dd.py

rm -rf tmp/ __pycache__/

cd ../
