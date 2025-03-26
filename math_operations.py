import math
def math_operations(num: int) -> dict:
    if not 1<=num<=100:
        raise ValueError("Number must be between 1 and 100")
    return {
        "square_root": math.sqrt(num),
        "sin_of_90_degrees":math.sin(math.radians(90)),
        "factorial": math.factorial(num)
    }
N=int(input())
results=math_operations(N)
print(results)