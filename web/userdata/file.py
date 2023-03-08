def make(destigation: str) -> None:
    with open(file=destigation, mode="w") as file:
        return file


def edit(destigation: str, data: any) -> None:
    with open(file=destigation, mode="w+") as file:
        return file.write(data)


def read(destigation: str, split: str = None) -> any:
    with open(file=destigation, mode="r") as file:
        if split:
            return file.read().split(split)

        elif split is None:
            return file.read()

        else:
            return print(f"error argument split({split})")
