import json
from dice_roller import Dice


class Character:
    def __init__(self):
        self.name = str
        self.char_class = int
        self.race = int
        self.MIND = int
        self.STR = int
        self.DEX = int
        self.HP = int
        self.AC = int
        self.level = int
        self.melee = int
        self.ranged = int
        self.magic = int
        self.physical = int
        self.subterfuge = int
        self.knowledge = int
        self.communication = int
        self.damage_bonus = int

    def char_gen(self):
        """
        Function to generate a new character, as stated in the Microlite d20 Revised rules
        Races: 0 =
        :return: nothing
        """

        self.HP = 6
        self.AC = 10
        self.melee = 1
        self.ranged = 1
        self.magic = 1
        self.damage_bonus = 0
        self.level = 1
        self.physical = 1
        self.subterfuge = 1
        self.knowledge = 1
        self.communication = 1
        self.DEX = 0
        self.MIND = 0
        self.STR = 0

        print("Generating character based on Microlite20 Revised Rules.")
        self.name = str(input("What is your characters name?"))
        response = True

        while response:
            print("\nRaces: \n \u2022 Humans, +1  to  all  skill  rolls\n \u2022 Elves, +2 MIND"
                  "\n \u2022 Dwarves, +2 STR \n \u2022 Halflings, +2 DEX")
            race_response = str(input("Are they a Human[A], Elf[B], Dwarf[C] or Halfling[D]?"))
            response = False
            if race_response == "A" or race_response == 'a':
                self.race = 0
                self.physical += 1
                self.subterfuge += 1
                self.knowledge += 1
                self.communication += 1
            elif race_response == "B" or race_response == "b":
                self.MIND += 2
                self.race = 1
            elif race_response == "C" or race_response == "c":
                self.STR += 2
                self.race = 2
            elif race_response == "D" or race_response == "d":
                self.DEX += 2
                self.race = 3
            else:
                response = True

        response = True
        while response:
            print("\nClasses: \n \u2022"
                  " Fighters, "
                  "may wear any kind of armor and use shields, +3 bonus to Physical, +1 to all attack and damage rolls"
                  "\n \u2022 "
                  "Rogues, "
                  "may use light armor, +3 bonus to Subterfuge, after successful sneak may add Subterfuge to damage"
                  "\n \u2022 "
                  "Magi, "
                  "may not wear armor, +3 bonus to Knowledge, may cast Magi spells "
                  "\n \u2022"
                  " Clerics, "
                  "may use light or medium armor, +3 bonus to Communication,"
                  " can turn undead with Magic Attacks and cast Divine spells")
            class_response = str(input("Are they a Fighter[A], Rogue[B], Magi[C] or Cleric[D]?"))
            response = False
            if class_response == "A" or class_response == 'a':
                self.char_class = 0
                self.physical += 3
                self.damage_bonus += 1
                self.melee += 1
                self.ranged += 1
                self.magic += 1
            elif class_response == "B" or class_response == "b":
                self.subterfuge += 3
                self.char_class = 1
            elif class_response == "C" or class_response == "c":
                self.knowledge += 3
                self.char_class = 2
            elif class_response == "D" or class_response == "d":
                self.communication += 3
                self.char_class = 3
            else:
                response = True

        print("\nAttributes  represent  the  overall  physical  and  mental  qualities  of  an  individual."
              " They  define  the  raw  potential  an  individual  has  regardless  of  actual  skill.")
        print("To define these Attributes, the computer will roll 4D6, dropping the lowest roll, and you"
              " will choose which score to assign to 3 Attributes:\n \u2022 Strength(STR)"
              "\n \u2022 Dexterity(DEX)\n \u2022 Mind(MIND)")

        outs = []
        for i in range(0, 3):
            roll = Dice.roller(4, 6, 0)['rolls']
            roll.remove(min(roll))
            roll = sum(roll)
            outs.append(roll)

        self.STR = int(input("Assign STR {}, {} or {}".format(outs[0], outs[1], outs[2])))
        outs.remove(self.STR)
        self.DEX = int(input("Assign DEX {} or {}".format(outs[0], outs[1])))
        outs.remove(self.DEX)
        print("Assigning {} to MIND".format(outs[0]))
        self.MIND = outs[0]

        self.HP += self.STR
        self.AC += self.DEX
        self.melee += self.STR
        self.ranged += self.DEX
        self.magic += self.MIND

    def level_up(self):
        """
        Levels character up, including recalculating stats dependant on the core stats
        Accounts for both 3rd level extra attribute point, and fighter 5th level bonus
        :return:
        """
        print("Congratulations! You have leveled up! Your skills and attack rolls have been increased by 1.")
        self.level += 1
        self.melee += 1
        self.ranged += 1
        self.magic += 1
        self.subterfuge += 1
        self.knowledge += 1
        self.communication += 1
        self.physical += 1

        if self.level % 3 == 0:
            print("As this is a level divisible by 3,"
                  " you may choose whether to allocate an extra point to STR(A), DEX(B) or MIND(C)")
            response = True
            while response:
                choice = input("Allocate to STR(A), DEX(B) or MIND(C)?")
                response = False
                if choice == "A" or choice == 'a':
                    self.STR += 1
                    self.HP += 1
                    self.melee += 1
                elif choice == "B" or choice == "b":
                    self.DEX += 1
                    self.AC += 1
                    self.ranged += 1
                elif choice == "C" or choice == "c":
                    self.MIND += 1
                    self.magic += 1
                else:
                    response = True
        if self.char_class == 0 and self.level % 5 == 0:
            print("Congratulations Fighter, this level you get an extra bonus to damage and attack rolls!")
            self.melee += 1
            self.ranged += 1
            self.magic += 1
            self.damage_bonus += 1

    def json_output(self):
        """
        Outputs the class dict as a json
        :return: the json tree
        """
        output = json.dumps(self.__dict__)
        print(output)
        return output


if __name__ == "__main__":
    zed = Character()
    Character.char_gen(zed)
    Character.json_output(zed)
    Character.level_up(zed)
    Character.level_up(zed)
    Character.level_up(zed)
    Character.level_up(zed)
    Character.json_output(zed)
