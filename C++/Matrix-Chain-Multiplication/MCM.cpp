#include <iostream>
#include <climits>
using namespace std;

int MatrixChainMultiplication(int dims[], int n)
{
	int c[n + 1][n + 1];

    // Initializing matrix
	for (int i = 1; i <= n; i++)
		c[i][i] = 0;

	for (int len = 2; len <= n; len++) // Subsequence lengths
	{
		for (int i = 1; i <= n - len + 1; i++)
		{
			int j = i + len - 1;
			c[i][j] = INT_MAX;

			for (int k = i; j < n && k <= j - 1; k++)
			{
				int cost = c[i][k] + c[k + 1][j] +
							dims[i - 1]*dims[k]*dims[j];

				if (cost < c[i][j])
					c[i][j] = cost;
			}
		}
	}
	return c[1][n - 1];
}

int main()
{
    int n;
    cout << "Enter the Number of matrix: ";
    cin >> n;
    n++;
    cout << "Enter thr dimensions of matrix: ";
	int dims[n];
    for (int i=0; i<n; i++) cin >> dims[i];
	cout << "Minimum cost is " << MatrixChainMultiplication(dims, n);

	return 0;
}
