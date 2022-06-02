def option1():
      import menu
      import pymysql as pym
      from datetime import date, datetime, timedelta
      db=pym.connect(host="localhost",user="root",passwd="root1",database="project_library_management")
      cursor=db.cursor()
      count=0
      
      #checking redundancy of b_code, book name and author's name(for corresponding book)
      cursor.execute("select* from books")
      data=cursor.fetchall()
      a=[]
      b=[]
      c=[]
      for i in data :
            a.append(i[0])
            b.append(i[1])
            c.append(i[2])

      cursor.execute("select* from issue")
      data=cursor.fetchall()
      ai=[]
      for i in data :
            ai.append(i[1])

      print("1. Adding book record")
      print("2. Searching book record")
      print("3. Updating book record")
      print("4. Deleting book record")
      print("5. Displaying book record")
      print("6. Return to main menu")
      print("=========================================================")
      choice=input("Choose from options (1-6) given above : ")
      print("=========================================================")

      if choice=="1":
            a1=int(input("Enter book code(3-digit, reqd.) : "))
            if a1 in a:
                  print()
                  print("Record with given BOOK CODE already exists. Returning to main menu!!")
            else:
                  b1=input("Enter book name(reqd.) : ") 
                  c1=input("Enter author name(reqd.) : ")
                  if b1 in b:
                        if c1 in c:
                              print()
                              print("ATTEMPTED TO INSERT SAME DATA WITH A DIFFERENT BOOK CODE!!! ")
                        else:
                              d1=float(input("Enter book price(reqd.) : "))
                              e1=input("Enter book publisher(reqd.) : ")
                              f1=input("Enter date of purchase(YYYY-MM-DD) : ")
                              g1=int(input("Enter qty purchased : "))
                              st="insert into books values({},'{}','{}',{},'{}','{}',{},{})".format(a1,b1,c1,d1,e1,f1,g1)
                              cursor.execute(st)
                              print()
                              print("RECORD SUCCESSFULLY INSERTED!!!")
                  else:
                        d1=float(input("Enter book price(reqd.) : "))
                        e1=input("Enter book publisher(reqd.) : ")
                        f1=input("Enter date of purchase(YYYY-MM-DD) : ")
                        g1=int(input("Enter qty purchased : "))
                        st="insert into books values({},'{}','{}',{},'{}','{}',{},{})".format(a1,b1,c1,d1,e1,f1,g1)
                        cursor.execute(st)
                        print()
                        print("RECORD SUCCESSFULLY INSERTED!!!")
                  db.commit()                  
            print("=========================================================")
          
      elif choice=="2":
            code=int(input("Enter the code of the book to be searched for : "))
            print()
            if code in a:
                  st="select * from books where b_code={}".format(code)
                  cursor.execute(st)
                  data=cursor.fetchall()
                  for row in data:
                        print("Book Code = ",row[0])
                        print("Book Name = ",row[1])
                        print("Author's Name = ",row[2])
                        print("Publisher's Name = ",row[4])
                        print("Book Price = ",row[3])
                        print("Date of purchase = ", row[5])
                        print("Quantity Purchased = ", row[6])
                        print()
            else:
                  print()
                  print("RECORD WITH GIVEN BOOK CODE DOES NOT EXIST!!!")
            print("=========================================================")
          
      elif choice=="3":
            print("Name of Columns are : 'b_code', 'b_name', 'author', 'b_price', 'publisher', 'date_of_purchase', 'qty_purchased' ")
            print()
            number= int(input("Enter the no. of columns you want to update : "))
            for i in range(number):
                  col=input("Enter column's name : ")
                  if col in ["b_code"]:
                        d=int(input("Enter the new data : "))
                        if d not in a :
                              c=int(input("Enter book code  : "))
                              if c not in ai:
                                    st="update books set {}='{}' where b_code={} ".format(col,d,c)
                                    cursor.execute(st)
                                    print()
                                    print("Record Updated!!!")
                              else:
                                    print()
                                    print("INVALID REQUEST!!! The book is already issued. To do so, delete issued books record.")
                                    print()
                                    choice2=input("Delete above provided book's issued record also? [y/n] : ")
                                    print()
                                    if choice2=="y":
                                          st="delete from issue where b_code={}".format(c)
                                          cursor.execute(st)
                                          st="update books set {}='{}' where b_code={} ".format(col,d,c)
                                          cursor.execute(st)
                                          db.commit()
                                    elif choice2=="n":
                                          print("Accepted!!! Returning to main menu.")
                                    else:
                                          print("INVALID CHOICE!!! RETURNING TO MAIN MENU.")
                        else:
                              print()
                              print("INVALID UPDATION, As it will lead to duplicate data in b_code which is not allowed.")                        
                  elif col in ["b_price","qty_purchased","b_name","author","publisher","date_of_purchase"]:
                        d=input("Enter new data : ")
                        c=int(input("Enter book code : "))
                        st="update books set {}='{}' where b_code={} ".format(col,d,c)
                        cursor.execute(st)
                        print()
                        print("Record Updated!!!")
                  else:
                        print()
                        print("INVALID ATTRIBUTE NAME FOR BOOKS TABLE")
            db.commit()
            print("=========================================================")
          
      elif choice=="5":
            a=cursor.execute("select * from books")
            if a==0:
                   print("THERE ARE NO EXISTING RECORDS!!!")
            else:
                  data=cursor.fetchall()
                  co=0
                  for row in data:
                        co+=1
                        print("Record",co)
                        print()
                        print("Book Code = ",row[0])
                        print("Book Name = ",row[1])
                        print("Author's Name = ",row[2])
                        print("Publisher's Name = ",row[4])
                        print("Book Price = ",row[3])
                        print("Date of purchase = ", row[5])
                        print("Quantity Purchased = ", row[6])
                        print()
            print("=========================================================")
          
      elif choice=="4":
            code=int(input("Enter the BOOK CODE of book whose record you want to delete : "))
            print()
            if code in a and code not in ai:
                  st="delete from books where b_code={}".format(code)
                  cursor.execute(st)
                  db.commit()
                  print()
                  print("RECORD DELETED!!!!")
            elif code not in a:
                  print("NO RECORD WITH THE GIVEN BOOK CODE EXISTS!!!")
            elif code in ai:
                  print("INVALID REQUEST!!! The book is already issued.")
                  print()
                  choice2=input("Delete above provided book's issued record also? [y/n] : ")
                  print()
                  if choice2=="y":
                        st1="delete from issue where b_code={}".format(code)
                        cursor.execute(st1)
                        st="delete from books where b_code={}".format(code)
                        cursor.execute(st)
                        db.commit()
                        print("RECORD DELETED!!!")
                  elif choice2=="n":
                        print("Accepted!!! Returning to main menu.")
                  else:
                        print("INVALID CHOICE!!! RETURNING TO MAIN MENU.")
            print("=========================================================")
            
      elif choice=="6":
            print("RETURNING TO MAIN MENU!!!")
            print("=========================================================")

      else:
            count+=1
            if count<=3:
                  print("Invalid request!!! Please try again.")
                  choice=input("Choose from options (1-6) given above : ")
                  print("=========================================================")
            else:
                  print("Number of wrong attempts exceeded. RETURNING TO MAIN MENU!!!")
                  print("=========================================================")
            

