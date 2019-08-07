#Importing SQLAlchemy and other imports from sqlalchemy import create_engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from database_setup import Catagory, Base, BookItem, MusicItem, MovieItem

#Create the engine and bind the engine to the metadata.
engine = create_engine('sqlite:///storeitems.db')

Base.metadata.bind = engine

#Create a session.
DBSession = sessionmaker(bind=engine)

session = DBSession()

#Item inventory for the books section.
bookCatagory = Catagory(name="Books")

session.add(bookCatagory)
session.commit()

book1 = BookItem(title="Python Crash Course", author="Eric Matthes", genre="Computer Programming",\
		description="A hands-on, project-based introduction to programming.", price="29.95",\
		catagory=bookCatagory)

session.add(book1)
session.commit()

book2 = BookItem(title="Automate the Boring Stuff with Python", author="Al Sweigart", \
	    genre="Computer Programming", description="Practical programming for beginners",\
	    price="29.95", catagory=bookCatagory)

session.add(book2)
session.commit()

book3 = BookItem(title="Don Quioxte", author="Migual De Cervantes", genre="Classic Literature",\
		description="Alonso Quixano, a retired country gentleman in his fifties, lives in an\
		unnamed section of La Mancha with his niece and a housekeeper. He has become obsessed\
		with books of chivalry, and believes their every word to be true, despite the fact that\
		many of the events in them are clearly impossible. Quixano eventually appears to other\
		people to have lost his mind from little sleep and food and because of so much reading.",\
		price="15.00", catagory=bookCatagory)

session.add(book3)
session.commit()

book4 = BookItem(title="A Brief History of Time", author="Stephen Hawking", genre="Science",\
		description="This essential book on cosmology explains complex concepts such as space,\
		time, and black holes to the layman from a scientific point of view. Published in 1988,\
		this is one of the best science books of all time. It has since sold ten million copies\
		and been revised to represent advances in technology made in the past two decades. Through\
		it readers will be able to understand and appreciate the complexity of the universe.",\
		price="15.00", catagory=bookCatagory)

session.add(book4)
session.commit()

book5 = BookItem(title="Catch-22", author="Joseph Heller", genre="Classic Literature",\
		description="Catch-22 is a satirical, historical novel by the American author \
		Joseph Heller, first published in 1961. The novel, set during the later stages \
		of World War II from 1943 onwards, is frequently cited as one of the great literary \
		works of the twentieth century. It has a distinctive non-chronological style where \
		events are described from different characters' points of view and out of sequence so\
		that the time line develops along with the plot.", catagory=bookCatagory)

session.add(book5)
session.commit()



#Inventory for the music section.
musicCatagory = Catagory(name="Music")

album1 = MusicItem(title="Sgt. Pepper's Lonely Hearts Club Band by The Beatles", \
		 artist="The Beatles", genre="Rock",price="15.00", catagory=musicCatagory)

session.add(album1)
session.commit()

album2 = MusicItem(title="1999", artist="Prince", genre="R&B/Soul", price="$10.00", \
	     catagory=musicCatagory)

session.add(album2)
session.commit()

album3 = MusicItem(title="Tapestry", artist="Carol King", genre="Pop", price="$10.00",\
		 catagory=musicCatagory)

session.add(album3)
session.commit()

album4 = MusicItem(title="21", artist="Adele", genre="Pop", price="$10.00")

session.add(album4)
session.commit()

album5 = MusicItem(title="The Planets", artist="Gustav Holst", genre="Classical", price="$10.00")

session.add(album5)
session.commit()


#Inventory for the movie section.

movieCatagory = Catagory(name="Movies")

movie1 = MovieItem(title="Dr. Strangelove, or How I Learned to Stop Worrying and Love the Bomb",\
		 director="Stanley Kubrick", genre="Comedy", stars="Peter Sellers; George C. Scott;\
		 Sterling Hayden; Slim Pickens", description="Kubrick's black comedy of US \
		 nuclear bomb launch on Russia, focuses on an American president, played by Sellers in \
		 one of his three roles, who must contend with a Soviet nuclear attack on the United \
		 States and his own maniacal staff, including Scott's memorable General Turgidson. \
		 Features a memorable triad of performances by Sellers (as US president, British officer,\
		 and deranged scientist) and Pickens's wild ride on a missile.", price="$10.00",\
		 catagory=movieCatagory)

session.add(movie1)
session.commit()

movie2 =  MovieItem(title="All about Eve", genre="Drama", director="Joseph L. Mankiewicz",\
	   stars="Bette Davis; Anne Baxter; George Sanders;Celeste Holm; Thelma Ritter ",\
	   description="Classic story of backstage betrayal, with Davis as the aging star\
	   Margo Channing and Baxter as the young schemer Eve Harrington. Fasten your seat\
	   belts for a bumpy ride in this story of an aging actress who is undone by a young,\
	   ambitious fan. Sophisticated performances by Davis, Sanders and Baxter shine in this\
	   scathing look at the world of the theater. Academy Award winner for Best Picture, \
	   it is memorable for Sanders' role as the cynical critic and Marilyn Monroe as his \
	   scene-stealing consort.", price="$10.00", catagory=movieCatagory)

session.add(movie2)
session.commit()

movie3 = MovieItem(title="Fantasia", genre="Animation", director="James Algar, Ben Sharpsteen,\
	     Walt Disney",stars="Deems Taylor (narrator); Leopold Stokowski (himself) and the\
	     Philadelphia Orchestra", description="Disney's groundbreaking union and mixture of \
	     classical music and animated images is a visual feast for young and old. Presented\
	     in a dazzling, eight-part imaginative journey. Musical selections include Dukas'\
	     'The Sorcerer's Apprentice', with Mickey Mouse as the apprentice in one of the \
	     film's most indelible images, and Stravinsky's 'Rite of Spring'.", price="$5.00",\
	     catagory=movieCatagory)

session.add(movie3)
session.commit()

movie4 = MovieItem(title="Citizen Kane", genre="Drama", director="Orson Wells", stars="Orson Welles;\
 		 Joseph Cotten; Everett Sloane, Agnes Moorehead", description="Welles' first feature - the\
 		 tragic story of newspaper tycoon Charles Foster Kane (Welles), loosely modeled after the \
 		 life of William Randolph Hearst, founder of the Hearst publishing empire, and the publisher's\
 		 ultimately empty rise to power. Acclaimed for its innovative narrative structure, deep focus\
 		 cinematography, soundtrack, literate screenplay, and nuanced portrayal of the central character)",\
 		 price="10.00", catagory=movieCatagory)

session.add(movie4)
session.commit()

movie5 = MovieItem(title="Star Wars", genre="Science Fiction", director="George Lucas", stars="Mark Hamill;\
         Harrison Ford; Carrie Fisher; Alec Guinness", description="Spectacular space adventure combined a \
         simple story of good vs. evil with stunning visual effects and endearing robotic characters to \
         revolutionize the science fiction and action genres and make a star of Harrison Ford. A landmark\
         science fiction fantasy about a young man, Luke Skywalker (Hamill), who finds his calling as a\
         Jedi warrior and with the help of 'droids' and an outlaw named Han Solo (Ford), then embarks on\
         a mission to rescue a princess (Fisher) and save the galaxy from the Dark Side. 'May the force \
         be with you.' Two sequels and prequels followed.", price="$10.00", catagory=movieCatagory)

session.add(movie5)
session.commit()


print("Added Store Items!")
