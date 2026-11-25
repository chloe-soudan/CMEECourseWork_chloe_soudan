# !/bin/bash
# Chloe Soudan
# Script: tiff2_png.sh
# Desc: Converting TIFF images to PNG format
# Date: Oct 2026

# had to install ImageMagick (contains the Converting command) using the following command in terminal:
#  sudo apt install imagemagick

for filename in *.tif
do
    echo "Converting $filename"
    convert "$filename" "$(basename "$filename" .tif).png"
done

# ran the script in the terminal (from CMEECourseWork directory) by using following commands:
# project_root=$PWD
# script_path=$project_root/code/tiff2_png.sh
# mkdir "$shell_practice/images"
# cd "$shell_practice/images"
# pwd

# created a tif image: convert -size 100x100 xc:blue test.tif
# ran the script in the terminal (from CMEECourseWork directory) by using following command:
# bash ~/Documents/CMEECourseWork/code/tiff2_png.sh
# checked if it worked by using ls in the terminal. Output for that  was test.tif (the test image)
# and test.png (the converted tif image). The conversion was thus sucessful.
