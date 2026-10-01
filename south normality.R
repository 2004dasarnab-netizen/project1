error1<-south_kolkata_modified2$error1
error2<-south_kolkata_modified2$error2
error3<-south_kolkata_modified2$error3
shapiro.test(error1)
shapiro.test(error2)
shapiro.test(error3)
qqnorm(error2)
qqline(error2)
n<-length(error2)
set.seed(123)
x<-rnorm(n)
y<-x+error2
model<-lm(y~x)
bptest(model)

