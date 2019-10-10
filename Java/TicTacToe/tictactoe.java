import java.util.Scanner;
class ticktack
{
	public static void main(String...arg)
	{
		Scanner scan=new Scanner(System.in);
		int i,j,k=0;
		String [][]arr=new String[3][3];
		for(i=0;i<3;i++)
		{
			for(j=0;j<3;j++)
			{
				arr[i][j]=" ";
			}
			
		}
		
		System.out.println("|"+arr[0][0]+"|"+arr[0][1]+"|"+arr[0][2]+"|");
		System.out.println("|-----|");
		System.out.println("|"+arr[1][0]+"|"+arr[1][1]+"|"+arr[1][2]+"|");
		System.out.println("|-----|");
		System.out.println("|"+arr[2][0]+"|"+arr[2][1]+"|"+arr[2][2]+"|");
		
		System.out.println("Player 1 insert x");
		System.out.println("Player 2 insert O");
		for(;;)
		{
			if(k%2==0)
				{
					try{
					System.out.println("Player 1's turn");
					System.out.println("Where would u like to insert x");
					System.out.println("Enter desired row and column");
					int r=scan.nextInt();
					int c=scan.nextInt();
					arr[r][c]="x";
					
		System.out.println("|"+arr[0][0]+"|"+arr[0][1]+"|"+arr[0][2]+"|");
		System.out.println("|-----|");
		System.out.println("|"+arr[1][0]+"|"+arr[1][1]+"|"+arr[1][2]+"|");
		System.out.println("|-----|");
		System.out.println("|"+arr[2][0]+"|"+arr[2][1]+"|"+arr[2][2]+"|");
	
					int res=diduwin(arr);
					if(res==1)
						break;
					}catch(Exception e){}
				}
			else
				{
					try{
					System.out.println("Player 2's turn");
					System.out.println("Where would u like to insert o");
					System.out.println("Enter desired row and column");
					int r=scan.nextInt();
					int c=scan.nextInt();
					arr[r][c]="o";
					
					
		System.out.println("|"+arr[0][0]+"|"+arr[0][1]+"|"+arr[0][2]+"|");
		System.out.println("|-----|");
		System.out.println("|"+arr[1][0]+"|"+arr[1][1]+"|"+arr[1][2]+"|");
		System.out.println("|-----|");
		System.out.println("|"+arr[2][0]+"|"+arr[2][1]+"|"+arr[2][2]+"|");
		
					int res=diduwin(arr);
					if(res==1)
						break;
					int result=istie(arr,res);
					if(result==-1)
						break;
					}catch(Exception e){}
					
				}
			k++;
				
		}
				
				
	}
	static int diduwin(String arr[][])
	{
		int i,j;
		//diagonal wise
		if(arr[0][0]=="x"&& arr[1][1]=="x" && arr[2][2]=="x")
		{
			System.out.println("Game over.Player1 wins.");
			return 1;	
		}
		else if(arr[0][0]=="o"&& arr[1][1]=="o" && arr[2][2]=="o")
		{
			System.out.println("Game over.Player2 wins.");
			return 1;	
		}
		else if(arr[0][2]=="x"&& arr[1][1]=="x" && arr[2][0]=="x")
		{
			System.out.println("Game over.Player1 wins.");
			return 1;	
		}
		else if(arr[0][2]=="o"&& arr[1][1]=="o" && arr[2][0]=="o")
		{
			System.out.println("Game over.Player2 wins.");
			return 1;	
		}
		//row wise
		else if(arr[0][0]=="o"&& arr[0][1]=="o" && arr[0][2]=="o")
		{
			System.out.println("Game over.Player2 wins.");
			return 1;	
		}
		else if(arr[0][0]=="x"&& arr[0][1]=="x" && arr[0][2]=="x")
		{
			System.out.println("Game over.Player1 wins.");
			return 1;	
		}
		else if(arr[1][0]=="o"&& arr[1][1]=="o" && arr[1][2]=="o")
		{
			System.out.println("Game over.Player2 wins.");
			return 1;	
		}
		else if(arr[1][0]=="x"&& arr[1][1]=="x" && arr[1][2]=="x")
		{
			System.out.println("Game over.Player1 wins.");
			return 1;	
		}
		else if(arr[2][0]=="o"&& arr[2][1]=="o" && arr[2][2]=="o")
		{
			System.out.println("Game over.Player2 wins.");
			return 1;	
		}
		else if(arr[2][0]=="x"&& arr[2][1]=="x" && arr[2][2]=="x")
		{
			System.out.println("Game over.Player1 wins.");
			return 1;	
		}
		//column wise
		else if(arr[0][0]=="o"&& arr[1][0]=="o" && arr[2][0]=="o")
		{
			System.out.println("Game over.Player2 wins.");
			return 1;	
		}
		else if(arr[0][0]=="x"&& arr[1][0]=="x" && arr[2][0]=="x")
		{
			System.out.println("Game over.Player1 wins.");
			return 1;	
		}
		else if(arr[0][1]=="o"&& arr[1][1]=="o" && arr[2][1]=="o")
		{
			System.out.println("Game over.Player2 wins.");
			return 1;	
		}
		else if(arr[0][1]=="x"&& arr[1][1]=="x" && arr[2][1]=="x")
		{
			System.out.println("Game over.Player1 wins.");
			return 1;	
		}
		else if(arr[0][2]=="o"&& arr[1][2]=="o" && arr[2][2]=="o")
		{
			System.out.println("Game over.Player2 wins.");
			return 1;	
		}
		else if(arr[0][2]=="x"&& arr[1][2]=="x" && arr[2][2]=="x")
		{
			System.out.println("Game over.Player1 wins.");
			return 1;	
		}
		
		return 0;
	}
	static int istie(String arr[][],int flag)
	{
		int i,j,count=0;
		for(i=0;i<3;i++)
		{
			for(j=0;j<3;j++)
			{
				if(arr[i][j]=="x"||arr[i][j]=="o")
					count++;
			}
		}
		if(flag==0 && count==9)  //Didnt win the game and the matrix is full already.
		{
			System.out.println("Its a Tie game.");
			return -1;
		}
		return 0;
	}
}
