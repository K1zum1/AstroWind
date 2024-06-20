rm ./velocity_channels/image*.out
for (( i=$1; i<=$2; ++i ))
do
  echo $i
  radmc3d image iline 6 incl 80 vkms $i
  mv image.out velocity_channels/image_${i}.out
done
