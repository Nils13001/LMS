def option2():
      import menu
      import pymysql as pym
      db=pym.connect(host="localhost",user="root",passwd="root1",database="project_library_management")
      cursor=db.cursor()
      count=0

      #checking redundancy of id_no
      cursor.execute("select* from members")
      data=cursor.fetchall()
      a=[]
      for i in data :
            a.append(i[0])

      #checking presence of data in child table(issue)
      cursor.execute("select * from issue")
      data1=cursor.fetchall()
      ai=[]
      for i in data1:
            ai.append(i[1])
            
      print("1. Adding member record")
      print("2. Searching member record")
      print("3. Updating member record")
      print("4. Deleting member record")
      print("5. Displaying member record")
      print("6. Return to main menu")
      print("=========================================================")
      choice=input("Choose from options (1-6) given above : ")
      print("=========================================================")
      
      if choice=="1":
            a1=int(input("Enter ID no. (5-digit, reqd.) : "))
            if a1 in a:
                  print()
                  print("Record with given ID NO. already exists. Returning to main menu!!")
            else:
                  b1=input("Enter member name (reqd) : ")
                  c1=int(input("Enter class (in digits, reqd) : "))
                  d1=input("Enter section (reqd.)  :")
                  st="insert into members values({},'{}',{},'{}')".format(a1,b1,c1,d1)
                  cursor.execute(st)
                  db.commit()
            print()
            print("RECORD SUCCESSFULLY INSERTED!!!")
            print("=========================================================")
            
      elif choice=="2":
            code=int(input("Enter the id no. of the member to be searched for : "))
            if code in a:
                  st="select * from members where ID_NO={}".format(code)
                  cursor.execute(st)
                  data=cursor.fetchall()
                  for row in data:
                        print()
                        print("ID NO. = ",row[0])
                        print("Student Name = ",row[1])
                        print("Class  = ",row[2])
                        print("Section = ",row[3])
                        print()
            else:
                  print()
                  print("RECORD WITH GIVEN ID_NO DOES NOT EXIST!!!")
            print("=========================================================")

      elif choice=="3":
            print("Name of Columns are : 'ID_NO', 'S_Name', 'Class', 'Section' ")
            print()
            number= int(input("Enter the no. of columns you want to update : "))
            for i in range(number):
                  col=input("Enter column's name : ")
                  if col in ["ID_NO"]:
                        d=int(input("Enter the new data : "))
                        if d not in a :
                              c=int(input("Enter ID_NO  : "))
                              if c not in ai:
                                    st="update members set {}='{}' where ID_NO={} ".format(col,d,c)
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
                                          st="delete from issue where ID_NO={}".format(c)
                                          cursor.execute(st)
                                          st="update members set {}='{}' where ID_NO={} ".format(col,d,c)
                                          cursor.execute(st)
                                          db.commit()
                                          print("RECORD UPDATED!!!")
                                    elif choice2=="n":
                                          print("Accepted!!! Returning to main menu.")
                                    else:
                                          print("INVALID CHOICE!!! RETURNING TO MAIN MENU.")
                        else:
                              print()
                              print("INVALID UPDATION, As it will lead to duplicate data in ID_NO which is not allowed.")                        
                  elif col in ["S_Name","Class","Section"]:
                        d=input("Enter new data : ")
                        c=int(input("Enter ID NO. : "))
                        st="update members set {}='{}' where ID_NO={} ".format(col,d,c)
                        cursor.execute(st)
                        print()
                        print("Record Updated!!!")
                  else:
                        print()
                        print("INVALID ATTRIBUTE NAME FOR BOOKS TABLE")
            db.commit()
            print("=========================================================")
      
      elif choice=="5":
            count=cursor.execute("select * from members")
            if count==0:
                  print("THERE ARE NO EXISTING RECORDS!!!")
            else:
                  data=cursor.fetchall()
                  co=0
                  for row in data:
                        co+=1
                        print("Record",co)
                        print()
                        print("ID NO. = ",row[0])
                        print("Student Name = ",row[1])
                        print("Class  = ",row[2])
                        print("Section = ",row[3])
                        print()
            print("=========================================================")
                  
      elif choice=="4":
            code=int(input("Enter the ID NO. of member whose record you want to delete : "))
            if code in a and code not in ai:
                  st="delete from members where ID_NO={}".format(code)
                  cursor.execute(st)
                  db.commit()
                  print()
                  print("RECORD DELETED!!!")
            elif code not in a:
                  print()
                  print("NO RECORD WITH THE GIVEN ID NO. EXISTS!!!")
            elif code in ai:
                  print("INVALID REQUEST!!! The member has issued a book.")
                  print()
                  choice2=input("Delete above provided member's issue record also? [y/n] : ")
                  if choice2=="y":
                        st1="delete from issue where id_no={}".format(code)
                        cursor.execute(st1)
                        st="delete from members where ID_NO={}".format(code)
                        cursor.execute(st)
                        db.commit()
                        print()
                        print("RECORD DELETED!!!")
                  elif choice2=="n":
                        print()
                        print("Accepted!!! Returning to main menu.")
                  else:
                        print()
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

