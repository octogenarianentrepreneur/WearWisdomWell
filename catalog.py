"""WearWisdomWell catalog: the single source for every product page.
Edit here, then run build.py. Etsy IDs must match the live listings."""

ETSY = "https://www.etsy.com/listing/{id}"

CC1717_COLORS = ["Black", "Navy", "Blue Spruce", "Pepper", "Espresso", "Wine"]
CC1717_PRICES = "S–XL $26.99 · 2XL $29.99 · 3XL $33.99 · 4XL $37.99"
CC1717_BUILD = ("Comfort Colors 1717: soft, substantial garment-dyed ring-spun cotton, "
                "sizes S to 4XL.")

COLLECTIONS = [
    {
        "slug": "quiet-patriotism",
        "name": "Quiet Patriotism",
        "short": "1776, liberty and America's 250th, worn without argument.",
        "intro": ("Love of country that doesn't need to raise its voice. A date, a flag, "
                  "a line from the founding — enough for anyone paying attention, and "
                  "nothing for anyone looking for a fight."),
    },
    {
        "slug": "understated-wit",
        "name": "Understated Wit",
        "short": "Dry humor for handymen, coworkers and engineers.",
        "intro": ("The joke you only get on the second look. Clever without being loud, "
                  "and never at anyone's expense but our own."),
    },
    {
        "slug": "reflective-faith",
        "name": "Reflective Faith",
        "short": "Quiet convictions, no sermon.",
        "intro": ("Faith worn the way it's lived: steadily, with gratitude, and without "
                  "pointing it at anyone. Fit for church and the hardware store alike."),
    },
    {
        "slug": "thoughtful-expression",
        "name": "Thoughtful Expression",
        "short": "Words for the one who listens first and speaks last.",
        "intro": ("Lines that reward a slow read. For people who would rather be understood "
                  "than seen, and who have earned the right to say a little less than they know."),
    },
]

PRODUCTS = [
    # ---------------- Quiet Patriotism ----------------
    {
        "slug": "united-since-1776-tee",
        "name": "United Since 1776 T-Shirt",
        "short": "United Since 1776",
        "collection": "quiet-patriotism",
        "etsy_id": "4468693510",
        "price_from": "22.99",
        "price_high": "28.99",
        "shirt_text": "United Since 1776 · Out of Many, One",
        "blurb": "A fifty-states flag and the oldest motto we have.",
        "body": [
            "Out of many, one. Fifty states, fifty ways of seeing things, and one country that "
            "somehow holds them all. That's the promise folded into 1776, and it's worth saying "
            "plainly: e pluribus unum, worn without argument.",
            "It's for the American who still believes the disagreements are part of the point — "
            "that a country big enough for fifty different voices is a feature, not a flaw. You "
            "don't need to shout over anyone. You just know what holds the whole thing together.",
        ],
        "build": "Printed to order on 100% ring-spun cotton, sizes S to 5XL.",
        "colors": ["Charcoal", "Maroon", "Navy", "Sand", "Sport Grey", "Military Green"],
        "sizes": "S–5XL",
        "cc1717": False,
        "alts": ["United Since 1776 tee with a fifty-states American flag graphic",
                 "United Since 1776 tee, second view", "United Since 1776 tee, detail"],
        "close": "Fifty voices. One story.",
    },
    {
        "slug": "liberty-legacy-1776-2026-tee",
        "name": "Liberty Legacy 1776–2026 T-Shirt",
        "short": "Liberty Legacy",
        "collection": "quiet-patriotism",
        "etsy_id": "4602701821",
        "price_from": "26.99",
        "price_high": "37.99",
        "shirt_text": "Statue of Liberty engraving · July IV MDCCLXXVI",
        "blurb": "Lady Liberty in vintage engraving, dated the old way.",
        "body": [
            "The torch, rendered like an old banknote engraving, and a date written the way the "
            "founders would have recognized it: July IV, MDCCLXXVI. No slogan. The image has been "
            "saying it for a hundred and forty years.",
            "It's for the veteran, the history reader, the grandfather who still stands for the "
            "anthem at the ballgame — the one who marks the 250th by remembering what it cost, "
            "not by setting off the loudest fireworks on the block.",
        ],
        "build": CC1717_BUILD,
        "colors": CC1717_COLORS,
        "sizes": "S–4XL",
        "cc1717": True,
        "alts": ["Liberty Legacy tee with a vintage engraving of the Statue of Liberty",
                 "Liberty Legacy tee in a lifestyle setting", "Liberty Legacy tee, close-up of the engraving"],
        "close": "Lit in 1776. Still burning.",
    },
    {
        "slug": "americas-250th-anniversary-tee",
        "name": "America's 250th Anniversary T-Shirt",
        "short": "America's 250th",
        "collection": "quiet-patriotism",
        "etsy_id": "4454385743",
        "price_from": "22.99",
        "price_high": "28.99",
        "shirt_text": "America's Sestercentennial · 1776–2026",
        "blurb": "A keepsake for the year the country turned 250.",
        "body": [
            "Two hundred and fifty years happens once. This one marks it with the proper name — "
            "the Sestercentennial — a map of the country and a row of stars, the kind of shirt "
            "that ends up in a drawer of keepsakes rather than a rag bin.",
            "It's for the family that gathered for the Fourth this year and wants something to "
            "remember it by, and for the friend who knows exactly what Sestercentennial means "
            "and is quietly pleased when someone asks.",
        ],
        "build": "Printed to order on soft cotton, sizes S to 5XL.",
        "colors": ["Charcoal", "Maroon", "Navy", "Sport Grey", "Black", "Forest Green"],
        "sizes": "S–5XL",
        "cc1717": False,
        "alts": ["America's 250th Sestercentennial tee with a US map and stars",
                 "America's 250th tee, second view", "America's 250th tee, detail"],
        "close": "Two hundred fifty years. Worth remembering.",
    },
    {
        "slug": "rosie-the-riveter-flag-tee",
        "name": "Be a Rosie T-Shirt",
        "short": "Be a Rosie",
        "collection": "quiet-patriotism",
        "etsy_id": "4464812454",
        "price_from": "22.99",
        "price_high": "28.99",
        "shirt_text": "She didn't wait to be asked. · Be a Rosie.",
        "blurb": "For the woman who shows up before anyone asks.",
        "body": [
            "In 1943 nobody drafted her. The work needed doing, so she showed up, and kept "
            "showing up until it was done. Here she's drawn like an old two-color poster in "
            "navy and cream, with one quiet line in muted gold above her.",
            "It's for the woman who still works that way. She runs the church kitchen, drives "
            "the neighbor to the doctor, takes the night shift, and signs up before the sign-up "
            "sheet comes around. A considered gift for a mother, a grandmother, a wife or a daughter.",
        ],
        "build": "Printed to order on heavyweight 100% cotton, sizes S to 5XL (the largest sizes come in fewer colors).",
        "colors": ["Black", "Navy", "Charcoal", "Forest Green", "Maroon"],
        "sizes": "S–5XL",
        "cc1717": False,
        "alts": ["Be a Rosie tee on a workbench: Rosie the Riveter poster art under the line She didn't wait to be asked",
                 "Woman on an airfield wearing the black Be a Rosie tee",
                 "Close-up of the Be a Rosie print in navy, cream and gold"],
        "close": "No one had to ask.",
    },
    # ---------------- Understated Wit ----------------
    {
        "slug": "duct-tape-cant-fix-stupid-tee",
        "name": "Duct Tape Can't Fix Stupid T-Shirt",
        "short": "Duct Tape Can't Fix Stupid",
        "collection": "understated-wit",
        "etsy_id": "4468427445",
        "price_from": "25.99",
        "price_high": "29.99",
        "shirt_text": "Duct Tape Can't Fix Stupid",
        "blurb": "Lettered in duct tape, for the man who has tried.",
        "body": [
            "Duct tape fixes the dryer vent, the cooler lid, the truck's side mirror and, in a "
            "pinch, a pair of boots. It has exactly one known limit, and it's spelled out here "
            "in strips of tape.",
            "It's for the handyman, the dad with a garage full of half-finished repairs, and the "
            "coworker who has watched a well-meaning plan go sideways more than once. He doesn't "
            "say it out loud. The shirt does, with a straight face.",
        ],
        "build": "Printed to order on soft cotton, sizes S to 2XL.",
        "colors": ["Dark Grey Heather", "Heather Navy", "Maroon", "Navy", "Black Heather", "Brown"],
        "sizes": "S–2XL",
        "cc1717": False,
        "alts": ["Duct Tape Can't Fix Stupid tee with duct tape lettering",
                 "Duct Tape Can't Fix Stupid tee, second view", "Duct Tape Can't Fix Stupid tee, detail"],
        "close": "Some things you just walk away from.",
    },
    {
        "slug": "never-assume-donkey-tee",
        "name": "Never Assume T-Shirt",
        "short": "Never Assume",
        "collection": "understated-wit",
        "etsy_id": "4598312227",
        "price_from": "26.99",
        "price_high": "37.99",
        "shirt_text": "Never assume. The word explains itself.",
        "blurb": "A line drawing, four words and the oldest office joke.",
        "body": [
            "A simple line-drawn donkey, two short lines of type, and the rest is left to the "
            "reader. Everyone who has sat through a meeting built on a bad assumption gets it in "
            "about two seconds. Nobody else needs to.",
            "It's for the coworker who asks the clarifying question, the project manager who has "
            "seen this movie before, and the retiree who spent forty years politely checking "
            "other people's math.",
        ],
        "build": CC1717_BUILD,
        "colors": CC1717_COLORS,
        "sizes": "S–4XL",
        "cc1717": True,
        "alts": ["Never Assume tee with a line-drawn donkey and gold type",
                 "Never Assume tee in a lifestyle setting", "Never Assume tee, close-up"],
        "close": "Ask first. Nod later.",
    },
    {
        "slug": "leetspeak-anonymous-tee",
        "name": "Definition of Insanity Leetspeak T-Shirt",
        "short": "Definition of Insanity",
        "collection": "understated-wit",
        "etsy_id": "4600286788",
        "price_from": "26.99",
        "price_high": "37.99",
        "shirt_text": "The definition of insanity, written in leetspeak",
        "blurb": "A famous line, hidden in code. Engineers read it instantly.",
        "body": [
            "The old line about insanity — doing the same thing over and over and expecting a "
            "different result — set in leetspeak, numbers standing in for letters, with the turn "
            "picked out in gold. To most people it's a pattern. To a programmer it's a sentence.",
            "It's for the engineer, the IT veteran, the retired sysadmin who has rebooted the "
            "same server a few too many times, and anyone who enjoys a joke that has to be "
            "decoded first.",
        ],
        "build": CC1717_BUILD,
        "colors": CC1717_COLORS,
        "sizes": "S–4XL",
        "cc1717": True,
        "alts": ["Definition of Insanity tee with leetspeak code typography",
                 "Definition of Insanity tee in a lifestyle setting", "Definition of Insanity tee, close-up"],
        "close": "Same input. Same output. Try again.",
    },
    # ---------------- Reflective Faith ----------------
    {
        "slug": "answer-to-one-tee",
        "name": "Answer to One T-Shirt",
        "short": "Answer to One",
        "collection": "reflective-faith",
        "etsy_id": "4606684043",
        "price_from": "26.99",
        "price_high": "37.99",
        "shirt_text": "What would Dad say? What would Jesus do? What would AI suggest? Listen to all three. Answer to One.",
        "blurb": "Three counsels, one allegiance.",
        "body": [
            "What would Dad say? What would Jesus do? What would AI suggest? Most of us ask all "
            "three now, some days before breakfast. The line beneath them settles who gets the "
            "last word: listen to all three, answer to One.",
            "It's for the man who takes advice seriously and his faith more seriously still. He "
            "hears his father's voice in his head, weighs what the new tools have to offer, and "
            "never confuses either one with the counsel he answers to. Three portraits in the "
            "style of an old engraving; the illustration began with AI from our own prompts, and "
            "the lettering was set by hand.",
        ],
        "build": CC1717_BUILD,
        "colors": CC1717_COLORS,
        "sizes": "S–4XL",
        "cc1717": True,
        "alts": ["Answer to One tee with three engraved portraits and gold type",
                 "Answer to One tee in a lifestyle setting", "Answer to One tee, close-up"],
        "close": "Counsel from many. Allegiance to One.",
    },
    {
        "slug": "old-and-wise-tee",
        "name": "Old and Wise T-Shirt",
        "short": "Old and Wise",
        "collection": "reflective-faith",
        "etsy_id": "4610195179",
        "price_from": "26.99",
        "price_high": "37.99",
        "shirt_text": "The reason I'm old and wise is because God protected me when I was young and foolish.",
        "blurb": "Read the big lines, it's a joke. Read the small one, it's a thank-you.",
        "body": [
            "The reason I'm old and wise is because God protected me when I was young and "
            "foolish. Read the two big lines and it's a joke. Read the small gold one and it's a "
            "thank-you.",
            "It's for the man who can laugh at the things he did at nineteen, and knows exactly "
            "Who kept him in one piece through them. It says \"foolish,\" as Proverbs would, so "
            "it's as easy to wear to church as to the hardware store. Set like the title page of "
            "an old book.",
        ],
        "build": CC1717_BUILD,
        "colors": ["Black", "Navy", "Blue Spruce", "Pepper", "Espresso"],
        "sizes": "S–4XL",
        "cc1717": True,
        "alts": ["Old and Wise tee set like the title page of an old book",
                 "Old and Wise tee worn on a porch", "Old and Wise tee, close-up of the gold line"],
        "close": "Kept, not by luck.",
    },
    {
        "slug": "god-whisperer-tee",
        "name": "God Whisperer T-Shirt",
        "short": "God Whisperer",
        "collection": "reflective-faith",
        "etsy_id": "4481594011",
        "price_from": "22.99",
        "price_high": "28.99",
        "shirt_text": "God Whisperer · meditating figure in a galaxy glow",
        "blurb": "For the one who prays more than he talks.",
        "body": [
            "A figure at rest, lit from within against a field of stars. Prayer and stillness "
            "have always gone together; this is a shirt for the part of faith that happens "
            "quietly, before the day gets loud.",
            "It's for the early riser with a worn Bible, the friend who says \"I'll pray for you\" "
            "and actually does, and anyone whose faith is more listening than talking.",
        ],
        "build": "Printed to order on soft cotton, sizes S to 5XL.",
        "colors": ["Charcoal", "Maroon", "Navy", "Sport Grey", "Black", "Forest Green"],
        "sizes": "S–5XL",
        "cc1717": False,
        "alts": ["God Whisperer tee with a meditating figure and galaxy glow",
                 "God Whisperer tee, second view", "God Whisperer tee, detail"],
        "close": "Be still, and know.",
    },
    # ---------------- Thoughtful Expression ----------------
    {
        "slug": "know-more-than-i-say-tee",
        "name": "Know More Than I Say T-Shirt",
        "short": "Know More Than I Say",
        "collection": "thoughtful-expression",
        "etsy_id": "4594292479",
        "price_from": "26.99",
        "price_high": "37.99",
        "shirt_text": "I know more than I say. Think more than I speak. Notice more than you realize.",
        "blurb": "Three lines, set quietly. The last one turns toward the reader.",
        "body": [
            "I know more than I say. Think more than I speak. Notice more than you realize. Three "
            "lines, set quietly — and the last one turns, gently, toward whoever is reading it.",
            "It's for the one at the table who listens first and speaks last. The one who'd "
            "rather be understood than seen, and who is usually underestimated right up until "
            "the one sentence that settles the matter. A classic serif in cream and muted gold.",
        ],
        "build": CC1717_BUILD,
        "colors": CC1717_COLORS,
        "sizes": "S–4XL",
        "cc1717": True,
        "alts": ["Know More Than I Say tee folded on a book with reading glasses",
                 "Know More Than I Say tee in a library setting", "Know More Than I Say tee, close-up"],
        "close": "Say it once, quietly, and let it land.",
    },
    {
        "slug": "with-all-due-respect-tee",
        "name": "With All Due Respect T-Shirt",
        "short": "With All Due Respect",
        "collection": "thoughtful-expression",
        "etsy_id": "4599115072",
        "price_from": "26.99",
        "price_high": "37.99",
        "shirt_text": "With all due respect… I will quietly transition to friends who know my true character.",
        "blurb": "A courteous exit, set in type.",
        "body": [
            "With all due respect. If you perceive me to be incompetent, irrelevant, intolerant, "
            "irreverent or insincere, I will quietly transition to friends who know my true "
            "character. No argument, no raised voice.",
            "It's for the one who has outgrown the need to win every exchange. He knows who he "
            "is, and so do the people who matter. Everyone else is welcome to an opinion, from a "
            "respectful distance.",
        ],
        "build": CC1717_BUILD,
        "colors": CC1717_COLORS,
        "sizes": "S–4XL",
        "cc1717": True,
        "alts": ["With All Due Respect tee laid flat on a desk",
                 "With All Due Respect tee, full text close-up", "With All Due Respect tee with an old hardback"],
        "close": "Say it once, quietly, and let it land.",
    },
    {
        "slug": "thomas-edison-quote-tee",
        "name": "Thomas Edison \"I Have Not Failed\" T-Shirt",
        "short": "I Have Not Failed",
        "collection": "thoughtful-expression",
        "etsy_id": "4600742322",
        "price_from": "26.99",
        "price_high": "37.99",
        "shirt_text": "I have not failed. I've just found ten thousand ways that won't work.",
        "blurb": "Edison on perseverance, for the patient tinkerer.",
        "body": [
            "I have not failed. I've just found ten thousand ways that won't work. Edison's line "
            "has outlasted most of his inventions, because anyone who has built anything "
            "recognizes the truth in it.",
            "It's for the inventor, the engineer, the farmer on his fourth try at a stubborn "
            "repair, and the retiree who finally has time for the workshop. Perseverance, worn "
            "without a pep talk.",
        ],
        "build": CC1717_BUILD,
        "colors": CC1717_COLORS,
        "sizes": "S–4XL",
        "cc1717": True,
        "alts": ["Thomas Edison quote tee in cream and gold type",
                 "Thomas Edison quote tee in a lifestyle setting", "Thomas Edison quote tee, close-up"],
        "close": "Ten thousand and one. Keep going.",
    },
]

# Old site slugs that must keep working.
REDIRECTS = [
    ("/shop/wisdom-faith-ai-tee/", "/shop/answer-to-one-tee/"),
    ("/shop/celebrities-reimagined/", "/shop/thoughtful-expression/"),
]
