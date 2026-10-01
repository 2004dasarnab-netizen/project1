error1<-central_modified$`error2 modified`
shapiro.test(error1)
error2<-central_modified$error2
shapiro.test(error2)

qqnorm(error1)
qqline(error1)
n<-length(error1)
set.seed(123)
x<-rnorm(n)
y<-x+error1
model<-lm(y~x)
bptest(model)

