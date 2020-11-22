import time
import importlib
from aaa_starting_word import lis


#a=0

val=0.000000000000001

def train(s):
    #a=a+1
    s=s+" "+"*"
    s=s.lower()
    words=s.split(" ")
    neuron={}
    try:
        lis[words[0]]
    except:
        neuron[1]={}
        list_of_words={}
        neuron[1][words[0]]=list_of_words
        file=open(words[0]+".py","w+")
        text="neural_network="+str(neuron)
        file.write(text)
        file.close()

        lis[words[0]]=1
        file=open("aaa_starting_word.py","w+")
        text="lis="+str(lis)
        file.write(text)
        file.close()
    
    mymodule = importlib.import_module(words[0])
    neuron=mymodule.neural_network
    #print(dic[1][prev])
    dic=neuron[1][words[0]]
    for i in range(1,len(words)):
        try:
            dic[words[i]]
        except:
            list_of_words={}
            dic[words[int(i)]]=list_of_words
            dic[words[int(i)]]["%val%"]=0.0
        #divisor=(a+0.0)
        #dic[1][prev][words[i]]=dic[1][prev][words[i]]+((1+0.0)/a)
        dic[words[i]]["%val%"]=dic[words[i]]["%val%"]+ val
        if(dic[words[i]]["%val%"]>0.01):
            for ele in dic:
                if(ele=="%val%"):
                    continue
                dic[ele]["%val%"]=dic[ele]["%val%"]/100
        dic=dic[words[i]]
    file=open(words[0]+".py","w+")
    text="neural_network="+str(neuron)
    file.write(text)
    file.close()
    print(neuron)


def predict(s):
    print("type quit() to move out or double enter to end the sentence")
    if(s==""):
        return
    sentence=""
    check=1
    s=s.lower()
    word1=s.split(" ")[0]
    try:
        lis[word1]
    except:
        check=0
        word1=list(lis.keys())[0]
    mymodule = importlib.import_module(word1)
    dic=mymodule.neural_network[1]
    s=s[0].upper()+s[1:]
    while(1):
        list_=[]
        sentence=sentence+" "+str(s)
        s=s.lower()
        if(check==0):
            print(sentence)
            s=input()
            if(s==""):
                return
            if(s=="quit()"):
                quit()
            continue
        try:
            for i in s.split(" "):
                dic[i]
                dic=dic[i]
        except:
            check=0
            print(sentence)
            s=input()
            if(s=="quit()"):
                quit()
            if(s==""):
                return
            continue
        def creation(temp,alpha,val):
            for i in temp:
                if(i=="%val%"):
                    continue
                zeta=val*100*temp[i]["%val%"]
                if(i=="*"):
                    li2=[]
                    li2.insert(0,zeta)
                    li2.insert(0,alpha)
                    list_.insert(0,li2)
                    continue
                creation(temp[i],alpha+" "+i,zeta)

        creation(dic,sentence,1)
        

        def takeSecond(elem):
            return elem[1]
        
        list_.sort(key=takeSecond)

        for beta in range(min(5,len(list_))):
            print(list_[beta][0])
                
            
        s=input()
        if(s=="quit()"):
            quit()
        if(s=="end()"):
            return
        
while(1):
        
    print("type train() if you want to train only otherwise type sentence in regressive model")
    print("type quit() to quit")
    s=input()
    if(s=="train()"):
       print("requires admin permission enter passkey")
       passkey=input()
       if(passkey!="1234"):
           print("request denied")
           time.sleep(1)
           quit()
       print("enter move() to move out from training otherwise provide training sentence")
       while(1):
           s=input()
           if(s=="move()"):
               s=input()
               break
           if(s=="quit()"):
               quit()
           print("entry") #checking commands
           train(s)
    if(s=="quit()"):
        break
    predict(s)
