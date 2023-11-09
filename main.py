import argparse
from datetime import datetime


# Generate name gives you a name based on the value and parameter
# e.x. for first structure with height 10 and second structure with height 20
# the name should be H10-H20.gsa
# if you need to provide a date then
# the name should be 20231009_H10-H20.gsa

# The name should optionally include the date
# the name should include the heights of the two structures showing from and to
# if the transition is on ground it should have the first height and then the second,
# it should be the other way around if not.
# if the height for the second structure is zero it should only display the height of the first structure
# you will always have a height for the first structure

def calc_height(height_1: int, height_2: int) -> str:
    return f"H{height_1}-H{height_2}"


def get_date() -> str:
    return f"{datetime.now().strftime('%Y%m%d')}_"


def name_generator(height_1: int, height_2: int, include_date: bool = False) -> str:
    height_chunk = calc_height(height_1, height_2)
    date = get_date() if include_date else ""
    name = f"{date}{height_chunk}.gsa"
    print(name)
    return name


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Hello World!")
    parser.add_argument('-h1', '--height1', type=int, help='height of the first structure')
    parser.add_argument('-h2', '--height2', type=int, help='height of the second structure')
    args = parser.parse_args()
    name_generator(args.value, args.parameter)
