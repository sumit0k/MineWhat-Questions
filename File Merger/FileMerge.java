import java.io.*;
import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;
public class FileMerge{  
  public static String[] myTrim(String a[]){
    for(int i=0;i<a.length;i++)
      a[i]=a[i].trim();
    return a;
  }
  public static int myIndex(String a[],String index){
    for(int i=0;i<a.length;i++){
      if (a[i].equals(index)){
        return i;
      }
    }
    return -1;
  }
  public static void main(String[] args){
    
    File myFile1,myFile2,outputFile,tempFile1,tempFile;
    myFile1=new File("File1.txt");
    myFile2=new File("File2.txt");
    outputFile= new File("outputFile.txt");
    tempFile1= new File("tempFile1.txt");
    tempFile= new File("tempFile.txt");
    String s1,s2,h1[],h2[],primary="NAME";
    BufferedReader in1,in2;
    PrintWriter out,tempout,tempout1;
    int index1,index2;
    boolean flag=false,file1flag=false;
//try start main code
    try{      
//initialising all readers and writers
      in1 = new BufferedReader(new FileReader(myFile1));
      in2 = new BufferedReader(new FileReader(myFile2));
      out=new PrintWriter(new FileWriter(outputFile));
      tempout=new PrintWriter(new FileWriter(tempFile1));
//getting final lines in uppercase to remove case sensitivity
      s1=in1.readLine().toUpperCase();
      s2=in2.readLine().toUpperCase();
      h1=s1.split(",");
      h2=s2.split(",");      
//making in list for merging of arrays
      List<String> fileline1=new ArrayList<String>();
      List<String> fileline2=new ArrayList<String>();
      List<String> finalline=new ArrayList<String>();      
//trimming both arrays for extra spaces  
      h1=myTrim(h1);
      h2=myTrim(h2);
//getting index for primary key
      index1=myIndex(h1,primary);
      index2=myIndex(h2,primary);
//closing the readers
      in1.close();
      in2.close();
      
//creating two copies of file 2 so as to keep backup and reduce comparisons
      in2 = new BufferedReader(new FileReader(myFile2));
      s2=in2.readLine();
//copying complete file2.txt to tempFile1.txt
      while(s2!=null){
        tempout.println(s2);
        s2=in2.readLine();
      }
//closing the reader and writer for backup
      in2.close();
      tempout.close();
      
//Reading File 1 and Searching for it in every line on File 2
      in1 = new BufferedReader(new FileReader(myFile1));
//flag for switching the tempFiles
      s1=in1.readLine();//initialising file1.txt
      while(s1!=null){ //Checking end of file
        s1=s1.toUpperCase();//removing the case sensitivity
        h1=null;//emptying the arrays for splitter
        fileline1.clear();//emptying list fileline1
        h1=s1.split(","); //storing in array the contents of file 1's line
        h1=myTrim(h1);//trimming for extra spaces
        fileline1.addAll(Arrays.asList(h1));//adding array to list
//switching the temp files based on flag
        if(flag){
          myFile2=new File("tempFile.txt");
          tempFile1=new File("tempFile1.txt");
        }
        else{
          myFile2=new File("tempFile1.txt");
          tempFile1=new File("tempFile.txt");
        }
//initialising the reader and writer for temp file and reading file2
        in2 = new BufferedReader(new FileReader(myFile2));
        tempout=new PrintWriter(new FileWriter(tempFile1));
        s2=in2.readLine().toUpperCase(); //Reading File 2
        while(s2!=null){//Reading Every line
          s2=s2.toUpperCase();
//clearing the lists and array
          h2=null;
          fileline2.clear();
          finalline.clear();
          h2=s2.split(",");//storing in array the contents of file 2's line
          h2=myTrim(h2);//trimming for extra spaces
          fileline2.addAll(Arrays.asList(h2));//adding content in fileline2 list
//if primary key matches then content is written to outputFile
          if(h1[index1].equals(h2[index2])){//checking for primary key
//removing duplicates
            fileline2.removeAll(fileline1);     
//adding to main output finalline
            finalline.addAll(fileline1);
            finalline.addAll(fileline2);
//Printing Main Header
            out.println(finalline.toString());//output to output file
            file1flag=true;//file1 flag to true if match found
          }
          else{//if primary key does not match then content is written to tempFile for next comparison
            tempout.println(s2);
          }
          s2=in2.readLine();//reading next line of file 2
        }
//closing the readers and writers so as to reset the readline pointer
        in2.close();
        tempout.close();
//toggling the value of flag
        if(flag)
          flag=false;
        else
          flag=true;
        if(!file1flag)
          out.println(fileline1.toString());
        file1flag=false;//resetting the file1 flag to false if match found or not
        s1=in1.readLine(); //reading next line of file 1
      }
//Closing every Reader and Writer
      in1.close();
      in2 = new BufferedReader(new FileReader(tempFile1));
      s2=in2.readLine();
      while(s2!=null){
        h2=null;
        fileline2.clear();
        h2=s2.split(",");//storing in array the contents of file 2's line
        h2=myTrim(h2);//trimming for extra spaces
        fileline2.addAll(Arrays.asList(h2));//adding content in fileline2 list
        out.println(fileline2);
        s2=in2.readLine();
      }
      in2.close();
      //outt.close();
      out.close();
      System.out.println("File Merged");
    }
//handling File Exception
    catch(FileNotFoundException e1){
      System.err.println("File not found");
    }
//handiling IO exception
    catch(IOException e2){
      e2.printStackTrace();
    }
    finally{
        tempFile1.delete();
        tempFile.delete();
    }
  }
}