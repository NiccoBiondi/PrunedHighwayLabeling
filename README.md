# PrunedHighwayLabeling

Reimplementation of "Fast Shortest-path Distance Queries on Road Networks by Pruned Highway Labeling" by Takuya Akiba, 
Yoichi Iwata, Ken-ichi Kawarabayashi, Yuki Kawata. 


## Abstract

We propose a new labeling method for shortest-path and distance queries on road networks. We present a new
framework (i.e. data structure and query algorithm) referred to as highway-based labelings and a preprocessing
algorithm for it named pruned highway labeling. Our proposed method has several appealing fea-
tures from different aspects in the literature. Indeed, we take advantages of theoretical analysis of the seminal re-
sult by Thorup for distance oracles, more detailed structures of real road networks, and the pruned labeling al-
gorithm that conducts pruned Dijkstra’s algorithm. The experimental results show that the proposed
method is comparable to the previous state-of-the-art labeling method in both query time and in data size,
while our main improvement is that the preprocessing time is much faster.


