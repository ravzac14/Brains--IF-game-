#brains.py
#Zack Raver
#Start Date: 11/26/13
import sys
from pyf import items, game, interface, props


##################################### Playable Character #######################
whichGame = raw_input("Which character would you like to play as: Rick Grimes(Sweet), Brandon Conchobhair(Mild), Steve Butler(Medium), Zack Raver(Hotasfuck)?\n")
if whichGame[0]== "R" or "r" or "E" or "e" or WhichGame == "sweet" or "Sweet":
    class rickGame(game.Game):
        pass
elif whichGame[0]=="Z" or "z" or "h" or "H" or "L":
    class zackGame(game.zackGame):
        pass
elif whichGame[1]=="t" or "u" or whichGame == "medium" or "hard": 
    class steveGame(game.steveGame):
        pass
elif whichGame[1]== "r" or "o"  or whichGame== "mild":
    class brandonGame(game.brandonGame):
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
    
class PharmacyMain(items.Room):
    pass
    
class PharmacyBehindCounter(items.Room):
    pass
    
class GrocerEntrance(items.Room):
    pass
    
class ProduceSection(items.Room):
    pass
    
class TwinkySection(items.Room):
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
class BWParkingLotOne(items.Room):
    pass
    
class BWParkingLotTwo(items.Room):
    pass
    
class BWElectricBox(items.Room):
    pass
    
class BWShopsTwo(items.Room):
    pass
    
class BWShopsThree(items.Room):
    pass
    
class BWShopsFour(items.Room):
    pass
    
class HauntedHouseGame(items.Room):
    pass
    
class CarnyGames(items.Room):
    pass
    
class RollerCoasterControls(items.Room):
    pass
    
class RollerCoaster(items.Room):
    pass
    
class FerrisWheelControls(items.Room):
    pass
    
class FerrisWheel(items.Room):
    pass
    
class BWOne(items.Room):
    pass
    
class BWTwo(items.Room):
    pass
    
class BWThree(items.Room):
    pass
    
class BWFour(items.Room):
    pass
    
class BWEntrance(items.Room):
    pass
    
class ClownRoom(items.Room):        ########### ENDING POSSIBILITY #################
    pass

########################### Zoo Classes ########################################
class ZooParkingLotOne(items.Room):
    pass

class ZooParkingLotTwo(items.Room):
    pass
    
class ZooTicketBooths(items.Room):
    pass
    
class ZooEntrance(items.Room):
    pass
    
class ZooFountain(items.Room):
    pass

class ZooPenguins(items.Room):
    pass
    
class ZooAquariumEntrance(items.Room):
    pass
    
class ZooAquariumSharks(items.Room):
    pass
    
class ZooAnimalsOne(items.Room):
    pass
    
class ZooAnimalsTwo(items.Room):
    pass
    
class ZooAnimalThree(items.Room):
    pass
    
class ZooSecret(items.Room):
    pass

################################## Mansion/Houses Classes ######################
class HouseFourMain(items.Room):
    pass
    
class HouseFourBY(items.Room):
    pass
    
class HouseThreeGar(items.Room):
    pass
    
class HouseThreeMain(items.Room):
    pass
    
class HouseThreeBYMain(items.Room):
    pass
    
class HouseThreeBYPool(items.Room):
    pass
    
class HouseTwoGar(items.Room):
    pass
    
class HouseTwoMain(items.Room):
    pass
    
class HouseTwoAttic(items.Room):
    pass
    
class HouseTwoBYMain(items.Room):
    pass
    
class HouseTwoBYPool(items.Room):
    pass
    
class HouseTwoBYTrashFence(items.Room):
    pass
    
class HouseOneGar(items.Room):
    pass
    
class HouseOneMain(items.Room):
    pass
    
class HouseOneBY(items.Room):
    pass
    
class ManDW(items.Room):
    pass
    
class ManEntrance(items.Room):
    pass
    
class ManGar(items.Room):
    pass
    
class ManRV(items.Room):
    pass
    
class ManFFBedRoom(items.Room):
    pass
    
class ManFFKitchen(items.Room):
    pass
    
class ManArmory(items.Room):
    pass
    
class ManSFBath(items.Room):
    pass
    
class ManSFLibrary(items.Room):
    pass
    
class ManSFBedroom(items.Room):
    pass
    
class ManSFTorture(items.Room):
    pass

###############################Elementary School Classes #######################
class SchoolParkingLot(items.Room):
    pass
    
class SchoolBus(items.Room):
    pass
    
class KinderClass(items.Room):
    pass
    
class GradeClass(items.Room):
    pass
    
class LunchArea(items.Room):
    pass
    
class Playground(items.Room):
    pass
    
class AuditoriumMain(items.Room):
    pass
    
class AudStorage(items.Room):
    pass

############################# Forest/Graveyard/Swamp Classes ###################
class ForestOne(items.Room):     ##Leftwise
    pass
    
class ForestTwo(items.Room):
    pass

class ForestThree(items.Room):
    pass

class SwampOne(items.Room):
    pass
    
class SwampTwo(items.Room):
    pass
    
class SwampThree(items.Room):
    pass
    
class GraveyardOne(items.Room):
    pass
    
class GraveyardTwo(items.Room):
    pass
    
class Sinkhole(items.Room):
    pass

############################# Hills/ Lake/ Cabin Classes #######################
class WaterfrontHills(items.Room):
    pass

class HillsTwo(items.Room):
    pass
    
class HillsThree(items.Room):
    pass
    
class HillsFour(items.Room):
    pass
    
class HillsFive(items.Room):
    pass
    
class HillsSix(items.Room):
    pass
    
class HillsSeven(items.Room):
    pass
    
class LakeInlet(items.Room):
    pass

############################# Romero St./Construction Site/ Field Classes #############quit
####
class RomeroStOne(items.Room):
    pass
    
class RomeroStTwo(items.Room):
    pass
    
class RomeroStThree(items.Room):
    pass
    
class RomeroStFour(items.Room):
    pass

class RomeroStFive(items.Room):
    pass
    
class ForemansOffice(items.Room):
    pass
    
class ConstructionSiteOne(items.Room):
    pass
    
class ConstructionSiteTwo(items.Room):
    pass

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
