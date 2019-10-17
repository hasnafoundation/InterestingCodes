#K-Means Clustering

#Importing the mall dataset
dataset <- read.csv('Mall_Customers.csv')
dataset <- dataset[4:5]

#Using the elbow method to find the optimal number of clusters
set.seed(6)
wcss <- vector()
for (i in 1:10) wcss[i] <- sum(kmeans(dataset, i)$withinss)
plot(1:10, wcss, type = 'b', main = paste('The Elbow Method'), xlab = 'Number of clusters', ylab = 'WCSS')


#Applying k-means to the mall dataset
set.seed(29)
kmeans <- kmeans(X, 5, iter.max = 300, nstart = 10)

#Visualizing the clusters
library(cluster)
clusplot(dataset,
         kmeans$cluster,
         lines = 0,
         shade = TRUE,
         color = TRUE,
         labels = 2,
         plotchar = FALSE,
         span = TRUE,
         main = paste('Clusters of customers'),
         xlab = 'Annual Income',
         ylab = 'Spending Score')