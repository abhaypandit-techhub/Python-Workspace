class animal :
  def animal_sound(self) :
    return print("some sound")
class dog :  
# class dog(animal) :#inheritance
  def sound(self) :
    # super().animal_sound()#calling animal class
    return print("Bark!")
Dog_1=animal()
Dog_2=dog()
Dog_1.animal_sound()
Dog_2.sound()
   