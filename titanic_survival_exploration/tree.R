setwd("D:/Dropbox/learning/udacity_ML/titanic_survival_exploration")

dt<-read.csv("titanic_data.csv")

dt0<-dt[,c( "Survived",    "Pclass",        "Sex",         "Age",         "SibSp",       "Parch")]
dt0$Age <-floor(dt0$Age/10) * 10 

library(rpart)

fit<-rpart(Survived~.,data=dt0, 	method="class")

printcp(fit) # display the results 
plotcp(fit) # visualize cross-validation results 
summary(fit) # detailed summary of splits

plot(fit, uniform=TRUE)
text(fit, use.n=TRUE, all=TRUE, cex=.8)
fit
