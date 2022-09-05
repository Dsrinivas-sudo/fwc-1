.include "/data/data/com.termux/files/home/m328pdef.inc"

ldi r16,0b00000001; 
out DDRB,r16;  declare 8 pin as a output pin

ldi r16,0b00000000;
ldi r17,0b00000001;
mov r18,r16;  move register 16 to register 17
and r16,r17;
and r17,r18;  perform and operation
cp r16,r17;
breq lbl;  break equal
lbl:
eor r16,r17;
COM r16;
out PORTB,r16;  its giving output as led on and off
start:
rjmp start
