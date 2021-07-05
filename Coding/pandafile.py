import pandas

# df1 = pandas.DataFrame([[2,4,6], [10,20,30]], columns=["Price", "Age", "Value"], index=["First", "Second"])

# print(df1)
# print(type(df1))
import pandas
df1 = pandas.read_json("C:/Users/Peter/Desktop/supermarkets/supermarkets.json")
print(df1)