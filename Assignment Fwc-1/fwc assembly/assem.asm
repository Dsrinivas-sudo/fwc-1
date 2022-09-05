.include "/data/data/files/home/m328pdef.inc"
 
ldi r16,0b00000001; declare 8 pin as output pin
out DDRB,r16;
ldi r16,0b00000000;
ldi r17,0b00000001;
mov r18,r16; move register 17 to register 18
and r16,r17;
and r17,r18;  perform and operation
cp r16,r17; comapre
breq lbl; check  equal or not if equal move to next
lbl:
eor r16,r17; perform xor  operation
COM r16;
out PORTB,r16;  produce output in the form of led blinking
start:
rjmp start
