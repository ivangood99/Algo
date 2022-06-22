# N_LETTERS = 26
#
# n, m = map(int, input().split())
# s = input()
# cards = input()
# cnt_cards = [0 for i in range(N_LETTERS)]
# cnt_s = [[0] * N_LETTERS for i in range(n + 1)]
# for i in range(m):
#     cnt_cards[ord(cards[i]) - ord('a')] += 1
# for i in range(1, n + 1):
#     for j in range(N_LETTERS):
#         cnt_s[i][j] = cnt_s[i - 1][j]
#     cnt_s[i][ord(s[i - 1]) - ord('a')] += 1
# left = 0
# right = 1
# ans = 0
# while (right <= n):
#     flag = True
#     for i in range(N_LETTERS):
#         if cnt_s[right][i] - cnt_s[left][i] > cnt_cards[i]:
#             flag = False
#             break
#     if flag == True:
#         ans += right - left
#         right += 1
#     else:
#         left += 1
# print(ans)

MAX_N = 26
CODE_A = ord('a')

# input
in_list = list(map(int, input().split()))
n = in_list[0]
m = in_list[1]

grishina_str = input()
cards = input()

substr_cnt = 0

def returnCnt(s : str) -> list:
	cnt = [0] * MAX_N

	for value in s:
		cnt[ord(value) - CODE_A] += 1

	return 	cnt

cnt_cards = returnCnt(cards)

def isSubStr(s_cnt : list) -> bool:
	for i in range(MAX_N):
		if cnt_cards[i] < s_cnt[i]:
			return False

	return True

def sumTwoLists(a : list, b : list) -> list:
	arr = list()
	for i in range(min(len(a), len(b))):
		arr.append(a[i] + b[i])

	return arr

def subtractTwoLists(a : list, b : list) -> list:
	arr = list()
	for i in range(MAX_N):
		arr.append(a[i] - b[i])

	return arr
# заполняем массив куммулятивным cnt
cum_cnt_grishina_str = [[0] * MAX_N, [0] * MAX_N]

cum_cnt_grishina_str[1][ord(grishina_str[0]) - CODE_A] += 1

for i in range(1, len(grishina_str)):
	cnt_ = [0] * MAX_N
	cnt_[ord(grishina_str[i]) - CODE_A] += 1
    cum_cnt_grishina_str.append(sumTwoLists(cum_cnt_grishina_str[i], cnt_))



# идем по куммулятивному cnt и считаем нужные подстроки
i = 0
j = 1

while j <= n:

	# if j == n:
	# 	i += 1
	# 	continue
	print('cnt = ', substr_cnt, ' i = ', i, ' j = ', j)
	arr_ = subtractTwoLists(cum_cnt_grishina_str[j], cum_cnt_grishina_str[i])
	if isSubStr(arr_):
		substr_cnt += j - i
		j += 1

	else:
		i += 1
	# substr_cnt_ = 0
	# while j <= n:
	# 	arr_ = subtractTwoLists(cum_cnt_grishina_str[j], cum_cnt_grishina_str[i])
	# 	if isSubStr(arr_):
	# 		substr_cnt_ = ((j - i) * (j - i + 1) / 2)
	# 		j += 1
	# 	else:
	# 		break

	# substr_cnt += substr_cnt_
	# i = j - 1

print(int(substr_cnt))
