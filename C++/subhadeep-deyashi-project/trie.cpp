#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

#define newTrie (Trie*) calloc(1, sizeof(Trie))

typedef struct node{
	bool isWord;
	struct node *next[26];
}Trie;

void insert(char*, Trie*);
void print(Trie *, char*, int);

int main(void)
{
	int n;
	char string[1234];
	
	scanf("%i", &n);
	Trie *t = newTrie; 
	while(n--)
	{
		scanf("%s", string);
		insert(string, t);
	}	
	print(t, string, 0);
	return 0;
}

void insert(char *string, Trie *root)
{
	if (*string!='\0')
	{
		if (root->next[*string - 'a'] == NULL)
			root->next[*string - 'a'] = newTrie;
        
		insert(string + 1, root->next[*string - 'a']);		
	}
	else
		root->isWord = true;
}

void print(Trie *root, char *string, int level)
{

	if(root->isWord == true)
	{	
		string[level] = '\0';
		puts(string);
	}
	
	for( int i = 0; i < 26; i++)
	{
		if (root->next[i])
		{
			string[level] = i + 'a';
			print(root->next[i], string, level + 1);
		}			
	}		
	
}
