kor = ["사과", "바나나", "오렌지"]
eng = ["apple", "banana", "orange"]
print(kor)
print(eng)
print(list(zip(kor,eng)))
mixed = [('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]
print(list(zip(*[('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')])))
kor2, eng2 = zip(*mixed)
print(kor2)
print(eng2)

print(list(zip(*zip(kor,eng))))
kor3, eng3 = zip(*zip(kor,eng))
print(kor3)
print(eng3)