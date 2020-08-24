#FEUMI163 UMAIR MOHAMED FEROZE PROGRAMMING PRINCIPLES
#Assignment("Golf Club")

#Create an empty list
name_list=[]
score_list=[]

while True:
    #Welcome the user and display the menu.
    print('\n\t Welcome to Springfield Golf Club')   
    print('\t Select Options:')
    print('\t 1) Enter Scores')
    print('\t 2) Find Golfer')
    print('\t 3) Display Scoreboard')
    print('\t 4) Exit Program')

    #Enter the desired input.
    option=int(input('\n Enter your desired option:'))
    #Error message incase invalid option entered.
    if option<1 or option>4:
        print('\t *Invalid input.!Please enter a valid option..!*')
   
    #Option 1: Enter Scores
    if option==1:
        print('\n Enter Scores \n ------------')
        count=1
        no_golf=int(input('\t Enter the number of golfers:')) #Prompt user to enter number of golfers.
        while count<=no_golf:
            name=input('\n\t Enter Golfer Name: ')#Prompt user to enter name.
            if name not in name_list:
                name_list.append(name)
                score=float(input('\t Enter Score: '))#Prompt user to enter score.
                #Validation for score.
                if score<18 or score>108:           
                    print('\n*Error, Enter a score in between 18 and 108..!*')#Error message if score is not in range.
                    print('\t*PLease re enter name and score.!*')
                    count=count-1
                    score_list.append(score)
                else:
                    score_list.append(score) 

            else:
                proceed='y'  #Variable to control the loop/conditon.              
                proceed=input('\t *The name already exists,Enter y'+
                              ' if you want to continue*:')
                if proceed =='y':
                    score=float(input('\t Enter Score: ')) #Prompt user to enter score
                    if score<18 or score>108:
                        print('\t *Error, Enter a score in between 18 and 108..!*')#Error message if score si not in range.
                        print('\t*PLease re enter name and score.!*')
                        count=count-1
                        score_list.append(score)
                    else:
                        item_index=name_list.index(name)
                        score_list[item_index]=score
            count=count+1
            
    #Option 2: Find Golfer
    elif option==2:
        print('\n Find Golfer \n ------------')
        name=input('\n \t Enter the name of the Golfer: ') #Prompt user to enter Golfer name.
        if name in name_list:
            item_index=name_list.index(name)
            print("\n \t Name \t\t Score \n\t ----------------------")
            print('\t',name,' \t',score_list[item_index])#Print name and score of golfer.
        else:
            print('\t      *Error..Name not in name list..!*')#Print error message
        

    #Option 3
    elif option==3:
        print('\n Display Scoreboard \n ------------------')
        length=len(name_list)
        index=0
        print("\n \t Name \t\t Score \n\t -----------------------")
        while index!=length:           
            score_list,name_list=zip(*sorted(zip(score_list,name_list))) #sort the two lists
            print('\t',name_list[index],'  \t',score_list[index]) #print scoreboard
            index=index+1

    #Option 4
    elif option==4:
        exit()
    
   
       
