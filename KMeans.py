#!/usr/bin/env python

#Author: Guotao Meng
#Email: kakaguotao@hotmail.com
#Time: May, 2016
#This is just for fun!!
#the input should be a N*M ".mat" file. Where M is the number of samples and N is the dimension of each sample.


import numpy
import random
import scipy.io as sio


#The number of classes
K=10

#Read the data
data = sio.loadmat('')
samples=data['data']
#samples=numpy.random.rand(1000,3)              #just random a set of data for testing
samplesum=samples.shape[0]
sampledim=samples.shape[1]
print samplesum,'samples, the dimension is',sampledim

kernals=numpy.random.rand(K,sampledim)



for index in xrange(100):
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
