import random


def guess_number():
    target = random.randint(1, 100)
    attempts = 0

    print("欢迎来到猜数字游戏！")
    print("我想好了一个 1～100 的整数，来猜猜看吧。")

    while True:
        user_input = input("请输入你的猜测：").strip()

        try:
            guess = int(user_input)
        except ValueError:
            print("输入无效，请输入整数，例如 42。")
            continue

        if not 1 <= guess <= 100:
            print("数字超出范围，请输入 1～100 的整数。")
            continue

        attempts += 1

        if guess < target:
            print("小了，再试一次！")
        elif guess > target:
            print("大了，再试一次！")
        else:
            print(f"恭喜你猜对了！答案是 {target}。")
            print(f"你一共猜了 {attempts} 次。")
            break


if __name__ == "__main__":
    guess_number()
