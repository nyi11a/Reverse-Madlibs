import textwrap

nums_to_fill= ["-1-", "-2-", "-3-", "-4-"] #the blanks in each text
levels= ["easy", "hard", "medium"]
answers= []
answers2= ["string", "indexing", "subsequence", "method"]
answers3= ["procedures", "calling", "defining", "parameters"]
answers1= ["numbers", "assignment", "variables", "string"]

text1= """ Variables are names that stand in for -1- . -2- statements are how we 
introduce variables and they tend to look something like this: Name = Expression, where the 
name refers to the value that the expression has. -3- can vary, they don't always stay 
constant. Variabls can also be letters in which case they form a -4- , a sequence of 
characters surrounded by single or double quotes."""


text2= """ Each character in a -1- is numbered starting from zero, with the number
 increasing all the way to the end of the string. For example, in 'udacity' [0], the 
 number zero corresponds to the letter "u." To find a particular character or set of 
 characters in a string you need to become familiar with string -2-. Indexing looks
 like this: <string> [< start- expression (number)>:< stop- expression(number>]. The
 result will be a string that is a -3- of all the characters in the string, 
 starting from position start and ending with position stop but not including that 
 character (so up through stop minus 1). The find -4- is a more straightforward way 
 to to find a string within a string."""


text3="""Functions are also called -1- or methods. They take input, do something 
with it and return an output. We use functions by passing in values for the parameters 
of the inputs in the parenthesis. This process is what is meant by -2- the 
function: Calling a function is the act of executing it. But before a function can be 
called, it must be declared. -3- a function is the process of declaring the 
function that you will call and the arguments/operants that you will pass into it.
On the first line of your function definition, you must begin with "def". After "def" 
you must assign a function name. Next, you must have a set of parentheses 
with the required -4- inside.The line must end with a colon.  """

def process_madlib1(mad_lib): #once level selected user_input will fill in responses
	i= 0 
	while i <= 3: # i is 3 because counter only needs to go from 0-3... number of questions in each level
		user_input= raw_input("Give the answer for number"+ " " + str(i+1) + " ") 
		while user_input != answers[i]: #loop to ask for user input until a correct answer is entered
			print "Sorry, wrong answer. Try again"
			user_input= raw_input("Give the answer for number"+ " " + str(i+1) + " ")
		if user_input in answers[i]: 
			blank= nums_to_fill[i]
			fill= answers[i]
			filled_in_response= mad_lib.replace(blank, fill)
			print textwrap.fill(filled_in_response, 75)
			if i >= 3: 
				print "You are done with this level. Nice Job!"
				break
			i += 1

def pick_answer_key(num): 
	global answers 
	answers= []
	answers2= ["string", "indexing", "subsequence", "method"]
	answers3= ["procedures", "calling", "defining", "parameters"]
	answers1= ["numbers", "assignment", "variables", "string"]
	if num == 1: 
		answers= answers1
	elif num == 2:
		answers = answers2 
	else: 
		answers= answers3 



def pick_level(): #Users will pick one of the three text levels to play
	level_selection= raw_input("Type Your level: Easy, Medium or Hard" + " ")
	if level_selection not in ["easy", "medium", "hard"]: 
		level_selection= raw_input("Please Type Your Level: Easy, Medium or Hard" + " ")
	if level_selection == "easy":
		pick_answer_key(1)
		print textwrap.fill(text1,75)
		return process_madlib1(text1)
	elif level_selection== "medium":#changing the values in the answer key to reflect level of difficulty
		pick_answer_key (2)
		print textwrap.fill(text2,75) 
		return process_madlib1(text2)
	elif level_selection== "hard": 
		pick_answer_key(3)
		print textwrap.fill(text3,75) 
		return process_madlib1(text3)
pick_level ()