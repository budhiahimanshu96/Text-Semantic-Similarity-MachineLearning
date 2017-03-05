clc;
clear all;

count = 0;

% First File input
[fname,path] = uigetfile('*.txt','Take input of the first text file')
fname1= strcat(path,fname);

% Second File input
[fname,path] = uigetfile('*.txt','Take input of the second text file')
fname2= strcat(path,fname);

% Reading File 1
fileID = fopen(fname1,'r');
formatSpec = '%c';
File1 = fscanf(fileID,formatSpec)

% Reading File 2
fileID = fopen(fname2,'r');
formatSpec = '%c';
File2 = fscanf(fileID,formatSpec)

remain1 = File1;
remain2 = File2;

words_split1 = strsplit(File1);
words_split2 = strsplit(File2);

min_len = min(length(words_split1),length(words_split1));

 for i = 1 : min_len
    [token1,remain1] = strtok(remain1);
    [token2,remain2] = strtok(remain2);
    
   if((length(token1) == length(token2)) & (token1 == token2))
        count = count + 1;
   end
   
 end
 
 if(count == min_len)
     
     disp('Two files are same'); %Message box 
 else
     
      disp('Two files are different'); %Message box
 end
     

