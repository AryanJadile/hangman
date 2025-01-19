fruit_hints = {
    "apple": "I keep doctors away, but Snow White might disagree!",
    "banana": "I'm long and yellow—monkeys love me, and you might slip on me too!",
    "cherry": "I'm small, red, and on top of your sundae—just don't eat my pit!",
    "peach": "I'm soft, sweet, and blushing like a princess at the royal ball—Cinderella would totally pick me!",
    "watermelon": "I'm big, juicy, and full of water—perfect for a summer day!",
    "grapes": "I hang out in bunches, sometimes I turn into wine, cheers!",
    "mango": "I'm the king of fruits—juicy, messy, and loved in the summer!",
    "orange": "Peel me, juice me, but don't call me the color of my own name!",
    "pineapple": "I'm spiky on the outside, but once you peel me, I'm sweet and tropical inside!",
    "strawberry": "I wear my seeds on the outside, fashion-forward and delicious!"
}

def hint(guess):
    for i in range(len(fruit_hints)):
        if guess == list(fruit_hints.keys())[i]:
            return (list(fruit_hints.values())[i])

def disp_word(word,inp):
    return ' '.join([letter if letter in inp else '_' for letter in word])
    

# def hint(guess):
#     if guess in fruits:
#         if guess == "Apple":
#             print("I keep the doctors away!")
#         elif guess == "Banana":
#             print("Slip on me if you're not careful, but I’m delicious inside!")
#         elif guess == "Cherry":
#             print("I’m small, red, and on top of your sundae!!")
#         elif guess == "Peach":
#             print("I’m soft, sweet, and blushing like a princess at the royal ball—Cinderella would totally pick me!")
#         elif guess == "Watermelon":
#             print("I’m big, juicy, and full of water—perfect for a summer day!")
#         elif guess == "Grapes":
#             print("I hang out in bunches, sometimes I turn into wine, cheers!")
#         elif guess == "Mango":
#             print("King of the fruits they call me, but I come only in summers!!")
#         elif guess=="Orange":
#             print("Peel me, juice me, but don’t call me the color of my own name!")
#         elif guess == "Pineapple":
#             print("I’m spiky on the outside, but once you peel me, I’m sweet and tropical inside!")
#         elif guess == "Strawberry":
#             print("I wear my seeds on the outside, fashion-forward and delicious!")
#     else:
#         return None

