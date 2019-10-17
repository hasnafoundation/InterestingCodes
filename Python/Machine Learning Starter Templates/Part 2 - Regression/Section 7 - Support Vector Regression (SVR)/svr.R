#SVR Model

# Importing the dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[2:3]

#Fitting SVR to the dataset
library(e1071)
regressor = svm(formula = Salary ~ .,
                data = dataset,
                type = 'eps-regression')

#Predicting a new result 
y_pred = predict(regressor, data.frame(Level = 6.5))

#Visualizing SVR Results
ggplot() + 
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             colour = 'red') +
  geom_line(aes(x = dataset$Level, y = predict(regressor, newdata = dataset)),
            color = 'blue') +
  ggtitle('Truth or Bluff (SVR)') +
  xlab('Level') + 
  ylab('Salary')

#Visualizing the SVR Results (for higher resolution and smoother curver)
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.1)
ggplot() + 
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             colour = 'red') +
  geom_line(aes(x = x_grid, y = predict(regressor, newdata = data.frame(Level = x_grid))),
            color = 'blue') +
  ggtitle('Truth or Bluff (SVR') +
  xlab('Level') + 
  ylab('Salary')