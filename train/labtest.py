from train import train_test
import pandas as pd
import csv

ACC, RECALL, PREC, F1 = train_test(max_depth=7, learning_rate=0.5, objective='multi:softprob', booster='gbtree', n_jobs=-1, min_child_weight=6, gamma=0.1, subsample=0.8, colsample_bytree=0.8)
print(ACC, RECALL, PREC, F1)