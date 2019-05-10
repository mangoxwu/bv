#!/bin/bash
count=1
for file_name in `ls ./cif_file`; do
  #run cube
  echo "run ${count} cube..."  
  ./bin-static/softBV.x --gen-cube ./cif_file/${file_name} Li 1
  echo "finished ${count} cube"
  #run bv
  echo "run ${count} bv..."
  ./bin-static/softBV.x --gh ./cif_file/${file_name} ./cif_file/${file_name}.cube Li 1
  echo "finished ${count} bv"
  #get txt
  mv ./cif_file/${file_name}.gh.txt ./cif_txt
  #move finished cif
  mv ./cif_file/${file_name} ./finish_bv
  #remove cube file and gh file
  rm ./cif_file/${file_name}.cube
  rm ./cif_file/*.gh.*
  let count=count+1
done
