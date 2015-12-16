class WikiGame:
    'Solution to wiki game'
        
def main ():
    #list of some wiki pages for game
    listOfArticles = ["http://en.wikipedia.org/wiki/Roanoke_Colony",
"http://en.wikipedia.org/wiki/John_Murray_Spear",
"http://en.wikipedia.org/wiki/Arecibo_reply",
"http://en.wikipedia.org/wiki/Tanganyika_Laughter_Epidemic",
"http://en.wikipedia.org/wiki/The_Mad_Gasser_of_Mattoon",
"http://en.wikipedia.org/wiki/Concrete-Encased_High_School_Girl_Murder_Case",
"http://en.wikipedia.org/wiki/Peoples_Temple",
"http://en.wikipedia.org/wiki/UKUSA",
"http://en.wikipedia.org/wiki/MRSA",
"http://en.wikipedia.org/wiki/Sailing_stones",
"http://en.wikipedia.org/wiki/Thalidomide",
"http://en.wikipedia.org/wiki/Unit_731",
"http://en.wikipedia.org/wiki/Bunny_Man",
"http://en.wikipedia.org/wiki/Sedlec_Ossuary",
"http://en.wikipedia.org/wiki/Bubbly_Creek",
"http://en.wikipedia.org/wiki/Original_Spanish_Kitchen",
"http://en.wikipedia.org/wiki/Charles_Bonnet_syndrome",
"http://en.wikipedia.org/wiki/Voynich_manuscript",
"http://en.wikipedia.org/wiki/Markovian_parallax_denigrate",
"http://en.wikipedia.org/wiki/Toynbee_tiles",
"http://en.wikipedia.org/wiki/Alien_hand_syndrome",
"http://en.wikipedia.org/wiki/Phaistos_Disc",
"http://en.wikipedia.org/wiki/Pykrete",
"http://en.wikipedia.org/wiki/Capgras_delusion",
"http://en.wikipedia.org/wiki/Polywater",
"http://en.wikipedia.org/wiki/Whole-body_transplant",
"http://en.wikipedia.org/wiki/Head_transplant",
"http://en.wikipedia.org/wiki/Robert_J._White",
"http://en.wikipedia.org/wiki/Vladimir_Demikhov",
"http://en.wikipedia.org/wiki/Guided_rat",
"http://en.wikipedia.org/wiki/Exploding_head_syndrome",
"http://en.wikipedia.org/wiki/Hamster_zona-free_ovum_test",
"http://en.wikipedia.org/wiki/Quantum_immortality",
"http://en.wikipedia.org/wiki/Chandre_Oram",
"http://en.wikipedia.org/wiki/Lina_Medina",
"http://en.wikipedia.org/wiki/Mellified_Man",
"http://en.wikipedia.org/wiki/STS-75",
"http://en.wikipedia.org/wiki/Atuk",
"http://en.wikipedia.org/wiki/Kennedy_Curse",
"http://en.wikipedia.org/wiki/Cure_for_Insomnia",
"http://en.wikipedia.org/wiki/Pripyat%2C_Ukraine",
"http://en.wikipedia.org/wiki/British_Rail_flying_saucer",
"http://en.wikipedia.org/wiki/Mary_Tofts",
"http://en.wikipedia.org/wiki/Trepanation",
"http://en.wikipedia.org/wiki/Grey_Goo",
"http://en.wikipedia.org/wiki/The_Grinning_Man",
"http://en.wikipedia.org/wiki/Crawfordsville_monster",
"http://en.wikipedia.org/wiki/Dulce_Base",
"http://en.wikipedia.org/wiki/Junko_Furuta",
"http://en.wikipedia.org/wiki/The_Hermitage_%28Ontario%29",
"http://en.wikipedia.org/wiki/Donner_Party",
"http://en.wikipedia.org/wiki/Albert_Fish",
"http://en.wikipedia.org/wiki/Starchild_skull",
"http://en.wikipedia.org/wiki/Jersey_Devil",
"http://en.wikipedia.org/wiki/Jack_Parsons",
"http://en.wikipedia.org/wiki/Faces_of_belmez",
"http://en.wikipedia.org/wiki/David_Parker_Ray",
"http://en.wikipedia.org/wiki/Total_information_awareness",
"http://en.wikipedia.org/wiki/Penis_panic",
"http://en.wikipedia.org/wiki/Wilhelm_Reich",
"http://en.wikipedia.org/wiki/The_Mahavishnu_Orchestra",
"http://en.wikipedia.org/wiki/Devil%27s_Footprints",
"http://en.wikipedia.org/wiki/The_Great_Thunderstorm%2C_Widecombe",
"http://en.wikipedia.org/wiki/The_Bloop",
"http://en.wikipedia.org/wiki/Out_of_place_artifacts",
"http://en.wikipedia.org/wiki/Mothman",
"http://en.wikipedia.org/wiki/Shadowpeople",
"http://en.wikipedia.org/wiki/Ararat_anomaly",
"http://en.wikipedia.org/wiki/String_theory",
"http://en.wikipedia.org/wiki/Tunguska_event",
"http://en.wikipedia.org/wiki/British_big_cats",
"http://en.wikipedia.org/wiki/Goatman_%28cryptozoology%29",
"http://en.wikipedia.org/wiki/Greys",
"http://en.wikipedia.org/wiki/Jackalope",
"http://en.wikipedia.org/wiki/Stargate_Project",
"http://en.wikipedia.org/wiki/Spring_Heeled_Jack",
"http://en.wikipedia.org/wiki/Owlman",
"http://en.wikipedia.org/wiki/Anomalous_phenomenon",
"http://en.wikipedia.org/wiki/Bermuda_triangle",
"http://en.wikipedia.org/wiki/Overtoun_Bridge",
"http://en.wikipedia.org/wiki/The_Mad_Gasser_of_Mattoon",
"http://en.wikipedia.org/wiki/Chupa_%28anomaly%29",
"http://en.wikipedia.org/wiki/Silverpilen",
"http://en.wikipedia.org/wiki/Lost_Dutchman%27s_Gold_Mine",
"http://en.wikipedia.org/wiki/Aokigahara",
"http://en.wikipedia.org/wiki/Pope_Lick_Monster",
"http://en.wikipedia.org/wiki/Shadow_people",
"http://en.wikipedia.org/wiki/Steam_tunnel_incident",
"http://en.wikipedia.org/wiki/Montauk_Project",
"http://en.wikipedia.org/wiki/Moll_Dyer",
"http://en.wikipedia.org/wiki/Belchen_Tunnel",
"http://en.wikipedia.org/wiki/Boy_Scout_Lane",
"http://en.wikipedia.org/wiki/The_Devil%27s_Footprints",
"http://en.wikipedia.org/wiki/Chase_Vault",
"http://en.wikipedia.org/wiki/Dyatlov_pass_accident",
"http://en.wikipedia.org/wiki/Tunguska_event",
"http://en.wikipedia.org/wiki/Borley_Rectory",
"http://en.wikipedia.org/wiki/Clapham_Wood_Mystery",
"http://en.wikipedia.org/wiki/Reality_shift",
"http://en.wikipedia.org/wiki/Moberly-Jourdain_incident",
"http://en.wikipedia.org/wiki/Ed_Gein",
"http://en.wikipedia.org/wiki/Adam_%28unsolved_Thames_murder_case%29",
"http://en.wikipedia.org/wiki/Who_put_Bella_in_the_Wych_Elm%3F",
"http://en.wikipedia.org/wiki/Cleveland_Torso_Murderer",
"http://en.wikipedia.org/wiki/Monster_of_Glamis",
"http://en.wikipedia.org/wiki/Ediacaran_biota",
"http://en.wikipedia.org/wiki/H._H._Holmes",
"http://en.wikipedia.org/wiki/Loveland_Frog",
"http://en.wikipedia.org/wiki/Mariana_UFO_Incident",
"http://en.wikipedia.org/wiki/Amelia_Earhart",
"http://en.wikipedia.org/wiki/Valentich_Disappearance",
"http://en.wikipedia.org/wiki/Original_Night_Stalker",
"http://en.wikipedia.org/wiki/Black_Dahlia",
"http://en.wikipedia.org/wiki/Joachim_Kroll",
"http://en.wikipedia.org/wiki/Peter_K%C3%BCrten",
"http://en.wikipedia.org/wiki/Gilles_de_Rais",
"http://en.wikipedia.org/wiki/Joseph_Vacher",
"http://en.wikipedia.org/wiki/Melonheads",
"http://en.wikipedia.org/wiki/D._B._Cooper",
"http://en.wikipedia.org/wiki/Philadelphia_Experiment",
"http://en.wikipedia.org/wiki/Mokele-mbembe",
"http://en.wikipedia.org/wiki/New_Jersey_Devil",
"http://en.wikipedia.org/wiki/Allagash_Abductions",
"http://en.wikipedia.org/wiki/Midgetville#Vienna.2C_Virginia",
"http://en.wikipedia.org/wiki/Gef_the_talking_mongoose",
"http://en.wikipedia.org/wiki/Villisca%2C_Iowa",
"http://en.wikipedia.org/wiki/Tunguska_event",
"http://en.wikipedia.org/wiki/Decompression_sickness",
"http://en.wikipedia.org/wiki/Diving_medicine",
"http://en.wikipedia.org/wiki/Decompression_illness",
"http://en.wikipedia.org/wiki/Air_embolism",
"http://en.wikipedia.org/wiki/John_Fare",
"http://en.wikipedia.org/wiki/Kuchisake-Onna",
"http://en.wikipedia.org/wiki/The_Licked_Hand",
"http://en.wikipedia.org/wiki/Raymond_Robinson_%28Green_Man%29",
"http://en.wikipedia.org/wiki/Albert_Fish" ] 
    #demo version for testing
    listOfArticles = ["http://en.wikipedia.org/wiki/Albert_Fish","http://en.wikipedia.org/wiki/The_Licked_Hand"]
    articlesDict = parseListOfArticles (listOfArticles)
    print (articles)
    #So far the method returns dictionary (map) of links and their content as received from Wiki.
    #Serious data science ahead.
    
    
def parseListOfArticles (listOfArticles):
    forRet = []
    dictionary = dict()
    for link in listOfArticles:
        try:
            #prints link for testing purposes
            print (link)
            parsedArticle = getArticleFromWiki (link)
            dictionary [link] = parsedArticle
        except Exception as e:
            print ( "<p>Error: %s</p>" % str(e) )
        
    return dictionary;
        
def getArticleFromWiki( url ):
    import urllib.request 
    response = urllib.request.urlopen (url)
    page = response.read()
    return page;
    

main ()
