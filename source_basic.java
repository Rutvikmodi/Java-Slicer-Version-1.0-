import java.util.*;
import java.io.*;
public class source
{  	
	public static int fun(int x, int y)
	{
		int k = 1;
		x = x + 1;
		y = x + y;
		System.out.println(y);
		k = k + x;
		return x;
	}
	public static void main(String[] args)
	{
		Scanner sc=new Scanner(System.in);
		int x;
		int y;
		int z;
		int n;
		int k=19;
		if(!sc.hasNext())
		{
			System.out.println("Helllo");
		}
		x=sc.nextInt();
		y=sc.nextInt();
		z=sc.nextInt();
		n=sc.nextInt();
		y=z;
		x=y+z;
		int i;
		for(i=0;i<n;i=i+1)
		{
			x = fun(x,y);
			System.out.println(i);
			x = x + 1;
		}
		System.out.println(x);
		if(x > 0)
		{
			y = y + 1;
			System.out.println(y);
		}
		else if(x < 0)
		{
			x = x + y;
			System.out.println(x);
		}
		z = x + y;
	}
}