car1={
    "brand":input("Brand 1:"),

    "model":input("Model 1: "),

    "horsepower":int(input("Horsepower 1: "))
}

car2={
    "brand":input("Brand 2:"),

    "model":input("Model 2: "),

    "horsepower":int(input("Horsepower 2: "))
}

if car1["horsepower"]>car2["horsepower"]:
    print(f"{car1["brand"]} {car1["model"]} is faster")
else: 
    print(f"{car2["brand"] + car2["model"]} is faster")