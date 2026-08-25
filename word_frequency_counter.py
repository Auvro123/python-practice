sentence=input("enter a sentence : ")
words=sentence.split()
freq={}

for word in words:
    if word not in freq:
        freq[word]=1
    else:
        freq[word]+=1

for key in freq.keys():
    print(key," ",freq[key])



