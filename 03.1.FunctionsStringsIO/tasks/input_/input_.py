import sys
import typing as tp


def input_(prompt: str | None = None,
       inp: tp.IO[str] | None = None,
       out: tp.IO[str] | None = None) -> str | None:
       out.write(prompt)
       out.flush()
       
       line = inp.readline()
       if line is None or line == "\xo4":
              return None 
       return line.rstrip()

