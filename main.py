ENTRY = (
    "Every Sunday my grandma still sets a plate for Grandpa, who died in 2019, then eats his portion herself\n"
    "and says, 'He never liked it cold, somebody has to keep his standards up.'"
)


def check_entry(text):
    if not isinstance(text, str) or not text.strip():
        raise ValueError("entry must be a non-empty string")
    if len(text) > 280:
        raise ValueError("entry exceeds 280 characters")
    lines = text.split("\n")
    if not 1 <= len(lines) <= 2:
        raise ValueError("entry must be one or two lines")
    if any(not line.strip() for line in lines):
        raise ValueError("entry lines must not be blank")


def main():
    import os

    check_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("written entry does not match the entry text")


if __name__ == "__main__":
    main()
