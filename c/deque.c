#include <stdio.h>
#include <stdlib.h>
#define max 5
typedef struct Queue{
	int arr[max],front,rear;
}queue;
queue q={{0},-1,-1};
int isEmpty()
{
	if(q.front==-1&&q.rear==-1)
	    return 1;
	return 0;
}
int isFull()
{
	if(q.rear==max-1||q.rear+1==q.front)
	    return 1;
	return 0;
}
void insertFront(int n)
{
	if(isFull())
	    printf("OverFlow\n");
	else if(isEmpty()){
		q.front=1;
		q.rear=0;
	}
	q.front=(q.front-1)%max;
	q.arr[q.front]=n;	
}
void insertEnd(int n)
{
	if(isFull())
	    printf("OverFlow\n");
	else if(isEmpty())
		q.front=0;
	q.rear=(q.rear+1)%max;
	q.arr[q.rear]=n;
}
void delFront()
{
	if(isEmpty())
	    printf("UnderFLow\n");
	else
	    printf("The deleted element is %d\n",q.arr[q.front]);
	q.front=(q.front+1)%max;
}
void delEnd()
{
	if(isEmpty())
	    printf("UnderFlow\n");
	else
	    printf("The deleted element is %d\n",q.arr[q.rear]);
	q.rear=(q.rear-1)%max;
}
void display()
{
	int i;
	printf("The Elements are:\n");
	if(q.front<=q.rear)
	{
		for(i=q.front;i<=q.rear;i++)
			printf("%d  ",q.arr[i]);
	}
	else
	{
		for(i=q.front;i<max;i++)
			printf("%d  ",q.arr[i]);
			for(i=0;i<=q.rear;i++)
			printf("%d  ",q.arr[i]);
	}
}
int main()
{
	int c=0,n;
	while(c!=6)
	{
		printf("\nEnter the choice:\n 1.Insert at Front\n 2.Insert at End\n 3.Delete from Front\n 4.Delete from End\n 5.Display\n 6.End\n");
	    scanf("%d",&c);
	    switch(c)
	    {
	    	case 1:printf("Enter the number:");
	    	       scanf("%d",&n);
			       insertFront(n);
			       break;
			case 2:printf("Enter the number:");
	    	       scanf("%d",&n);
			       insertEnd(n);
			       break;
			case 3:delFront();
			       break;
			case 4:delEnd();
			       break;
			case 5:display();
			       break;
			case 6:exit(0);
			       break;
			default:printf("Invalid\n");
		}
	}
	return 0;
}
