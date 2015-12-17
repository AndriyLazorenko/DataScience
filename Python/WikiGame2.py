import wikipedia

def getListOfRandomArticlesNames ( numberOfArticles ):
    listPageNames = []
    for x in range (0,numberOfArticles):
        listPageNames.append(wikipedia.random(pages = 1))
        
    return listPageNames;

def printContent ( inList ):
    for i in inList:
        j = i.content
        print (j)
        print ("___________________________________")
        
def getArticleList ( inList ):
    forRet = []
    for i in inList:
        forRet.append(wikipedia.page(i))
        
    return forRet

def getTextArray (inList):
    forRet = []
    for i in inList:
        forRet.append(i.content)
        
    return forRet

listNames = getListOfRandomArticlesNames (10)
listArticles = getArticleList (listNames)
printContent (listArticles)
