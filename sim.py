# Simulated Ideas, Man (SIM)

from random import random
import time
import sys

class Simulation(object):
    
    def __init__(self):
        print 'Simulation initialized'

        """ What is a simulation?

            Attempt #1:
              a simulation is a set of occurrences in a finite amount of time

                time        | where the line begins
                time_end    | where the line ends

                step        | the amount of time increased in each cycle
                            | total # of cycles = (time_end - time) / step

                occurrences | a list of things that happen
                            | "occurs" for short..

                dynamics    | a list of things that cause change

                sim         | the way in which all of the parts work together
        
        """
        # time is infinite, you are not
        self.time     = 0
        self.time_end = 0

        self.step     = 0

        self.occurs   = []
        self.dynamics = []

    def tick(self):
        self.time += self.step
        time.sleep(1)

    def simulate(self):
        for event in self.occurs[:-1]:
            for variable in self.dynamics:
                event(variable) 
        self.occurs[-1]("")

    def run(self):

        # time starts here
        while self.time <= self.time_end or not self.time_end:

            # things happen
            self.simulate()

            # time ticks by
            print 'Tick: %d' % self.time
            self.tick()

class Life(Simulation):

    def __init__(self):
        Simulation.__init__(self)
        
        self.time     = 2013
        self.time_end = 0
        
        print "Life has begun has begun."
        self.beginning_of_time = self.time

        self.step     = 1

        self.occurs   = []

        self.dynamics = []

        self.ready    = 0

    def setup(self):
        print "Populating simulation..."

        self.population = 100
        self.next_birth = 1
        self.death_rate = 0.05
        self.birth_rate = 0.002

        for new_life in xrange(self.population):
            life_form = self.new_life()
            self.dynamics.append(life_form)

        self.occurs.append(self.death)
        self.occurs.append(self.life)
        self.occurs.append(self.eotw)


    def new_life(self):
        life_form = {}
        life_form['life'] = 'alive'
        life_form['type'] = 'human'
        life_form['id']   = self.next_birth
        self.next_birth += 1
        self.dynamics.append(life_form)
        return life_form


    def death(self, type_of_life):
        if type_of_life.get('life'):
            life = None if random() < self.death_rate else type_of_life.get('life')

            if not life and type_of_life['life']:
                type_of_life['life'] = life
                self.population -= 1
                print "A death to %d" % type_of_life['id']

    def life(self, _):
        life = 1 if random() < self.birth_rate else None
        if life:
            type_of_life = self.new_life()
            self.population += 1
            print "A life to %d" % type_of_life['id']

    def eotw(self, _):
        if self.population == 0:
            print 'Game over. Time = %d' % self.time
            sys.exit(1)
        
        print "There are %d life forms still available." % self.population



l = Life()
l.setup()

l.run()
