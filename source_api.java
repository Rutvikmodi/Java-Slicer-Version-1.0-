import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Scanner;
import java.util.Iterator;
import org.json.*;
import org.json.simple.parser.JSONParser;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import java.util.*;
import java.io.*;

public class source
{
	public static int fun(int x, int y)
	{
		int diff = 0;
		if(x>=y)
		{
			diff = x-y;
		}
		else
		{
			diff = y-x;
		}
		return diff;
	}
	public static void main(String[] args) 
	{   
		Scanner scc = new Scanner(System.in);
		System.out.println("Enter the name of first country 123455"); 
		String country1 = scc.next();
		System.out.println("Enter the name of second country");	    
		String country2 = scc.next();
		scc.close();
		try 
		{
			URL url = new URL("https://coronavirus-19-api.herokuapp.com/countries");
			HttpURLConnection conn = (HttpURLConnection) url.openConnection();
			conn.setRequestMethod("GET");
			conn.connect();
			int responsecode = conn.getResponseCode();
			if (responsecode != 200) 
			{
				throw new RuntimeException("HttpResponseCode: " + responsecode);
			} 
			else 
			{
				String inline = "";
				Scanner scanner = new Scanner(url.openStream());
				while (scanner.hasNext()) 
				{
					String temp = scanner.nextLine();
					inline = inline + temp;
				}
				scanner.close();
				JSONParser parse = new JSONParser();
				Object data_obj = parse.parse(inline);
				JSONArray arr = (JSONArray) data_obj;	
				Iterator<JSONObject> iterator = arr.iterator();					
				int flag=0;
				int recovered1=0;
				int recovered2=0;
				int total_cases1=0;
				int total_cases2=0;
				int critical1=0;
				int critical2=0;
				int active1=0;
				int active2=0;
				int today_cases1=0;
				int today_cases2=0;
				int today_deaths1=0;
				int today_deaths2=0;
				int d_recovered=0;
				int d_total_cases=0;
				int d_critical=0;
				for(;iterator.hasNext();) 
				{
					JSONObject rec = iterator.next();
					if(rec.get("country").equals(country1))
					{
						recovered1 = Integer.parseInt(rec.get("recovered").toString());
						total_cases1 = Integer.parseInt(rec.get("cases").toString());
						critical1 = Integer.parseInt(rec.get("critical").toString());
						active1 = Integer.parseInt(rec.get("active").toString());
						today_cases1 = Integer.parseInt(rec.get("todayCases").toString());
						today_deaths1= Integer.parseInt(rec.get("todayDeaths").toString());
						flag++;
					}
					else if(rec.get("country").equals(country2))
					{
						recovered2 = Integer.parseInt(rec.get("recovered").toString());
						total_cases2 = Integer.parseInt(rec.get("cases").toString());
						critical2 = Integer.parseInt(rec.get("critical").toString());
						active2 = Integer.parseInt(rec.get("active").toString());
						today_cases2 = Integer.parseInt(rec.get("todayCases").toString());
						today_deaths2 = Integer.parseInt(rec.get("todayDeaths").toString());
						flag++;
					}
					if(flag==2)
					{
						break;
					}
				}
				d_recovered = fun(recovered1,recovered2);
				d_total_cases = fun(total_cases1,total_cases2);
				d_critical = fun(critical1,critical2);
				System.out.println(country1 + ": Recovered -->" +recovered1+ " ::: " + country2 + ": Recovered -->" +recovered2+ " ::: " + " Difference: " + d_recovered);
				System.out.println(country1 + ": Total_Cases -->" +total_cases1+ " ::: " + country2 + ": Total_Cases -->" +total_cases2+ " ::: " + " Difference: " + d_total_cases);
				System.out.println(country1 + ": Critical_Cases -->" +critical1+ " ::: " + country2 + ": Critical_Cases -->" +critical2+ " ::: " + " Difference: " + d_critical);
			}
		} 
		catch (Exception e)
		{
			e.printStackTrace();
		}
	}
}