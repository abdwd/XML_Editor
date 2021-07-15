def minifying (file):
    list=[]
    paragragh=""
    for i, line in enumerate(file):

        space=0
        for j,letter in enumerate(line):

            if letter ==' ':
                space+=1
            else:
                break


        line = line[space:]
        for letter in line :
            if letter != '\n':
                paragragh += letter

        list.append(line)
        temp = "".join(paragragh)
    return temp,list


if __name__ == "__main__":
    file = open("data-sample.xml", "r")
    file1 ,list =minifying(file)
    print(file1)

