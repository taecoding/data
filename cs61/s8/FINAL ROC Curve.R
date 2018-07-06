###################################
#
rm(list=ls(all=TRUE))
##################################
# Generate training and testing data similar to IRIS
set.seed(100)
numbers1 = rnorm(400)
rows1 = 40
columns1 = 10
training = matrix(numbers1, rows1, columns1)

##############
set.seed(100)
#set.seed(0)
numbers2 = rnorm(400)
rows2 = 40
columns2 = 10
testing = matrix(numbers2, rows2, columns2)

###############################
head(training)
head(testing)

###############################################
# Binary Response Variable for ROC Curve
#
# Generate class labels training data
(cl_training <- rep(c(-1, 1), each=20))
length(cl_training)

# Generate class labels testing data
(cl_testing <- rep(c(-1,1),each=20))
length(cl_testing)
########################################
# Apply KNN Modeling method
#
m1 <- class::knn(training, testing, cl_training, k=2, prob=TRUE)
m1
# Compute the probabilities
#
(prob1 <- attr(m1, "prob"))

(prob2 <- 2*ifelse(m1 == "-1", 1-prob1, prob1) - 1)

#########################################
library(ROCR)
pred_knn <- prediction(prob2, cl_testing)

pred_knn <- performance(pred_knn, "tpr", "fpr")

plot(pred_knn, avg= "threshold", colorize=T, lwd=3, main="ROC curve")

plot(pred_knn, avg= "threshold", lwd=3, main="ROC curve")

abline(a=0,b=1)

############################################

