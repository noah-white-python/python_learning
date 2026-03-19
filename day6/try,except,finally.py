try:
    with open('scores.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print('读取成功！')

except FileNotFoundError:
    print('错误：找不到 scores.txt，请先创建文件！')
    lines = []

except PermissionError:
    print('错误：没有权限读取文件！')
    lines = []

finally:
    print('读取操作结束')


scores = []
for line in lines:
    parts = line.strip().split()
    name = parts[0]
    score = int(parts[1])
    scores.append((name, score))
    print(f'{name} 的成绩是 {score}')

if scores:
    average = sum(s[1] for s in scores) / len(scores)
    print(f'\n平均分：{average:.1f}')

try:
    if not scores:  # 加这个判断，如果成绩为空就不写入
        print('没有成绩数据，跳过写入！')
    else:
        with open('result.txt', 'w', encoding='utf-8') as f:
            for name, score in scores:
                f.write(f'{name} {score}\n')
            f.write(f'\n平均分：{average:.1f}\n')
        print('结果已写入 result.txt！')

except PermissionError:
    print('错误：没有权限写入文件！')

except Exception as e:
    print(f'写入时发生未知错误：{e}')

finally:
    print('写入操作结束')