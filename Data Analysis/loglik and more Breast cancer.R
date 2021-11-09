install.packages("lmtest")
library(lmtest)

TeaTasting<-matrix(c(39, 30961, 63, 30937),
                   nrow = 2,
                   dimnames = list(Guess = c("Death", "Survive"),
                                   Group = c("Treatment", "Control")));TeaTasting

coso <- lm(Death~Treatment,data=TeaTasting)
logLik(TeaTasting)

x <- 1:5
lmx <- lm(x ~ 1)
summary(lmx)
logLik(lmx) # using print.logLik() method


Xs = c( 0.387, 0.723, 1.00, 1.52, 5.20, 9.54, 19.2, 30.1, 39.5 )
Ys = c( 0.241, 0.615, 1.00, 1.88, 11.9, 29.5, 84.0, 165.0, 248 )

Xs<-log(Xs)
Ys<-log(Ys)
m1<-lm(Ys~Xs)
summary(m1)
plot(m1)

