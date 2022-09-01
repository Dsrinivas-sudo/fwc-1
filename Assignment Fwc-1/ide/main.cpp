#include<Ardunio.h>
int a;
int b;
int f;
int g;
int h;
int i;
void setup()
{
pinMode(2,INPUT);
pinMode(3,INPUT);
pinMode(13,OUTPUT);
pinMode(5,OUTPUT);
pinMode(6,OUTPUT);
pinMode(7,OUTPUT);
}
void loop()
{
a=digitalRead(2)
b=digitalRead(3)
f=a||b;
g=b||a;
h=a&&b;
i=b&&a;
digitalWrite(13,f);
digitalWrite(5,g);
digitalWrite(6,h);
digitalWrite(7,i);
}
