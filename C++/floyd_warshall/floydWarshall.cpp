#include <bits/stdc++.h> 
using namespace std; 

//#define V 4 

#define INF 99999 

int main() 
{
    int V;
    cout << "enter the no of rows of adjacency matrix: ";
    cin >> V;
    cout << "Enter the values in Adjacency matrix(enter 99999 if there is no path): ";
	int graph[V][V];
    for (int i=0; i<V; i++)
        for (int j=0; j<V; j++)
            cin >> graph[i][j];

	
	for (int k = 0; k < V; k++) 
	{ 
		for (int i = 0; i < V; i++) 
		{ 
			for (int j = 0; j < V; j++) 
			{ 
				if (graph[i][k] + graph[k][j] < graph[i][j]) 
					graph[i][j] = graph[i][k] + graph[k][j]; 
			} 
		} 
	} 

    cout<<"The following matrix shows the shortest distances between every pair of vertices \n"; 
        for (int i = 0; i < V; i++) 
        { 
            for (int j = 0; j < V; j++) 
            { 
                if (graph[i][j] == INF) 
                    cout<<"INF"<<"	 "; 
                else
                    cout<<graph[i][j]<<"	 "; 
            } 
            cout<<endl; 
        } 

    return 0; 
} 
