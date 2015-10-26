#!/usr/bin/python

import graphModule
import queueModule
import stackModule


def demo():
	g = graphModule.Graph()
	for i in range(6):
		g.addVertex(i)

	print g.vertList

	g.addEdge(0,1,5)
	g.addEdge(0,5,2)
	g.addEdge(1,2,4)
	g.addEdge(2,3,9)
	g.addEdge(3,4,7)
	g.addEdge(3,5,3)
	g.addEdge(4,0,1)
	g.addEdge(5,2,8)
	g.addEdge(5,2,1)

	for v in g:
		for w in v.getConnections():
			print ("(%s , %s)" % (v.getId(),w.getId()))

def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile,'r')
    # create buckets of words that differ by one letter
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)
    return g


def bfs(g,start):
  start.setDistance(0)
  start.setPred(None)
  vertQueue = Queue()
  vertQueue.enqueue(start)
  while (vertQueue.size() > 0):
    currentVert = vertQueue.dequeue()
    for nbr in currentVert.getConnections():
      if (nbr.getColor() == 'white'):
        nbr.setColor('gray')
        nbr.setDistance(currentVert.getDistance() + 1)
        nbr.setPred(currentVert)
        vertQueue.enqueue(nbr)
    currentVert.setColor('black')


if __name__ == '__main__':
	demo()
