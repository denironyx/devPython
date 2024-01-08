## Counting to twenty
for count in range(1, 21):
    print(count)

## One Million - a list 
million = list(range(1, 1_000_001))

## Summing a million
min(million)
max(million)
sum(million)

odd_numbers = list(range(1, 20, 3))
print(odd_numbers)

## Find the Multiple Threes
mulitiple_of_three = [three * 3 for three in range(3, 30)]
mulitiple_of_three

# Cubes
cubes = [cube**3 for cube in range(1, 10)]
print(cubes)