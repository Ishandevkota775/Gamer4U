import random

RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
RED = "\033[31m"

questions = [
{"q": "What is the capital of France?",
"o": ["Rome", "Madrid", "Paris", "Berlin"],
"a": "Paris"},

  {"q":"Who painted the Mona Lisa?",
  "o":["Van Gogh","Picasso","Da Vinci","Rembrandt"],
  "a":"Da Vinci"}
      ,
  {"q":"Which planet is the largest in our solar system?",
  "o":["Earth","Mars","Jupiter","Saturn"],
  "a":"Jupiter"},
      
  {"q":"What is the chemical symbol for gold?",
  "o":["Ag","Au","Gd","Go"],
  "a":"Au"},
      
  {"q":"Who wrote the novel named 1984?",
  "o":["Orwell","Huxley","Kafka","Bradbury"],
  "a":"Orwell"},
      
  {"q":"What is the speed of light approximately?",
  "o":["300 km/s","300,000 km/s","150,000 km/s","30,000 km/s"],
  "a":"300,000 km/s"},
      
  {"q":"What is the square root of 64?",
  "o":["6","7","8","9"],
  "a":"8"},
      
  {"q":"Which river is the longest in the world?",
  "o":["Amazon","Nile","Yangtze","Mississippi"],
  "a":"Nile"},
      
  {"q":"Who invented the telephone?",
  "o":["Edison","Bell","Tesla","Newton"],
  "a":"Bell"},
      
  {"q":"What is H2O commonly called?",
  "o":["Salt","Hydrogen","Water","Oxygen"],
  "a":"Water"},
      
  {"q":"Who was the first President of the United States?",
  "o":["Lincoln","Washington","Jefferson","Adams"],
  "a":"Washington"},
      
  {"q":"What is the smallest prime number?",
  "o":["0","1","2","3"],
  "a":"2"},
      
  {"q":"Which gas do plants use during photosynthesis?",
  "o":["Oxygen","Nitrogen","Carbon dioxide","Hydrogen"],
  "a":"Carbon dioxide"},
      
  {"q":"What is the hardest natural substance?",
  "o":["Gold","Iron","Diamond","Quartz"],
  "a":"Diamond"},
      
  {"q":"Which planet is known as the Red Planet?",
  "o":["Venus","Mars","Jupiter","Mercury"],
  "a":"Mars"},
      
  {"q":"Who wrote Pride and Prejudice?",
  "o":["Bronte","Austen","Eliot","Shelley"],
  "a":"Austen"},
      
  {"q":"How many continents are there on Earth?",
  "o":["5","6","7","8"],
  "a":"7"},
      
  {"q":"At what temperature does water boil in Celsius?",
  "o":["90","95","100","110"],
  "a":"100"},
      
  {"q":"Which instrument has keys, strings, and pedals?",
  "o":["Guitar","Violin","Piano","Flute"],
  "a":"Piano"},
      
  {"q":"What is the largest mammal on Earth?",
  "o":["Elephant","Blue whale","Giraffe","Shark"],
  "a":"Blue whale"},
      
  {"q":"What is the fastest land animal?",
  "o":["Lion","Horse","Cheetah","Tiger"],
  "a":"Cheetah"},
      
  {"q":"Which organ pumps blood through the body?",
  "o":["Lungs","Brain","Heart","Liver"],
  "a":"Heart"},
      
  {"q":"What is the SI unit of force?",
  "o":["Watt","Joule","Newton","Pascal"],
  "a":"Newton"},
      
  {"q":"Who painted The Starry Night?",
  "o":["Van Gogh","Monet","Da Vinci","Picasso"],
  "a":"Van Gogh"},
      
  {"q":"What is the capital of Nepal?",
  "o":["Pokhara","Lalitpur","Kathmandu","Bhaktapur"],
  "a":"Kathmandu"},
      
  {"q":"What is the binary representation of the number 5?",
  "o":["101","110","111","100"],
  "a":"101"},
  
  {"q":"Who co-founded Microsoft?",
  "o":["Jobs","Gates","Zuckerberg","Bezos"],
  "a":"Gates"},
      
  {"q":"What shape has exactly three sides?",
  "o":["Square","Triangle","Circle","Rectangle"],
  "a":"Triangle"},
      
  {"q":"What is the study of fossils called?",
  "o":["Biology","Geology","Paleontology","Zoology"],
  "a":"Paleontology"},
      
  {"q":"What is the tallest mountain above sea level?",
  "o":["K2","Kangchenjunga","Everest","Makalu"],
  "a":"Everest"},
      
  {"q":"Which metal is liquid at room temperature?",
  "o":["Iron","Mercury","Aluminum","Silver"],
  "a":"Mercury"},
      
  {"q":"Who wrote the Harry Potter series?",
  "o":["Tolkien","Rowling","Lewis","Martin"],
  "a":"Rowling"},
      
  {"q":"In which year did World War II end?",
  "o":["1943","1944","1945","1946"],
  "a":"1945"},
      
  {"q":"Which device measures temperature?",
  "o":["Barometer","Thermometer","Hygrometer","Altimeter"],
  "a":"Thermometer"},
      
  {"q":"Who is known as the father of geometry?",
  "o":["Pythagoras","Euclid","Archimedes","Plato"],
  "a":"Euclid"},
      
  {"q":"Which vitamin is produced by sunlight in humans?",
  "o":["Vitamin A","Vitamin B","Vitamin C","Vitamin D"],
  "a":"Vitamin D"},
      
  {"q":"Which country contains the pyramids of Giza?",
  "o":["Mexico","Peru","Egypt","India"],
  "a":"Egypt"},
      
  {"q":"What is the most abundant gas in Earth’s atmosphere?",
  "o":["Oxygen","Carbon dioxide","Nitrogen","Hydrogen"],
  "a":"Nitrogen"},
      
  {"q":"Which instrument measures earthquakes?",
  "o":["Thermometer","Seismograph","Barometer","Anemometer"],
  "a":"Seismograph"},
      
  {"q":"What is the chemical formula for carbon dioxide?",
  "o":["CO","CO2","C2O","O2C"],
  "a":"CO2"},
      
  {"q":"Who was the first human to walk on the Moon?",
  "o":["Buzz Aldrin","Neil Armstrong","Yuri Gagarin","Michael Collins"],
  "a":"Neil Armstrong"},
      
  {"q":"Which language has the highest number of native speakers?",
  "o":["English","Spanish","Hindi","Mandarin"],
  "a":"Mandarin"},
  
  {"q":"What do you call a polygon with eight sides?",
  "o":["Hexagon","Heptagon","Octagon","Nonagon"],
  "a":"Octagon"},
  
  {"q":"What form of energy is generated by flowing water?",
  "o":["Solar","Wind","Hydroelectric","Nuclear"],
  "a":"Hydroelectric"},
  
  {"q":"Who wrote The Hobbit?",
  "o":["Lewis","Rowling","Tolkien","Martin"],
  "a":"Tolkien"},
  
  {"q":"Which planet is famous for its ring system?",
  "o":["Mars","Venus","Saturn","Neptune"],
  "a":"Saturn"},
  
  {"q":"What is the unit of electrical resistance?",
  "o":["Volt","Ampere","Ohm","Watt"],
  "a":"Ohm"},
  
  {"q":"What is the capital city of Australia?",
  "o":["Sydney","Melbourne","Canberra","Perth"],
  "a":"Canberra"},
  
  {"q":"What process allows plants to make food?",
  "o":["Respiration","Digestion","Photosynthesis","Fermentation"],
  "a":"Photosynthesis"},
      
  {"q":"What is the basic unit of life?",
  "o":["Atom","Cell","Tissue","Molecule"],
  "a":"Cell"},
      
  {"q":"Who was the Greek god of war?",
  "o":["Zeus","Apollo","Ares","Hermes"],
  "a":"Ares"},
      
  {"q":"What is the distance light travels in one year called?",
  "o":["Parsec","Astronomical Unit","Light year","Kilometer"],
  "a":"Light year"
      },

{"q": "Which country has the largest population?",  
 "o": ["USA", "India", "China", "Russia"],  
 "a": "India"},  

{"q": "Which ocean is the largest?",  
 "o": ["Atlantic", "Indian", "Arctic", "Pacific"],  
 "a": "Pacific"},  

{"q": "Who wrote Hamlet?",  
 "o": ["Dickens", "Shakespeare", "Tolkien", "Austen"],  
 "a": "Shakespeare"},  

{"q": "What is the currency of Japan?",  
 "o": ["Yen", "Won", "Dollar", "Peso"],  
 "a": "Yen"},

]

random.shuffle(questions)
score = 0
letters = ["A", "B", "C", "D"]

print(BOLD + CYAN + "\nINTERNATIONAL QUIZ\n" + RESET)

for i, q in enumerate(questions, start=1):
    print(BOLD + f"\nQuestion {i}" + RESET)
    print(YELLOW + q["q"] + RESET)

    opts = q["o"].copy()  
    random.shuffle(opts)  

    answer_map = dict(zip(letters, opts))  
    correct_letter = next(k for k, v in answer_map.items() if v == q["a"])  

    for k, v in answer_map.items():  
        print(CYAN + f"{k}. {v}" + RESET)  

    ans = input(BOLD + "Your answer: " + RESET).strip().upper()  

    if ans == correct_letter:  
        print(GREEN + "Correct" + RESET)  
        score += 1  
    else:  
        print(RED + f"Wrong. Correct answer is {correct_letter}" + RESET)

print(BOLD + f"\nFinal score: {score} / {len(questions)}" + RESET)
