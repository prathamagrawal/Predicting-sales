import pandas as pd
import numpy as np

categories=pd.read_csv('./data/item_categories.csv')
items=pd.read_csv('./data/items.csv')
shops=pd.read_csv('./data/shops.csv')
sales_train=pd.read_csv('./data/sales_train.csv')


print("Unique Categories: "+str(len(categories['item_category_name'].unique())))
categoriesd=categories.set_index('item_category_id').T.to_dict('list')



item_category_names=[]
for ri,rd in items.iterrows():
    item_category_names.append(categoriesd[rd['item_category_id']])
items['item_category_names']=item_category_names