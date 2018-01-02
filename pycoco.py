from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
import os
pylab.rcParams['figure.figsize'] = (8.0, 10.0)

dataDir='.'
dataTypes=['train2017', 'val2017']

def generateData(dataType):
    annFile='{}/annotations/instances_{}.json'.format(dataDir,dataType)

    coco=COCO(annFile)
    #cats = coco.loadCats(coco.getCatIds())
    imgIds = coco.getImgIds()
    catIds = coco.getCatIds()
    annIds = coco.getAnnIds()

    print('TotalImgs: {0}, TotalCats: {1}, TotalAnns: {2}'.format(len(imgIds), len(catIds), len(annIds)))

    path = 'labels'
    if not os.path.exists(path):
        os.makedirs(path)
    path = 'labels/' + dataType
    if not os.path.exists(path):
        os.makedirs(path)

    for imgId in imgIds:
        imgs = coco.loadImgs(imgId)
        img = imgs[0]
        #print(imgId, img['width'], img['height'])
        annIds = coco.getAnnIds(imgIds=imgId)
        filename = img['file_name']
        # 000000249977
        filename = 'COCO_' + dataType + '_' + filename[0:12] + '.txt'
        fo = open(os.path.join(path, filename), 'w')
        for annId in annIds:
            anns = coco.loadAnns(annId)
            ann = anns[0]
            # [x, y, width, height]
            bbox = ann['bbox']
            bbox[0] /= img['width']
            bbox[1] /= img['height']
            bbox[2] /= img['width']
            bbox[3] /= img['height']


            stdout = '{0} {1} {2} {3} {4}\n'.format(
                ann['category_id'],
                round(ann['bbox'][0], 6),
                round(ann['bbox'][1], 6),
                round(ann['bbox'][2], 6),
                round(ann['bbox'][3], 6))
            line = fo.writelines(stdout)
        fo.close()

for datatype in dataTypes:
    print('Generate Data for', datatype)
    generateData(datatype)
#catIds = coco.getCatIds()
##print(catIds)
#for catId in catIds:
#    cat = coco.loadCats(catId)
#    imgIds = coco.getImgIds(catIds=[catId])
#    for imgId in imgIds:
#        #img = coco.loadImgs(imgIds[np.random.randint(0,len(imgIds))])[0]
#        annIds = coco.getAnnIds(imgIds=imgId)
#        anns = coco.loadAnns(annIds)
#        stdout = 'imgId: {0}, catId: {1}, catNms: {2}, Area: {3}, Bbox: {4}'
#        print(stdout.format(imgId, catId, cat[0]['name'], anns[0]['area'], anns[0]['bbox']))
#imgIds = coco.getImgIds(catIds=catIds);
#ids=[iid for iid in imgIds]
#print(ids)
#
#imgIds = coco.getImgIds(imgIds = [379520])
#img = coco.loadImgs(imgIds[np.random.randint(0,len(imgIds))])[0]
#
#annIds = coco.getAnnIds(imgIds=img['id'], catIds=catIds, iscrowd=None)
#anns = coco.loadAnns(annIds)

#print(anns)
#cats = coco.loadCats(coco.getCatIds())
#nms=[cat['name'] for cat in cats]
#print('COCO categories: \n{}\n'.format(' '.join(nms)))
#
#nms = set([cat['supercategory'] for cat in cats])
#print('COCO supercategories: \n{}'.format(' '.join(nms)))
#
#
#
#dataDir='.'
#dataType='val2017'
#annFile='{}/annotations/instances_{}.json'.format(dataDir,dataType)
#
#coco=COCO(annFile)
# get all images containing given categories, select one at random
#catIds = coco.getCatIds(catNms=['person','dog','skateboard']);
#imgIds = coco.getImgIds(catIds=catIds );
#imgIds = coco.getImgIds(imgIds = [324158])
#img = coco.loadImgs(imgIds[np.random.randint(0,len(imgIds))])[0]

# load and display image
# I = io.imread('%s/images/%s/%s'%(dataDir,dataType,img['file_name']))
# use url to load image
#I = io.imread(img['coco_url'])
#plt.axis('off')
#plt.imshow(I)
#plt.show()

# load and display instance annotations
#plt.imshow(I); plt.axis('off')
#annIds = coco.getAnnIds(imgIds=img['id'], catIds=catIds, iscrowd=None)
#anns = coco.loadAnns(annIds)
#coco.showAnns(anns)


# initialize COCO api for person keypoints annotations
#annFile = '{}/annotations/person_keypoints_{}.json'.format(dataDir,dataType)
#coco_kps=COCO(annFile)

# load and display keypoints annotations
#plt.imshow(I); plt.axis('off')
#ax = plt.gca()
#annIds = coco_kps.getAnnIds(imgIds=img['id'], catIds=catIds, iscrowd=None)
#anns = coco_kps.loadAnns(annIds)
#coco_kps.showAnns(anns)

# initialize COCO api for caption annotations
#annFile = '{}/annotations/captions_{}.json'.format(dataDir,dataType)
#coco_caps=COCO(annFile)


# load and display caption annotations
#annIds = coco_caps.getAnnIds(imgIds=img['id']);
#anns = coco_caps.loadAnns(annIds)
#coco_caps.showAnns(anns)
#plt.imshow(I); plt.axis('off'); plt.show()


