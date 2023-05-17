# t=int(input())
# while t>0:
#     n=int(input())
#     budgets=[]
#     t-t-1
#     for x in range(0,n):
#         x=int(input())
#         budgets.append(x)
#     def max_revenue(budgets):
#         def merge_sort(budgets):
#             if len(budgets) <= 1:
#                 return budgets
            
#             mid = len(budgets) // 2
#             left = merge_sort(budgets[:mid])
#             right = merge_sort(budgets[mid:])
    
#             result = []
#             i = j = 0
#             while i < len(left) and j < len(right):
#                 if left[i] < right[j]:
#                     result.append(left[i])
#                     i += 1
#                 else:
#                     result.append(right[j])
#                     j += 1
#             result += left[i:]
#             result += right[j:]
#             return result
        
#         budgets = merge_sort(budgets)
    
#         max_revenue = 0
#         for i, budget in enumerate(budgets):
#             revenue = (i+1) * budget
#             if revenue > max_revenue:
#                 max_revenue = revenue
        
#         return max_revenue

#     max_revenue(budgets)
# cook your dish here

t=int(input())
a=[]
for i in range(t):


    n=int(input())
    for j in range(n):

    
        x=int(input())
        a.append(x)
    b=a
    maximum=max(a)
    count=a.count(maximum)
    if count%2==1:

        print("Marichka \n")
    else:
        print("Zenyk \n")


