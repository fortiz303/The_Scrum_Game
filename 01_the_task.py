import time

print ("You are a Scrum Master without much experience and are interviewing at a company that is building a subdivision of houses. They are looking for a Scrum Master and ask if Scrum is the best framework to help manage workers and the process of building houses...") 

time.sleep(2)

house_scrum_accepted = str(input("Do you believe that Scrum is the best framework to build these houses? Type yes or no: "))

#print(house_scrum_accepted)
#print(type(house_scrum_accepted))

if house_scrum_accepted == "yes":
	print("Scrum is a framework that deals with unknown complexities. In a project like building houses, a lot is already known (e.g. materials that will be used, speed of construction of one house), and so a Waterfall approach would be better suited for this type of project. Waterfall is better suited when we are solving problems with a lot of certanties, Scrum deals where there are a number of uncertanties. Start over:) ")
if house_scrum_accepted == "no":
	print("Good job! Scrum is better suited where there are a lot of unknowns. During these projects, there is a lot of uncertainty, so the team is able to build, measures, and learn much faster, and that way improve much faster for the next iteration. This is what it means when Scrum is defined as a framework that is able to generate value through adaptive solutions for complex problems. Although building a house is difficult work, it is not complex as the whole scope of the project is already known")
