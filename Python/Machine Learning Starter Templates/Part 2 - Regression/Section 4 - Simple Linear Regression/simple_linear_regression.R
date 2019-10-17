#Read dataset from csv file
dataset = read.csv('Salary_Data.csv')
# dataset = dataset[, 2:3]

#Divide dataset into test set and training set
library(caTools)
set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

#Feature Scaling
# training_set[,2:3] = scale(training_set[,2:3])
# test_set[,2:3] = scale(test_set[,2:3])

regressor = lm(formula = Salary ~ YearsExperience,
               data = training_set)

y_pred = predict(regressor, newdata = test_set)

library(ggplot2)
ggplot() + 
  geom_point(aes(x = training_set$YearsExperience, y = training_set$Salary),
             colour = 'red') + 
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, new_data = training_set)),
            color = 'blue') +
  ggtitle('Salary vs Experience (Training Set)') + 
  xlab("Years of experience") + 
  ylab("Salary")

ggplot() + 
  geom_point(aes(x = test_set$YearsExperience, y = test_set$Salary),
             colour = 'red') + 
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, new_data = training_set)),
            color = 'blue') +
  ggtitle('Salary vs Experience (Test Set)') + 
  xlab("Years of experience") + 
  ylab("Salary")
  
  