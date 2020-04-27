# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 09:57:17 2020

@author: User-PC
"""

import PySimpleGUI as sg
import random
import pyperclip


#The Game
###version changes 
#0.0.1 - make changes to main screen to update units.
#0.0.2 - update to have layout creation definitions rather than layouts in the code
#     - also included unit starring
#0.0.3 - get the do a run get a prize system going "ROMP"
#also added a class for boards, and a bunch of boards, because I lost track of what I was doing
###Begin putting in items, and implement the XP spend shop
###0.0.4 Mostly changes to try fix up battle screen and get ready for pyinstaller
###0.0.5 sudden swap after inspiration to fix unit display. Mostly fixed, but now only 
### updates the display for a full new row. Goddamnit. ---never mind, fixed it, I'm dumb
### unit display now vastly superior. Implemented difficulty growth
###0.0.6 - trying to clean up how it looks a bit. Added an image on title screen. 
###Images broke everything, yes, python itself imploded when looking at the script. 
##not running. Literally opening the script. Decided to work on itemshop/smith instead.
### Also added a very basic HowTo section to use in the mean time. 
###0.0.7 Hopefully fix the item shop.

###dictionaries and libraries 

allItems={"Tier 1":["Claymore","Chainmail","Gloves of Haste","Headress of Rejuvenation",
                    "Hood of Defiance","Kaya","Morbid Mask","Ogre Cap","Talisman of Evasion",
                    "Vitality Booster","Void Stone"],
          "Tier 2":["Arcane Boots","Armlet of Mordiggian","Barricade","Blink Dagger",
                    "Crystalys","Desolator","Dragon Lance","Force Staff",
                    "Mantle of the Flayed Twins","Orb of Venom","Quelling Blade",
                    "Target Buddy","Vanguard"],
          "Tier 3":["Battlefury","Blade Mail","Crown of Antlers","Eul's Scepter",
                    "Hand of Midas","Leg Breaker's Fedora","Maelstrom","Mango Tree",
                    "Mask of Madness","Octarine Essence","Pipe of Insight","Ristful Circlet",
                    "Silver Edge","Skull Basher"],
          "Tier 4":["Black King Bar","Butterfly","Dagon","Diffusal Blade","Eye of Skadi",
                    "Kaden's Blade","Mekansm","Moon Shard","Refresher Orb",
                    "Scythe of Vyse","Vladmir's Offering"],
          "Tier 5":["Aegis of the Immortal","Bloodthorn","Divine Rapier","Heart of Tarrasque",
                    "Horn of the Alpha","Radiance","Satanic","Shiva's Guard",
                    "Tombstone","Vesture of the Tyrant"]}

allUnits={"Tier 1":["Arc Warden","Batrider","Bloodseeker","Crystal Maiden"
                    ,"Drow","Magnus","Nyx Assassin","Razor","Shadow Demon","Snapfire",
                    "Tiny","Tusk","Venomancer","Warlock","Weaver"],
       "Tier 2":["Beastmaster","Bristleback","Chaos Knight","Dazzle","Earth Spirit",
                 "Luna","Nature's Prophet","Ogre Magi","Pudge","Queen of Pain","Slardar",
                 "Storm Spirit","Windranger","Witch Doctor"],"Tier 3":
               ["Abaddon","Broodmother","Ember Spirit","Enigma","Io","Juggernaut",
                "Lifestealer","Lycan","Morphling","Omniknight","Shadow Fiend",
                "Shadow Shaman","Terrorblade","Treant Protector","Viper"],
               "Tier 4":["Disruptor","Doom","Keepr of the Light","Lone Druid","Mirana",
                "Necrophos","Slark","Sven","Templar Assassin","Tidehunter","Void Spirit"],
               "Tier 5":["Axe","Dragon Knight","Faceless Void","Lich","Medusa",
                "Sand King","Troll Warlord"]}
unitCost={'Arc Warden': 1, 'Batrider': 1, 'Bloodseeker': 1, 'Crystal Maiden': 1, 'Drow': 1, 'Magnus': 1, 'Nyx Assassin': 1, 'Razor': 1, 'Shadow Demon': 1, 'Snapfire': 1, 'Tiny': 1, 'Tusk': 1, 'Venomancer': 1, 'Warlock': 1, 'Weaver': 1, 'Beastmaster': 2, 'Bristleback': 2, 'Chaos Knight': 2, 'Dazzle': 2, 'Earth Spirit': 2, 'Luna': 2, "Nature's Prophet": 2, 'Ogre Magi': 2, 'Pudge': 2, 'Queen of Pain': 2, 'Slardar': 2, 'Storm Spirit': 2, 'Windranger': 2, 'Witch Doctor': 2, 'Abaddon': 3, 'Broodmother': 3, 'Ember Spirit': 3, 'Enigma': 3, 'Io': 3, 'Juggernaut': 3, 'Lifestealer': 3, 'Lycan': 3, 'Morphling': 3, 'Omniknight': 3, 'Shadow Fiend': 3, 'Shadow Shaman': 3, 'Terrorblade': 3, 'Treant Protector': 3, 'Viper': 3, 'Disruptor': 4, 'Doom': 4, 'Keepr of the Light': 4, 'Lone Druid': 4, 'Mirana': 4, 'Necrophos': 4, 'Slark': 4, 'Sven': 4, 'Templar Assassin': 4, 'Tidehunter': 4, 'Void Spirit': 4, 'Axe': 5, 'Dragon Knight': 5, 'Faceless Void': 5, 'Lich': 5, 'Medusa': 5, 'Sand King': 5, 'Troll Warlord': 5}    
allTavernLevel=[[90,10,0,0,0],[70,30,0,0,0],[50,35,15,0,0],[40,35,25,0,0],
             [35,30,30,5,0],[25,30,35,10,0],[22,27,35,15,1],[20,27,30,20,3],[15,21,28,30,6],
             [15,20,25,30,10],[10,20,25,30,15],[10,10,25,35,20]]
Tiers=["Tier 1","Tier 2","Tier 3", "Tier 4","Tier 5"]
tlvlmodifier=0
tavernLevel=allTavernLevel[tlvlmodifier]
tlvlcost=int(2**((tlvlmodifier+2)/2))


allSmithLevel=[[100,0,0,0,0],[60,39,1,0,0],[15,65,29,1,0],[0,35,55,10,0],[0,0,45,48,7],[0,0,15,70,15]]
slvlmodifier=0
smithLevel=allSmithLevel[slvlmodifier]
allSmithUpgradeCost=[15,20,25,30,35]
smithUpgradeCost=allSmithUpgradeCost[slvlmodifier]


### Image Codes
dotaIcon="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"



## little code for Roster pricing
unitCount=3
expandRosterPrice=[6,9,12,15,15,20,20,30,40]            
rosterCostCount=0


#Code to generate the random units for tavern 
def unitR():
    tavernLevel=allTavernLevel[tlvlmodifier]
    tierR=random.choices(Tiers, weights= tavernLevel)
    return random.choices(allUnits[tierR[0]])

def itemR():
    smithLevel=allSmithLevel[slvlmodifier]
    tierSR=random.choices(Tiers, weights= smithLevel)
    return random.choices(allItems[tierSR[0]])
    
#The smith
def fillTheSmith():
    theSmith=[]
    theSmith+=itemR()
    theSmith+=itemR()
    theSmith+=itemR()
    return theSmith    
theSmith=fillTheSmith()    
            ###need to put the code for item cost here

#The tavern

theTavern=[]
def fillTheTavern():
    theTavern=[]
    theTavern+=unitR()
    theTavern+=unitR()
    theTavern+=unitR()
    theTavern+=unitR()
    theTavern+=unitR()
    return theTavern


theTavern=fillTheTavern()
theTavernCost=[unitCost[theTavern[n]] for n in range(5)]

#BOARD CODES AND DESCRIPTIONS FOR BATTLES + some code for it that is probably temporary
class Boards:
    def __init__(self,n="needs a name",c="Board code missing"):
        self.name=n
        self.code=c
        self.entrance="empty"
        self.victory="empty"
        self.defeat="empty"
        self.difficulty=1   #for now just a placeholder on what round it should be on 
        self.rewards=[7,3]   #gold and xp respectively, will see about other rewards for fun later
        self.rules="None"   #this governs if there are any special rules for a board, normally there aren't.
### this is how each board should be set up. 
spiritBros=Boards("the Spirit Brothers") ##name in the instantialisation 
spiritBros.code=('8qAMAAKYBAASyJ0osAGoVAGobAFIBAFIwAF4BAD4tAAANCSkAeQkHAHoJBwB7ERAAfAkQAAAREBEBCHkAKxELrgEAODAAAAADAxAgIBAAAgAAIK47AN4BAA==')
spiritBros.entrance="I don't want to fight a family..."    #not used yet from here
spiritBros.victory="Wow, blood really is thicker than water"
spiritBros.defeat="Overcome by the power of family..."
spiritBros.difficulty=15
spiritBros.rewards=[7,7] #change their rewards off the standard, not needed, but should be fairly often


## from this point boards will generally be easier earlier, harder later
firstBattle=Boards("your first combat")
firstBattle.code=('8qAMAAP4BAP4BAP4BAE4BAACAQtUAAEAFEkYYANYBAAQBEA04AAENCP4BAIYBAA==')
firstBattle.entrance=("This should be easy enough")
firstBattle.victory=("Hope this sets the tone going forward")
firstBattle.defeat=("... next time try use units")
firstBattle.difficulty=1

secondBattle=Boards("Undercity welcome crew")
secondBattle.code=("8qAMAAP4BAP4BAP4BAAEBDFEAAAXSyAAActI2AAABCTYAEAEHDQz+AQCCAQA=")
secondBattle.entrance=("Aw, fan favourites out to play!")
secondBattle.victory=("I mean, they were already dead right?")
secondBattle.defeat=("How do you kill that which has no life")
secondBattle.difficulty=2

thirdBattle=Boards("A totally unique crew of enemies")
thirdBattle.code=("8qAMAAP4BAP4BAP4BADYBAABABc8APgUGRgEAGRgJKN4BAAQBEAU6DBAAAAEFCf4BAIoBAA==")
thirdBattle.entrance=("This seems familiar")
thirdBattle.victory=("That was somehow notably harder")
thirdBattle.defeat=("oh the humiliation...")
thirdBattle.difficulty=3

arachnophobia=Boards("Arachnophobia")
arachnophobia.code=("8qAMAAP4BAP4BAP4BAAEBDGVmZmYByABmDQgEZWUJEAxlZmYhARgMZWVmZAkIBGVlTggAugEAABE6AQC6PwDSAQA=")
arachnophobia.difficulty=4
arachnophobia.entrance=("Oh no...")
arachnophobia.victory=("Ha! Insects, easy to crush")
arachnophobia.defeat=("This was literally the worst, I need AOE")

humanity=Boards("Humanity")
humanity.code=("8qAMAAP4BAP4BAP4BAAUBACsJxgQcDQkIADEJB/4BAF4BABAQAQAAEf5dAF5dAFoBAA==")
humanity.difficulty=5
humanity.entrance=("Today humanity rises up to face you!")
humanity.victory=("Maybe try trained combatants next time humanity")
humanity.defeat=("Truly humans are the pinnacle of might and beauty")


jumpy=Boards("Blink crew 1")
jumpy.code=("8qAMAAEYBAASGJ0YUAG4BAP4wAP4wAAEwAHo6oQAAETIQAABiOhAAAABCMAC6AQAAAQUwCAECAgkJ/gEAigEA")
jumpy.difficulty=6
jumpy.entrance=("Catching these guys may be a problem")
jumpy.victory=("They needed a bit more survivability in that lineup")
jumpy.defeat=("Too fast :(")


theFinalBattle=Boards("Your final fight")
theFinalBattle.difficulty=20
### the board list ordered by difficulty. boardList[1] being all the 
###difficulty one boards boardList[1][0] the first example of it
boardList=[["Empty 0 difficulty"],[firstBattle],[secondBattle],[thirdBattle],
           [arachnophobia],[humanity],[jumpy],[],[],[],[],[],[],[],[],[spiritBros],[],[],[],[],[theFinalBattle]]



difficulty=1  ##this just starts the difficulty off 
currentBoard=boardList[difficulty][0]
###Code for checking if you have sufficient gold to complete the transaction. 

def spendGold(n):
    if player["Gold"]>=n:
        player["Gold"]-=n
        return True
    else:
        sg.popup("You don't have enough gold :( ")
        return False

def getGold(n):
    player["Gold"]+=n
    
def spendXP(n):
    if player["XP"]>=n:
        player["XP"]-=n
        return True
    else:
        sg.popup("You don't have enough XP ! ")
        return False
    
def getXP(n):
    player["XP"]+=n
    
###What the player has / starts with 
player={"Gold":10,"XP":0,"Rounds Remaining":20,}
units=[]
items=[]

### 2 and 3 staring units 
def unitStar():
    temp=units
    for i in temp:
        n=0
        for i2 in temp:
            if i==i2:
                n+=1
        if n>=3:
            if i[-1]!="*":
                temp+=[i+"**"]
            else:
                temp+=[i+"*"]
            for count in range(n):
                temp.remove(i) 
    return temp
            
            



###This should give the main game screen from which others stem 
##also has unitframe because main screen uses it

sg.theme("DarkPurple1")

def makeUnitsFrame(color="Dark Orchid"):       
    tempframe=[]
    temperframe=[]
    units.sort()
    for i in range(len(units)):
        temperframe+=[sg.Text(units[i],size=(12,1),background_color=color)]
        if (i+1)%3==0 or i==(len(units)-1):
            tempframe+=[temperframe]
            temperframe=[]
    return sg.Frame("Your units",tempframe,background_color=color)     ##need to look at colours
sg.Text(units,key="--colUnits")


###OKAY!!! UNITS IS LOOKING MUCH BETTER,
def makeMain():  
    layoutmain=[[sg.Text('Underlords Romp',size=(30,2))],
        [sg.Button(image_data=dotaIcon,pad=[100,5],border_width=0)],
        [sg.Text(player,key="-stats-")],
        [makeUnitsFrame()],
        [sg.Button("Spend Gold",size=(15,1)),sg.Button("Spend XP",size=(15,1))],
        [sg.Button("Go Romping!",size=(15,1)),sg.Button("How to Play",size=(15,1))],
        [sg.Quit('Quit')]]      
    return layoutmain

layoutmain=makeMain()

###Layouts

def makeSpendGold():
    layoutGold=[[sg.Text('Spend your Gold!')],
                    [sg.Text("You have "+str(player["Gold"])+" gold.",key="-gold-")],
                [sg.Button("Buy Unit",size=(15,1)),sg.Button("Buy Item",size=(15,1))],
                [sg.Button("Upgrade Tavern",size=(15,1)),sg.Button("Upgrade Blacksmith",size=(15,1))],
                [sg.Button("Back")]]
    return layoutGold

def makeUnitBuy():         #need to add button that sends sg.popup(makeUnitsFrame())
    layoutUnits=[[sg.Text('Buy a unit!')],            
                   [sg.Button(theTavern[i],key="Button "+str(i),size=(15,2)) for i in range(5) ],
                   [sg.Text(str(theTavernCost[i])+" gold",justification='center',size=(15,2)) for i in range(5)],
                   [sg.Text("Your current unit odds are:")],
                   [sg.Text(tavernLevel)],
                   [sg.Button("Reroll the tavern (2 gold)")],
                   [sg.Button("Back")]]
    return layoutUnits

def makeTavernUp():
    layoutTavernUp=[[sg.Text("Are you sure you want to tavern up?")],
                                [sg.Text("It will cost "+str(tlvlcost)+" gold.")],
                                [sg.Text("Your unit odds will go from:")],
                                [sg.Text(allTavernLevel[tlvlmodifier])],
                                [sg.Text("to")],
                                [sg.Text(allTavernLevel[tlvlmodifier+1])],
                                [sg.Button("Yes!"),sg.Button("No :( (back)")]]
    return layoutTavernUp

def makeItemBuy():         #need to add button that sends sg.popup(makeUnitsFrame())
    layoutSmith=[[sg.Text('Your friendly local Smithy')],            
                   [sg.Button(theTavern[i],key="Button "+str(i),size=(15,2)) for i in range(5) ],
                   #[sg.Text(str(theTavernCost[i])+" gold",justification='center',size=(15,2)) for i in range(5)],
                   [sg.Text("Your current item odds are:")],
                   [sg.Text(smithLevel)],
                   [sg.Button("Reroll the blacksmith (5 gold)")],
                   [sg.Button("Back")]]
    return layoutSmith               ###Need to finish this - not half done

def makeSpendXP():
    layoutXP=[[sg.Text('Use Experience to Grow in Power!')],
                [sg.Button("Expand your Roster"),],
                [sg.Button("Get an Underlord!")],
                [sg.Button("Increase difficulty O_O")],
                [sg.Button("Back")]]
    return layoutXP

###This is a set up to make several pages that you go through. There is a page count that iterates
### and it makes the page one further forward or backwards. 
### we don't have to have a termination or control, we just drop the "Next" button on the last page.
def makeHowToPlay(n=1):
    if n==1:
        layoutHowToPlay=[[sg.Text("Underlords Romp is a companion app, not a game in itself.")],
                     [sg.Text("It is intended to be used with Dota Underlords which")],
                     [sg.Text("can be found by clicking these words!",click_submits=True)],
                     [sg.Text("(The app and myself are not affiliated with Valve in any way.)")],
                     [sg.Text("If you don't have Dota Underlords, grab it now!")],
                     [sg.Text("")],[sg.Text("")],
                     [sg.Button("Back"),sg.Button("Next")],[sg.Quit()]]
    if n==2:
        layoutHowToPlay=[[sg.Text("Once you have Dota Underlords working, play their tutorial.")],
                      [sg.Text("Maybe even play the game a bit! This is made for people who")],
                      [sg.Text("enjoy Dota underlords! But once you're done...")],
                      [sg.Text("Go ahead and hit the FIGHT button, then TRAINING, FREESTYLE.")],
                      [sg.Text("We're ready to get started! By hitting... START")],
                      [sg.Text("")],[sg.Text("")],[sg.Text("")],
                      [sg.Button("Back"),sg.Button("Next")],[sg.Quit()]]
    if n==3:
        layoutHowToPlay=[[sg.Text("This app gives us a dungeon crawler in the Dota Underlords Game.")],
                         [sg.Text("You can buy your units, items, upgrade your tavern and much more here")],
                         [sg.Text("Once you've done that, you GO ROMP!")],
                         [sg.Text("Follow the instructions, and it'll generate a board code for you")],
                         [sg.Text("In Dota Underlords, double click -clear board- and then ")],
                         [sg.Text("click -paste board code-")],
                         [sg.Text("if you grabbed my text right, you should get some opponents!")],
                         [sg.Text("")],[sg.Text("")],
                         [sg.Button("Back"),sg.Button("Next")],[sg.Quit()]]
    if n==4:
        layoutHowToPlay=[[sg.Text("On the battle screen, you'll see your units and items on the right.")],
                         [sg.Text("You can use the Dota Underlords freestyle menu to add those to your board")],
                         [sg.Text("Place them anywhere and on anyone you want... as long as you stick")],
                         [sg.Text("to the rules. Those are at the top -example: You can have 3 units")],
                         [sg.Text("")],
                         [sg.Text("Try as many times as you like, Report your victory or defeat")],
                         [sg.Text("and then go back and spend your hard-fought")],
                         [sg.Text("rewards! (or consolation prize)")],[sg.Text("")],[sg.Text("")],
                         [sg.Button("Back"),sg.Button("Next")],[sg.Quit()]]
    if n==5:
        layoutHowToPlay=[[sg.Text("That's it! Go ahead and start romping. I hope you enjoy it!")],
                         [sg.Text("")],[sg.Text("")],[sg.Text("")],[sg.Text("")],[sg.Text("")],[sg.Text("")],[sg.Text("")],[sg.Text("")],                         
                         [sg.Button("Back")],[sg.Quit()]]
    return layoutHowToPlay

  

def makeRomping():
    layoutRomp=[[sg.Text("Time to ROMP!")],
                [sg.Frame("",[[sg.Text("You battle against "+currentBoard.name)],
                [sg.Text(currentBoard.entrance)]])],
                [sg.Text("")],
                [sg.Text("Click the button below to get your board code")],
                [sg.Button("The Code awaits inside...")],
                [sg.Button("To battle!")],
                [sg.Button("Back")]]
    return layoutRomp



def makeBattle():
    layoutBattle=[[sg.Text("Here's everything you need to know about your batt`le")],
                  [sg.Button("Here's the board code if you forgot to grab it on the last screen")],
                  [sg.Column([[sg.Text("You face "+currentBoard.name)],
                              [sg.Text(currentBoard.entrance)],
                              [sg.Text("There are no special board rules:")],
                                       [sg.Text("Don't touch what's already there")]],
                             background_color="medium purple",size=(300,300)),
                            sg.Column( [[sg.Text("You can have "+str(unitCount)+" units on the board")],
                             [makeUnitsFrame("medium orchid")]],background_color="#D8BFD8",
                                      size=(400,300))],    ### could fix colours
                  [sg.Text("After you've completed the battle, let us know whether you achieved")],
                  [sg.Button("Victory!"),sg.Button("Defeat")],
                  [sg.Button("Back-for developer")]]   #This button should be removed in the final version
    return layoutBattle

####starter stuff             






win1=sg.Window('Romping in progress',layout=layoutmain,grab_anywhere=True,location=(800,380)).finalize()


win2_active=False
win3_active=False
###read the window / event loop

while True:
    button, values=win1.Read(timeout=100)
    if button in (None, 'Quit'):
        break
    win1["-stats-"].update(player)
######################################
    if button in ("How to Play"):    
         win2_active = True  
         win1.hide()
         pageCount=1
         win2=sg.Window("How to Play",layout=makeHowToPlay(),grab_anywhere=True,location=(800,380),size=(500,350))
         while True:
             button2,values2=win2.read(timeout=0)    #this gets used for all the how to pages
             if button2 in(None, "Quit"):            #all these instructions are used for all
                win2_active=False
                win2.close()
                win1.UnHide()
                break
             if button2 in ("Back"):
                 if pageCount==1:
                     win2_active=False
                     win2.close()
                     win1.UnHide()
                 else:
                     pageCount-=1
                     win2.close()
                     win2=sg.Window("How to Play",layout=makeHowToPlay(pageCount),grab_anywhere=True,location=(800,380),size=(500,350))
             if button2 in ("can be found by clicking these words!"):
                 pyperclip.copy("https://store.steampowered.com/app/1046930/Dota_Underlords/")
                 sg.Popup("Oops, not working yet, but I sneakily ",
                          "put it in your clipboard, so go hit paste",
                          "in your browser and you'll get the page.")
             if button2 in ("Next"):
                 win2.close()
                 pageCount+=1
                 win2=sg.Window("How to Play",layout=makeHowToPlay(pageCount),grab_anywhere=True,location=(800,380),size=(500,350))
#######################    
    if button == "Spend Gold"  and not win2_active:  
        win2_active = True  
        win1.hide()
        layoutGold=makeSpendGold()
        win2 = sg.Window('Gold Store',layout=layoutGold,grab_anywhere=True,location=(800,380))
        while True:    
            button2,values2=win2.read(timeout=0)
            if button2 in(None, "Back"):
                win2_active=False
                win2.close()
                #this updates units to star any units in triplicate
                units=unitStar()
                #this updates win1 with any units that have been bought or sold before showing it again
                #win1["--colUnits"].update(units) 
                win1.close()
                layoutmain=makeMain()
                win1=sg.Window('Romping in progress',layout=layoutmain,grab_anywhere=True,location=(800,380)).finalize()
                win1.UnHide()
                break
            win2["-gold-"].update("You have "+str(player["Gold"])+" gold.")
            if button2=="Upgrade Tavern" and not win3_active:
                win2.hide()
                win3_active=True
                layoutTavernUp=makeTavernUp()
                win3=sg.Window("Tavern up!",layout=layoutTavernUp,grab_anywhere=True,location=(800,380))
                while True:
                    button3,values3=win3.read(timeout=10000)
                    if button3 in(None, "No :( (back)"):
                        win3_active=False
                        win3.close()                    
                        win2.UnHide()
                        break
                    if button3 in ("Yes!"):
                        if spendGold(tlvlcost):
                            tlvlmodifier+=1
                            tavernLevel=allTavernLevel[tlvlmodifier]
                            tlvlcost=int(2**((tlvlmodifier+2)/2))
                        win3_active=False
                        win3.close()                    
                        win2.UnHide()
                        break
            if button2=="Buy Unit" and not win3_active:
                win2.hide()
                win3_active=True
                layoutUnits=makeUnitBuy()
                win3=sg.Window("The Tavern",layout=layoutUnits,grab_anywhere=True,location=(800,380))
                while True:
                    button3,values3=win3.read(timeout=10000)
                    if button3 in(None, "Back"):
                        win3_active=False
                        win3.close()
                        win2.UnHide()
                        break
                    if button3 in ("Reroll the tavern (2 gold)") and spendGold(2):
                        theTavern=fillTheTavern()
                        theTavernCost=[unitCost[theTavern[n]] for n in range(5)]
                        win3.close()
                        layoutUnits=makeUnitBuy()
                        win3=sg.Window("The Tavern (again)",layout=layoutUnits,grab_anywhere=True,location=(800,380))
                    if button3 in ["Button 0","Button 1","Button 2","Button 3","Button 4"]:
                        if spendGold(theTavernCost[int(button3[-1])]):
                            units+=[theTavern[int(button3[-1])]]
                            win3[button3].update("Empty")
                            win3[button3].update(disabled=True)
            if button2 in ("Buy Item"):
                sg.Popup("Oops, sorry, not implemented yet")
            if button2 in ("Upgrade Blacksmith"):
                sg.Popup("Ayyy lmao, not implemented")
######################################                            
    if button in ("Spend XP"):
        win2_active = True  
        win1.hide()
        layoutXP=makeSpendXP()
        win2 = sg.Window('Your experience earns you new power',layout=layoutXP,grab_anywhere=True,location=(800,380))
        while True:    
            button2,values2=win2.read(timeout=0)
            if button2 in(None, "Back"):
                win2_active=False
                win2.close()
                win1.UnHide()
                break
            if button2 in ("Expand your Roster"):
                if spendXP(expandRosterPrice[rosterCostCount]):
                    sg.Popup("Congrats, you moved from "+str(unitCount)+" to "+
                             str(unitCount+1)+" units on the board.")
                    rosterCostCount+=1
                    unitCount+=1             
            if button2 in ("Get an Underlord!"):
                sg.Popup("Oops, sorry, not implemented yet!")
            #    if spendXP(10):
           #         get an underlord - need to implement
            if button2 in ("Increase difficulty O_O"):
               sg.Popup("Oops, sorry, not implemented yet!")
#######################################
    if button in ("Go Romping!"):
        if len(units)==0:
            sg.Popup("You don't have any units, might make a battle tough")
            continue
        win2_active=True
        win1.hide()
        layoutRomp=makeRomping()
        win2=sg.Window("The battle awaits you",layout=layoutRomp,grab_anywhere=True,location=(800,380))
        
        while True:
            button2,values2=win2.read(timeout=0)
            if button2 in(None, "Back"):
                win2_active=False
                win2.close()
                win1.UnHide()
                break
            if button2 in ("The Code awaits inside..."):
               pyperclip.copy(currentBoard.code)
            if button2 in ("To battle!"):
                win3_active=True
                win2.hide()
                layoutBattle=makeBattle()
                win3=sg.Window("The battle station", layout=layoutBattle,grab_anywhere=True,location=(800,380))
                while True:
                    button3,values3=win3.read(timeout=0)
                    if button3 in(None, "Back-for developer"):
                        win3_active=False
                        win3.close()
                        win2.UnHide()
                        break
                    if button3 in ("Victory!"):     #need to figure out how to line break and add victory message
                        sg.Popup("Congrats! "+"You earned "+
                                 str(currentBoard.rewards[0])+" gold and "+
                                 str(currentBoard.rewards[1])+" XP!")
                        getGold(currentBoard.rewards[0])
                        getXP(currentBoard.rewards[1])
                        difficulty+=1
                        currentBoard=boardList[difficulty][0]
                        theTavern=fillTheTavern()
                        theTavernCost=[unitCost[theTavern[n]] for n in range(5)]
                        win3_active=False
                        win3.close()
                        win2.UnHide()
                        win2_active=False
                        win2.close()
                        win1.UnHide()
                    if button3 in ("Defeat"):
                        sg.Popup(currentBoard.defeat)
                        difficulty+=1
                        currentBoard=boardList[difficulty][0]
                        theTavern=fillTheTavern()
                        theTavernCost=[unitCost[theTavern[n]] for n in range(5)]
                        getXP(currentBoard.rewards[1])    ###later on should have specific defeat consolation prize
                        win3_active=False
                        win3.close()
                        win2.UnHide()
                        win2_active=False
                        win2.close()
                        win1.UnHide()
win1.close()

