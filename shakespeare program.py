
#you need to write a program that opens the files individually, displays the first line of each
#file, then allows the user to select which files to dive into. this can be done using if 'title'
#in file-maybe make it equal to userinput?
#once in the correct file, you need to start sectioning out parts-probably line by line with
#using indexing. after this you could divide by tabs, then by character (if startswith tab then ask for user input, do startswith(input)) (gonna be a pain in the ass)



shakespeareplays = {} #empty dictionary

import os

path = os.getcwd()

playList = os.listdir(path)

for items in playList:
    if '.txt' in items:
        print(items) #printing out all the text files in the current directory-hopefully theyre named with the names of the plays lol and theres nothing else in there
    else:
        pass

playName = input('please select a play from the list above and enter the name here: ') #setting the input as the play name to use in the loop later

#above works perfectly dont mess with it 


#make a .startwith(enter) to make the program ignore lines that start with enter
#you do not need to populate a dictionary right away-make empty ones and go from there
#you need to use indexing-not sure how to do this though


for items in os.listdir(path):
    file = os.path.join(path, items)
    if playName in file: #taking the user input from earlier
           with open(file, 'r') as inFile:
               for lines in inFile:
                    if lines.startswith ('ACT'): #searching for a line starting with act
                        acts = lines.strip() #stripping the line
                        shakespeareplays[acts] = {} #adding it to the shakespeare plays dictionary as a key without any values
                    else:
                        if lines.startswith('SCENE'): #rinse and repeat
                            scenes = lines.strip()
                            shakespeareplays[acts][scenes] = {}
                        else:
                            if "    " not in lines: #rinse and repeat with a little difference
                                characters = lines.strip()
                            else:
                                if characters not in shakespeareplays[acts][scenes].keys():
                                    shakespeareplays[acts][scenes][characters] = []
                                    shakespeareplays[acts][scenes][characters].append(lines.strip())

#EVERYTHING WORKS ABOVE THIS!!!! if you print the shakespeare dictionary it is perfect: dictionaries inside dictionaries with the lines being a list in the center
          
for keys in shakespeareplays: #printing the keys then giving the values
    print(keys)
acts = input('Please select an act from the list above. ')

for keys in shakespeareplays[acts]: #etc
    print(keys)
scenes = input('Please select a scene from the list above. ')

for keys in shakespeareplays[acts][scenes]: #this is where the code breaks. nothing beneath this works, it doesn't print the keys
    print(keys)
characters = input('Please select a character from the list above. ')

print('The lines for this character in the play,act,and scene you selected are ' + str(shakespeareplays[act][scene][characters][0]))

#youre going to have to fix this: you might just be able to print EVERYTHING that is inside a certain key. plus i dont think you need the len command here

    
'''

#code graveyard




                    else:
                        if lines.startswith('SCENE'):
                            a = lines.strip()
                            scenes = [1]
                            shakespeareplays[acts][scenes] = {}
                        else:
                            if not lines.startswith(' '):
                                a = lines.strip()
                                characters = [1]
                                shakespeareplays[acts][scenes][characters] = {}
                            else:
                                a = lines.strip()
                                finallines = [1]
                                shakespeareplays[acts][scenes][characters] = [finallines]


else:
                        if A.startswith('SCENE'):
                            shakespeareplays[A][A[0]] = {}
                        else:
                            if not A.startswith('\s'):
                                shakespeareplays[A][A[0]][A[1]] = {}
                            else:
                                shakespeareplays[A][A[0]][A[1]][A[2]] = [A[3]]

  A = lines.strip()
                   if A.startswith('ACT'):
                           shakespeareplays[A] = {}
                   else:
                        if A.startswith('SCENE'):
                            shakespeareplays[A] = {}
                           

'''


