# 縦横を探索してproblem[][]を含めばcandidate[][]を更新

cnt=0
flag=0
while(flag==0):# 候補を1つに絞れる限り繰り返す
  flag=1

  #途中経過の表示
  print()
  print("cnt",cnt)
  # print("problem")
  # for i in range(0,9,1):
  #   print(problem[i])
  # print()
  print("candidate")
  for i in range(0,9,1):
    print(candidate[i])

  # 横の探索
  for i in range(0,9,1):
    for j in range(0,9,1):
      for k in range(0,9,1):
        if(problem[i][j]!=0)and(isinstance(candidate[i][k],list)):
          if(problem[i][j] in candidate[i][k]):
            candidate[i][k].remove(problem[i][j])

  # 縦の探索
  for i in range(0,9,1):
    for j in range(0,9,1):
      for k in range(0,9,1):
        if(problem[j][i]!=0)and(isinstance(candidate[k][i],list)):
          if(problem[j][i] in candidate[k][i]):
            candidate[k][i].remove(problem[j][i])

  #１つに絞れている個所はlist→intに変換
  for i in range(0,9,1):
    for j in range(0,9,1):
      if(isinstance(candidate[i][j],list)):
        if(len(candidate[i][j])==1)and(problem[i][j]==0):
          candidate[i][j]=candidate[i][j][0]
          problem[i][j]=candidate[i][j]
          flag=0
  
  cnt+=1

#確率の表示
pro=1.0
for i in range(0,9,1):
  for j in range(0,9,1):
    if(isinstance(candidate[i][j],list)):
      pro*=1/len(candidate[i][j])
print()
print("count",cnt)
print("probability:",pro)

# ここまでだけで答えが出る問題もある
