r1 = {'name':'lxy','age':10,"salary":2222222,'city':'CD'}
r2 = {'name':'l22','age':22,"salary":22222222,'city':'CD'}
r3 = {'name':'l33','age':33,"salary":222222222,'city':'CD'}

tb1 = [r1,r2,r3]

print(tb1[1].get('age'))

for i in range(len(tb1)):
    print(tb1[i].get('name'),tb1[i].get('age'),
          tb1[i].get('salary'),tb1[i].get('city'),end='\t',)
