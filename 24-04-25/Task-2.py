string="Madhukiran"
vow="aeiouAEIOU"


res1=map(lambda s: s in vow,string )
res2=filter(lambda s: s in vow,string )

print(list(res1))
print(list(res2))