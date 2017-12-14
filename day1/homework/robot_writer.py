# -*- coding: utf-8 -*-

""" See robot_writer.md for instruction
"""

total_unemployment_2009 = 5.9
total_unemployment_2014 = 8.0




def write_story(municipality, unemployment_2009, unemployment_2014):
    unemployment_diff = unemployment_2014 - unemployment_2009)
    total_unemployment_diff = total_unemployment_2014 - total_unemployment_2009
    if unemployment_2014 > unemployment_2009:
        print("In 2014, unemployment in %s was %s higher than before the financial crisis in 2009." % (municipality, unemployment_diff))
        print("It increased from %s%% to %s%%." % (unemployment_2009, unemployment_2014))
    else:
        print("In 2014, unemployment in %s was %s lower than before the financial crisis in 2009." % (municipality, -unemployment_diff))
        print("It decreased from %s%% to %s%%." % (unemployment_2009, unemployment_2014))
    if unemployment_diff > total_unemployment_diff:
        print "The development of this city has been a little worse than in the country where the unemployment rate during the same period grew by %s" % total_unemployment_diff
    else:
        print "The development of this city has been a little better than in the country where the unemployment rate during the same period grew by %s" % total_unemployment_diff


write_story("Stockholm", 7.1, 6.6)
print("**************")

write_story("Kiruna", 7.6, 4.2)
print("**************")

write_story("Lessebo", 9.5, 13.2)
print("**************")

"""
Source: http://www.ekonomifakta.se/sv/Fakta/Regional-statistik/Din-kommun-i-siffror/
"""
