def get_fizz_buzz(n: int) -> list[int | str]:
   result = []
   for i in range(1, n + 1):
      if i % 15 == 0:
           ∏result.append("FizzBuzz")
      elif i % 3 == 0:
         result.append("Fizz")
      elif i % 5 == 0:
         result.append("Buzz")
      else:
         result.append((i))
   return result


