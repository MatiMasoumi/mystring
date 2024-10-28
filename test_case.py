from mystring import MyString
def test_lower():
    my_str=MyString('Hello Python')
    assert my_str.lower() == "hello python","Test for lower() failed."
def test_count_words():
    my_str=MyString("Hello Python from us")
    assert my_str.count_words() ==4,"Test for count_words() failed."
def test_replace():
    my_str=MyString("Hello Python")
    assert my_str.replace("Word Universe") == "HELLO UNIVERSE","Test for replace() failed"
def test_add():
    my_str1=MyString("Hello")
    my_str2=MyString("Python")
    assert my_str1 + my_str2 == "Hello Python","Test for __add__() failed."
def test_mul():
    my_str=MyString("Hello")
    assert my_str * 3 == "Hello-Hello-Hello","Test for __mul__() failed."

if __name__=="__main__":
    test_lower()
    test_count_words()
    test_replace()
    test_add()
    test_mul()
    print("All tests passed.")
    
