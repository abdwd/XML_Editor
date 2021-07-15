def adjust (file):
    list=[]
    for i, line in enumerate(file):

        space=0
        for j,letter in enumerate(line):

            if letter ==' ':
                space+=1
            else:
                break


        line = line[space:]

        list.append(line)
        temp = "".join(list)
    return temp,list

def helper (line):
    count =0
    for i,letter in enumerate(line) :
        if letter =='<' :
            if i<len(line)-1:
                if (not(line[i+1]=='/' or line[i+1]=='!' or line[i+1]=='?' )):
                    count +=1
                elif  line[i + 1] == '/' :
                    count -=1
        elif letter == '>' :
            if line[i-1] =='/' :
                count -=1
    return count
def indentation (file_):
    temp1,file = adjust(file_)
    list = []
    ind="    "

    current = ""
    for i, line in enumerate(file):
        n=helper(line)
        if n>-1:
            temp= current +line
            list.append(temp)
            current = ind * n + current
        else :
            current = current[4:]
            temp = current + line
            list.append(temp)


    list2=[]
    for i in list:
        temp2=""
        for j in i :
            if j!='\n':
                temp2+=j
        list2.append(temp2)



    temp = "".join(list)
    return temp,list,list2

if __name__ == "__main__":
    file = open("data-sample.xml", "r")
    file1,file2,file3 = indentation(file)
   
    print(file3)
    my_file = open("my file.txt", "w+")
    my_file.write(file1)


