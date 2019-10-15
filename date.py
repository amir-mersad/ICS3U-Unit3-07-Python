#!/usr/bin/env python3

# Created by Amir Mersad
# Created on September 2019
# This program accepts users with age between 25 and 40 for dating


def main():
    # This function accepts users with age between 25 and 40 for dating

    # Input
    age_str = input("Please enter you age: ")

    # Process and Output
    try:
        age = int(age_str)
        if age > 25 and age < 40:
            print("You are accepted to date the girl and do other stuff")
        elif age < 25:
            print("You are young, come back later when you are older")
        else:
            print("You are too old!")
    except Exception:
        print("Wrong input!!!")


if __name__ == "__main__":
    main()
