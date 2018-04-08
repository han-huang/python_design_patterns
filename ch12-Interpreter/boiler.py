# -*- coding: utf-8 -*-

from pyparsing import Word, OneOrMore, Optional, Group, Suppress, alphanums

class Boiler:

    def __init__(self):
        self.temperature = 83  # in celsius

    def __str__(self):
        return 'boiler temperature: {}'.format(self.temperature)

    def increase_temperature(self, amount):
        print("increasing the boiler's temperature by {} degrees".format(amount))
        self.temperature += amount

    def decrease_temperature(self, amount):
        print("decreasing the boiler's temperature by {} degrees".format(amount))
        self.temperature -= amount

def main():
    word = Word(alphanums)
    command = Group(OneOrMore(word))
    token = Suppress("->")
    device = Group(OneOrMore(word))
    argument = Group(OneOrMore(word))
    event = command + token + device + Optional(token + argument)

    boiler = Boiler()
    print(boiler)

    cmd, dev, arg = event.parseString('increase -> boiler temperature -> 3 degrees')
    if 'increase' in ' '.join(cmd) :
        if 'boiler' in ' '.join(dev) :
            boiler.increase_temperature(int(arg[0]))
    print(boiler)

if __name__ == '__main__':
    main()
