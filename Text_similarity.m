clc;
clear all;

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

% Removing Spaces between 2 words in File1 and File2 
File1 =  regexprep(File1,'[^\w'']','');
File2 =  regexprep(File2,'[^\w'']','');

% Comparing  files on the basis of its length
if(length(File1) ~= length(File2))
    
   msgbox('Two files are different'); 
else

if(File1 == File1)
    
   msgbox('Two files are same'); %Message box
   
   
else
    msgbox('Two files are different'); %Message box
   
    
end
end