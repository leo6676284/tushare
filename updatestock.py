# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 10:04:59 2018

@author: chris
"""
"""
import tushare as ts #引入库
import time
import threading
updatetime = time.strftime('%Y-%m-%d',time.localtime(float(time.time())))
stock_info=ts.get_stock_basics()#获取全部名称
arr = []
for i in stock_info.index: #把名称放入数组
    arr.append(i)
len(arr)
for i in arr: #下载
    try:
        print('正在更新%s数据...'%i)
        data=ts.get_hist_data(i,start=updatetime,end=updatetime) #获取数据
        data.to_csv('D:/stockdata/%s.csv'%i,mode='a',header=0)#把数据存入csv文件
        
    except:
        print('%s股票数据不存在！'%i)#抛出异常
print('更新完成！')
"""
from sqlalchemy import create_engine
import pandas as pd
from sigmoid.myThread import MyThread
from time import ctime,sleep
import tushare as ts #引入库
from queue import Queue
import threading
import time
'''
df = pd.read_csv('D:/stockdata/600291.csv')
engine = create_engine('mysql://root:''@127.0.0.1/stock_data?charset=utf8')
df.to_sql('sh600291',engine,if_exists='append')
ts.get_hist_data()
data=ts.get_hist_data('600291') #获取数据
#print(data)
#engine = create_engine('mysql://root:''@127.0.0.1/stock_data?charset=utf8')
#data.to_sql('sh600291',engine,if_exists='replace',index=False)
#data.to_sql('sh600291',engine,if_exists='replace',index=False)
#print(arr.get())
'''
def download(arr):
    #updatetime1 = time.strftime('%Y-%m-%d',time.localtime(float(time.time())))
    while not arr.empty():
        i =  arr.get()#
        try:
            print(ctime(),'正在更新%s数据,数据还有%s条...'%(i,arr.qsize()))
            data=ts.get_hist_data(i) #获取数据
            #data.to_csv('D:/stockdata/%s.csv'%i,mode='a',header=0)#把数据存入csv文件
            data.to_csv('D:/stockdata/%s.csv'%i)#把数据存入csv文件
            #data = pd.read_csv('D:/stockdata/%s.csv'%i)#读取csv文件
            #engine = create_engine('mysql://root:''@127.0.0.1/stock_data?charset=utf8')#连接数据库
            #data.to_sql('%s'%i,engine,if_exists='replace')#创建数据表并存入数据库
            #sleep(2)
        except:
            print(ctime(),'%s数据不存在！'%i)#抛出异常
            #arr.put(i)
    #else:
        #print('更新完成！')
#download(arr)    
def main():
       
    #多线程
    print('多线程模式')
    a = time.time()
    stock_info=ts.get_stock_basics()#获取全部名称
    arr = Queue()
    for i in stock_info.index: #把名称放入队列
        arr.put(i)
    
    threads = []
    for i in range(10): #创建并开启10个线程
        thread = MyThread(download,arr,'thread'+str(i+1))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()      
    print('下载结束,总共花费%s分钟' %((time.time()-a)/60))
    
#if    
main()