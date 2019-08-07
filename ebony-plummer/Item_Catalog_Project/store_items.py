#Importing SQLAlchemy and other imports from sqlalchemy import create_engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from database_setup import Catagory, Base, StoreItem

#Create the engine and bind the engine to the metadata.
engine = create_engine('sqlite:///storeitems.db')

Base.metadata.bind = engine

#Create a session.
DBSession = sessionmaker(bind=engine)

session = DBSession()


#Item inventory for the books section.
books = Catagory(name="Books")

session.add(books)
session.commit()

storeItem1 = StoreItem(title="Python Crash Course", author="Eric Matthes", genre="Computer Programming",\
		description="A hands-on, project-based introduction to programming.", price="29.95",\
		catagory=books)

session.add(storeItem1)
session.commit()

storeItem2 = StoreItem(title="Automate the Boring Stuff with Python", author="Al Sweigart", \
	    genre="Computer Programming", description="Practical programming for beginners",\
	    price="29.95", catagory=books)

session.add(storeItem2)
session.commit()

storeItem3 = StoreItem(title="Don Quioxte", author="Migual De Cervantes", genre="Classic Literature",\
		description="Alonso Quixano, a retired country gentleman in his fifties, lives in an\
		unnamed section of La Mancha with his niece and a housekeeper. He has become obsessed\
		with books of chivalry, and believes their every word to be true, despite the fact that\
		many of the events in them are clearly impossible. Quixano eventually appears to other\
		people to have lost his mind from little sleep and food and because of so much reading.",\
		price="15.00", catagory=books)

session.add(storeItem3)
session.commit()

storeItem4 = StoreItem(title="A Brief History of Time", author="Stephen Hawking", genre="Science",\
		description="This essential book on cosmology explains complex concepts such as space,\
		time, and black holes to the layman from a scientific point of view. Published in 1988,\
		this is one of the best science books of all time. It has since sold ten million copies\
		and been revised to represent advances in technology made in the past two decades. Through\
		it readers will be able to understand and appreciate the complexity of the universe.",\
		price="15.00", catagory=books)

session.add(storeItem4)
session.commit()

storeItem5 = StoreItem(title="Catch-22", author="Joseph Heller", genre="Classic Literature",\
		description="Catch-22 is a satirical, historical novel by the American author \
		Joseph Heller, first published in 1961. The novel, set during the later stages \
		of World War II from 1943 onwards, is frequently cited as one of the great literary \
		works of the twentieth century. It has a distinctive non-chronological style where \
		events are described from different characters' points of view and out of sequence so\
		that the time line develops along with the plot.", catagory=books)

session.add(storeItem5)
session.commit()



#Inventory for the music section.
music = Catagory(name="Music")

session.add(music)
session.commit()

storeItem6 = StoreItem(title="Sgt. Pepper's Lonely Hearts Club Band by The Beatles", \
		 author="The Beatles", genre="Rock",price="15.00", catagory=music)

session.add(storeItem6)
session.commit()

storeItem7 = StoreItem(title="1999", author="Prince", genre="R&B/Soul", price="$10.00", \
	     catagory=music)

session.add(storeItem7)
session.commit()

storeItem8 = StoreItem(title="Tapestry", author="Carol King", genre="Pop", price="$10.00",\
		 catagory=music)

session.add(storeItem8)
session.commit()

storeItem9 = StoreItem(title="21", author="Adele", genre="Pop", price="$10.00", catagory=music)

session.add(storeItem9)
session.commit()

storeItem10 = StoreItem(title="The Planets", author="Gustav Holst", genre="Classical", price="$10.00",\
		 catagory=music)

session.add(storeItem10)
session.commit()


#Inventory for the movie section.

movies = Catagory(name="Movies")

session.add(movies)
session.commit

storeItem11 = StoreItem(title="Dr. Strangelove, or How I Learned to Stop Worrying and Love the Bomb",\
		 author="Stanley Kubrick", genre="Comedy", description="Stars: Peter Sellers; George C. Scott;\
		 Kubrick's black comedy of US nuclear bomb launch on Russia, focuses on an American president,\
		 played by Sellers in one of his three roles, who must contend with a Soviet nuclear attack on \
		 the United States and his own maniacal staff, including Scott's memorable General Turgidson. \
		 Features a memorable triad of performances by Sellers (as US president, British officer,\
		 and deranged scientist) and Pickens's wild ride on a missile.", price="$10.00",\
		 catagory=movies)

session.add(storeItem11)
session.commit()

storeItem12 =  StoreItem(title="All about Eve", genre="Drama", author="Joseph L. Mankiewicz,",\
	   description="Stars: Bette Davis; Anne Baxter; George Sanders;Celeste Holm; Thelma Ritter \
	   Classic story of backstage betrayal, with Davis as the aging star Margo Channing and Baxter\
	   as the young schemer Eve Harrington. Fasten your seat belts for a bumpy ride in this story of\
	   an aging actress who is undone by a young, ambitious fan. Sophisticated performances by Davis,\
	   Sanders and Baxter shine in this scathing look at the world of the theater. Academy Award winner\
	   for Best Picture, it is memorable for Sanders' role as the cynical critic and Marilyn Monroe as\
	   his scene-stealing consort.", price="$10.00", catagory=movies)

session.add(storeItem12)
session.commit()

storeItem13 = StoreItem(title="Fantasia", genre="Animation", author="James Algar, Ben Sharpsteen,\
	     Walt Disney",description="Stars: Deems Taylor (narrator); Leopold Stokowski (himself) and the\
	     Philadelphia Orchestra Disney's groundbreaking union and mixture of classical music and \
	     animated images is a visual feast for young and old. Presented in a dazzling, eight-part \
	     imaginative journey. Musical selections include Dukas''The Sorcerer's Apprentice', with \
	     Mickey Mouse as the apprentice in one of the film's most indelible images, and Stravinsky's\
	     'Rite of Spring'.", price="$5.00",catagory=movies)

session.add(storeItem13)
session.commit()

storeItem14 = StoreItem(title="Citizen Kane", genre="Drama", author="Orson Wells", description="Stars:\
	  	 Orson Welles; Joseph Cotten; Everett Sloane, Agnes Moorehead Welles' first feature - the\
 		 tragic story of newspaper tycoon Charles Foster Kane (Welles), loosely modeled after the \
 		 life of William Randolph Hearst, founder of the Hearst publishing empire, and the publisher's\
 		 ultimately empty rise to power. Acclaimed for its innovative narrative structure, deep focus\
 		 cinematography, soundtrack, literate screenplay, and nuanced portrayal of the central character)",\
 		 price="10.00", catagory=movies)

session.add(storeItem14)
session.commit()

storeItem15 = StoreItem(title="Star Wars", genre="Science Fiction", author="George Lucas", description="Stars:\
	     Mark Hamill; Harrison Ford; Carrie Fisher; Alec Guinness Spectacular space adventure combined\
	     a simple story of good vs. evil with stunning visual effects and endearing robotic characters \
	     to revolutionize the science fiction and action genres and make a star of Harrison Ford. \
	     A landmark science fiction fantasy about a young man, Luke Skywalker (Hamill), who finds his \
	     calling as a Jedi warrior and with the help of 'droids' and an outlaw named Han Solo (Ford),\
	     then embarks on a mission to rescue a princess (Fisher) and save the galaxy from the Dark Side.\
	     'May the force be with you.' Two sequels and prequels followed.", price="$10.00",\
	     catagory=movies)

session.add(storeItem15)
session.commit()


print("Added Store Items!")
