

def count_util(text: str, flags: str | None = None) -> dict[str, int]:
        result = {}
        if flags is None or "-m" in flags:
                result['chars'] = len(text)
        if flags is None or "-l" in flags:
                result['lines'] = text.count('\n')
        if flags is None or "-L" in flags:
                result['longest_line'] = max(len(line) for line in text.splitlines())
        if flags is None or "-w" in flags:
                result['words'] = len(text.split())
        return result

print(count_util("Hello" , "-m"))