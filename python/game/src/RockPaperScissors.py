class RockPaperScissors:
    
    options = ('rock', 'paper', 'sicssors')
    
    computer_wins = 0
    
    user_wins = 0
    
    round = 1

    def __init__(self):
        start = input("Do you want to start the game y/n-> ")
        
        if start == "y":
            
            print(self.start())
    
    def start(self):
        
        option = input("choice your option ")
        
        if not option in self.options:
            return "this option is not valid"
        
        self.compare(option,'sicssors')
    
    def compare(self,inputuser,inputpc):
        
        print(self.tie(inputuser,inputpc))
        # self.user_win(self,inputuser,inputpc)
        # self.pc_win(self,inputuser,inputpc)
            
    # def user_win(self,inputuser,inputpc):
    #     if inputuser == 'rock':
    #         if inputpc == 'sicssors':             
    #             return 'user win'
    #     return False      
    
    # def pc_win(self,inputuser,inputpc):
    #     if inputuser == 'rock':
    #         if inputpc == 'papper':             
    #             return 'pc win'
    #     return False  
    
    def tie(self,inputuser,inputpc):
        
        if inputuser == inputpc:
        
            return 'tie'
  
print(RockPaperScissors())