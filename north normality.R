error1<-north_kolkata_modified$error2
error2<-north_kolkata_modified$`error 2 modified`
shapiro.test(error1)
shapiro.test(error2)
qqnorm(error2)
qqline(error2)
n<-length(error2)
set.seed(123)
x<-rnorm(n)
y<-x+error2
model<-lm(y~x)
bptest(model)
