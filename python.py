# def encrypt():
#     phrase = input('enter message: ')
#     print(phrase[::-1])
# encrypt()

def encrypt ():
    phrase = input("enter a phrase : ")
    new_list = ""
    counter = 0 
    for i in range(len(phrase)):
        counter = counter -1
        new_list = new_list + (phrase[counter])
    print(new_list)
    
encrypt()