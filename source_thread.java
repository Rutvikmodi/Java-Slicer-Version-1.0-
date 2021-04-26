import java.io.*;
import java.util.*;
class MultithreadingDemo extends Thread 
{
    public void run()
    {
		long x=0;
		long y=0;
		long ans=0;
        long vari = 5;	    
        try
		{
            if(Thread.currentThread().getId()%10<5)
			{
				ans = vari + Thread.currentThread().getId()%10;
				x = x+1;
				y = y-1;
			}
			else
			{
				ans = vari - Thread.currentThread().getId()%10; 
				y = y +1;
				x = x-1;	
			}
			if(ans<0)
			{
				x = ans+y;
				System.out.println("Greater threads are executing more");
			}
			else
			{
				y = ans + x;
				System.out.println("Smaller threads are executing more");
			}
			if(x + y <0)
			{
				x = x + y;
				x = -x;
				System.out.println("Now x is positive");
			}
			else
			{
				x = x + y;
				System.out.println("Now x is negative");
			}
        }
        catch (Exception e) 
		{
            // Throwing an exception
            System.out.println("Exception is caught");
        }
    }
}
 
// Main Class
public class source 
{
    public static void main(String[] args)
    {
		System.out.println("Input number of threads");
        int n;
		Scanner sc = new Scanner(System.in);
		n=sc.nextInt();	
        for (int i = 0; i < n; i++) 
		{
            MultithreadingDemo object = new MultithreadingDemo();
            object.start();
        }
		for(int i=0;i<4;i++)
		{
			System.out.println("Rutvik");
		}
    }
}