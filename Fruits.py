import pandas as pd

df = pd.read_csv("Fruits.csv", index_col="Name")

fruit = input("Enter the name of the fruit: ").strip().lower()

try:
    print(df.loc[fruit])
except :
    print("Fruit not found in the dataset.")

new = input("Do you want information about anouther fruit? (yes/no): ").strip().lower()
if new == "yes":
    fruit = input("Enter the name of the fruit: ").strip().lower()
    try:
        print(df.loc[fruit])
    except :
        print("Fruit not found in the dataset.")
else:
    print("Okay! :D ")

test = input("Do you want to see the dataset? (yes/no): ").strip().lower()
if test == "yes":
    print(df)   

add = input("Do you want to add a new fruit to the dataset? (yes/no): ").strip().lower()
if add == "yes":
    name = input("Enter the name of the fruit: ").strip().lower()
    size = input("Enter the size of the fruit (small/medium/big): ").strip().lower()
    weight = input("Enter the weight of the fruit: ").strip().lower()
    price = int(input("Enter the price of the fruit: ").strip().lower())
    df.loc[name] = [size, weight, price]
    df.to_csv("Fruits.csv", index=True)
    print("Fruit added successfully!")
    print(df)
else:
    print("Thank you for using the fruit information system!")
