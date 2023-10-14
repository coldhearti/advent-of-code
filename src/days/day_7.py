from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Set

SIZE_THRESHOLD = 100000
MINIMUM_REQUIRED_SPACE = 30000000
TOTAL_SYSTEM_SIZE = 70000000


@dataclass(init=True)
class Directory:
    name: str
    parent_dir: Directory = None
    child_dirs: Dict[str, Directory] = field(default_factory=dict)
    files: Set[File] = field(default_factory=set)
    _size: int = None

    def __hash__(self) -> int:
        if self.parent_dir is not None:
            return hash(self.name) + hash(self.parent_dir)
        return hash(self.name)

    @property
    def size(self):
        if self._size is None:
            self._size = sum([file.size for file in self.files]) + sum([dir.size for dir in self.child_dirs.values()])
        return self._size


@dataclass(init=True)
class File:
    size: int
    name: str
    parent_dir: Directory

    def __hash__(self) -> int:
        return hash(self.size) + hash(self.name) + hash(self.parent_dir)


def parse_tree(lines: List[str]) -> Directory:
    root: Directory = None
    curr_dir: Directory = None

    for line in lines:
        line = line.lstrip("$ ").rstrip("\n")
        if line.startswith("dir"):
            # Dir
            dir_name = line.split(" ")[1]
            new_dir = Directory(dir_name, curr_dir)
            curr_dir.child_dirs[new_dir.name] = new_dir
        elif line.startswith("cd"):
            # Move
            dir_name = line.split(" ")[1]
            if curr_dir is None:
                curr_dir = Directory(dir_name, None)
                root = curr_dir
            elif dir_name == "..":
                curr_dir = curr_dir.parent_dir
            else:
                curr_dir = curr_dir.child_dirs[dir_name]
        elif line.startswith("ls"):
            ...
        else:
            # File
            file_size, file_name = line.split(" ")
            file = File(int(file_size), file_name, curr_dir)
            curr_dir.files.add(file)
    return root


def threshold_child_sizes(root: Directory):
    sizes = []
    if root.size <= SIZE_THRESHOLD:
        sizes.append(root.size)
    for child in root.child_dirs.values():
        sizes.extend(threshold_child_sizes(child))
    return sizes


def threshold_smallest(root: Directory, required_size, smallest=None):
    if smallest is None:
        smallest = root.size
    if smallest >= root.size >= required_size:
        smallest = root.size
        for child in root.child_dirs.values():
            smallest = threshold_smallest(child, required_size, smallest)
    return smallest


def solve_part_1(input_path):
    with open(input_path, mode="r") as fp:
        lines = fp.readlines()
        root = parse_tree(lines)
        return sum(threshold_child_sizes(root))


def solve_part_2(input_path):
    with open(input_path, mode="r") as fp:
        lines = fp.readlines()
        root = parse_tree(lines)
        free_space = TOTAL_SYSTEM_SIZE - root.size
        required_space = MINIMUM_REQUIRED_SPACE - free_space
        return threshold_smallest(root, required_space)
