import java.io.*;
import java.util.Scanner;
import java.util.Arrays;
public class ArrayLarge{
  //function to compare two numbers which gives the largest
  public static int compare(String a, String b){
    String temp1=a+b;// a before b
    
    String temp2=b+a;//b before a
    return Integer.parseInt(temp1)>Integer.parseInt(temp2)?1:0;
  }  
  public static void main(String args[]){
    String s2[],out="";   
    Scanner s=new Scanner(System.in);//Input STring
    String s1=s.nextLine();
    s2=s1.split(" ");// splitting on the basis of space
    Arrays.sort(s2);//sorting the array
    int l=s2.length;
    String[] temp=new String[s2.length];
    System.arraycopy(s2,0,temp,0,s2.length);    //copying in backup array
    for(int i=0;i<l;i++){     
    temp[l-i-1]=s2[i];   //reversing the order
    }
    String[] s3=new String[s2.length];
    for(int i=0;i<l;i++){     
    s3[i]=temp[i];   // copying the reverse order in updated string
    }
    for(int i=0;i<s2.length-1;i++){
      int k=compare(s3[i],s3[i+1]);//comparing each of two numbers if they give larger output
      if(k==0){
       String tem=s3[i];//swapping if the reverse order gives larger value
       s3[i]=s3[i+1];
      s3[i+1]=tem;
      }
    }
    for(int i=0;i<s3.length;i++){
    out=out+s3[i];//developing the output string
    }
    System.out.println(out);//printing output
    }
}