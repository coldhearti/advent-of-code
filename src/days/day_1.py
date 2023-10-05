def solve(inputPath):
    with open(inputPath, mode="r") as fp:
        lines = fp.readlines()
        elf_count = 0
        max_elf_count = 0
        elf_idx = 0
        for line in lines:
            if line.startswith("\n"):
                if elf_count > max_elf_count:
                    max_elf_count = elf_count
                elf_idx += 1
                elf_count = 0
            else:
                elf_count += int(line.rstrip("\n"))

        return max_elf_count
