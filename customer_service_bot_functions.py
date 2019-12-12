


import string





# Code from A3
def prepare_text(user_input):
    input_list = []
    temp_string = user_input.lower()
    input_list  = temp_string.split()
    return input_list





track_order_input = ['track', 'check', 'delivery', 'update', 'where', 'when']
track_order_output = "On 'Your Orders' page, click the 'Track package' and get the deliver information of your package."
return_order_input = ['return', 'refund', 'back', 'send back', 'replace']
return_order_output = "One 'Your Orders' page and click 'Return or place items' to return your item."
other_info = "Sorry. I can't help you with this problem. Please call 1-888-280-4331 for help."





def start():
    """Print the first message from Amazon online order customer service bot."""

    print("Hi. I'm your Amazon customer service assistant.")
    print('What can I help you about your orders?')




def identify_problem(input_list):
    """Identify what help customers need."""

    identify = False

    #Loop through customer input and print corresponding answer if customer's need is identified
    for word in input_list:
        if word in track_order_input:
            print(track_order_output)
            identify = True
        elif word in return_order_input:
            print(return_order_output)
            identify = True
        break

    #If can't identify customer's need, print contact information of a real customer service agent
    if not identify:
        print(other_info)
    else:
        print('Do you need other help?')

    return







#Modify the code from A3
def end_chat(input_list):
    """Exits out of the chat."""

    global output

    if 'no' in input_list:
        output = True
    elif 'thanks' in input_list:
        output = True
    elif 'bye' in input_list:
        output = True
    else:
        output = False
    return output



#start the chat
def customer_service():

    # Print first message from customer service bot
    start()

    chat = True
    while chat:

        #Get the message from customer
        custom_input = input()

        #Prepare the input message
        msg = prepare_text(custom_input)

        #Check if end the chat
        if end_chat(msg):
            print('Bye. Have a nice day!')
            chat = False
            break


        #Otherwise check customer's problem and respond
        identify_problem(msg)


