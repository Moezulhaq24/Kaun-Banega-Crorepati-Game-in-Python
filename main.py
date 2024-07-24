KBC = " WELCOME TO THE SHOW \"KAUN BANEGA CROREPATI\""
name = "MY NAME IS AMITAB BACHAN"
game = "AND THE GAME SHOW BEGINS\n"
print(KBC.center(70))
print(name.center(70))
# print(game.center(70))
# print("Questions&Answer\n")

questions =[  
["1:In the game  of ludo the discs or tokens are of how many colours?","a.One", "b.Two", "c.Three", "d.Four"],
["2: Which of these are names of national parks located in Madhya Pradesh?","a.Krishna and Kanhaiya", "b.Kanha and Madhav","c. Ghanshyam and Murari", "d.Girdhar and Gopal"],
["3:Where was the BRICS summit held in 2014?","a.Brazil", "b.India", "c.Russia", "d.China"],
["4:Who wrote the introduction to the English translation of Rabindranath Tagore’s Gitanjali?","a. P.B. Shelley", "b.Alfred Tennyson","c. W.B. Yeats", "d. T.S. Elliot"],
["5.Which of these sports requires you to shout out a word loudly during play?","a.Ludo","b.Kho-kho","c.Playing cards","d.Chess"],
["6.Which of these spices is the smallest in size?","a.Ajwain","b.Jeera","c.Saunf","d.Methi Seeds"],
["7.Which is the second most spoken language of Nepal?","a.Bajjika","b.Nepali","c.Maithili","d.Bhojpuri"],
["8.Which battle in 1757 marked the beginning of British occupation in India?","a.Plassey","b.Assaye","c.Buxar","d.Cuddalore"]
]

answers = ["D", "B", "A", "C","B", "A", "C", "A"]
a=0
total=5000
sum=5000
m=int(0)
input("PRESS ENTER TO START THE GAME\n")
print(game.center(70))
print("Questions&Answer\n")
for i in questions:
    for j in range(0,5):
        print(i[j])
    ans=input("\nChoose the Correct Option\n: ")
    ans=ans.upper()
    
    if(answers[m]==ans):
        pass
        a=a+5000
        print("Answer is correct\nYou have won ", a,"Rupees of this question\n.")
        print("!!!***CONGRATULATIONS YOU HAVE WON TOTAL OF",total,"RUPEES!!!***\n")
        total+=5000
        total=total+a
      
        if(total>=180000):
          str="$$$$ WON THE GAME $$$$"
          # print(str.upper())
          print(str.center(50))
    
    else:
        total=total-a
        total=total-5000
        print("Wrong Answer\nYou Only get",total,"Rupees\n!!!Game Ended!!! " )
        
        # print("YOU ONLY GET",total,"RUPEES!!!***\n")
        break
    m+=1

# print("CONGRATULATIONS!!!!\nYOU HAVE WON TOTAL OF 180,000 RUPEES") 
      
      
  
