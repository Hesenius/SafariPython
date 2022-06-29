
# with closes the resource "reliably"
# implemented with __enter__/__exit__ ??
with open("data.txt", "r") as input:
    with open("output.txt", "r") as input2:
        for l in input:
            print(l, end="")
        input.close()

