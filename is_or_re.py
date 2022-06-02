def option3():
      import menu
      import pymysql as pym
      from datetime import date,datetime,timedelta
      db1 = pym.connect(host = "localhost", user = "root", passwd = "root1", database = "project_library_management")
      cursor = db1.cursor()
      db2= pym.connect(host = "localhost", user = "root", passwd = "root1", database = "project_library_management")
      cursor2 = db2.cursor()
      count=0

      cursor.execute("select* from issue")
      data=cursor.fetchall()
      ais=[]
      for i in data :
            ais.append(i[1])

      cursor.execute("select* from issue")
      data=cursor.fetchall()
      aim=[]
      for i in data :
            aim.append(i[0])

      cursor.execute("select* from books")
      data=cursor.fetchall()
      ab=[]
      for i in data :
            ab.append(i[0])
            

      cursor.execute("select* from members")
      data=cursor.fetchall()
      am=[]
      for i in data :
            am.append(i[0])


      print("1. Issue a book.")
      print("2. Display issued Books")
      print("3. Return a book")
      print("4. Return to main menu")
      print("=========================================================")
      choice = input("Enter a choice from above (1-4)")
      print("=========================================================")

      if choice == "1":
            member=int(input("Enter the id no of member (reqd) : "))
            if member not in am:
                  print()
                  print("NO RECORD WITH THE GIVEN ID NO. EXISTS!!!")
            else:
                  book=int(input("Enter the book code (reqd) : "))
                  if book not in ab:
                        print()
                        print("NO RECORD WITH THE GIVEN BOOK CODE EXISTS!!!")
                  else:
                        st="select qty_purchased from books where b_code={}".format(book)
                        cursor.execute(st)
                        data=cursor.fetchall()
                        q=0
                        for i in data:
                              for j in i:
                                    q=j
                        if q>0:
                              print("Enter date of issue seperately as below : ")
                              dd=int(input("Enter the day (2 digit, reqd.) : "))
                              mm=int(input("Enter the month (2 digit, reqd.) : "))
                              yy=int(input("Enter the year (4 digit, reqd.) : "))
                              datei=date(yy,mm,dd)
                              st="insert into issue values({},{},'{}')".format(member,book,datei)
                              cursor.execute(st)
                              db1.commit()
                              st="update books set qty_purchased=qty_purchased-{} where b_code={}".format(1,book)
                              cursor2.execute(st)
                              db2.commit()
                              print()
                              print("BOOK ISSUED!!!")
                        else:
                              print()
                              print("Book unavailable!!!")
            print("=========================================================")
            
      elif choice == "2":
            st="select issue.b_code, issue.ID_NO, date_of_issue, b_name, author, publisher, S_Name, Class, Section from issue,books,members where(issue.b_code=books.b_code and issue.ID_NO=members.ID_NO)"
            acount=cursor.execute(st)
            if acount==0:
                  print("THERE ARE NO EXISTING RECORDS!!!")
            else:
                  data=cursor.fetchall()
                  co=0
                  for row in data:
                        co+=1
                        print("Record",co)
                        print()
                        print("Book Code = ",row[0])
                        print("ID NO. = ",row[1])
                        print("Date of Issue = ",row[2])
                        print("Book Name = ",row[3])
                        print("Author's Name = ",row[4])
                        print("Publisher's Name = ",row[5])
                        print("Student Name = ",row[6])
                        print("Class  = ",row[7])
                        print("Section = ",row[8])
                        print()
            print("=========================================================")
             
      elif choice=="3":
            member=int(input("Enter the ID NO. of member (reqd) : "))
            if member not in aim:
                  print()
                  print("NO SUCH MEMBER ISSUED A BOOK!!!")
            else:
                  book=int(input("Enter the BOOK CODE (reqd) : "))
                  if book not in ais:
                        print()
                        print("NO SUCH BOOK IS ISSUED!!!")
                  else:
                        st="delete from issue where(b_code={} and id_no={})".format(book,member)
                        cursor.execute(st)
                        db1.commit()
                        st="update books set qty_purchased=qty_purchased+{} where b_code={}".format(1,book)
                        cursor2.execute(st)
                        db2.commit()
                        print()
                        print("BOOK RETURNED!!!")
            print("=========================================================")
            
      elif choice == "4":
            print("RETURNING TO MAIN MENU!!!")
            print("=========================================================")

      else:
            count+=1
            if count<=3:
                  print("Invalid request!!! Please try again.")
                  choice=input("Choose from options (1-4) given above : ")
                  print("=========================================================")
            else:
                  print("Number of wrong attempts exceeded. RETURNING TO MAIN MENU!!!")
                  print("=========================================================")
