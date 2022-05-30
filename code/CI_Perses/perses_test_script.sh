#!/usr/bin/env bash

set -o pipefail
set -o nounset

root_path="/scratch/rabin/deployment/root-all/CI-DD-Perses/code/CI_Perses"
result_original=${root_path}/tmp/perses_result_original.txt
result_reduced=${root_path}/tmp/perses_result_reduced.txt

rm -rf ${root_path}/perses_test_original.java.*.orig
echo "" > ${result_reduced}

python3 ${root_path}/perses_test_script.py

orig=$(cat ${result_original})
pred=$(cat ${result_reduced})

if [[ "${pred}" == "${orig}" ]]; then
  exit 0
else
  exit 1
fi
