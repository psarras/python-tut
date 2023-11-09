import argparse


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

def name_generator(value: int, parameter: int) -> str:
    name = f"{value}-{parameter}"
    print(name)
    return name


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Hello World!")
    parser.add_argument('-v', '--value', type=int, help='one of the important values')
    parser.add_argument('-p', '--parameter', type=int, help='one of the important parameters')
    args = parser.parse_args()
    name_generator(args.value, args.parameter)
