# with open("900.txt", 'r') as f:
#     amount_lines = 0
#     for line in f:
#         numbers = line.split('\t')
#         s = []
#         for i in numbers:
#             s.append(int(i))
#         counter = 0
#         first = []
#         second = []
#         for i in s:
#             if s.count(i) != 1:
#                 first.append(i)
#                 continue
#             second.append(i)
#         if len(set(s)) == 4:
#             amount_lines += 1

# with open("905.txt", "r") as f:
#     amout_lines = 0
#     for line in f:
#         numbers = line.split('\t')
#         s = []
#         for i in numbers:
#             s.append(int(i))
#         if len(set(s)) == 3 and s.count(max(s)) > 1:
#             amout_lines += 1

