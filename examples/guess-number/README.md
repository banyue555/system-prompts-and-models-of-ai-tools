# Python 猜数字游戏

程序随机生成 1～100 的整数，根据猜测提示“大了”或“小了”，猜中后显示有效猜测次数。非整数和超出范围的输入不计次数。

## 运行

需要 Python 3.6 或更新版本，无需安装第三方依赖。在本目录打开终端，执行：

```bash
python guess_number.py
```

## 代码分段说明

1. `import random`：导入 Python 自带的随机数模块。
2. `def guess_number()`：定义游戏函数；`random.randint(1, 100)` 生成包含两端的随机整数，`attempts = 0` 初始化次数。
3. 两个 `print()`：显示欢迎信息和猜测范围。
4. `while True`：持续读取猜测；`input()` 获取字符串，`.strip()` 去掉首尾空白。
5. `try/except ValueError`：使用 `int()` 转换整数。字母、小数或空输入会显示提示，`continue` 跳到下一轮。
6. `if not 1 <= guess <= 100`：检查数字范围，超出范围时重新输入。
7. `attempts += 1`：在验证通过后增加次数，因此无效输入不会计数。
8. `if/elif/else`：比较猜测和答案，提示大小；猜中时通过 f-string 显示答案和次数，再用 `break` 结束循环。
9. `if __name__ == "__main__"`：直接执行文件时启动游戏，被其他模块导入时不会自动启动。
