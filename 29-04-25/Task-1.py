string="racecar"  #racecar  aceca cec 
small=""
for i in range(len(string)):
    pal_str=""
    for j in range(i,len(string)):
        pal_str+=string[j]
        if pal_str==pal_str[::-1] and len(pal_str)>=2:
            small=pal_str
print(small)
            
    
        
        
        