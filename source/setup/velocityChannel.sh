mkdir -p velocity_channels
for i in {1..64}
do
   radmc3d image iline 6 incl 80 vkms $i
   mv image.out velocity_channels/image_$i.out
done
