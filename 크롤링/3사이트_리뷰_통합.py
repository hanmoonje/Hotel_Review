# -*- coding: utf-8 -*-
"""3사이트 리뷰 통합.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eGP7TwzFs8mi7qT5fTe3r_RpN_BsGDbt
"""

import pandas as pd

df_yanolja = pd.read_csv('야놀자.csv')
df_daily = pd.read_csv('데일리호텔.csv')
df_yogi = pd.read_csv('여기어때.csv')

df_hotel = pd.concat([df_yogi, df_yanolja, df_daily],ignore_index = True)
df_hotel.sort_values(['addr'], inplace=True)

df_hotel.reset_index().drop('index', axis=1).drop('score', axis=1)

hotel_addr = df_hotel['addr']
address = [] 
for addr in hotel_addr:
  if( addr not in address):
    address.append(addr)

address

hotel_comment = df_hotel[df_hotel['addr']== address[0]].drop_duplicates(['review'],ignore_index = True, keep='first')

for i in range(1,len(address)):
  bb = df_hotel[df_hotel['addr']==address[i]].drop_duplicates(['review'], keep='first')
  hotel_comment = pd.concat([hotel_comment,bb])
hotel_comment

hotel_comment = hotel_comment.reset_index().drop(columns = 'index').drop(columns='score', axis=1)
hotel_comment

df = hotel_comment.to_csv('리뷰통합.csv', encoding= 'utf-8-sig')