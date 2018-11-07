.libPaths(c(.libPaths(),"/home/tomabo/R/x86_64-pc-linux-gnu-library/3.5"))
seto<-subset(iris[1:50,],select=-Species)
virgi<-subset(iris[101:150,],select=-Species) 

seto.m<-apply(seto[1:45,],2,mean)
virgi.m<-apply(virgi[1:45,],2,mean)
seto.v<-var(seto[1:45,])
virgi.v<-var(virgi[1:45,],) 

mul <- function(x){
    print(x)
    x[1:4] %*% x[5:8]
}

maha <- function(x,y,S){
    Sinv <- solve(S)
    sub <- function(x){
        x - y
    }
    d <- t(as.matrix(apply(x,1,sub)))
    k <- Sinv %*% t(d)
    k <- t(k)
    apply(cbind(d,k), 1, mul)
}

D1<-maha(seto[46:50,],seto.m,seto.v)
D2<-maha(seto[46:50,],virgi.m,virgi.v) 

print(cbind(D1,D2))

#46 2.1752192 137.9376
#47 2.8163645 173.8815
#48 1.4346178 142.1425
#49 1.2398930 182.5972
#50 0.4700029 160.2070