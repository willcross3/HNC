import pandas as pd
import numpy as np

#Task 1

#Total Population

#world = pd.read_csv(r"C:\Users\WILLCROSS\Desktop\HNC\pandas\world_population.csv")

#totalpop = world["2022 Population"].sum()

#print("Total population is: ",totalpop)


#Average population

#world = pd.read_csv(r"C:\Users\WILLCROSS\Desktop\HNC\pandas\world_population.csv")

#totalpop = world["2022 Population"].sum()

#totalcountry = len(world["Country"])
#avgpop = totalpop // totalcountry

#print("Average population is: ",avgpop)


#Population Distibution

#world = pd.read_csv(r"C:\Users\WILLCROSS\Desktop\HNC\pandas\world_population.csv")

#totalpop = world["2022 Population"].sum()

#totalcountry = len(world["Country"])
#avgpop = totalpop // totalcountry

#minpop = min(world["2022 Population"])
#maxpop = max(world["2022 Population"])
#medianpop = world["2022 Population"].median()
#quartilepop25 = world["2022 Population"].quantile(0.25)
#quartilepop75 = world["2022 Population"].quantile(0.75)


#print("Population distibution of the world: ")
#print("Minimum popultaion: ",minpop)
#print("Maximum popultaion: ",maxpop)
#print("Median popultaion: ",medianpop)
#print("Quartile popultaion: ","\n25%:",quartilepop25, "\n75%:",quartilepop75 )


#Task 2

#Top 10 countries by population

#world = pd.read_csv(r"C:\Users\WILLCROSS\Desktop\HNC\pandas\world_population.csv")

#pd.set_option('display.float_format', '{:.0f}' .format)

#population = world[["Country", "2022 Population"]]

#top10 = population.nlargest(10,"2022 Population")

#print("The countries with the top 10 poplulations are: ", top10)


#Top 10 countries with the lowest population

#world = pd.read_csv(r"C:\Users\WILLCROSS\Desktop\HNC\pandas\world_population.csv")

#pd.set_option('display.float_format', '{:.0f}' .format)

#population = world[["Country", "2022 Population"]]

#top10 = population.nsmallest(10,"2022 Population")

#print("The countries with the top 10 smallest poplulations are: ", top10)


#Percentage of population each country holds

#world = pd.read_csv(r"C:\Users\WILLCROSS\Desktop\HNC\pandas\world_population.csv")

#world = pd.DataFrame(world, columns = ["Country", "2022 Population"])

#world["Percentage share"] = (world["2022 Population"] / world["2022 Population"].sum()) * 100
 
#pd.set_option('display.max_rows', None)  
#pd.set_option('display.max_columns', None)  


#print(world[["Country", "2022 Population", "Percentage share"]].sort_values("Percentage share", ascending=False)) 


#Task 3 

#Population by continent

world = pd.read_csv(r"C:\Users\WILLCROSS\Desktop\HNC\pandas\world_population.csv")


