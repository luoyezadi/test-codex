"""一个简单的命令行计算器。"""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("除数不能为 0")
    return a / b


def calculate(a: float, operator: str, b: float) -> float:
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    if operator not in operations:
        raise ValueError("不支持的运算符，请使用 + - * /")

    return operations[operator](a, b)


def main() -> None:
    print("欢迎使用 Python 计算器（输入 q 退出）")

    while True:
        raw = input("请输入表达式（例如 1 + 2）：").strip()
        if raw.lower() in {"q", "quit", "exit"}:
            print("已退出。")
            break

        parts = raw.split()
        if len(parts) != 3:
            print("输入格式错误，请按：数字 运算符 数字")
            continue

        left, operator, right = parts
        try:
            a = float(left)
            b = float(right)
            result = calculate(a, operator, b)
            print(f"结果：{result}")
        except ValueError as exc:
            print(f"错误：{exc}")


if __name__ == "__main__":
    main()
