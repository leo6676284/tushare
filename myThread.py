# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 10:11:15 2018

@author: chris
"""

import threading
from time import ctime
#threadLock = threading.Lock()
class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.name = name
        self.args = args
        
    def run(self):
        print('开始执行',self.name,' 在：',ctime())
        #threadLock.acquire()# 获取锁，用于线程同步
        self.func(self.args)
        print(self.name,'结束于：',ctime())
        #threadLock.release()# 释放锁，开启下一个线程
        
    #def getResult(self):
        #return self.res