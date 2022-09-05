
#include <avr/io.h>
#include <util/delay.h>

 
int main (void)
{
	int A,B;
	int a=1,b=0;
	DDRB |= ((1 <<DDB5));
        while(1)
	{
	A=a||b;
	//B=b||a;
	if(A==1)
	PORTB=((1<<PB5));

	}
	return 0;

}
