#!/usr/bin/python

from __future__ import division
from scipy.io.arff import loadarff
import arff


#TODO
# Check Rounding of Naive from Manav
#

dataset=()
# Stores the list of features
features = []
# Contains data items in key / value format
data = []
data_list=[]
# frequency of each item
frequency = []  # Not needed for now
# Number of unique types each feature can take
feature_freq = {}
feature_freq_list = []
feature_list=[]
test_file="abc"
training_file="abc"
param="b"

def build_features(dataset):
    """
    Construct the list of features from the test file
    """
    for x in dataset[1]:
        features.append(x)

def print_features(features):
    """
    Print the list of features from the test file
    """
    for i in range(len(features)):
        print features[i]

# Construct from the test data.
def build_feature_vector(dataset):
    """
    Construct the dictionary of data from the test file
    """
    for data_line in dataset[0]:
        dic = {}
        lst = []
        for i in range(len(data_line)):
            dic[features[i]]=data_line[i]
            lst.append(data_line[i])
        data.append(dic)
        data_list.append(lst)

def build_feature_frequency():
    """
    Construct the frequency from the attributes, not data
    This will have the unique entries each feature can take
    """
    liac_parse=arff.load(open('lymph_train.arff','rb'))
    for k in liac_parse.keys():
        if k == 'attributes':
            for x in liac_parse[k]:
                feature_list.append(x[1])
                feature_freq[x[0]]=len(x[1])
                feature_freq_list.append(len(x[1]))

def compute_cond_probability(i,a,b):
    """
    Naive Bayes
    """
    j=0
    num=0.0
    den=0.0
    for x in range(len(data)):
        if data[x]['class']==b:
            den+=1
            if data_list[j][i]==a:
                num+=1
        j+=1
    num+=1
    den=den+feature_freq_list[i]
    return num/den

def compute_probability(a):
    """
    Compute the probability of the class in Naive Bayes
    """
    num=0.0
    den=0.0
    for x in range(len(data)):
        if data[x]['class']==a:
            num+=1.0
        den+=1.0
    num+=1.0
    den=den+2.0
    prob=num/den
    return prob

def preprocessing_background_work(dataset):
    build_features(dataset)
    build_feature_vector(dataset)
    build_feature_frequency()


def get_other(a):
    i=0
    x=0
    y=0
    for feature_name in feature_list[len(feature_list)-1]:
        if i==0:
            x=feature_name
            i+=1
        else:
            y=feature_name
    if a==x:
        return y
    else:
        return x

def compute_naive(test_file):
    """
    Main module to compute BN
    """
    count=0
    test_file=arff.load(open(test_file,'rb'))
    for x in test_file['data']:
        pxi=1.0
        pxj=1.0
        for i in range(len(x)-1):
            prob_xi=compute_cond_probability(i,x[i],x[len(x)-1])
            pxi=pxi*prob_xi
            prob_xj=compute_cond_probability(i,x[i],get_other(x[len(x)-1]))
            pxj=pxj*prob_xj
        n1=pxi*compute_probability(x[len(x)-1])
        n2=pxj*compute_probability(get_other(x[len(x)-1]))
        if n1>n2:
            print x[len(x)-1],x[len(x)-1],n1/(n1+n2)
            count+=1
        else:
            print get_other(x[len(x)-1]),x[len(x)-1],n2/(n1+n2)

    print "\n",count
    print ""

def main():
    """
    Main starting function of the code
    """

    training_file,test_file,param="lymph_train.arff","lymph_test.arff","t"
    dataset = loadarff(training_file)
    preprocessing_background_work(dataset)
    compute_naive(test_file)

if __name__ == '__main__':
    main()
