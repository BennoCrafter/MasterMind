import random


class MasterMind:
    def __init__(self):
        self.max_trys = 12
        self.sequence_len = 5
        self.player_try = 0
        
        self.colors = ["rot", "gelb", "grün", "pink", "blau", "grau"]
        self.sequence = []
        self.player_sequence = []
        self.player_sequence_prev = []


    def setup_sequence(self):
        # creates the solution sequence
        while not len(self.sequence) == self.sequence_len:
            next_sequence_choice = random.choice(self.colors)
            if next_sequence_choice not in self.sequence:
                self.sequence.append(next_sequence_choice)


    def get_user_inputs(self):
        step = 0
        while len(self.player_sequence) != self.sequence_len: 
            player_input = input("Welches soll dein " + str(step+1) + ". Element sein?") 
            if player_input not in self.player_sequence:
                if player_input in self.colors:
                    self.player_sequence.append(player_input)
                    step +=1
                    
                else:
                    print("\nDeine eingegebene Farbe ist nicht vorhanden!")
                    print("Zur Auswahl stehen: " + str(self.colors))
            else:
                print("\nDeine eingegebene Farbe ist bereits in deiner Auswahl bereits vorhanden!")
        print("\nDeine eingegebene Zahlen sind:", self.player_sequence, "\nDeine vorherigen Eingaben waren:", self.player_sequence_prev)
        self.player_try += 1
        self.check_win()

    
    def check_win(self):
        print("\n")
        on_right_pos = 0
        right_color = 0

        if self.player_sequence == self.sequence:
            print("Du hast gewonnen!")
        else:
            if self.player_try != self.max_trys:
                print("Da ist noch was falsch.")
                for y in range(self.sequence_len):
                    # check right positions
                    if self.player_sequence[y] == self.sequence[y]:
                        on_right_pos += 1
                    elif self.player_sequence[y] in self.sequence:
                        right_color += 1        
                print("Du hast",str(on_right_pos),"Farben auf der richtigen Position und",str(right_color),"Farben deiner Wahl sind in der Lösung vorhanden.")
                self.player_sequence_prev = self.player_sequence.copy()
                self.player_sequence.clear()
                master_mind.get_user_inputs()
            else:
                print("Du hast verloren! Die Lösung wäre", self.sequence, "gewesen.")

if __name__ == "__main__":
    print("Welcome by MaserMind!")
    master_mind = MasterMind()
    master_mind.setup_sequence()
    master_mind.get_user_inputs()
