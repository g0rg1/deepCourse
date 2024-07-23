import typing as tp


def reformat_git_log(inp: tp.IO[str], out: tp.IO[str]) -> None:
    for input in inp:
        sha , date , email ,author, message = input.split("\t")
        out.write(f"{sha[:7]}...{message[:72]}\n")
        