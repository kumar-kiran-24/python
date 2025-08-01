import pandas as pd
df=pd.read_csv('data.csv')
print(df.to_string())

#pandas series
a=["a","b","c"]
print(pd.Series(a))

res1=pd.Series(a,index=["A","B","C"])#name the rquiremet series

b={
    "a":1,
    "b":2,
    "c":3
}
res2=pd.Series(b)#series the diticonary key and values

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories, index = ["day1", "day2"])#get the require data using keys
print(myvar)

#data frames
data1={
    "date":[1,2,3,4],
    "day":["mon","tue","wed","thu"]
}
print(pd.DataFrame(data1))

print(pd.options.display.max_rows)# to check the maximum rows in system

#read json
jsonfile=pd.read_json("data.json")
print(jsonfile)

#head method
print(jsonfile.head(5))#specified the number of rows would be return from starting

#tail method
print(jsonfile.tail(6))#return from the last of the json file data

#info method
print(jsonfile.info())#gives information about data like data type ,data set ,storage and etc


#data cleaning
import pandas as pd

df = pd.read_csv('da.csv')
new_df = df.dropna()#to remove the row of  empty values
print(new_df.to_string())
df.dropna(inplace = True)#remove the empty value rows in data file

#replace emplty values(finall() method)
df.fillna(60, inplace = True)#replace the null value where value is 130

#data realtaion
print(df.corr())

#data plotting
import matplotlib.pyplot as plt
df.plot()
plt.show()
