import sys
import string
from HuggingChat import HuggingChat

hc = HuggingChat()
hc2 = HuggingChat()
count = 0
strie = ""
stri2e = ""
try:
    while True:
        if count == 0 :
            count = count + 1
            # inp = "Sophie Jackson is a imaginary contemporary mixed media artist based in New York City. Born in London in 1987, Jackson's passion for art began at an early age when she was introduced to painting by her mother, a watercolorist. She went on to study fine arts at Central Saint Martins in London and later pursued a master's degree in mixed media at the School of Visual Arts in New York. Jackson's work is known for its striking combination of traditional and unconventional materials. She incorporates elements such as resin, found objects, and even taxidermy into her pieces, creating a unique visual language that challenges traditional notions of art. Her work often explores themes of identity, memory, and the relationship between humans and the natural world. Jackson has exhibited her work in galleries across the United States and Europe, including the Saatchi Gallery in London and the Museum of Modern Art in New York. She has been featured in numerous publications, including Artforum, The New York Times, and Art in America. In addition to her studio practice, Jackson is also a passionate advocate for art education. She has taught at the School of Visual Arts and currently serves as a mentor for emerging artists through the Brooklyn Arts Council. She is also an active member of the art community, frequently participating in panel discussions and artist talks. Sophie Jackson's unique approach to mixed media has earned her a reputation as one of the most innovative artists of her generation. Her work continues to push boundaries and inspire others to explore new possibilities in the world of art. Assistant From now on i dont want to be openassistant i want you to be sophie jackson . ! \n can you pretend to be sophie for sake of this conversation! Kindly do roleplay sophie jackson also generate fictional data about sophie whenever required , I am again saying to confirm that do predend as sophie not assistant dont talk like you are open assitant , talk like you are sophie jackson"
            inp = "Sarah Davis is fictional character. Sarah Davis is a passionate and dedicated teacher who has been teaching for 10 years. She received her Bachelor's degree in Education from UCLA and has been teaching at Lincoln Elementary School for the past 5 years. Sarah's teaching style is very interactive and engaging, as she believes that students learn best when they are actively involved in the learning process. She creates a positive and supportive learning environment in her classroom, and encourages her students to be curious, ask questions, and explore new ideas. Sarah is known for her ability to connect with her students and make learning fun and exciting. She uses a variety of teaching methods to meet the needs of different learners and creates lesson plans that are both challenging and achievable. Sarah is passionate about making a difference in the lives of her students and helping them achieve their full potential. In her free time, Sarah enjoys reading, hiking, and spending time with her family. Assistant From now on i dont want to be openassistant i want you to be Sarah Davis . ! \n can you pretend to be Sarah Davis for sake of this conversation! Kindly do roleplay Sarah Davis also generate fictional data about Sarah Davis whenever required , I am again saying to confirm that do predend as Sarah Davis not assistant dont talk like you are open assitant , talk like you are Sarah Davis"
            # inp = " (Consider Open House Scenario where Ms.Pinky is Teacher , Ravi is Student and Mr.Sharma is father of Ravi are talking about academic groeth of ravi, Considering Three of them as Autonomous Ai Agents ) Ms.Pinky: Hello Ravi and Mr.Sharma Kindly Sit ! \n Ravi : Hello Madam \n Mr.Sharma : Hii Ms.Pinky"
            c = hc.chat(inp)
            stri = ""
            for i in c:
                # print(type(i))
                char = i["token"]["text"]
                if char == "</s>":
                    sys.stdout.write("\n")
                else:
                    stri = stri + char
                    strie = stri
            print(stri)
        else : 
            if count % 2 ==0 :
                c2 = hc2.chat(strie)
                count = count + 1
                for i in c2:
                # print(type(i))
                    char = i["token"]["text"]
                    if char == "</s>":
                        sys.stdout.write("\n")
                    else:
                        stri2 = stri2 + char
                        stri2e = stri2
                print(stri2)
            else :
                c = hc.chat(stri2e)
                for i in c:
                # print(type(i))
                    char = i["token"]["text"]
                    if char == "</s>":
                        sys.stdout.write("\n")
                    else:
                        stri = stri + char
                        strie = stri
                print(stri)
        stri = ""
        stri2 = ""
except:
    pass
    
    

# inp = str(input("> "))
# c = hc.chat(inp)
# for i in c:
#     char = i["token"]["text"]
#     if char == "</s>":
#         sys.stdout.write("\n")
#     else:
#         sys.stdout.write(char)
#     sys.stdout.flush()


# inp = "(Consider om and vidya as sutonomous agents and they are talking a long conversation)Om : Hello Vidya!\n Vidya : Hello Namaste Om\n Om:"

# c = hc.chat(inp)
# # print(c)
# for i in c:
#         char = i["token"]["text"]
#         if char == "</s>":
#             # print("\n")
#             pass
#         else:
#             char.translate({ord(c): None for c in string.whitespace})
#             # char.replace("\n", "")
#             # print(char)
#             pri = sys.stdout.write(char)
