mkdir -p velocity_channels
for v in {-12..12}
do
   radmc3d image iline 6 incl 80 vkms $v
   mv image.out velocity_channels/image_${v}.out
done