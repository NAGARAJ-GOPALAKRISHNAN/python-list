import re
this_list=[]

no_of_element=int(input("enter the number of element to add the list : "))

for i in range(0,no_of_element):
    data=input("enter the data - ")
    this_list.append(data)


def check():
    valid_string=0
    invalid_string=0
    for i in this_list: 
        for single_letter in i: #"developer"
            patt=r"[a-zA-z]"
            pattern=re.compile(patt)
            if re.match(pattern,single_letter):
                valid_string+=1
            else:
                invalid_string+=1
    print(valid_string)
    print(invalid_string)
check() 

