.libPaths(c(.libPaths(),"/home/tomabo/R/x86_64-pc-linux-gnu-library/3.5"))
seto<-subset(iris[1:50,],select=-Species)
versi<-subset(iris[51:100,],select=-Species)
virgi<-subset(iris[101:150,],select=-Species) 

seto.m<-apply(seto[1:45,],2,mean)
versi.m<-apply(versi[1:45,],2,mean)
virgi.m<-apply(virgi[1:45,],2,mean)
seto.v<-var(seto[1:45,])
versi.v<-var(versi[1:45,])
virgi.v<-var(virgi[1:45,],) 


mul <- function(x){
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

disc <- function(A,B){
    A.m<-apply(A[1:45,],2,mean)
    B.m<-apply(B[1:45,],2,mean)
    A.v<-var(A[1:45,])
    B.v<-var(B[1:45,])
    data <- rbind(A[1:45,],B[1:45,])
    data.v<- var(data)

    D1<-maha(A[46:50,],A.m,A.v)
    D2<-maha(A[46:50,],B.m,B.v) 

    a <- cbind(D1,D2)

    D1<-maha(B[46:50,],A.m,A.v)
    D2<-maha(B[46:50,],B.m,B.v) 

    b <- cbind(D1,D2)
    print(rbind(a,b))

    D1<-maha(A[46:50,],A.m,data.v)
    D2<-maha(A[46:50,],B.m,data.v) 

    a <- cbind(D1,D2)

    D1<-maha(B[46:50,],A.m,data.v)
    D2<-maha(B[46:50,],B.m,data.v) 

    b <- cbind(D1,D2)
    print(rbind(a,b))

}

disc(seto,versi)
disc(seto,virgi)
disc(versi,virgi)