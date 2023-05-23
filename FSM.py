"""
Lab discretka
"""
import random
class FSM:
    """Class FSM
    """
    def __init__(self):
        # initializing generators and priming them
        self.sleep_s = self.sleep()
        next(self.sleep_s)
        self.rest_s = self.rest()
        next(self.rest_s)
        self.studying_s = self.studying()
        next(self.studying_s)
        self.walking_s = self.walking()
        next(self.walking_s)
        self.eating_s = self.eating()
        next(self.eating_s)
        self.talking_s = self.talking()
        next(self.talking_s)
        self.washing_s = self.washing()
        next(self.washing_s)
        self.watching_film_s = self.watching_film()
        next(self.watching_film_s)
        self.shopping_s = self.shopping()
        next(self.shopping_s)
        self.talking_parents_s = self.talking_parents()
        next(self.talking_parents_s)
        self.writting_essay_s = self.writting_essay()
        next(self.writting_essay_s)

        self.hour = 0
        self.annoyed=False
        self.hungry=0

        # setting current state of the system
        self.current_state = self.sleep_s

        # stopped flag to denote that iteration is stopped due to bad
        # input against which transition was not defined.
        self.stopped = False

    def add_hour(self):
        """Adding 1 hour to hour counter
        """
        self.hour += 1

    def send(self):
        """The method generates 24 hour long day
        """
        while self.hour <= 24:
            self.current_state.send(self.hour)
            self.add_hour()
            self.hungry+=18
    def sleep(self):
        """Sleeping state
        """
        while True:
            hour = yield
            print(str(hour)+": Sleeping...")
            possible = random.random()
            if hour==7:
                if 0<possible<=0.5:
                    self.current_state=self.eating_s
                elif 0.5<possible<0.8:
                    self.current_state=self.washing_s
                else:
                    self.current_state=self.studying_s
    def eating(self):
        """
        Eating state
        """
        while True:
            hour = yield
            self.hungry=0
            print(str(hour)+": Eating...")
            possible = random.random()
            if 0<possible<0.6:
                self.current_state=self.studying_s
            else:
                self.current_state=self.talking_s
    def rest(self):
        """
        Rest state
        """
        while True:
            hour = yield
            print(str(hour)+": Resting")
            possible = random.random()
            if hour>=23:
                self.current_state=self.sleep_s
                continue
            if self.hungry>=80:
                self.current_state=self.eating_s
                continue
            if 0<possible<0.6:
                self.current_state=self.studying_s
            elif 0.6<possible<0.8:
                self.current_state=self.walking_s
            else:
                self.current_state=self.writting_essay_s
    def studying(self):
        """
        Studying state
        """
        while True:
            # Wait till the input is received.
            # once received store the input in `char`
            char = yield
            print(str(char)+": Studying...")
            possible = random.random()
            if self.hungry>=80:
                self.current_state=self.eating_s
            elif char>=20:
                self.annoyed=True
            elif char>=23:
                self.current_state=self.sleep_s
            elif self.annoyed:
                self.current_state=self.writting_essay_s
            elif 0<possible<0.4:
                self.current_state=self.rest_s
            else:
                continue
    def walking(self):
        """
        Walking state
        """
        while True:
            # Wait till the input is received.
            # once received store the input in `char`
            char = yield
            print(str(char)+": Walking in park...")
            if self.hungry>=80:
                self.current_state=self.eating_s
                continue
            elif char>=23:
                self.current_state=self.sleep_s
                continue
            self.current_state=self.studying_s
    def talking(self):
        """
        Walking state
        """
        while True:
            # Wait till the input is received.
            # once received store the input in `char`
            char = yield
            print(str(char)+": Talking...")
            possible = random.random()
            if char>=23:
                self.current_state=self.sleep_s
                continue
            elif self.hungry>=80:
                self.current_state=self.eating_s
                continue

            elif possible<0.8:
                self.current_state=self.talking_parents_s
            else:
                self.current_state=self.shopping_s
    def washing(self):
        """
        Walking state
        """
        while True:
            # Wait till the input is received.
            # once received store the input in `char`
            char = yield
            print(str(char)+": Washing...")
            possible = random.random()
            self.annoyed=False
            if char>=23:
                self.current_state=self.sleep_s
                continue
            if self.hungry>=80:
                self.current_state=self.eating_s
            if possible<0.1:
                self.current_state=self.walking_s
            elif 0.1<=possible<=0.4:
                self.current_state=self.studying_s
            else:
                self.current_state=self.eating_s
    def watching_film(self):
        """
        Walking state
        """
        while True:
            # Wait till the input is received.
            # once received store the input in `char`
            char = yield
            print(str(char)+": Watching film...")
            self.annoyed=False
            if self.hungry>=80:
                self.current_state=self.eating_s
            if char>=23:
                self.current_state=self.sleep_s
                continue
            self.current_state=self.studying_s
    def shopping(self):
        """
        Walking state
        """
        while True:
            # Wait till the input is received.
            # once received store the input in `char`
            char = yield
            print(str(char)+": Shopping...")
            possible = random.random()
            self.annoyed=False
            if char>=23:
                self.current_state=self.sleep_s
                continue
            if self.hungry>=80:
                self.current_state=self.eating_s
            if 0<=possible<=0.7:
                self.current_state=self.eating_s
            else:
                self.current_state=self.shopping_s
    def talking_parents(self):
        while True:
            hour=yield
            self.annoyed=False
            if hour>=23:
                self.current_state=self.sleep_s
                continue
            possible=random.random()
            if possible<0.7:
                self.current_state=self.studying_s
            else:
                self.current_state=self.watching_film_s
            print(str(hour)+": Talking to parents...")
    def writting_essay(self):
        while True:
            hour=yield
            self.annoyed=False
            if hour>=23:
                self.current_state=self.sleep_s
                continue
            possible=random.random()
            if possible<=0.2:
                self.current_state=self.rest_s
            elif possible<0.7:
                self.current_state=self.studying_s
            else:
                self.current_state=self.shopping_s

            print(str(hour)+": Writing essay...")
