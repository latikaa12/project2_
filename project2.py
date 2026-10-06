import numpy as np
import pandas as pd

df = pd.read_csv("day02_usage.csv")
print(df.columns)

a = df["Day"].to_numpy()
b = df["Chat"].to_numpy()
c = df["Video"].to_numpy()
d = df["Study"].to_numpy()
e = df["Games"].to_numpy()

print(a)

print(a.sum())
print(b.sum())
print(c.sum())

print(f"{d.mean():.1f}")

f = d-e

print(f)

g = a+b+c+d

each_a = (a/g)*100

each_b = (b/g)*100

each_c = (c/g)*100

each_d = (d/g)*100

print(each_d)