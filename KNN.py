#-*- coding:UTF-8 -*-
import numpy as np
import math

class kNeighborsClassifier():
    """
        parameters:
        ----------
        x: the sample of input
        y: the label of x
        test: the predict data
        neighbors: number of neighbors;
    """
    def __init__(self,x,y,test,neighbors):
        self.x = x
        self.y = y
        self.test = test
        self.neighbors = neighbors
        self.ans = []

    def classify(self):
        for j in self.test:
            for i in self.x:
                distance = self.euclidianDistance(i,j)
                i.append(distance)
        [a.append(b) for a,b in zip(self.x,self.y)]

    def euclidianDistance(self,arr1,arr2):
        arr1 = list(arr1)
        arr2 = list(arr2)
        return math.sqrt(sum([(a-b)**2 for a,b in zip(arr1,arr2)]))

    def predict(self):
        predict_result = []
        for j in range(len(self.test),0,-1):
            self.x = sorted(self.x,key = lambda x:x[-1-j])
            for i in range(self.neighbors):
                self.ans.append(self.x[i][-1])
            predict_result.append(self.max_list())
            self.ans = []
        return predict_result

    def max_list(self):
        max_count = 0
        for i in self.ans:
            count = self.ans.count(i)
            if count>max_count:
                max_count = count
                predict_c = i
        return  predict_c

if __name__ == "__main__":
    x = [[0],[1],[2],[3]]
    y = [0,0,1,1]
    test = [[1.9],[0.6]]
    c = kNeighborsClassifier(x,y,test,2)
    c.classify()
    print(c.predict())