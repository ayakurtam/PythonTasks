######## ITIan Store #######
shop = {"products":[["apples",100,"Cost in EGP =",50],["bannaa",100,"Cost in EGP =",26],["cherry",100,"Cost in EGP =",140]]}
while(1):
	print("------------Welcome to ITI  Grosery shop------------")
	print("1- Customer")
	print("2- Admin")
	print("3- Exit")
	choice = int (input(" 1-Customer  , 2-Admin  , 0 Exit "))
	if choice == 1:
		print("Welcome Dear Customr")
		print(" Press 1 To Show products")
		print(" Press 2 To Buy products")
		print(" Press 0 To Exit")
		option1 =int(input(" Your Choice: "))
		if option1 ==1:
			print(shop)
		elif option1 ==2:
			sum=0
			print(my_shop)
			To_buy_list=input("please enter the number of product you wanna buy seperatd by space :").split(" ")
			x=0
			for i in To_buy_list:									
				value=int(shop["products"][x][1])														
				if int(y) > int(shop["products"][x][1]):		 
					print(" your request is out of stock "+str(y))
				else:
					value = value-(int(y))							
					shop["products"][x][1] = value				
					price=int(shop["products"][x][3])		
					sum=sum+(price)*(int(y))					
					x+=1										
					
			print("your total bill value is ="+str(sum)+"EGP")		
			print(shop)
		elif option1 ==0:
			print("Thank you")
		else:
			print("invalid choice")
	elif choice ==2:
		print("Welcome Admain")
		print("1- To Add new product ")
		print("2- To Show products")
		print("3- To Change cost")
		print("4- To delete product")	
		print("5- Exit")
		option2 =int(input("Enter your choice :"))
		if option2 ==1:
			print("Warnning!! be  careful during entering products details")
			add=input("Enter the product name ,stock , Cost in EGP = , cost Seperated by space :").split(" ")
			shop["products"].append(add)	
		elif option2==2:
			print(shop)
		elif option2==3:
			product_name =input(" name of the product to change its price :")		
			for y in shop["products"]:					
				if product_name == y[0]:						
					new_cost =input("please enter the new cost :")
					y[3]= new_cost						
				else:
					print("product name not found")
					break;
		elif option2==4:
			product =input(" product name to delete :")
			removed=0										
			for i in shop["products"]:					
				if product == y[0]:							 	
					shop ["products"].remove(y)			
					removed =1								
					break;		
			if removed ==0:					
				print("product name not found")
			else:	
				print("removed succefully")	
		elif option2==0:
			print("thank you !")		
		else:
			print("invalid choice")			
	elif choice ==0:	
		print("thank you ")
	else :
		print("invalid choice")