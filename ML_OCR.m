clc;
clear all;
clf;

%[fname,path] = uigetfile('*');
%fname= strcat(path,fname);
im = imread('text.png');
imshow(im);
results = ocr(im);
word = results.Words{2};
wordBBox = results.WordBoundingBoxes(2,:);
figure,Iname = insertObjectAnnotation(im, 'rectangle', wordBBox, word);
imshow(Iname);