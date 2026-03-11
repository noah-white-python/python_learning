text = "期末成绩单"
name = "小明"
subject = "科目"
subject1 = "数学"
subject2 = "英语"
subject3 = "Python"
score = "成绩"
score1 = 98
score2 = 85
score3 = 100
average = "平均分"
average_score = (score1 + score2 +score3) / 3

print(f"{text:^20}")
print(name,subject,score,sep="      ")
print(name,subject1,score1,sep="      ")
print(name,subject2,score2,sep="      ")
print(name,subject3,score3,sep="      ")
print(average,f"{average_score:.2f}",sep="              ")