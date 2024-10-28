from mystring import MyString
def main():
    my_str = MyString("Hello Python from MyString")
    print("Lowercase:",my_str.lower())

    print("Number of words:",my_str.count_words())

    replace_str=my_str.replace("Word","Universe")
    print("Replace string:",replace_str)

    my_str2=MyString("How are you?")
    combined_str=my_str + my_str2
    print("Combined Str",combined_str)

    multiplied_str=my_str * 2
    print("multiplied str",multiplied_str)

if __name__=="__main__":
    main()
