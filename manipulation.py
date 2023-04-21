this_list=["this","is","a","developer"]
# print(this_list)

#to add the data in the last list
# this_list.append("in 2023")
# print(this_list)

#to clear all the datas in the variable not the varibale
# this_list.clear()
# print(this_list)

#copy the datas 
# another_list=this_list.copy()
# print(this_list)
# print(another_list)

#to count the dat inside the list
# my_list=[1,2,3,4,2]
# a=my_list.count(2)
# print(a)


#to add the one list to another list
# another_list=["in 2023"]
# this_list.extend(another_list)
# print(this_list)

#to get the index through passing the data 
# a=this_list.index("this")
# print(a)

#to add the element in this specified index
# this_list.insert(4,"in 2023")
# print(this_list)

#remove the last element in the list
# this_list.pop()
# print(this_list)

#to remove the specified index element
# this_list.pop(0)
# print(this_list)

#to remove the specified data
# this_list.remove("this")
# print(this_list)


#to print the data in alpha order 
# this_list.sort()
# print(this_list)

#to print the data in alpha reverse order
# this_list.sort(reverse=True)
# print(this_list)

str="i am singer 123"
def remove(string):
    vowels="aeiouAEIOU"
    result=""
    for char in string:
        if char not in vowels:
            result+=char
    return result


input_data=input("enter the string here and remove the vowels :")
final_data=remove(input_data)
print(final_data)

