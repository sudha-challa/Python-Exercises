# n=20
# for i in range(1, n//2):
#     for j in range(1, n+1):
#         if j<=i or i+j>=(n+1):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()


# s="AdethfjuyFScfdg"
# s1="r4ecdgghvt"
# r=""
# i=0
# while i<len(s) and i<len(s1):
#     r+=s[i]+s1[i]
#     i+=1
# r=r.lower()
# r+=s[i:].upper() if len(s)> len(s1) else s1[i:].upper()
# print(r)


# n=20
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i==j or (i+j)==(n+1) or j==1 or j==n:
#             print("* ",end="")
#         else:
#             print("  ",end="")
#     print()

# s="computer"
# for i in range(1,len(s)):
#     print(s[:i])
# for i in range(len(s),-1,-1):
#     print(s[:i])


# s=input().lower()
# sum=0
# for i in s:
#     sum+=ord(i)-96
# print(sum)

n=[1,2,0,5,4,5]
for i in range(len(n)):
