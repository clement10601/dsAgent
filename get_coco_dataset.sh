#!/bin/bash
pip install -r requirements.txt
grep -q -F 'export WORKON_HOME=~/.virtualenvs' ~/.bashrc || echo 'export WORKON_HOME=~/.virtualenvs' >> ~/.bashrc
grep -q -F 'source /usr/bin/virtualenvwrapper.sh' ~/.bashrc || echo 'source /usr/bin/virtualenvwrapper.sh' >> ~/.bashrc
source ~/.bashrc
mkvirtualenv datasetAgent

# Clone COCO API
git https://github.com/clement10601/cocoapi.git
cd cocoapi
pip install -r requirements.txt
cd cocoapi/Python
make && make install
cd ../..
mkdir images
cd images

# Download Images
wget -c http://images.cocodataset.org/zips/train2017.zip
wget -c http://images.cocodataset.org/zips/val2017.zip
wget -c http://images.cocodataset.org/zips/test2017.zip
# Unzip
unzip -q train2017.zip
unzip -q val2017.zip
unzip -q test2017.zip
# rm -rf *.zip
cd train2017
for f in *.jpg; do mv "$f" "COCO_train2017_$f"; done
cd ..
cd val2017
for f in *.jpg; do mv "$f" "COCO_val2017_$f"; done
cd ..
cd test2017
for f in *.jpg; do mv "$f" "COCO_test2017_$f"; done
cd ..
# back to root
cd ..
mkdir exports
find images/train2017/ -exec readlink -f {} \; >  exports/train2017.txt
find images/val2017/ -exec readlink -f {} \; >  exports/val2017.txt
find images/test2017/ -exec readlink -f {} \; >  exports/test2017.txt

# Download COCO Metadata
cd exports
wget -c http://images.cocodataset.org/annotations/annotations_trainval2017.zip
wget -c http://images.cocodataset.org/annotations/stuff_annotations_trainval2017.zip
unzip -q annotations_trainval2017.zip
unzip -q stuff_annotations_trainval2017.zip

mv annotations/ ..
cd ..
python pycoco.py
