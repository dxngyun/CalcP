
print("Hello from feature-branch1")



# 두 정수를 입력받기
num1 = int(input("첫 번째 정수를 입력하세요: "))
num2 = int(input("두 번째 정수를 입력하세요: "))

# 합과 차를 계산
sum = num1 + num2
diff = num1 - num2
mul = num1 * num2
if num2 != 0:
    div = num1 / num2
else:
    div = "나눗셈 불가 (0으로 나눌 수 없음)"

# 결과 출력
print(f"두 수의 합: {sum}")
print(f"두 수의 차: {diff}")
print(f"두 수의 곱: {mul}")
print(f"두 수의 나눗셈: {div}")
