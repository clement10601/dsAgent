#!/bin/bash
pip install -r requirements.txt
p=`which virtualenvwrapper.sh`
echo "$p"
echo "========================"
echo "Setup python environment"
echo "========================"
grep -q -F 'export WORKON_HOME=~/.virtualenvs' ~/.bashrc || echo 'export WORKON_HOME=~/.virtualenvs' >> ~/.bashrc
grep -q -F 'source $p' ~/.bashrc || echo 'source /usr/bin/virtualenvwrapper.sh' >> ~/.bashrc
source ~/.bashrc
source `which virtualenvwrapper.sh`
mkvirtualenv datasetAgent
which python

# Clone COCO API
git clone https://github.com/clement10601/cocoapi.git
cd cocoapi
which pip
pip install -r requirements.txt
cd PythonAPI
make && make install

echo "====================================="
echo "Download and extract images from COCO"
echo "====================================="
cd ../..
mkdir images
mkdir downloads
cd downloads
# Download Images
wget -c http://images.cocodataset.org/zips/train2017.zip
wget -c http://images.cocodataset.org/zips/val2017.zip
wget -c http://images.cocodataset.org/zips/test2017.zip
# Unzip
unzip -q train2017.zip
unzip -q val2017.zip
unzip -q test2017.zip
# rm -rf *.zip
echo "=================="
echo "Changing file name"
echo "=================="
cd train2017
for f in *.jpg; do mv "$f" "COCO_train2017_$f"; done
cd ..
cd val2017
for f in *.jpg; do mv "$f" "COCO_val2017_$f"; done
cd ..
cd test2017
for f in *.jpg; do mv "$f" "COCO_test2017_$f"; done
cd ..
echo "============================"
echo "Moving data to images folder"
echo "============================"
mv train2017 ../images
mv val2017 ../images
mv test2017 ../images
# back to root
cd ..

echo "======================================="
echo "Exporting absolute path list for images"
echo "======================================="
mkdir exports
find images/train2017/ -exec readlink -f {} \; >  exports/train2017.txt
find images/val2017/ -exec readlink -f {} \; >  exports/val2017.txt
find images/test2017/ -exec readlink -f {} \; >  exports/test2017.txt
# Download COCO Metadata
cd downloads
echo "=============================="
echo "Download and unzip annotations"
echo "=============================="
wget -c http://images.cocodataset.org/annotations/annotations_trainval2017.zip
wget -c http://images.cocodataset.org/annotations/stuff_annotations_trainval2017.zip
unzip -q annotations_trainval2017.zip
unzip -q stuff_annotations_trainval2017.zip

mv annotations/ ..
cd ..

echo "============================================================"
echo "Run Python Script to generate image information with cocoAPI"
echo "============================================================"

python pycoco.py
