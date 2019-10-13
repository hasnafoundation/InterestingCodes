/* hackerearth bfs  ----- how many nodes are present in a particular level */

#include<iostream>
#include<vector>
#include<queue>
using namespace std;
#define N 100000
int k;
vector <int> adj[N];
int level[N];       // to determine the level of each node
bool visited[N];

void BFS(int s, int x)
{
    level[s] = 1;
    queue<int> q;
    q.push(s);
    cout << s << " -> ";
    visited[s] = true;
    while(!q.empty())
    {
        int p = q.front();
        q.pop();
        for(int i = 0; i < adj[p].size(); i++)
        {
            if(visited[ adj[p][i] ] == false)
            {
                level[ adj[p][i] ] = level[p] + 1;
                
                if(level[ adj[p][i] ] == x)
                {
                    k++;
                }
                
                q.push( adj[p][i] );
                visited[ adj[p][i] ] = true;
                cout << adj[p][i] << " -> ";
            }
        }
    }
    cout << " end\n";
}


int main()
{
    int x, y, nodes, edges;
    cin >> nodes;
    for(int i = 0; i < edges; i++)
    {
        cin >> x;
        cin >> y;
        adj[x].push_back(y);
        adj[y].push_back(x); 
    }
    int b;
    cin >> b;
    BFS(1, b);
    //cout << k;
    return 0;
}