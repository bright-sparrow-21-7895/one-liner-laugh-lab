# The entry: one funny line for the One-Liner Laugh Lab.
ENTRY = "My code works on my machine — we've since shipped my machine."


def main():
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
