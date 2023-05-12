from abc import ABC,abstractmethod
import random

def show_message(message:str):
    print(f"{message}")
   
class Unit(ABC):
    """
    Abstract class that represents a unit
    """ 
    
    def __init__(self, name:str) -> None:
        """Initializes an instance of the Unit class

        Args:
           protected name (str): The name of the unit
           protected alive (bool): the unit is alive?
           protected hp (int): hp points
        """
        self._name = name
        self._alive = True
        self._hp = 40
    
    @property
    def name(self):
        return self._name
    
    @property
    def hp(self):
        return self._hp
    
    # @hp.setter
    # def hp(self,points:int):
    #     self._hp = points
    #     show_message(f"{self.name} now has {self._hp} hit points")
        
    def move(self,direction:str):
        """ Moves the unit in a specific direction.

        Args:
             direction (str): The specific direction in which the unit is moving.
        """
        show_message(f'{self._name} walks to {direction}')
        
    @abstractmethod
    def attack(self,enemy:'Unit'):
        """Abstract Method for enemy attacks

        Args:
            enemy (str): the name of the enemy being attacked
        """
        pass
    
    def take_damage(self,damage:int):
        self._hp -=  self.absorbDamage(damage)
        show_message(f"{self.name} now has {self._hp} hit points")
        if self._hp <= 0 :
            self.die()
            exit()
    
    def die(self):
        show_message(f"{self.name} dies")
    
    def absorbDamage(self,damage:int):
        return damage


class Soldier(Unit):
    """Represent a Solidier class
    """
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._damage = 40
        self._armor = None 
    
    @property
    def damage(self):
        return self._damage
    
    @damage.setter
    def damage(self,damage):
        self._damage = damage
        
    @property
    def armor(self):
        return self._armor
        
    @armor.setter
    def armor(self,armor:'Armor'):
        self._armor = armor
        
    def attack(self, enemy):
        show_message(f'{self._name} cuts {enemy.name}')
        enemy.take_damage(self._damage)
    
    # def take_damage(self, damage: int):
    #     return super().take_damage(damage / 2)
    def absorbDamage(self,damage: int):
        
        if self._armor :
            damage = self.armor.absorbDamage(damage)
        return damage
    
class Archer(Unit):
    """Represent an Archer class
    """
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._damage = 20
    
    def attack(self, enemy):
         show_message(f'{self._name} shoots an arrow to {enemy.name}')
         enemy.take_damage(self._damage)
    
    # def take_damage(self, damage: int):
    #     if random.randrange(2) == 1:
    #         super().take_damage(damage)

#interface Armor
class Armor(ABC):
    @abstractmethod
    def absorbDamage(self,damage:int):
        pass

class BronzeArmor(Armor):
    
    def absorbDamage(self,damage:int):
        return damage // 2

armor = BronzeArmor()
           
marcus = Soldier('Marcus')

skorge = Archer('Skorge')

skorge.attack(marcus)

marcus.armor = armor

skorge.attack(marcus)

marcus.attack(skorge)