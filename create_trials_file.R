rm (list=ls())
blocks<-3
n.block<-120
trials<-data.frame(trial=seq(1,blocks*n.block),red=0,green=0,blue=0)
for (i in 1:blocks){
  trials[((i-1)*n.block+1):(n.block*i),i+1]<-1
}
distances<-rep(seq(0.01,.12,.01),10)
distances[1:length(distances)/2]<- -distances[1:length(distances)/2]
distances.rand<-sample(distances,120,replace=F)
distances.rand[1]<-runif(1)
distances.rand<-cumsum(distances.rand)
sum(which(distances.rand>1|distances.rand<0))

for (i in 1:blocks){
  if(i==1)col<-3
  if(i==2)col<-4
  if(i==3)col<-2
  trials[((i-1)*n.block+1):(n.block*i),col]<-distances.rand
}
write.csv("trials_sequential_dec_making.csv")