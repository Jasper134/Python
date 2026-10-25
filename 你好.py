def is_even(num: int) -> bool:
    """判断整数是否为偶数。"""
    return num % 2 == 0


def main() -> None:
    user_input = input("请输入一个整数：").strip()
    try:
        number = int(user_input)
    except ValueError:
        print("输入无效，请输入一个整数。")
        return

    if is_even(number):
        print(f"{number} 是偶数。")
    else:
        print(f"{number} 是奇数。")


if __name__ == "__main__":
    main()
