
#!! Cada décimo paso (stepNumber % 10 == 0) es un 10% más largo a menos que provenga de un CityId primo.

library(tidyverse)
library(primes)
library(dplyr)
library(data.table)

cities <- data.frame(fread("C:/Users/Enric/PycharmProjects/caminos_cortos/data/cities.csv"))

dim(cities)
str(cities)

# Ploting X and Y to see their behaviour.
cities %>% 
  ggplot(aes(x=X, y=Y))+
  geom_point(shape = ".", alpha="0.75")


# Since we need to know which cities are "prime", let's create a new column with 1 for prime and 0 
# for non-prime cities.
cities <- cities %>% 
  mutate('Prime'=ifelse(is_prime(CityId),1,0))

head(cities)

#10% of the cities are prime
prop.table(table(cities$Prime))

cities %>% select(Prime) %>% summarize(Total = sum(Prime), Proportion=mean(Prime))

#We can see that almost 10% of the cities (17,802) are "primes". Since we need a prime city each 10th step, this could be a good thing.

# Let's plot out dataset again but including the Prime cities.

cond <- ifelse(cities$Prime==1, "red", "black") # a condition to make the prime cities points colour red.
cities %>% 
  ggplot(aes(x=X, y=Y))+
  geom_point(shape = ".", alpha="0.75", colour=cond)

#Let´s take a look only to Prime cities

cond2 <- ifelse(cities$Prime==1, "red", "white")
cities %>% 
  ggplot(aes(x=X, y=Y))+
  geom_point(shape = ".", alpha="1", colour=cond2)

#Prime cities not only correspond to (almost) 10% of the cities but they also seem to be very well distributed along the "map"

####---###




