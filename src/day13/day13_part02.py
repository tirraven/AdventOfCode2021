from src.day13.day13_common import get_folded_sheet_from_file


def get_part_two_result(file_name: str):
    return get_folded_sheet_from_file(file_name)


if __name__ == "__main__":
    sheet = get_part_two_result("input.txt")
    print(sheet)
