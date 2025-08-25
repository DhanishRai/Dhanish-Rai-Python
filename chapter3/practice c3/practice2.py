# write a program to fill in a letter template given below with name and date
# letter= ''' Dear <|Name|>,your are selected! <|Date|>'''

letter= ''' Dear <|Name|>,
 your are selected!
 <|Date|>'''
print(letter.replace("<|Name|>","Dhanish").replace("<|Date|>","06 september"))