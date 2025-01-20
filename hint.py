all_hints = {
    "apple": "I keep doctors away, but Snow White might disagree!",
    "banana": "I'm long and yellow—monkeys love me, and you might slip on me too!",
    "cherry": "I'm small, red, and on top of your sundae—just don't eat my pit!",
    "peach": "I'm soft, sweet, and blushing like a princess at the royal ball—Cinderella would totally pick me!",
    "watermelon": "I'm big, juicy, and full of water—perfect for a summer day!",
    "grapes": "I hang out in bunches, sometimes I turn into wine, cheers!",
    "mango": "I'm the king of fruits—juicy, messy, and loved in the summer!",
    "orange": "Peel me, juice me, but don't call me the color of my own name!",
    "pineapple": "I'm spiky on the outside, but once you peel me, I'm sweet and tropical inside!",
    "strawberry": "I wear my seeds on the outside, fashion-forward and delicious!",
    "mumbai": "The financial capital of India, home to Bollywood.",
    "delhi": "The capital city of India, known for India Gate and Red Fort.",
    "bangalore": "India’s Silicon Valley, a major IT hub.",
    "hyderabad": "City of Pearls, famous for biryani and Charminar.",
    "chennai": "Coastal city known for Marina Beach and filter coffee.",
    "kolkata": "Cultural capital, home to Howrah Bridge and Rosogolla.",
    "jaipur": "The Pink City, famous for Hawa Mahal and Amer Fort.",
    "ahmedabad": "Largest city of Gujarat, famous for Sabarmati Ashram.",
    "pune": "Oxford of the East, known for its educational institutions.",
    "lucknow": "City of Nawabs, known for its kebabs and chikankari embroidery.",
    "krishna": "The eighth avatar of Vishnu, known for the Bhagavad Gita.",
    "ravana": "The ten-headed king of Lanka, antagonist in the Ramayana.",
    "ganesha": "Elephant-headed god, remover of obstacles.",
    "karna": "Warrior of Mahabharata, known for his unwavering generosity.",
    "hanuman": "Devotee of Lord Rama, known for his immense strength.",
    "lakshmi": "Goddess of wealth and prosperity.",
    "shiva": "The destroyer in the Hindu trinity, carries a trident.",
    "draupadi": "Wife of the Pandavas, known for her vow of revenge.",
    "vishnu": "Preserver of the universe, has ten avatars.",
    "brahma": "The creator god, depicted with four heads."
}

fruits = [
    "apple", "banana", "cherry", "peach", "watermelon"
    "grapes", "mango", "orange", "pineapple", "strawberry"
]
cities = [
    "mumbai", "delhi", "bangalore", "hyderabad", "chennai", 
    "kolkata", "jaipur", "ahmedabad", "pune", "lucknow"
]
mythology = [
    "krishna", "Ravana", "ganesha", "karna", "hanuman", 
    "lakshmi", "shiva", "draupadi", "vishnu", "brahma"
]

def hint(guess,choose):
    # choose = str(input("Choose from one of the categories: \n1. Fruits \n2. Cities \n3. Mythology \n(Enter the name of your choice)"))
    for i in range(len(all_hints)):
        if guess == list(all_hints.keys())[i]:
            return (list(all_hints.values())[i])

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

