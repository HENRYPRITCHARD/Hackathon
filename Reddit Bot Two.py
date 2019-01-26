#Setup
import praw, re, csv, random
space = "\n "
separate = "--------"
code = input("code: ")
recounter = "0001"
counter = "0001"





#Temp Variable Declaration
location = 0
thepoints = 1
whopoints = 1
howpoints = 1
whypoints = 1
bigpoints = 1
sadpoints = 1
badpoints = 1
redpoints = 1
manpoints = 1
boypoints = 1
dogpoints = 1
catpoints = 1
ispoints = 1
goespoints = 1
addspoints = 1
payspoints = 1
bigtwopoints = 1
sadtwopoints = 1
badtwopoints = 1
redtwopoints = 1
temptopiconea   = 1
temptopictwoa   = 1
temptopicthreea = 1
temptopicfoura  = 1
temptopiconeb   = 1
temptopictwob   = 1
temptopicthreeb = 1
temptopicfourb  = 1
temptopiconec   = 1
temptopictwoc   = 1
temptopicthreec = 1
temptopicfourc  = 1
temptopiconed   = 1
temptopictwod   = 1
temptopicthreed = 1
temptopicfourd  = 1
temptopiconee   = 1
temptopictwoe   = 1
temptopicthreee = 1
temptopicfoure  = 1








#Validate Reddit Access
reddit = praw.Reddit(client_id='c0S04PHZGgx7Wg',
                     client_secret='PEUlA0ILn5OS1YbuAkd1tVNFRI8',
                     password='11365abc',
                     user_agent='pix3lbot_scrape by /u/pix3lbot2',
                     username='pix3lbot2')
subreddit = reddit.subreddit('pix3lspace')







#Recycleable Parser
def parse(comment,location):
    counter = 0
    for i in range(0,4):
        if counter == 0:
            first = comment[counter + location]
        if counter == 1:
            second = comment[counter + location]
        if counter == 2:
            third = comment[counter + location]
        if counter == 3:
            fourth = comment[counter + location]
        counter = counter + 1
    word = first + second + third + fourth
    return word   







#Calculate Score
word = " "
def calculate(comment):
    counter = 5
    points = 0
    for i in range(5):
        word = parse(comment,counter)
        if counter == 5:
            if word == "the-":
                points = points + 750
            if word == "who-":
                points = points + 187.5
            if word == "how-":
                points = points + 46.825
            if word == "why-":
                points = points + 15.625
        elif counter == 10:
            if word == "big-":
                points = points + 750
            if word == "sad-":
                points = points + 187.5
            if word == "bad-":
                points = points + 46.825
            if word == "red-":
                points = points + 15.625                    
        elif counter == 15:
            if word == "man-":
                points = points + 750
            if word == "boy-":
                points = points + 187.5
            if word == "dog-":
                points = points + 46.825
            if word == "cat-":
                points = points + 15.625           
        elif counter == 20:
            if word == "is--":
                points = points + 750
            if word == "goes":
                points = points + 187.5
            if word == "adds":
                points = points + 46.825
            if word == "pays":
                points = points + 15.625                           
        elif counter == 25:
            if word == "big-":
                points = points + 750
            if word == "sad-":
                points = points + 187.5
            if word == "bad-":
                points = points + 46.825
            if word == "red-":
                points = points + 15.625      
        counter = counter + 5
        score = points / 3750
    return score






#Generate Responses
def generate(temptopiconea,temptopictwoa,temptopicthreea,temptopicfour,temptopiconeb,temptopictwob,temptopicthreeb,temptopicfourb,temptopiconec,temptopictwoc,temptopicthreec,temptopicfourc,temptopiconed,temptopictwod,temptopicthreed,temptopicfourd,temptopiconee,temptopictwoe,temptopicthreee,temptopicfoure):
    #Question
    cques = [('the-', temptopiconea), ('who-', temptopictwoa), ('how-', temptopicthreea), ('why-', temptopicfoura)]
    pques = [val for val, cnt in cques for i in range (cnt)]
    chque = random.choice(pques)
    #Adjective One
    cadje = [('big-', temptopiconeb), ('sad-', temptopictwob), ('bad-', temptopicthreeb), ('red-', temptopicfourb)]
    padje = [val for val, cnt in cadje for i in range (cnt)]
    chadj = random.choice(padje) 
    #Noun
    cnoun = [('man-', temptopiconec), ('boy-', temptopictwoc), ('dog-', temptopicthreec), ('cat-', temptopicfourc)]
    pnoun = [val for val, cnt in cnoun for i in range (cnt)]
    chnou = random.choice(pnoun)
    #Verb
    cverb = [('is--',temptopiconed), ('goes', temptopictwod), ('adds', temptopicthreed), ('pays', temptopicfourd)]
    pverb = [val for val, cnt in cverb for i in range (cnt)]
    chver = random.choice(pverb) 
    #Adjective Two
    cadtw = [('big-', temptopiconee), ('sad-', temptopictwoe), ('bad-', temptopicthreee), ('red-', temptopicfoure)]
    padtw = [val for val, cnt in cadtw for i in range (cnt)]
    chadt = random.choice(padtw)
    final = chque + "-" + chadj + "-" + chnou + "-" + chver + "-" + chadt
    return final







#Weight Adjustment
def adjust(current,accurance,totalwords):
    usage = accurance / totalwords
    out = usage / current
    return out






#Choose Response
def choosescore(scoreone,scoretwo,scorethree,focus):
    one      = calculate(scoreone)
    two      = calculate(scoretwo)
    three    = calculate(scorethree)
    newone   = op(one,focus)
    newtwo   = op(two,focus)
    newthree = op(three,focus)
    foo      = [newone, newtwo, newthree]
    bar      = map(float, foo)
    newbar   = min(bar)
    if newone == newbar:
        return scoreone
    elif newtwo == newbar:
        return scoretwo
    elif newthree == newbar:
        return scorethree





    
#Chooser Operation + Flip
def op(inp,focus):
    out = (focus - inp)
    if out < 0:
        out = out * -1
    else:
        out = out
    return out
    







#Initial Comment
for submission in subreddit.hot(limit=1000):
        if re.search(code, submission.title, re.IGNORECASE):
            reinit   = "0001" + "-" + generate(thepoints,whopoints,howpoints,whypoints,bigpoints,sadpoints,badpoints,redpoints,manpoints,boypoints,dogpoints,catpoints,ispoints,goespoints,addspoints,payspoints,bigtwopoints,sadtwopoints,badtwopoints,redtwopoints)
            submission.reply(reinit)





#Following Comments         
while True:
    for submission in subreddit.hot(limit=1000):
        if re.search(code, submission.title, re.IGNORECASE):
            for top_level_comment in submission.comments:
                comment = top_level_comment.body
                ident = parse(comment,location)
                print(ident)
                print(comment)
                if (ident == recounter) and (int(ident) % 2 == 1):
                    score = calculate(comment)

                    #Internal Synchronous Incrementer
                    comp = int(counter)
                    if comp < 9:
                        counter = "000" + str(int(recounter) + 1)
                    if comp >= 9:
                        counter = "00" + str(int(recounter) + 1)

                    #Reponse Director Incrementer
                    recomp = int(recounter)
                    if recomp < 9:
                        recounter = "000" + str(int(recounter) + 2)
                    if recomp >= 9:
                        recounter = "00" + str(int(recounter) + 2)


                    









                    #Filtration
                    reone   = counter + "-" + generate(thepoints,whopoints,howpoints,whypoints,bigpoints,sadpoints,badpoints,redpoints,manpoints,boypoints,dogpoints,catpoints,ispoints,goespoints,addspoints,payspoints,bigtwopoints,sadtwopoints,badtwopoints,redtwopoints)
                    retwo   = counter + "-" + generate(thepoints,whopoints,howpoints,whypoints,bigpoints,sadpoints,badpoints,redpoints,manpoints,boypoints,dogpoints,catpoints,ispoints,goespoints,addspoints,payspoints,bigtwopoints,sadtwopoints,badtwopoints,redtwopoints)
                    rethree = counter + "-" + generate(thepoints,whopoints,howpoints,whypoints,bigpoints,sadpoints,badpoints,redpoints,manpoints,boypoints,dogpoints,catpoints,ispoints,goespoints,addspoints,payspoints,bigtwopoints,sadtwopoints,badtwopoints,redtwopoints)
                    refinal = choosescore(reone,retwo,rethree,score)
                    location = 5








                    #Question
                    chque = parse(refinal,location)
                    if chque == "the-":
                        thepoints = thepoints + 1
                    if chque == "who-":
                        whopoints = whopoints + 1
                    if chque == "how-":
                        howpoints = howpoints + 1
                    if chque == "why-":
                        whypoints = whypoints + 1
                    #Adjective One
                    location = 10   
                    chadj = parse(refinal,location)   
                    if chadj == "big-":
                        bigpoints = bigpoints + 1
                    if chadj == "sad-":
                        sadpoints = sadpoints + 1
                    if chadj == "bad-":
                        badpoints = badpoints + 1
                    if chadj == "red-":
                        redpoints = redpoints + 1
                    #Noun
                    location = 15
                    chnou = parse(refinal,location)
                    if chnou == "man-":
                        manpoints = manpoints + 1
                    if chnou == "boy-":
                        boypoints = boypoints + 1
                    if chnou == "dog-":
                        dogpoints = dogpoints + 1
                    if chnou == "cat-":
                        catpoints = catpoints + 1
                    #Verb
                    location = 20 
                    chver = parse(refinal,location)
                    if chver == "is--":
                        ispoints = ispoints + 1
                    if chver == "goes":
                        goespoints = goespoints + 1
                    if chver == "adds":
                        addspoints = addspoints + 1
                    if chver == "pays":
                        payspoints = payspoints + 1
                    #Adjective Two
                    location = 25  
                    chadt = parse(refinal,location)
                    if chadt == "big-":
                        bigtwopoints = bigtwopoints + 1
                    if chadt == "sad-":
                        sadtwopoints = sadtwopoints + 1
                    if chadt == "bad-":
                        badtwopoints = badtwopoints + 1
                    if chadt == "red-":
                        redtwopoints = redtwopoints + 1








                    #Finalization Formatting
                    location = 0
                    print(space)
                    print(separate)
                    print("original:" + str(comment) + str(score))
                    print("response:" + str(refinal) + str(calculate(refinal)))
                    calc = calculate(refinal)
                    out = op(calc, score)
                    print("loss:" + str(out))
                    print(separate)
                    print(space)
                    print(separate)
                    print("1  " + str(thepoints))
                    print("2  " + str(whopoints))
                    print("3  " + str(howpoints)) 
                    print("4  " + str(whypoints)) 
                    print("5  " + str(bigpoints)) 
                    print("6  " + str(sadpoints)) 
                    print("7  " + str(badpoints)) 
                    print("8  " + str(redpoints)) 
                    print("9  " + str(manpoints))
                    print("10 " + str(boypoints)) 
                    print("11 " + str(dogpoints)) 
                    print("12 " + str(catpoints))
                    print("13 " + str(ispoints))
                    print("14 " + str(goespoints)) 
                    print("15 " + str(addspoints)) 
                    print("16 " + str(payspoints))
                    print("17 " + str(bigtwopoints))
                    print("18 " + str(sadtwopoints))
                    print("19 " + str(badtwopoints)) 
                    print("20 " + str(redtwopoints))
                    print(separate)
                    submission.reply(refinal)
                    
        
            
                            
                            
                            
                
            



        
      


