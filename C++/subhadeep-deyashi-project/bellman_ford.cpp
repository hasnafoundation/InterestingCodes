// shortest path algorithm ( directed weightd graph )
// almost same as dijkstra's algoritm but here it takes care of the negative cycles as well
#include<bits/stdc++.h>
using namespace std;

vector<int> v[2000 + 10];   // array of vectors
int dis[1000 + 10];

int main()
{
    cout << "Enter the number of vertices and edges : ";
    int n, m;   // m = edges,  n = vertices
    cin >> n >> m;
    for (int i = 0; i < m + 2; i++)
    {
        v[i].clear();
        dis[i] = INT_MAX - 1;   // initially all distances are marked as infinity
     }

    cout << "Enter the vertices of " << m << " directed edges with its corresponding weight : \n";
    for (int i = 0; i < m; i++)
    {
        int from, next, weight;
        cin >> from >> next >> weight;
        v[i].push_back(from);
        v[i].push_back(next);
        v[i].push_back(weight);
    }

    int source, dest;
    cout << "Enter the source and destination : ";
    cin >> source >> dest;
    dis[source] = 0;
    for (int i = 0; i < n - 1; i++)
    {
        int j = 0;
        while (v[j].size() != 0)
        {
            // v[j][0] = present vertex, v[j][1] = next vertex, v[j][2] = weight
            dis[ v[j][1] ] = min(dis[ v[j][1] ], dis[ v[j][0] ] + v[j][2]);
            j++;
        }
    }
    cout << "Distance = " << dis[dest] << "\n";
    return 0;
}