#String manipulations in Python starts from here
print "===== String manipulations in Python starts from here ====="
str = 'hello world'
print'1 -', str               # 1 - prints hello world
print'2-', str[0]            # 2 - prints h
print'3-', str[2:]           # 3 - prints llo world
print'4-', str[2:7]          # 4 - prints llo w
print'5-', str * 2           # 5 - prints hello worldhello world
print'6-', str + " I am here"# 6 - prints hello world I am here
print'7-', str[:2]           # 7 - prints he
print'8-', str[-5:-3]        # 8 - prints wo
print'9-', str[-5:8]         # 9 - prints wo
print'10-', str[2:-4]         # 10 - prints llo w
print'11-', '''I am a good boy lets see '''   # 11-  prints this statement
print'12-', "this is a test"                  # 12 - prints this statement


#List manipulations in Python starts from here
print "===== List manipulations in Python starts from here ======"
list = ['good', 'better', 45, 'best', 39, 50.1, 0x78, 'result']
slist = ['bad', 'worst']
print '1-',list          # 1 - prints whole list
print '2-',list [0]      # 2 - prints good
print '3-',list [2]      # 3 - prints 45
print '4-',list [3:4]    # 4 - prints best
print '5-',list * 2      # 5 - prints list twice
print '6-',list + slist  # 6 - prints list and then slist
print '7-',list [2:]     # 7 - prints 45 till end
print '8-',list [:]      # 8 - prints whole list
print '9-',list [:2]     # 9 - prints good, better
print '10-',list [4:-3]   # 10 - prints 39
print '11-',list [-6:-2]  # 11 - prints 45 best 39 50.1
print '12-',list [-6: 5]  # 12 - prints 45 best 39
print '13-',list [-7:-3]  # 13 - prints better 45 best 39
print '14-',list [-3: 6]  # 14 - prints 50.1
print '15-',list [:-8]    # 15 - prints nothing
for index in range(len(list)):
    print 'Current Value is ', list[index]


#Tuple manipulations in Python starts from here
print "===== Tuple manipulations in Python starts from here ====="
tuple = ("what", 'when', 'how', 'who', 'why', 70.2, 45, 98.3,390)
stuple = ('I', "me", "my", '''mine''')
print'1-', tuple         # 1- prints full tuple
print'2-', tuple[0]      # 2- prints the value at 0th place i.e what
print'3-', tuple[5]      # 3- prints the value at 5th place i.e 70.2
print'4-', tuple[:]      # 4- prints the full tuple
print'5-', tuple[:2]     # 5- prints (what when)
print'6-', tuple[1:4]    # 6- prints (when, how, who)
print'7-', tuple[2:-3]   # 7- prints how till 70.2
print'8-', tuple[-3:2]   # 8- prints nothing
print'9-', tuple[-3:8]   # 9- prints 45 98.3
print'10-', tuple[9:-1]   # 10- prints nothing
print'11-', tuple[7:-1]   # 11- prints 98.3
print'12-', tuple[:-3]    # 12- prints from starting till 70.2
print'13-', tuple[3:]     # 13- prints from who till end
print'14-', tuple * 2     # 14- prints tuple twice
print'15-', tuple+stuple  # 15- prints tuple and then stuple

#Dictionary manipulations in Python starts from here
print "===== Dictionary manipulations in Python starts from here ====="
dict = {'1':'one', '2':'two', '3':3, '4':4.0, '5':'five', '6': -6}
print'1-', dict.keys()       # 1- prints the keys
print'2-', dict.values()     # 2- prints the values
print'3-', dict['1']         # 3- prints the value for key '1'
print'4-', dict              # 4- prints the full dictionary
print'5-', dict.get('4')     # 5- get the value for key '4' and prints
print'6-', dict.popitem()    # 6- pops one iteam from beginning and prints
print'7-', dict              # 7- prints the dict without the 1st item as the same has alreay been poped out
print'8-', dict.clear()      # 8- this clears the dictionary
print'9-', dict              # 9- prints nothing as the dictionary is cleared now
