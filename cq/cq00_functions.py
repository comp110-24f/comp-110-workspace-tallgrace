"""mimic function"""

__author__ = 730649724


def mimic(message: str) -> str:
    """repeat input back to me"""
    return message


def main():
    print(mimic(message=input("what is your message?")))


if __name__ == "__main__":
    main()
