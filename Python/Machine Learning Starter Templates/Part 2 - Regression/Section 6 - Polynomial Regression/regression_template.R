#Regression Template

# Importing the dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[2:3]

#Fitting Regression Model to the dataset
#Create your regressor here

#Predicting a new result 
y_pred = predict(regressor, data.frame(Level = 6.5))

#Visualizing the Regression Model Results
ggplot() + 
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             colour = 'red') +
  geom_line(aes(x = dataset$Level, y = predict(regressor, newdata = dataset)),
            color = 'blue') +
  ggtitle('Truth or Bluff (Regression Model') +
  xlab('Level') + 
  ylab('Salary')

#Visualizing the Regression Model Results (for higher resolution and smoother curver)
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.1)
ggplot() + 
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             colour = 'red') +
  geom_line(aes(x = x_grid, y = predict(regressor, newdata = data.frame(Level = x_grid))),
            color = 'blue') +
  ggtitle('Truth or Bluff (Regression Model') +
  xlab('Level') + 
  ylab('Salary')