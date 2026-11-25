ENTRY = (
    "Every Sunday my grandma still sets a plate for Grandpa, who died in 2019, then eats his portion herself\n"
    "and says, 'He never liked it cold, somebody has to keep his standards up.'"
)


def main():
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
