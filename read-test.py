
print('read-test.py v.0.1/1 of 2025-01-20/GF')
print('read-test of RFID from NFC Tools on iPhone SE')
print()
print('...')
print('Adr.  data...')
with open('Test2MetodTeknologer-bok.txt') as f:
    lines = f.readlines()
for i in range(10,38):
    s = lines[i] 
    sBeg = s[0:5]
    if sBeg != 'Adr. ':
        print('is diff!')
        continue

# Adr. 01 : DATA >> 30:30:30:30
# 0123456789012345678901234567890
# d1 = 18,21
    #print('Loop: i=',i)
    p = 18
    s1 = s[p:p+2]
    d1 = int("0x" + s1, 0)
    #print('s1="' + s1 + '"', ' d1=', d1)

    p = 21
    s2 = s[p:p+2]
    d2 = int("0x" + s2, 0)
    #print('s2="' + s2 + '"', ' d2=', d2)

    p = 24
    s3 = s[p:p+2]
    d3 = int("0x" + s3, 0)
    #print('s3="' + s3 + '"', ' d3=', d3)
    
    p = 27
    s4 = s[p:p+2]
    d4 = int("0x" + s4, 0)
    #print('s4="' + s4 + '"', ' d4=', d4)
    ch1Str = chr(d1)
    if d1 == 0:
        ch1Str = ' '
    ch2Str = chr(d2)
    if d2 == 0:
        ch2Str = ' '        
    ch3Str = chr(d3)
    if d3 == 0:
        ch3Str = ' '        
    ch4Str = chr(d4)
    if d4 == 0:
        ch4Str = ' '
    print(f"{i : > 3}{': '}{d1 : >4}{d2 : >4}{d3:>4}{d4 : >4}", ' Ch:s=', ch1Str, ch2Str, ch3Str, ch4Str)