class FizzBuzz:
    def convert(self,number):

        result = ""
        
        if number % 3 == 0: 
            result += "Fizz" 

        if number % 5 == 0:
            result += "Buzz"
        
        return result or number

# range of numbers
for i in range(1,100):
    print(FizzBuzz().convert(i))


     