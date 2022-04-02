import os
import numpy as np
import pandas as pd


os.system('unzip ./tissue-segment.zip')
os.system('mkdir ./dataset/')
os.system('mkdir ./dataset/scans/')
os.system('mkdir ./dataset/masks/')
metlst = []
for path in os.listdir('./tissue-segment'):
    if '_mask' not in path:
        respath = path.replace(' ','')
        os.system('mv ./tissue-segment/"%s" ./dataset/scans/%s'%(path, respath))
        resmaskpath = respath.split('.')[0]+'_mask.jpg'
        maskpath = path.split('.')[0]+'_mask.jpg'
        os.system('mv ./tissue-segment/"%s" ./dataset/masks/%s'%(maskpath, resmaskpath))
        metlst.append([respath,resmaskpath])
        print(path, maskpath)
metadata = pd.DataFrame(np.asarray(metlst), columns=['scan','mask'])
metadata.to_csv('./dataset/metadata.csv', sep=',')

