terrarium = {"container","soil","plants"}
vivarium = {"drift_wood","rock","sand & water"}
t=terrarium.union(vivarium)

for x in t:
    print(f"what you need to build terrarium/vivarium\n {x}:")
    if x == "drift_wood":
        print(f"you can use any type or any shape {x} ")
    elif x == "rock":
        print(f"you can using any size {x} it's total up to u ")
    elif x == "soil":
        print(f" 1 part each of coco coir, sphagnum moss, sand, and potting {x}")
    elif x == "plants":
        print(f"Fittonia (nerve plant), Peperomia, miniature ferns, mosses, and Pilea {x}")
    elif x == "container":
        print(f"clear glass or plastic vessels need to use {x}")
    elif x == "sand & water":
        print(f"you can use sylhet sand and give watering everyday {x}")

print(f"Most importain thiks you some tools also")
