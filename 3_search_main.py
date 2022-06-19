import random

#乱数を使って正解を探す
cnt=0
flag=0
print("10000回ごとのcorrect_cnt　27になれば正解です")
print()
while(flag==0):
  cnt+=1
  # 0からlen(candidate[i][j])までの乱数を生成してproblemに当てはめる
  for i in range(0,9,1):
    for j in range(0,9,1):
      if(isinstance(candidate[i][j],list)):
        problem[i][j]=candidate[i][j][random.randrange(0,len(candidate[i][j]))]
  correct_cnt=0
    
  #横の結果が正しいかの判定
  check_nums=[]
  for i in range(0,9,1):
    check_cnt=0
    for j in range(0,9,1):
      check_nums.append(problem[i][j])
    for j in range(0,9,1):
      if(j+1 in check_nums): # jが入っていたらcheck_cntを+1
        check_cnt+=1
    if(check_cnt==9): # 全部入っていたらcorrect_cntを+1
      correct_cnt+=1
    check_nums.clear()

  #縦の結果が正しいかの判定
  check_nums=[]
  for i in range(0,9,1):
    check_cnt=0
    for j in range(0,9,1):
      check_nums.append(problem[j][i])
    for j in range(0,9,1):
      if(j+1 in check_nums):
        check_cnt+=1
    if(check_cnt==9):
      correct_cnt+=1
    check_nums.clear()

  # ブロックの結果が正しいかの判定
  loop_cnt=0
  while(loop_cnt<3):
    start_i=0
    stop_i=3
    sumb1=[]
    sumb2=[]
    sumb3=[]
    for i in range(start_i,stop_i,1):
      for j in range(0,3,1):
        sumb1.append(problem[i][j])
      for j in range(3,6,1):
        sumb2.append(problem[i][j])
      for j in range(6,9,1):
        sumb3.append(problem[i][j])

    check_cnt=0
    for j in range(0,9,1):
      if(j+1 in sumb1):
        check_cnt+=1
      if(check_cnt==9):
        correct_cnt+=1

    check_cnt=0
    for j in range(0,9,1):
      if(j+1 in sumb2):
        check_cnt+=1
      if(check_cnt==9):
        correct_cnt+=1
      
    check_cnt=0
    for j in range(0,9,1):
      if(j+1 in sumb3):
        check_cnt+=1
      if(check_cnt==9):
        correct_cnt+=1
      
    sumb1.clear()
    sumb2.clear()
    sumb3.clear()
    start_i+=3
    stop_i+=3
    loop_cnt+=1

  # 動いているかの確認
  if(cnt%10000==0):
    print(correct_cnt,end=" ")
  if(cnt%500000==0):
    print()

  #正解の判定
  if(correct_cnt==27):
    flag=1


#正解を表示
print()
print("try:",cnt)
for i in range(0,9,1):
  print(problem[i])
