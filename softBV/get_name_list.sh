#!/bin/bash
for file_name in `ls ./finish_bv`; do
  echo $file_name >> name_list.txt
done
