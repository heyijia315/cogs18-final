
from my_module.customer_service_bot_functions import *



test_string = 'return my order'
test_list1 = ['return', 'my', 'order']
test_list2 = ['I', 'want', 'to', 'buy', 'snacks']





#Test function prepare_text function
def test_prepare_text():
    #test function for prepare text function
    assert callable(prepare_text)
    assert isinstance(prepare_text(test_string), list)
    assert prepare_text(test_string) == ['return', 'my', 'order']





#Test funtion for end_chat function
def test_end_chat():
    assert callable(end_chat)
    assert isinstance(end_chat(test_string), bool)
    assert end_chat(test_string) == False




#Test for identify_problem function
def test_identify_problem():
    assert callable(identify_problem)
    assert identify_problem(test_list2) == print("One 'Your Orders' page and click 'Return or place items' to return your item."
                                                    + 'Do you need other help?')
    assert identify_problem(test_list2) == print("Sorry. I can't help you with this problem. Please call 1-888-280-4331 for help.")
