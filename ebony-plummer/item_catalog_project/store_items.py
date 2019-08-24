# This file contains the items that will be inserted into the
# database_setup.py file.

# Import Dependencies
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, StoreItem, User

# Connect to the database that was created in the database_set.py file.
# engine = create_engine('sqlite:///storeitemsinventory.db')

engine = create_engine('sqlite:///storeitemsinventorywithusers.db')

"""
Bind the engine to the metadata of the Base class so that the
declaratives can be accessed through a DBSession instance.
"""
Base.metadata.bind = engine


# Create a session in order to insert data into the Store Items Inventory
# database.
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create a test user.
User1 = User(name="Ebony N. Plummer",
             email="ebony.plummer@keepitsts.com", picture="#")

session.add(User1)
session.commit()

# Books

category1 = Category(user_id=1, name="Books")

session.add(category1)
session.commit()

storeItem1 = StoreItem(user_id=1,
                       name="Python Crash Course",
                       author="Eric Matthes",
                       genre="Computer Programming",
                       price="$25.00",
                       description="""A hands-on, project-based introduction
                       to programming.""",
                       category=category1)

session.add(storeItem1)
session.commit()

storeItem2 = StoreItem(user_id=1,
                       name="Automate the Boring Stuff with Python",
                       author='Al Sweigart',
                       genre="Compute Programming",
                       price="$25.00",
                       description="""A practical guide to programming total
                       beginners.""",
                       category=category1)

session.add(storeItem2)
session.commit()

storeItem3 = StoreItem(user_id=1,
                       name="Don Quixote",
                       author="Miguel de Cervantes",
                       genre="Classic Literature",
                       price="$15.00",
                       description="""Alonso Quixano, a retired country
                       gentleman in his fifties,  lives in an unnamed section
                       of La Mancha with his niece and a housekeeper. He has
                       become  obsessed with books of chivalry, and believes
                       their every word to be true, despite the fact that many
                       of the events in them are clearly impossible. Quixano
                       eventually appears to other  people to have lost his
                       mind from little sleep and food and because of so much
                       reading.""",
                       category=category1)

session.add(storeItem3)
session.commit()

storeItem4 = StoreItem(user_id=1,
                       name="A Brief History of Time",
                       author="Stephen Hawking",
                       genre="Science",
                       price="$15.00",
                       description="""This essential book on cosmology
                       explains complex concepts such as space, time, and
                       black holes to the layman from a scientific point of
                       view. Published in 1988, this is one of the best
                       science books of all time. It has since sold ten
                       million copies and been revised to represent advances
                       in technology made in the past two decades. Through it,
                       readers will be able to understand and appreciate the
                       complexity of the universe.""",
                       category=category1)

session.add(storeItem4)
session.commit()

storeItem5 = StoreItem(user_id=1,
                       name="Catch-22",
                       author="Joseph Heller",
                       genre="Classic Fiction",
                       price="$10.00",
                       description="""Catch-22 is a satirical, historical
                       novel by the American author Joseph Heller, first
                       published in 1961. The novel, set during the later
                       stages of World War II from 1943 onwards, is frequently
                       cited as one of the great literary works of the
                       twentieth century. It has a distinctive
                       non-chronological style  where events are described
                       from different characters'  points of view and out of
                       sequence so that the time-line develops along with the
                       plot.""",
                       category=category1)

session.add(storeItem5)
session.commit()


# Music

category2 = Category(user_id=1, name="Music")

session.add(category2)
session.commit()

storeItem6 = StoreItem(user_id=1,
                       name="Sgt. Peppers Lonely Hearts Club Band",
                       author="The Beatles",
                       genre="Rock",
                       price="10.00",
                       description="Year Released: 1967",
                       category=category2)

session.add(storeItem6)
session.commit()

storeItem7 = StoreItem(user_id=1,
                       name="1999",
                       author="Prince",
                       genre="R&B/Soul",
                       price="$10.00",
                       description="Year Released: 1982",
                       category=category2)

session.add(storeItem7)
session.commit()


storeItem8 = StoreItem(user_id=1,
                       name="21",
                       author="Adele",
                       genre="Pop",
                       price="$10.00",
                       description="Year Release: 2011",
                       category=category2)

session.add(storeItem8)
session.commit()

storeItem9 = StoreItem(user_id=1,
                       name="Songs in the Key of Life",
                       author="Stevie Wonder",
                       genre="R&B/Soul",
                       price="10.00",
                       description="Year Released: 1976",
                       category=category2)

session.add(storeItem9)
session.commit()

storeItem10 = StoreItem(user_id=1,
                        name="The Planets",
                        author="Gustave Holst",
                        genre="classical",
                        price="$10.00",
                        description="Year Premiere: 1918",
                        category=category2)

session.add(storeItem10)
session.commit()


# Movies

category3 = Category(user_id=1, name="Movies")

session.add(category3)
session.commit()

storeItem11 = StoreItem(user_id=1,
                        name="Citizen Kane (1941)",
                        author="Orson Wells",
                        genre="Drama", price="$10.00",
                        description="""Stars: Orson Welles; Joseph Cotten;
                        Everett Sloane, Agnes Moorehead Synopsis: Welles'
                        first feature - the tragic story of newspaper tycoon
                        Charles Foster Kane (Welles), loosely modeled after
                        the life of William Randolph Hearst, founder of the
                        Hearst publishing empire, and the publisher's
                        ultimately empty rise to power. Acclaimed for its
                        innovative narrative structure,  deep focus
                        cinematography, soundtrack, literate screenplay, and
                        nuanced portrayal of the central  character.""",
                        category=category3)

session.add(storeItem11)
session.commit()

storeItem12 = StoreItem(user_id=1,
                        name="All about Eve (1950)",
                        author="Joseph L. Mankiewicz",
                        genre="Drama",
                        price="$10.00",
                        description="""Stars: Bette Davis; Anne Baxter; George
                        Sanders; Celeste Holm; Thelma Ritter Synopsis: Classic
                        story of backstage betrayal, with Davis as the aging
                        star Margo Channing and Baxter as the young schemer
                        Eve Harrington. Fasten your seat belts for a bumpy
                        ride in this story  of an aging actress who is undone
                        by a young, ambitious fan. Sophisticated performances
                        by Davis,  Sanders and Baxter shine in this scathing
                        look at the world of the theater. Academy Award winner
                        for Best Picture, it is memorable for Sanders' role
                        as the cynical critic and Marilyn Monroe as  his
                        scene-stealing consort.""",
                        category=category3)

session.add(storeItem12)
session.commit()

storeItem13 = StoreItem(user_id=1,
                        name="""Dr. Strangelove, Or: How I Learned To Stop
                        Worrying And Love The Bomb (1964)""",
                        author="Stanley Kubrick",
                        genre="Comedy",
                        price="$10.00",
                        description="""Stars: Peter Sellers;  George C. Scott;
                        Sterling Hayden; Slim Pickens Synopsis: Kubrick's
                        black comedy of US nuclear  bomb launch on Russia,
                        focuses on an American president, played by Sellers in
                        one of his three  roles, who must contend with a
                        Soviet nuclear attack on the United States and his own
                        maniacal  staff, including Scott's memorable General
                        Turgidson. Features a memorable triad of performances
                        by Sellers (as US president, British officer, and
                        deranged scientist) and Pickens's wild ride on  a
                        missile. "Gentlemen, you can't fight in here! This is
                        the War Room!""",
                        category=category3)

session.add(storeItem13)
session.commit()

storeItem14 = StoreItem(user_id=1,
                        name="Fantasia (1940)",
                        author="""James Algar, Ben Sharpsteen, Walt Disney and
                        others""",
                        genre="Animation",
                        price="$7.50",
                        description="""Stars: Deems Taylor (narrator); Leopold
                        Stokowski (himself) and the Philadelphia Orchestra
                        Synopsis: Disney's groundbreaking union and mixture of
                        classical music and animated images is a visual feast
                        for young and old. Presented in a dazzling,
                        eight-part imaginative journey. Musical selections
                        include Dukas' "The Sorcerer's Apprentice,"  with
                        Mickey Mouse as the apprentice in one of the film's
                        most indelible images, and Stravinsky's  "Rite of
                        Spring.""",
                        category=category3)

session.add(storeItem14)
session.commit()

storeItem15 = StoreItem(user_id=1,
                        name="Star Wars (1977)",
                        author="George Lucas",
                        genre="Science Fiction",
                        price="$10.00",
                        description="""Stars: Mark Hamill; Harrison Ford;
                        Carrie Fisher; Alec Guinness  Synopsis: Spectacular
                        space adventure combined a simple story of good vs.
                        evil with stunning visual  effects and endearing
                        robotic characters to revolutionize the science
                        fiction and action genres and  make a star of Harrison
                        Ford. A landmark science fiction fantasy about a young
                        man, Luke Skywalker (Hamill), who finds his calling as
                        a Jedi warrior and with the help of "droids" and  an
                        outlaw named Han Solo (Ford), then embarks on a
                        mission to rescue a princess (Fisher) and save the
                        galaxy from the Dark Side. "May the force be with
                        you." Two sequels and prequels followed.""",
                        category=category3)

session.add(storeItem15)
session.commit()


# Print out that the store items have been added to the database.
print("All items have been added to the database!")
