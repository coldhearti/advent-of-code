from typing import List

START_OF_PACKET_IDENTIFIER_SIZE = 4
START_OF_MESSAGE_IDENTIFIER_SIZE = 14


def idx_after_unique_identifier(data: str, identifier_size: int) -> int:
    check_buffer: List[str] = []
    for i, char in enumerate(data):
        if len(check_buffer) == identifier_size:
            check_buffer.pop(0)
        check_buffer.append(char)
        if len(set(check_buffer)) == identifier_size:
            break
    return i


def solve_part_1(inputPath):
    with open(inputPath, mode="r") as fp:
        data = fp.read()
        return idx_after_unique_identifier(data, START_OF_PACKET_IDENTIFIER_SIZE) + 1


def solve_part_2(inputPath):
    with open(inputPath, mode="r") as fp:
        data = fp.read()
        start_of_packet = idx_after_unique_identifier(data, START_OF_PACKET_IDENTIFIER_SIZE)
        start_of_message = idx_after_unique_identifier(data[start_of_packet::], START_OF_MESSAGE_IDENTIFIER_SIZE)
        return start_of_packet + start_of_message + 1
