import sys
import math
from typing import Any

PROMPT = '>>> '


def run_calc(context: dict[str, Any] | None = None) -> None:
    if context is None:
        context = {}
        context['math'] = math
    
    while True:
        try:
            line = input(PROMPT)
            if line == " ":
                break
            
            result = eval(line , context)
            
            print(result)
            
        except (SyntaxError , NameError) as e:
            print(f"Error:{e}")
        except Exception as e:
            print(f"Unexpected Error:{e}")
            
            


if __name__ == '__main__':
    context = {'math': math}
    run_calc(context)
