# ブロックごとに探索してcandidateを更新
cnt=0
start_i=0
stop_i=3
print("3*3ごとの要素の表示")
while(cnt<3):
  # 一度block_numsに入れて、それをcandidate[i][j]から引く
  block_nums1=[]
  block_nums2=[]
  block_nums3=[]
  for i in range(start_i,stop_i,1):
    for j in range(0,3,1):
      if(problem[i][j]!=0):
        block_nums1.append(problem[i][j])
    for j in range(3,6,1):
      if(problem[i][j]!=0):
        block_nums2.append(problem[i][j])
    for j in range(6,9,1):
      if(problem[i][j]!=0):
        block_nums3.append(problem[i][j])
  print(block_nums1)
  print(block_nums2)
  print(block_nums3)
  for i in range(start_i,stop_i,1):
    for j in range(0,3,1):
      if(problem[i][j]==0):
        candidate[i][j]=[i for i in candidate[i][j] if i not in block_nums1] # 配列から配列を引く処理（
    for j in range(3,6,1):
      if(problem[i][j]==0):
        candidate[i][j]=[i for i in candidate[i][j] if i not in block_nums2]
    for j in range(6,9,1):
      if(problem[i][j]==0):
        candidate[i][j]=[i for i in candidate[i][j] if i not in block_nums3]

  block_nums1.clear()
  block_nums2.clear()
  block_nums3.clear()

  start_i+=3
  stop_i+=3
  cnt+=1

      
print()
print("problem")
for i in range(0,9,1):
  print(problem[i])
print()
print("candidate")
for i in range(0,9,1):
  print(candidate[i])
print()
