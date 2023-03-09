from population import Population


generation = 0;


population = Population(150)


lastFittest = -1;


while generation < 100 and lastFittest < population.fittest: 

  generation += 1
  
  print(f'Generation[{generation}] - fittest({population.fittest})')
  
  population.calcPopulationFitness()
  
  parents = population.selectParents()


  firstParent = parents[0]

  secondParent = parents[1]
  
  if firstParent.fittest < secondParent.fittest:
    population.fittest = firstParent.fittest
  else:
    population.fittest = secondParent.fittest

  children = population.applyCrossing(firstParent, secondParent)
  
  lessFitIndex = population.getLessFit()

  population.cromossomos[lessFitIndex] = children
  





