from indentation import  helper
from operator import itemgetter
from copy import *
def errorDetect (file1) :
    n =0
    file=[]
    for line in file1:
        n+=1
        file.append(line)
    stack = []
    indecies = []
    ##file = open(filepath, "r")
    for i in range (n):
        flag= 0
        open= False
        close= False
        temp=""
        errortype = 0
        for j , letter in enumerate(file[i]) :

            if flag==0:
                if letter=='/' and file[i][j+1]=='>':
                    stack.pop()
                if letter != '<':
                    continue
                elif letter =='<' and  ( file[i][j+1]!='!' and file[i] [j+1]!='?') :
                    flag=1
                    if file[i][j+1]=='/':
                        close=True
                        open=False
                    else:
                        close = False
                        open = True

            else:
                if letter=='/' and file[i][j+1]=='>':
                    stack.pop()
                if letter!='>' and letter!= ' ' and letter !='/':
                    temp += letter
                elif letter =='/':
                    continue
                if letter == ' ' and open:
                    stack.append((temp,i))
                    open= False
                    flag=0
                    temp=''
                elif letter == '>':
                    if file[i][j-1]=='/':
                        continue
                    if open:
                        stack.append((temp,i))
                        open = False
                        flag = 0
                        temp = ''
                    elif close:
                        tag=stack.pop()
                        if tag[0]!= temp:
                            prev = stack[-1][0]
                            current = tag[0]
                            next=""
                            #temp
                            count=0
                            subflag=0
                            subflag2=0
                            for k in range(n):
                                if k <=i:
                                    continue
                                if subflag2 ==1 :
                                    break
                                count+= helper(file[k])
                                if count==-1:
                                    subflag2=1
                                    for l, ch in enumerate(file[k]):
                                        if subflag == 0:
                                            if ch == '/':
                                                if file[k][l - 1] == '<':
                                                    subflag = 1
                                        else:
                                            if ch != ' ' and ch != '>':
                                                next += ch
                                            elif ch == ' ' or ch == '>':
                                                break

                            if next== prev:
                                errortype=1
                            elif temp == prev:
                                stack.pop()
                                errortype=2
                            elif current== next:
                                stack.append(tag)
                                errortype=3

                            if errortype==1:
                                indecies.append([i+1,errortype,current])
                            elif errortype==2:
                                indecies.append([tag[1]+1,errortype,current,i+1])
                            elif errortype==3:
                                indecies.append([i+1,errortype,temp])

                        close = False
                        flag = 0
                        temp = ''
    #if len(stack)!=0:
     #   for i in range(len(stack)):
      #      tag = stack.pop()
       #     if tag[1] not in indecies:
        #        indecies.append((tag[1]+1,-1))



    return indecies

def erorr_fix (file,bugs):
    text=[]
    for j, line in enumerate(file):
        text.append(line)
    toadd= []
    add=0
    for z in range(len(bugs)) :

        index= bugs[z][0] -1
        if bugs[z][1]==1 and helper(text[index])==0:
            ind=0
            for k in range(len(text[index])):
                if text[index][k]=='<' and text[index][k+1]=='/':
                    ind = k
                    break
            text[index]= text[index][:k]+ "</"+ bugs[z][2]+ ">\n"

        elif bugs[z][1]==1:
            ind = 0
            for k in range(len(text[index])):
                if text[index][k] == '<' and text[index][k + 1] == '/':

                    ind = k
                    break
            text[index] = text[index][:k] + "</" + bugs[z][2] + ">\n"
        elif bugs[z][1]==2:
            temp=  "</" + bugs[z][2] + ">\n"
            toadd.append([temp,bugs[z][3]-1])
        elif bugs[z][1]==3:
            ind=0
            for x in range (index):
                n= helper(text[index-x])
                if n==1:
                    ind = index-x
                    break
            temp=  "</" + bugs[z][2] + ">\n"
            toadd.append([temp,ind+1])

    #adding
    #aList.insert( 3, 2009)

    toadd = sorted(toadd, key=itemgetter(1))
    for fix in toadd:
        text.insert(fix[1]+add,fix[0])
        add+=1


    return "".join(text)

if __name__ == "__main__":

    file = open("test.xml", "r")
    list =errorDetect(file)
    print (list)
    file = open("test.xml", "r")
    print((erorr_fix(file,list)))


