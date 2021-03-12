abc = "abcdefghijklmnopqrstuvwxyz"
abc_list = list(abc)
# print(abc_list)

def encrypt_2 ():
    message = input("enter your message : ")
    counter = 3
    result = ""
    for i in range((len(message))):
       counter = counter + 1
       result = result+ (message[counter])
    print(result)

encrypt_2()