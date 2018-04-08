# -*- coding: utf-8 -*-

# http://pythonhosted.org/pyparsing/

from pyparsing import Word, alphas, Suppress, Group, OneOrMore, FollowedBy, ZeroOrMore

# define grammar of a greeting
greet = Word(alphas) + "," + Word(alphas) + "!"

hello = "Hello, World!"
print (hello, "->", greet.parseString(hello))
print ("length : ", len(greet.parseString(hello)))

token = Suppress(",")
grammar = Word(alphas) + token + Group(OneOrMore(Word(alphas))) + "!"
yes = "Yes, You can!"
print (grammar.parseString(yes))
print ("length : ", len(grammar.parseString(yes)))


# http://pythonhosted.org/pyparsing/pyparsing.OneOrMore-class.html

# Class OneOrMore
# Repetition of one or more of the given expression.

# Parameters:

# expr - expression that must match one or more times
# stopOn - (default=None) - expression for a terminating sentinel (only required if the sentinel would ordinarily match the repetition expression)

data_word = Word(alphas)
label = data_word + FollowedBy(':')
attr_expr = Group(label + Suppress(':') + OneOrMore(data_word).setParseAction(' '.join))
text = "shape: SQUARE posn: upper left color: BLACK"
print(text)
OneOrMore(attr_expr).parseString(text).pprint() # Fail! read 'posn' as data instead of next label -> [['shape', 'SQUARE posn']]

# use stopOn attribute for OneOrMore to avoid reading label string as part of the data
attr_expr = Group(label + Suppress(':') + OneOrMore(data_word, stopOn=label).setParseAction(' '.join))
OneOrMore(attr_expr).parseString(text).pprint() # [['shape', 'SQUARE'], ['posn', 'upper left'], ['color', 'BLACK']]

# could also be written as
(attr_expr * (1,)).parseString(text).pprint() # [['shape', 'SQUARE'], ['posn', 'upper left'], ['color', 'BLACK']]

# what happen to remove .setParseAction(' '.join)
attr_expr = Group(label + Suppress(':') + OneOrMore(data_word, stopOn=label))
OneOrMore(attr_expr).parseString(text).pprint() # [['shape', 'SQUARE'], ['posn', 'upper', 'left'], ['color', 'BLACK']]


# http://pythonhosted.org/pyparsing/pyparsing.Suppress-class.html
# Converter for ignoring the results of a parsed expression.
source = "a, b, c, d"
wd = Word(alphas)
wd_list1 = wd + ZeroOrMore(',' + wd)
print(wd_list1.parseString(source)) # ['a', ',', 'b', ',', 'c', ',', 'd']

# often, delimiters that are useful during parsing are just in the
# way afterward - use Suppress to keep them out of the parsed output
wd_list2 = wd + ZeroOrMore(Suppress(',') + wd)
print(wd_list2.parseString(source)) # ['a', 'b', 'c', 'd']

