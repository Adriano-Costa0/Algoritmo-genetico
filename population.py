from cromossomo import Cromossomo;
import random


class Population:

  def __init__(self, size):
    self.cromossomos = []
    self.fittest = 0;
    self.generatePopulation(size)
  

  def generatePopulation(self, size):
    for index in range(size):
        cromossomo = Cromossomo(14)
        self.cromossomos.append(cromossomo)
        
  def getLessFit(self):
    lessfit = 0
    for index in range(0, len(self.cromossomos)):
      itemFittest = self.cromossomos[index].fittest 
      itemLessfit = self.cromossomos[lessfit].fittest
      if(itemFittest < itemLessfit):
        lessfit = index
    return lessfit
      

  def selectParents(self):
    parents = self.selectFittest()
    return parents
    

  def selectFittest(self):
    firstMaxFittestIndex = 0
    secondMaxFittestIndex = 0
    
    
    for index in range(len(self.cromossomos)):
      item = self.cromossomos[index]
      if item.fittest > self.cromossomos[firstMaxFittestIndex].fittest and item.capacity <= 3:
        secondMaxFittestIndex = firstMaxFittestIndex
        firstMaxFittestIndex = index
      elif item.fittest > self.cromossomos[secondMaxFittestIndex].fittest and item.capacity <= 3:
        secondMaxFittestIndex = index

    return [self.cromossomos[firstMaxFittestIndex], self.cromossomos[secondMaxFittestIndex]]
  
  def applyCrossing(self, firstParent, secondParent):
    cutIndex = random.randint(0, 13);
    
    firstChild = Cromossomo(14)
    secondChild = Cromossomo(14)
    
    for index in range(cutIndex):
      copy = firstParent.genes[index]
      
      firstChild.genes[index] = secondParent.genes[index]
      secondChild.genes[index] = copy
      
    percentOfmutation = random.randint(1, 100)
    
    if percentOfmutation <= 100 :
      return self.applyMutation(firstParent, secondParent)
    
    if firstChild.fittest > secondChild.fittest:
        return firstChild
    return secondChild

  def applyMutation(self, firstChild, secondChild ):
    
    for index in range(0,3):
      randomIndex = random.randint(0, 13)
      
      if firstChild.fittest > secondChild.fittest:
        if secondChild.genes[randomIndex] is 1:
          secondChild.genes[randomIndex] = 0
        else:
          secondChild.genes[randomIndex] = 1
      else:
        if firstChild.genes[randomIndex] is 1:
          firstChild.genes[randomIndex] = 0
        else:
          firstChild.genes[randomIndex] = 1
          
      if firstChild.fittest > secondChild.fittest:
        return firstChild
      return secondChild
  
  def calcPopulationFitness(self):
    for item in self.cromossomos:
      item.calcWeight()
