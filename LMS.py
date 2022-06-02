print()
print("===============================================LIBRARY MANAGEMENT==========================================================================")
import menu as a
import book_op as b
import mem_op as c
import is_or_re as d
count=0
choice=a.menu()
print("=========================================================")
while choice !="4":
      if choice=="1":
            b.option1()
            choice=a.menu()
            print("=========================================================")
      elif choice=="2":
            c.option2()
            choice=a.menu()
            print("=========================================================")
      elif choice=="3":
            d.option3()
            choice=a.menu()
            print("=========================================================")
      else:
            count+=1
            if count<=3:
                  print("Wrong Option!!!!! Please Try Again.")
                  print("=========================================================")
                  choice=a.menu()
            else:
                  print("ABORTING, as Number of allowed wrong inputs exceeded!!!! Run Again For Reuse.")
                  break
            
else:
      print("Thanks for coming, Run again for reuse.")
      print("=========================================================")

