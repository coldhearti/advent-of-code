from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

SIZE_THRESHOLD = 100000
MINIMUM_REQUIRED_SPACE = 30000000
TOTAL_SYSTEM_SIZE = 70000000


@dataclass(init=True)
class Directory:
    name: str
    parent_dir: Optional[Directory] = None
    child_dirs: Dict[str, Directory] = field(default_factory=dict)
    files: Set[File] = field(default_factory=set)
    _size: Optional[int] = None

    def __hash__(self) -> int:
        if self.parent_dir is not None:
            return hash(self.name) + hash(self.parent_dir)
        return hash(self.name)

    @property
    def size(self) -> int:
        if self._size is None:
            files_size = sum([file.size for file in self.files])
            child_dirs_size = sum([dir.size for dir in self.child_dirs.values()])
            self._size = files_size + child_dirs_size
        return self._size


@dataclass(init=True)
class File:
    size: int
    name: str
    parent_dir: Directory

    def __hash__(self) -> int:
        return hash(self.size) + hash(self.name) + hash(self.parent_dir)


def parse_tree(lines: List[str]) -> Optional[Directory]:
    root: Optional[Directory] = None
    curr_dir: Optional[Directory] = None

    for line in lines:
        line = line.lstrip("$ ").rstrip("\n")
        if line.startswith("dir"):
            # Dir
            dir_name = line.split(" ")[1]
            new_dir = Directory(dir_name, curr_dir)
            if curr_dir is not None:
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
            if curr_dir is not None:
                file = File(int(file_size), file_name, curr_dir)
                curr_dir.files.add(file)
    return root


def threshold_child_sizes(root: Directory) -> List[int]:
    sizes: List[int] = []
    if root.size <= SIZE_THRESHOLD:
        sizes.append(root.size)
    for child in root.child_dirs.values():
        sizes.extend(threshold_child_sizes(child))
    return sizes


def threshold_smallest(root: Directory, required_size: int, smallest: Optional[int] = None) -> Optional[int]:
    if smallest is None:
        smallest = root.size
    if smallest >= root.size >= required_size:
        smallest = root.size
        for child in root.child_dirs.values():
            smallest = threshold_smallest(child, required_size, smallest)
    return smallest


def solve_part_1(input_path: Optional[Path]) -> Any:
    if input_path is not None:
        with open(input_path, mode="r") as fp:
            lines = fp.readlines()
            root = parse_tree(lines)
            if root is not None:
                return sum(threshold_child_sizes(root))


def solve_part_2(input_path: Optional[Path]) -> Any:
    if input_path is not None:
        with open(input_path, mode="r") as fp:
            lines = fp.readlines()
            root = parse_tree(lines)
            if root is not None:
                free_space = TOTAL_SYSTEM_SIZE - root.size
                required_space = MINIMUM_REQUIRED_SPACE - free_space
                return threshold_smallest(root, required_space)
