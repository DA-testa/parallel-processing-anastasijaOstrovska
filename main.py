# python3

def parallel_processing(n, m, data):
    output = []
    thread = []
    for i in range (n):
        thread.append(0)
    time = 0
    i = 0
    j = 0

    while j < len(data):
        for i in range (len(thread)):
            if thread[i] == 0 :
                thread[i] = data[j]-1
                output.append([i, time])
                if j < len(data):
                    j += 1
            else:
                thread[i] -= 1
        time += 1

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n = 0
    m = 0

    i = input() # file or input
    if "i" in i.lower() :
        n,m = map(int, input().split())
        data = list(map(int, input().split()))

    elif "f" in i.lower() :
        name = input()
        #name = "./test/" + name
        if "a" not in name:
            with open(name, mode = 'r' ,  encoding = "utf8") as fail:
                n,m = map(int, fail.readline().split())
                data = list(map(int, fail.readline().split()))
        else :
            return
                
    else :
        return


    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for i, j in result :
        print(i,j)



if __name__ == "__main__":
    main()
