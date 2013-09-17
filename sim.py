# Simulated Ideas, Man (SIM)

from random import random
import time

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
        time.sleep(5)

    def simulate(self):
        for event in self.occurs:
            for variable in self.dynamics:
                event(variable) 

    def run(self):

        # time starts here
        while self.time <= self.time_end:

            # things happen
            self.simulate()

            # time ticks by
            print 'Tick: %d' % self.time
            self.tick()

class Life(Simulation):

    def __init__(self):
        Simulation.__init__(self)
        
        self.time     = 2013
        self.time_end = 2038
        
        print "Life has begun has begun."
        self.beginning_of_time = self.time

        self.step     = 1

        self.occurs   = []

        self.dynamics = []

        self.ready    = 0

        # life specific
        self.population = 0

    def setup(self):
        print "Populating simulation..."

        self.population = 1000
        self.death_rate = 0.01

        for new_life in xrange(self.population):
            life_form = {}
            life_form['life'] = 'alive'
            life_form['type'] = 'human'
            life_form['id']   = new_life

            self.dynamics.append(life_form)

        self.occurs.append(self.death)

    def death(self, type_of_life):
        if type_of_life.get('life'):
            life = None if not random() > self.death_rate else type_of_life.get('life')
            type_of_life['life'] = life

            if not life:
                self.population -= 1
                print "A death to %d" % type_of_life['id']
                print "There are %d life forms still available." % self.population


l = Life()
l.setup()

l.run()
