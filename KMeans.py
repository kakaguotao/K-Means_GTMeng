#!/usr/bin/env python

#Author: Guotao Meng
#Email: kakaguotao@hotmail.com
#Time: May, 2016
#This is for fun!! Just for practice!
#the input should be a N*M ".mat" file. Where M is the number of samples and N is the dimension of each sample.


import numpy
import random
import scipy.io as sio
import json


#The number is classes
K=3

#Read the data
data = sio.loadmat('')
samples=data['data']
'''
#just random a set of data for testing
mean1=(0,0,0)
mean2=(3,3,3)
mean3=(-3,-3,-3)
cov = [[0,0.5,1], [1,0.5, 0],[0.5,1,0]]
sample1=numpy.random.multivariate_normal(mean1,cov,500)
sample2=numpy.random.multivariate_normal(mean2,cov,500)
sample3=numpy.random.multivariate_normal(mean3,cov,500)
samples=numpy.concatenate((sample1,sample2,sample2),axis=0)
print samples.shape

'''
samplesum=samples.shape[0]
sampledim=samples.shape[1]
print samplesum,'samples, the dimension is',sampledim

samplemax=samples.max()
samplemin=samples.min()
samplemean=samples.mean()


kernals=0.5*(samplemax-samplemin)*numpy.random.rand(K,sampledim)-samplemean



for index in xrange(50):
    clusters=[]
    for k in xrange(K):
        clusters.append([])
    for sample in xrange(len(samples)):
        kernaldis=[]
        for KER in kernals:
            dis=numpy.sum((samples[sample]-KER)**2)
            kernaldis.append(dis)
        clusters[kernaldis.index(min(kernaldis))].append(samples[sample])
    for k in xrange(K):
        clu=numpy.array(clusters[k])
        clu=clu.mean(axis=0)
        kernals[k]=clu
    print 'index:',index
    print kernals
    print '----------------------------------------------------'

print 'completed!'
print kernals

#output the result
result=[]
for sample in xrange(len(samples)):
    kernaldis=[]
    for KER in kernals:
        dis=numpy.sum((samples[sample]-KER)**2)
        kernaldis.append(dis)
    result.append(kernaldis.index(min(kernaldis)))
print 'The result is:'
print result
