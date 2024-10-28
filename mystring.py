
class MyString(str):
    
    def lower(self):

        """
        converts the string to lowercase an appends an axclamation mark (!).

        """
        return super().lower() + "!"
    def count_words(self):

        """
        Count and return the number of words in the string.
        words are separated by space.
        
        """
        return len(self.split())
    def replace(self,old,new,count=-1):

        """
        Replace occurrences of 'old'  with 'new' after converting the string to 
        uppercase.

        """
        return super().upper().replace(old.upper(),new.upper(),count)
    def __add__(self,other):

        """
        Override the  + operator to insert a space between MtString object
        when concatenating.
        """
        if isinstance(other,MyString):
            return MyString(super().__add__(" " + other))
        return MyString(super().__add__(other))
    def __mul__(self,n):

        """
        Override the operator to report the string with a dash (-) separating
        each repetition.
        """
        return MyString((self + "-") * (n-1) + self) if n > 0 else MyString("")




