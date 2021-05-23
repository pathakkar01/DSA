open_list = ["(", "{", "["]
close_list = [")", "}", "]"]

str1 = input()
stack = []
for i in str1:
    if i in open_list:
        stack.append(i)
    elif i in close_list:
        pos = close_list.index(i)
        if len(stack) == 0 or open_list[pos] != stack[len(stack)-1]:
            print("unbalanced") 
        else:
            stack.pop()
print("balanced" if len(stack)==0 else "unbalanced" )

