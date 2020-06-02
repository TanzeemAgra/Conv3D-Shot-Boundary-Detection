#!/usr/bin/env python3
# -*- coding: utf-8 -*-

############################ VISUALISATION OF PREDICTION #####################
from visualizer import visualizer

video = 'test_data/final.mp4'
csv = 'test_data/final.csv'

"""
Instructions:
    k: stop or resume panel video
    n: next frame 
    q: quit video 
"""
#compare prediction from the Conv3D model and cineast
comp = visualizer(10,video, csv)
comp.compare_prediction('test_data/predict.csv','test_data/cineast.csv')

#prediction from model
# conv = datagen(10,video, 'test_data/predict.csv')
# conv.eval_csv()

# #prediction from cineast
# cin = datagen(10,video, 'test_data/cineast.csv')
# cin.eval_csv()

# #true cuts as reference
# ref = datagen(10,video, csv)
# ref.eval_csv()


