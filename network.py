# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 17:54:35 2018

@author: zhongyh
"""
import numpy as np

def sigmod(z):
        return 1.0/(1+np.exp(-z))
    
class Network(object): 
    def __init__(self,sizes):
        self.num_layer = len(sizes)  #数值类型，数组长度即为多少层
        self.sizes = sizes
        self.biases = [np.random.randn(y,1) for y in sizes[:1]]#[:1]表示截取第一列。随机创建y列的矩阵，代表阈值
        self.weights = [np.random.randn(x,y) for x,y in zip(sizes[:-1],sizes[1:])]
        #生成每个神经元的权重值
    
    def feedforward(self,a):
        for b,w in zip(self.biases,self.weights):
            a = sigmod(np.dot(b,w)+b)   #激活函数
        return a 
    def SGD(self,training_data,epochs,mini_batch_size,eta,test_data = None):
        if test_data:
            n_test = len(test_data)
            n = len(training_data)
        for j in xrange(epochs):
            np.random.shuffle(trainng_data)
            mini_batches = [training_data[k:k+mini_batch_size] 
                            for k in xrange(0,n,mini_batch_size)]
            for mini_batch in mini_batches:
                
        
