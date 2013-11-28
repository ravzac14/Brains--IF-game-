#brains.py
#Zack Raver
#Start Date: 11/26/13
import sys
from pyf import items, game, interface, props


##################################### Playable Character #######################
whichGame = raw_input("Which character would you like to play as: Rick Grimes(Sweet), Brandon Conchobhair(Mild), Steve Butler(Medium), Zack Raver(Hotasfuck)?\n")
if whichGame=="Rick" or "Rick Grimes" or "rick" or "sweet" or "easy":
    class rickGame(game.Game):
        pass
elif whichGame=="Brandon" or "Brandon Conchobhair" or "brandon" or "mild" or "normal" or "concho":
    class brandonGame(game.brandonGame):
        pass
elif whichGame=="Steve" or "Steve Butler" or "steve" or "medium" or "hard":
    class steveGame(game.steveGame):
        pass
elif whichGame=="Zack" or "Zack Raver" or "zack" or "hot" or "hotasfuck" or "legendary":
    class zackGame(game.zackGame):
        pass
else:
    print "Not a valid character, please restart the game and try again!"
    sys.exit(0)

##class Game(game.Game):
  ##  pass
        
################################# Hospital Grounds Classes #####################
class DocOffice(items.Room):
    pass

class DocHallOne(items.Room):
    pass

class NurseStation(items.Room):
    pass
    
class DocStairwell(items.Room):
    pass

class EROne(items.Room):
    pass

class Jibs(items.Room): 
    pass

class ERWaitingRoom(items.Room):
    pass
    
class HospitalParkingLot(items.Room):
    pass
    
class HospAmbulance(items.Room):
    pass
    
class JibsAmbulance(items.Room):
    pass

class PharmacyParkingLot(items.Room):
    pass
    
class JibsParkingLotExit(items.Room):
    pass
    
class GrocerParkingLot(items.Room):
    pass
    
class GrocerAmbulance(items.Room):
    pass
    
class PharmacySalesFloor(items.Room):
    pass
    
class PharmacyBehindCounter(items.Room):
    pass
    
class GrocerEntrance(items.Room):
    pass
    
class ProduceSection(items.Room):
    pass
    
class TwinkiesSection(items.Roon):
    pass

class Butchery(items.Room):
    pass

######################### MAIN STREET CLASSES ##################################
class MainStreetOne(items.Room):
    pass
    
class MainStreetTwo(items.Room):
    pass

class MainStreetThree(items.Room):
    pass
    
class MainStreetFour(items.Room):
    pass
    
class MainStreetFive(items.Room):
    pass
    
class MainStreetSix(items.Room):
    pass

class MainStreetSeven(items.Room):
    pass
    
class MainStreetEight(items.Room):
    pass
    
class MainStreetNine(items.Room):
    pass
    
class MainStreetTen(items.Room):
    pass
    
class CountryRoadOne(items.Room):
    pass
    
class CountryRoadTwo(items.Room):
    pass
    
class CountryRoadThree(items.Room):
    pass
    
class MilitarySafeZone(items.Room):    ###Ending Possibility############################
    pass
    
############################ 1st Avenue Classes ################################
class FirstAveOne(items.Room):
    pass
    
class FirstAveTwo(items.Room):
    pass
    
class FirstAveThree(items.Room):
    pass
    
class FirstAveFour(items.Room):
    pass
    
class FirstAveFive(items.Room):
    pass
    
class FirstAveSix(items.Room):
    pass
    
class FirstAveSeven(items.Room):
    pass
    
class FirstAveEight(items.Room):
    pass

########################### 2nd Avenue Classes #################################
class SecAveOne(items.Room):
    pass
    
class SecAveTwo(items.Room):
    pass
    
class SecAveThree(items.Room):
    pass
    
class SecAveFour(items.Room):
    pass
    
class SecAveFive(items.Room):
    pass
    
class EmergencyStreetExit(items.Room): ##SecAveSix
    pass
    
class SecAveSeven(items.Room):
    pass
    
class SecAveEight(items.Room):
    pass

########################### Alley Classes ######################################
class AlleyOne(items.Room):
    pass
    
class AlleyTwo(items.Room):
    pass
    
class AlleyThree(items.Room):
    pass
    
class AlleyFour(items.Room):
    pass
    
class AlleyFive(items.Room):
    pass

########################### Boardwalk Classes ##################################

########################### Zoo Classes ########################################

################################## Mansion/Houses Classes ######################

###############################Elementary School Classes #######################

############################# Forrest/Graveyard Classes ########################

############################# Hills/ Lake/ Cabin Classes #######################

############################# Construction Site/ Field Classes #################

################################ Actors ########################################
class Rick(items.Actor):
    pass
    

#################################### Items #####################################
class DocKey(items.Item):
    pass

class DocCabinet(items.Item):
    pass

class HosGown(items.Item):
    pass
    

##################### Create Game and Interface from brains.script.xml #########
game = game.createFromScript(open('brains.script.xml'), locals())
if whichGame=="Rick" or "Rick Grimes" or "rick" or "sweet" or "easy":
    game.actor = Rick.inst
elif whichGame=="Brandon" or "Brandon Conchobhair" or "brandon" or "mild" or "normal" or "concho":
    game.actor = Brandon.inst
elif whichGame=="Steve" or "Steve Butler" or "steve" or "medium" or "hard":
    game.actor = Steve.inst
elif whichGame=="Zack" or "Zack Raver" or "zack" or "hot" or "hotasfuck" or "legendary":
    game.actor = Zack.inst

interface.runGame(game)