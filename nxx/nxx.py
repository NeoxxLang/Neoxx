import traceback
import sys

KEYWORDS = {
    "script": "import",
    "pkg": "from",
    "function": "def",
    "textln": "print"
}

def translate(code):
    for k, v in KEYWORDS.items():
        code = code.replace(k, v)
    return code

def run_file(filepath):
    try:
        with open(filepath, "r") as f:
            code = f.read()

        translated = translate(code)
        exec(compile(translated, filepath, "exec"), {})

    except Exception as e:
        tb = traceback.extract_tb(e.__traceback__)
        last = tb[-1]

        print(f"{filepath}: {type(e).__name__}")
        print(f"          (line {last.lineno})")
        print(f"reason: {str(e)}")
