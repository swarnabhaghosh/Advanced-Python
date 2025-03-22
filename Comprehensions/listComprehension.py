#just to minimize the code

numbers=[1,2,3,4,5,6,7,8]
even=[i for i in numbers if i%2==0]
print(even)

squares=[i*i for i in numbers]
print(squares)

print("-----------------------------------")

s=set([1,2,3,4,5,6,2,3,1,4])
print(s)
even={i for i in s if i%2==0}
print(even)

print("-----------------------------------")

cities=["kolkata","new york","madrid"]
countries=["india","USA","spain"]
z=zip(cities,countries)
for a in z:
        print(a)
d={city:country for city,country in zip(cities,countries)}
print(d)
