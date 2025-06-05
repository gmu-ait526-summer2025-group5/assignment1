
adj_noun_patterns = [
    # 1. “I feel <adjective> about my <noun>”
    (
        r"(?i).*?\bI\s+feel\s+([A-Za-z]+(?:-[A-Za-z]+)?)\s+about\s+my\s+([A-Za-z]+(?:\s+[A-Za-z]+)*)\b.*",
        "Why do you feel {0} about your {1}, {name}?"
    ),

    # 2. “My <noun> is <adjective>”
    (
        r"(?i).*?\bMy\s+([A-Za-z]+(?:\s+[A-Za-z]+)*)\s+is\s+([A-Za-z]+(?:-[A-Za-z]+)?)\b.*",
        "When did your {0} become so {1}, {name}?"
    ),

    # 3. “Have you ever had a <adjective> <noun>?”
    (
        r"(?i).*?\bHave\s+you\s+ever\s+had\s+a\s+([A-Za-z]+)\s+([A-Za-z]+)\?\b.*",
        "What would it mean if you really had a {0} {1}, {name}?"
    ),

    # 4. “I’m trying to <verb> my <adjective> <noun>”
    (
        r"(?i).*?\bI['’]?m\s+trying\s+to\s+([A-Za-z]+)\s+my\s+([A-Za-z]+)\s+([A-Za-z]+)\b.*",
        "What makes it hard to {0} your {1} {2}, {name}?"
    ),

    # 5. “My <adjective> <noun> is broken”
    (
        r"(?i).*?\bMy\s+([A-Za-z]+)\s+([A-Za-z]+)\s+is\s+broken\b.*",
        "How long has your {0} {1} been broken, {name}?"
    ),

    # 6. “Can you describe your <adjective> <noun>”
    (
        r"(?i).*?\bCan\s+you\s+describe\s+your\s+([A-Za-z]+)\s+([A-Za-z]+)\b.*",
        "What does your {0} {1} feel like, {name}?"
    ),

    # 7. “I started <noun> and it became <adjective>”
    (
        r"(?i).*?\bI\s+started\s+([A-Za-z]+)\s+and\s+it\s+became\s+([A-Za-z]+)\b.*",
        "What changed that made your {0} so {1}, {name}?"
    ),

    # 8. “My <noun> feels <adjective>”
    (
        r"(?i).*?\bMy\s+([A-Za-z]+)\s+feels\s+([A-Za-z]+)\b.*",
        "Why do you think your {0} feels {1}, {name}?"
    ),

    # 9. “I’m <adjective> with my <noun>”
    (
        r"(?i).*?\bI['’]?m\s+([A-Za-z]+)\s+with\s+my\s+([A-Za-z]+)\b.*",
        "What about your {1} makes you feel {0}, {name}?"
    ),

    # 10. “Sometimes my <noun> turns <adjective>”
    (
        r"(?i).*?\bSometimes\s+my\s+([A-Za-z]+)\s+turns\s+([A-Za-z]+)\b.*",
        "When does your {0} usually turn {1}, {name}?"
    ),

    # 11. “I keep my <adjective> <noun> hidden”
    (
        r"(?i).*?\bI\s+keep\s+my\s+([A-Za-z]+)\s+([A-Za-z]+)\s+hidden\b.*",
        "Why do you keep your {0} {1} hidden, {name}?"
    ),

    # 12. “My <noun> looks <adjective> today”
    (
        r"(?i).*?\bMy\s+([A-Za-z]+)\s+looks\s+([A-Za-z]+)\s+today\b.*",
        "What makes your {0} look {1} today, {name}?"
    ),

    # 13. “I found my <noun> quite <adjective>”
    (
        r"(?i).*?\bI\s+found\s+my\s+([A-Za-z]+)\s+quite\s+([A-Za-z]+)\b.*",
        "In what way was your {0} quite {1}, {name}?"
    ),

    # 14. “My <adjective> <noun> inspires me”
    (
        r"(?i).*?\bMy\s+([A-Za-z]+)\s+([A-Za-z]+)\s+inspires\s+me\b.*",
        "How does your {0} {1} inspire you, {name}?"
    ),

    # 15. “I consider my <noun> kind of <adjective>”
    (
        r"(?i).*?\bI\s+consider\s+my\s+([A-Za-z]+)\s+kind\s+of\s+([A-Za-z]+)\b.*",
        "Why do you consider your {0} kind of {1}, {name}?"
    ),
]


simple_patterns = [
  
(r".*\b(happy|happiness|joy|joyful|cheerful|delighted)\b.*",
     "A good happy vibe! What’s got you feeling good, {name}?"),

    (r".*\b(excited|thrilled|elated|ecstatic|overjoyed)\b.*",
     "Someone’s riding the good wave! What’s the scoop, {name}?"),

    (r".*\b(grateful|thankful|blessed)\b.*",
     "Gratitude! What’s making your heart jump, {name}?"),

    (r".*\b(smile|smiling|beaming|grinning)\b.*",
     "What’s got you glowing, {name}?"),

    (r".*\b(celebrate|celebration|party|partying)\b.*",
     "What are we celebrating, {name}?"),

    (r".*\b(awesome|amazing|great|fantastic|fabulous|wonderful)\b.*",
     "That’s a whole vibe right there! What made your day so awesome, {name}?"),

    (r".*\b(chill|relaxed|laid back|zen|breezy)\b.*",
     "Chill mode. What’s helping you float like this, {name}?"),

    (r".*\b(loved|love|loving)\b.*",
     "Who or what’s getting all this affection, {name}?"),

    (r".*\b(good mood|feeling good|good vibes|great day)\b.*",
     "Catchin’ them good mood rays ☀️ What sparked it, {name}?"),

    (r".*\b(lucky|fortunate|on a roll|everything’s clicking)\b.*",
     "Jackpot energy 🎰 What’s going your way today, {name}?"),

    (r".*\b(won|winning|accomplished|achieved)\b.*",
     "What did you just crush, {name}?"),

    (r".*\b(promotion|new job|offer|accepted|greenlighted)\b.*",
     "Level up! Tell me all about the upgrade, {name}!"),

    (r".*\b(good news|great update|awesome message)\b.*",
     "Hit me with the headline, {name}!"),

    (r".*\b(inspired|creative|fired up|pumped|motivated)\b.*",
     "What are you cooking up, {name}?"),

    (r".*\b(laughing|lol|lmao|giggle|cracking up|funny)\b.*",
     "What cracked you up, {name}?"),

    (r".*\b(vacation|beach|trip|travel|getaway)\b.*",
     "Where are you off to, {name}?"),

    (r".*\b(food|dessert|ice cream|pizza|snack|brunch)\b.*",
     "What did you eat next, {name}?"),

    (r".*\b(music|dancing|groove|beats|jammed out|playlist)\b.*",
     "What was on the aux, {name}?"),

    (r".*\b(friend|friends|hangout|catch up|reunion)\b.*",
     "That sounds like a great hangout. Who’d you link up with, {name}?"),

    (r".*\b(cleaned|organized|productive|got stuff done)\b.*",
     "What’d you cross off the list, {name}?"),
]

happy_patterns = [
     *simple_patterns,
     *adj_noun_patterns
]
