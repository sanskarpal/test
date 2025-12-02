def to_int_or_error(s: str) -> int:
    return int(s)

def main():
    user_input = input()
    try:
        num = to_int_or_error(user_input)
        print(num * num)
    except Exception as e:
        print(f"error: {e}")

if __name__ == "__main__":
    main()
