#1
text=input("введите слово в кириллице:")
for i in range(len(text)):
  if i%2==0 and (text[i]!='а'and text[i]!='к'):
    print(text[i])

#2
N=int(input("введите число:"))
for i in range(N):
  word=input("введите слово:")
  if word=="программирование":
    break 
  else: 
    print(word)

#3
word=input("введите слово:")
temp=len(word)
for i in range(int(temp/2)):
  print(word[i])
for i in range((temp-1),int(temp/2)-1,-1):
  print(word[i])
