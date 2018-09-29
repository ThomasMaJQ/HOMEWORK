a=input("введите предложение:")
word=a.split()
for i in range(len(word)):
  temp=word[i]
  abc=""
  for j in range(len(temp)):
      if ord(temp[j])<1103 and ord(temp[j])>1071:
        abc+=(chr(ord(temp[j])+1))
      elif ord(temp[j])==1103:
        abc+=chr(1072)
  word[i]=abc
tmp=word[i-1]
word[i-1]=word[i]
word[i]=tmp
print(word)


