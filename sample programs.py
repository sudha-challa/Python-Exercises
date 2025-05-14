
# checking prime num or not
#method-1
# n = int(input())
# if n<2:
#     print("not a prime")
# else:
#     for i in range(2, int(n**0.5)+1):
#         if n%i==0:
#             print("not a prime")
#             break
#     else:
#         print("its a prime")
#
#method 2:

# n= int(input())
# for i in range(2, n):
#     if n%i==0:
#         print("not a prime")
#
#         break
# else:
#     print("prime")



#sum of integers
# n=int(input())
# sum=0
# for i in str(n):
#     sum=sum+int(i)
# print(sum)



#num palindrome
# n=int(input())
# rev_num=0
# while n!=0:
#     dig=n%10
#     rev_num=rev_num*10+dig
#     n=n//10
# print(rev_num)
# if n==rev_num:
#     print("it is palindrome")
# else:
#     print("it is not a palindrome")





#string palindrome
# def res(s):
#     print(s[::-1])
# s=input()
# a= res(s)
# if s==a:
#     print("it is palindrome")
# else:
#     print("it is not a palindrome")



#Armstrong number
# n=int(input())
# a=len(str(n))
# b=0
# for i in str(n):
#     b=b+(int(i)**a)
#
# if n==b:
#     print("number is amstrong")
# else:
#     print("number is not amstrong")



# # strong number
# def fact(n):
#     num=1
#     for i in range(1,n+1):
#         num=num*i
#     return num
# n=int(input())
# sum=0
# for i in str(n):
#     sum=sum+fact(int(i))
#
# if n==sum:
#     print("it is strong number")
# else:
#     print("it is not a strong number")



#list appending
# l=[1,5,7,8,9,32,0,2]
# for i in l:
#     if i%2!=0:
#         l.remove(i)
#         l.append(i)
# print(l)

# l=[1,5,7,0,9,32,0,2]
# for i in l:
#     if i==0:
#         l.remove(i)
#         l.append(i)
# print(l)


# l = [1, 5, 7, 8, 9, 32, 0, 2]
#
# for i in range(len(l)):
#     if l[i]%2==0:
#
#         k = "-"
#         l.pop(i)
#         l.append(k)
#
# print(l)


# s="4a3b"
# for i in range(0,len(s),2):
#     print(s[i+1]*int(s[i]),end="")


# a="31a72cg8ca"
# num=char=""
#
# for i in range(len(a)-1):
#     if a[i].isdigit():
#         num+=a[i]
#
#     else:
#         if a[i+1].isdigit():
#         char+=a[i]
#         print(char*int(num))
#         num =char= ""
#     else:char+=a[i]
# if a[-1].isalpha():
#     char+=a[-1]
#     print(char * int(num))


# a = "31ab72cg8ca"
# num = char = ""
# i=0
# while i<len(a):
#     while i<len(a) and a[i].isdigit():
#         num=num+a[i]
#         i+=1
#     while i<len(a) and a[i].isalpha():
#         char+=a[i]
#         i+=1
#     print(char*int(num))
#     num=char=""


# a="abcdefgh"
# l=["a","e","i","o","u"]
# for i in a:
#     if i in l:
#         print(i)


# a="abcdefgh"
# for i in a:
#     if i in "aeiou":
#         print(i)


# a="AFDEDCGYNGKKHIKN"
# for i in a:
#     if i in "aeiouAEIOU":
#         a=a.replace(i,i.upper())
#     else:
#         a=a.replace(i,i.lower())
# print(a)
#

# a="AFDEDCGYNGKKHIKN"
# a=a.lower()
# for i in a:
#      if i in "aeiouAEIOU":
#         a=a.replace(i,i.upper())
# print(a)


# jar=[10,20,30]
# a=0
# for i in jar:
#     a+=i//len(jar)  if i%len()==0  else i/len(jar)+1
# print(a)


#min max sum
# a=[8,9,6,4,2,3]
# min = max = a[0]
# for i in range(1,len(a)):
#     if min>a[i]:
#         min =a[i]
#     if max<a[i]:
#         max=a[i]
# print(min+max)

#superior count
# l=[8,9,4,2,3]
# count=0
# for i in range(0,len(l)-1):
#     a=l[i]
#     for j in range(i+1,len(l)):
#         if a<l[j]:
#             break
#     else:
#         count+=1
# print(count+1)


# a=[53,41,19,7,40,6,15]
# count=1
# for i in range(0,len(a)-1):
#     if a[i]>(max(a[i+1:len(a)])):
#         count+=1
# print(count)
#


# a=[1,2,4,1,9,5]
# i=0
# while i<len(a):
#     print(a[i])
#     i=i+a[i]


a="lokesh"
n=3
print(a[-1]+a[:-1])

