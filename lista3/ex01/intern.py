class Itern():

    def __init__(self, Name = "My name? I’m nobody, an intern, I have no name.") -> None:
        self.Name = Name

    def __str__(self) -> str:
        return self.Name

    class Coffe():

        def __str__(self) -> str:
            return "This is the worst coffee you ever tasted."

    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")
    
    def make_coffee(self):
        return(self.Coffe())

if __name__ == '__main__':
    no_name_intern = Itern()
    print(no_name_intern)
    Mark = Itern("Mark")
    print(Mark) 
    print(f"Mark could you make a coffe? {Mark.make_coffee()}")
    print(f"no_name_intern could you make a coffe? {no_name_intern.make_coffee()}")
    try:
        Mark.work()
    except Exception as e:
        print(f"Mark exception {e}")