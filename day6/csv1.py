import csv

try:
    with open('scores.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # 跳过第一行标题
        scores = []
        for row in reader:
            name = row[0]
            score = int(row[1])
            scores.append((name, score))
            print(f'{name} 的成绩是 {score}')

    average = sum(s[1] for s in scores) / len(scores)
    print(f'平均分：{average:.1f}')

except FileNotFoundError:
    print('找不到文件！')
except Exception as e:
    print(f'出错了：{e}')
finally:
    print('读取完毕')