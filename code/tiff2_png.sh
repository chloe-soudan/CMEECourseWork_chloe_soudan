# !/bin/bash
# Chloe Soudan
# Script: tiff2_png.sh
# Desc: Converting TIFF images to PNG format
# Date: Oct 2026

# had to install ImageMagick (contains the Converting command) using the following command in terminal:
#  sudo apt install imagemagick

for filename in "$1"/images/*.tif 
do
    echo "Converting $filename"
    convert "$filename" "${filename%.tif}.png"
done



# ran ny creating a temporary test image in the temporary images directory using the following command in the terminal:
# mkdir "$shell_practice/images"
# convert -size 100x100 xc:blue "$shell_practice/images/test.tif"
# Then ran the script from the project root using:  bash code/tiff2_png.sh "$shell_practice"`
# checked if it worked by using ls in the terminal. Output for that  was test.tif (the test image)
# and test.png (the converted tif image). The conversion was thus sucessful.

