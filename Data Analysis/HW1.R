LogPlanetMass = c(-0.31471074,  1.01160091,  0.58778666,  0.46373402, -0.01005034,
                          0.66577598, -1.30933332, -0.37106368, -0.40047757, -0.27443685,
                          1.30833282, -0.46840491, -1.91054301,  0.16551444,  0.78845736,
                          -2.43041846,  0.21511138,  2.29253476, -2.05330607, -0.43078292,
                          -4.98204784, -0.48776035, -1.69298258, -0.08664781, -2.28278247,
                          3.30431931, -3.27016912,  1.14644962, -3.10109279, -0.61248928)

LogPlanetRadius = c( 0.32497786,  0.34712953,  0.14842001,  0.45742485,  0.1889661 ,
                             0.06952606,  0.07696104,  0.3220835 ,  0.42918163, -0.05762911,
                             0.40546511,  0.19227189, -0.16251893,  0.45107562,  0.3825376 ,
                             -0.82098055,  0.10436002,  0.0295588 , -1.17921515,  0.55961579,
                             -2.49253568,  0.11243543, -0.72037861,  0.36464311, -0.46203546,
                             0.13976194, -2.70306266,  0.12221763, -2.41374014,  0.35627486)

LogPlanetOrbit = c(-2.63108916, -3.89026151, -3.13752628, -2.99633245, -3.12356565,
                           -2.33924908, -2.8507665 , -3.04765735, -2.84043939, -3.19004544,
                           -3.14655516, -3.13729584, -3.09887303, -3.09004295, -3.16296819,
                           -2.3227878 , -3.77661837, -2.52572864, -4.13641734, -3.05018846,
                           -2.40141145, -3.14795149, -0.40361682, -3.2148838 , -2.74575207,
                           -3.70014265, -1.98923527, -3.35440922, -1.96897409, -2.99773428)

StarMetallicity = c( 0.11 , -0.002, -0.4  ,  0.01 ,  0.15 ,  0.22 , -0.01 ,  0.02 ,
                             -0.06 , -0.127,  0.   ,  0.12 ,  0.27 ,  0.09 , -0.077,  0.3  ,
                             0.14 , -0.07 ,  0.19 , -0.02 ,  0.12 ,  0.251,  0.07 ,  0.16 ,
                             0.19 ,  0.052, -0.32 ,  0.258,  0.02 , -0.17 )

LogStarMass = c( 0.27002714,  0.19144646, -0.16369609,  0.44468582,  0.19227189,
                         0.01291623,  0.0861777 ,  0.1380213 ,  0.49469624, -0.43850496,
                         0.54232429,  0.02469261,  0.07325046,  0.42133846,  0.2592826 ,
                         -0.09431068, -0.24846136, -0.12783337, -0.07364654,  0.26159474,
                         0.07603469, -0.07796154,  0.09440068,  0.07510747,  0.17395331,
                         0.28893129, -0.21940057,  0.02566775, -0.09211529,  0.16551444)

LogStarAge = c( 1.58103844,  1.06471074,  2.39789527,  0.72754861,  0.55675456,
                        1.91692261,  1.64865863,  1.38629436,  0.77472717,  1.36097655,
                        0.        ,  1.80828877,  1.7837273 ,  0.64185389,  0.69813472,
                        2.39789527, -0.35667494,  1.79175947,  1.90210753,  1.39624469,
                        1.84054963,  2.19722458,  1.89761986,  1.84054963,  0.74193734,
                        0.55961579,  1.79175947,  0.91629073,  2.17475172,  1.36097655)


df = data.frame(LogPlanetMass,LogPlanetRadius,LogPlanetOrbit,StarMetallicity,LogStarMass,LogStarAge)
m1<-lm(LogPlanetMass~.,data=df)
summary(m1)

#####################################################
#gamma and x-ray
gamma.ray <- read.csv("C:/Users/gdiaz/Desktop/GDA/cursoMITx/Data Analysis/release_statsreview_release/data_and materials/gamma-ray.csv")
summary(gamma.ray)
df<-table(gamma.ray$count)

mean_df_variable<-mean(df)
#Chi-square test
library(plyr)
expected <- laply(0:7, function(x) dpois(x=x, lambda=mean_df_variable, log = FALSE))

df<-table(gamma.ray$count)
mean(df)
# calculate actual distribution of df$frequency
observed <- df/sum(df)

# does distribution of df$frequency differ from a poisson distribution? Apparently 
#   not because P-value is > 0.05
chisq.test(expected, observed)
o<-observed
e<-expected
chisq<-sum((o-e)^2/e);chisq

plot(gamma.ray$seconds,gamma.ray$count)
summary(gamma.ray)
poisson.test(gamma.ray$count, 0.61)

library(MASS)
parms <- fitdistr(gamma.ray$count*gamma.ray$seconds, "poisson")
parms 

# load the vcd package
#install.packages("vcd")
library(vcd) ## loading vcd package

# generate two processes for test
set.seed(2014);y=rpois(200,5)
set.seed(2014);y=rnorm(100, 5, 0.3) # goodfit asks for non-negative values
# output the results
gf = goodfit(gamma.ray$count,type= "poisson",method= "ML")
plot(gf,main="Count data vs Poisson distribution")
summary(gf)

# to automatically get the pvalue
gf.summary = capture.output(summary(gf))[[5]]
pvalue = unlist(strsplit(gf.summary, split = " "))
pvalue = as.numeric(pvalue[length(pvalue)]); pvalue

# to mannualy compute the pvalue
chisq = sum(  (gf$observed-gf$fitted)^2/gf$fitted )

df = length(gf$observed)-1-1
pvalue = pchisq(chisq,df)
pvalue


#Otra forma de hacer el chi-square
df<-gamma.ray$count
x<-table(df)
mean(x)#12.5
probs = dpois(0:5, lambda=mean(x))
probs
comp = 1-sum(probs)
xx<-c(68,19,7,2,1,1,1)
chisq.test(x=c(68,19,7,2,1,1,1), p=c(probs,comp))


#Mortality
mortality <- read.csv("C:/Users/gdiaz/Desktop/GDA/cursoMITx/Data Analysis/release_statsreview_release/data_and materials/mortality.csv")

y <- mortality$Mortality
X <- data.frame(mortality[,3:16])

y <- scale(y)
X <- scale(X)

y<- c(y)
X<- as.data.frame(X)
mortality<-data.frame(y,X)
model <- lm(y~., data = mortality)

round(coef(model),3)

summary(model)
plot(model)

labels <- colnames(X)

newfun <- function(x, y) qqPlot(x, main = paste(y, "QQ Plot", sep = " "))


mapply(newfun, mortality, labels)
mapply(plot,y,labels)
plot(mortality$NOx,mortality$y)

#Problem 1.4 Golub
install.packages("multtest")
library(multtest)
#Crema
#https://rstudio-pubs-static.s3.amazonaws.com/187747_3eb3fc30ad7f4d8e92ad73520a0ff8f5.html
#
#Datos de los 1000 genes y los 38 pacientes (efectivamente, 1000 genes y 38 pacientes)
golub <- read.csv("C:/Users/gdiaz/Desktop/GDA/cursoMITx/Data Analysis/release_statsreview_release/data_and materials/golub_data/golub.csv")
#Clasificacion de los pacientes por su tipo tumoral
golub_cl <- read.csv("C:/Users/gdiaz/Desktop/GDA/cursoMITx/Data Analysis/release_statsreview_release/data_and materials/golub_data/golub_cl.csv")
golub_gnames <- read.csv("C:/Users/gdiaz/Desktop/GDA/cursoMITx/Data Analysis/release_statsreview_release/data_and materials/golub_data/golub_gnames.csv")
golub
golub<-golub[,-1]
table(golub_cl$x)
summary(golub)
gol.fac <- factor(golub_cl$x, levels=0:1, labels = c("ALL","AML"))
golub[1042,gol.fac=="ALL"]

#mean of ALL
meanALL <- apply(golub[,gol.fac=="ALL"], 1, mean)
head(meanALL)
#Boxplot of 1042
g1042<-as.double(golub[1042,])
boxplot(g1042 ~ gol.fac, method="jitter")
t.test(g1042 ~ gol.fac, var.equal=FALSE)
t.test(g1042 ~ gol.fac, var.equal=FALSE)$p.value
#Para todos los genes 
#vector para guardar
ik<-c()
pvalues<-c()
for(i in 1:nrow(golub)) {
  row <- golub[i,]
  g1042<-as.double(row)
  pp<-t.test(g1042 ~ gol.fac, var.equal=FALSE)$p.value
  pvalues<-c(pvalues,pp)
  if(pp<0.05){
    ik<-c(ik,i)
  }
  # do stuff with row
}
p<-pvalues
#Siguiente pregunta: Holm-Bonferroni corrected p-values
table(p.adjust(p,method="holm")<0.05)
#Siguiente pregunta: Benjamini-Hochberg
table(p.adjust(p,method="BH")<0.05)
