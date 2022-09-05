.include "/data/data/com.termux/files/home/m328pdef.inc"
ldi r16,0b00000001;
out DDRB,r16;
ldi r16,0b00000000;
ldi r17,0b00000001;
mov r18,r16;
and r16,r17;
and r17,r18;
cp r16,r17;
breq lbl;
lbl:
eor r16,r17;
COM r16;
out PORTB,r16;
start:
rjmp start
