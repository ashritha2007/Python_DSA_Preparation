n = list(map(int, input().split()))

maxy = n[0]
minny = n[0]

for i in range(1, len(n)):
    if maxy < n[i]:
        maxy = n[i]

    if minny > n[i]:
        minny = n[i]

print(maxy, minny)
