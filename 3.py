#Q1 max of 3 num
# a,b,c=map(int,input().split())
# print(max(a,b,c))

#Q2 valid year
# a,b,c=map(int,input().split())
# if a>0 and a<31:
#     if b>0 and b<12:
#         if c>0:
#             print("Yes")
#         else:
#             print("Not a valid year")
#     else:
#         print("Not a valid year")
# else:
#     print("Not a valid year")

#Q3 electricity
# a=float(input())
# if a<=50:
#     ch=a*0.50
#     total=ch+(ch*0.2)
# elif a>50 and a<=150:
#     ch=(50*0.5)+((a-50)*0.75)
#     total=ch+(ch*0.2)
# elif a>150 and a<=250:
#     ch=(50*0.5)+(100*0.75)+((a-150)*1.20)
#     total=ch+(ch*0.2)
# else:
#     ch=(50*0.5)+(100*0.75)+(100*1.20)+((a-150)*1.50)
#     total=ch+(ch*0.2)
# print(total)

#Q4 elec. bill
# a=float(input())
# if a<=100:
#     print("NO charge")
# elif a>100 and a<=200:
#     ch=(a-100)*5
#     print(ch)
# else:
#     ch=(a-200)*10
#     ch1=5*100
#     print(ch+ch1)

#Q5 wages
# a=input()
# b,c=map(int,input().split())
# if a=="F":
#     if b>=18 and b<30:
#         print(c*750)
#     elif b>=30 and b<=40:
#         print(c*850)
# elif a=="M":
#     if b>=18 and b<30:
#         print(c*700)
#     elif b>=30 and b<=40:
#         print(c*800)

#Q6 library
# a=int(input())
# if a<=5:
#     print(a*2)
# elif a>5 and a<=10:
#     print(a*3)
# elif a>10 and a<=15:
#     print(a*4)
# else:
#     print(a*5)

#Q7 notes
# a=int(input())
# n=0
# if a>2000:
#     d=a//2000
#     a=a-(d*2000)
#     n+=d
# if a>500:
#     d=a//500
#     a=a-(d*500)
#     n+=d
# if a>200:
#     d=a//200
#     a=a-(d*200)
#     n+=d
# if a>100:
#     d=a//100
#     a=a-(d*100)
#     n+=d
# if a>20:
#     d=a//20
#     a=a-(d*20)
#     n+=d
# if a>10:
#     d=a//10
#     a=a-(d*10)
#     n+=d
# if a>5:
#     d=a//5
#     a=a-(d*5)
#     n+=d
# if a>2:
#     d=a//2
#     a=a-(d*2)
#     n+=d
# if a>1:
#     d=a//1
#     n+=d
# print(n)

#Q8 quadrilateral
# a,b,c,d,e=map(int,input().split())
# if a==b==c==d and e==90:
#     print("square")
# elif a==b==c==d and e<90:
#     print("rhombus")
# elif a==c and b==d and e==90:
#     print("rectangle")
# elif a==c and b==d and e<90:
#     print("parallelogram")
# else:
#     print("irregular quadrilateral")

# Q9 grades
# a,b=map(int,input().split())
# if a>=20 and a<=50:
#     if b>=20 and b<=50:
#         ap=a/100
#         bp=b/100
#         if ap+bp>=45:
#             print("pass")
#         elif ((a+b)/2)*100==44:
#             print("moderate pass")
#     elif ((a+b)/2)*100==44:
#         print("technical fail")
#     else:
#         print("fail")
# elif ((a+b)/2)*100==44:
#         print("technical fail")
# else:
#     print("fail")

# Q10 payment 
# a=int(input())
# if a>3000:
#     print(a+300)
# elif a>1600 and a<=3000:
#     s=a*0.10
#     if s>240:
#         print(a+240)
#     else:
#         print(a+(a*0.10))
# else:
#     s=a*0.15
#     if s>100:
#         print(a+100)
#     else:
#         print(a+(a*0.15))

# Q11 steel
# a,b,c=map(int,input().split())
# if a>50 and b>0.7 and c>5600:
#     print(10)
# elif a>50 and b>0.7:
#     print(9)
# elif b>0.7 and c>5600:
#     print(8)
# elif a>50 and c>5600:
#     print(7)
# else:
#     print(0)

# Q12 leap year
# a=int(input())
# if (a%4==0 and a%100!=0) or a%400:
#     print("leap year")
# else:
#     print("not a leap year")

#Q13 leap year
# a=int(input())
# if a%4!=0 and a%100==0:
#     print("not a leap year")
# elif a%400==0:
#     print("leap year")

#Q14 leap year
# a=int(input())
# if a%400==0:
#     print("leap year")
# else:
#     print("not a leap year")

#Q15 triangle
# a,b,c=map(int,input().split())
# if (a+b+c)==180:
#     if a==90 and b==90 and c==90:
#         print("equiangler")
#     elif (a==90) or (b==90) or (c==90):
#         print("right-angled")
#     elif (b<90 and a<90 and c<90):
#         print("acute-angled")
#     elif a<90 and b<90 and c>90:
#         print("obtuse-angled")
#     else:
#         print("invalid")
# else:
#     print("invalid")

# Q16 triangle
# a,b,c=map(int,input().split())
# if a>0 and b>0 and c>0:
#     if a+b>c and b+c>a and c+a>b:
#         if a==b==c:
#             print("equilateral triangle")
#         elif a==b or b==c or a==c:
#             print("isosceles triangle")
#         else:
#             x=a*a
#             y=b*b
#             z=c*c
#             if x+y==z or y+z==x or x+z==y:
#                 print("scalene","\nright-angled")
#             else:
#                 print("scalene")
#     else:
#         print("invalid")
# else:
#     print("invalid")

# Q17 divisible by 11 and 5
# a=int(input())
# if a%5==0 and a%11==0:
#     print("both")
# elif a%5==0 and a%11!=0:
#     print(5)
# elif a%5!=0 and a%11==0:
#     print(11)
# else:
#     print("none")

# Q18 max 
# a,b,c=map(int,input().split())
# print(max(a,b,c))

# Q19 second max
# a,b,c,d=map(int,input().split())
# maxa=0
# smax=0
# if a>b:
#     maxa=a
#     smax=b
#     if c>maxa:
#         smax=maxa
#         maxa=c
#     else:
#         if c>smax:
#             smax=c
#     if d>maxa:
#         smax=maxa
#         maxa=d
#     else:
#         if d>smax:
#             smax=d
# else:
#     maxa=b
#     smax=a
#     if c>maxa:
#         smax=maxa
#         maxa=c
#     else:
#         if c>smax:
#             smax=c
#     if d>maxa:
#         smax=maxa
#         maxa=d
#     else:
#         if d>smax:
#             smax=d
# print(smax)

# Q20 third max
# a,b,c,d=map(int,input().split())
# m=min(a,b,c,d)
# s=[a,b,c,d]
# s.remove(m)
# print(min(s))

#Q21 max occurence
# a,b,c,d,e=map(int,input().split())
# s=[a,b,c,d,e]
# c1=s.count(a)
# c2=s.count(b)
# c3=s.count(c)
# c4=s.count(d)
# c5=s.coiunt(e)
# m=max(c1,c2,c3,c4,c5)
# if m==c1:
#     print(a)
# elif m==c2:
#     print(b)
# elif m==c3:
#     print(c)
# elif m==c4:
#     print(d)
# elif m==c5:
#     print(e)
# else:
#     print("no maximum occurence")