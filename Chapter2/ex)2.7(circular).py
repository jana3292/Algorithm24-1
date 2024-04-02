#순환적인 팩토리얼 알고리즘
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

#구현을 위해 추가한 것
num = int(input("양의 정수를 입력하세요: "))
result = factorial(num)
print(f"{num}의 팩토리얼은 {result}입니다.")
