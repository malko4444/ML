import pandas as pd
x = [3,6,8,9,0,6,4]
x1 = [3,6,8,9,0,6,4,4,5,7]
y = pd.Series(x, index=['a','b', 'c', 'd', 'e', 'f', 'g'], dtype='float')
# print(y)
# print(type(y))

dic = {"name" : ['python','c', 'c++','java'], "age" : [25, 30, 35, 40], "score" : [90, 80, 70, 60]}
var1 = pd.Series(dic)
# print(var1)
# the main reason is to use the pandas as comapre to the numpy is that numpy show error when the we add the some missing data but the pandas use it as NAN of the issing value rather than the error 
s1 = pd.Series(x)
s2 = pd.Series(x1)
# print(s1+s2) 
# use the remainig as NAN



# dataframe 
# dt = pd.DataFrame(dic,columns=['name'],index=['a','s', 'c', 'd'])
dt = pd.DataFrame(dic)
list = [[2,3,4,5,6,7],[4,6,67,7,84,4]]
dt1 = pd.DataFrame(list)

print(dt1.loc[1,0])

# addition in coloums 
dt2 = pd.DataFrame({'a':[ 1,2,3,4], 'b':[5,6,7,8]})
print(dt2)
dt2['c'] = dt2['a'] + dt2['b']
# print(dt2)


# insert take three argumnent first = colum number , second = column name and the 3rd = value inside the colum 
# dt2.insert(2,"insert the elemnt", dt2['c'])
# print(dt2)
# to copy the half of the element we use in using Colon
dt2['HalfElement'] = dt2['a'][:2]
# print(dt2)



# pop to delete the colum in a dataset use pop () function
popedColum = dt2.pop('HalfElement')
print(popedColum)
# creat a csv file of the data set that are avaible in the same folder of the open in vscode 
dt2.to_csv("CSV file creation ")