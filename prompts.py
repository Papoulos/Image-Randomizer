import random

def generate_random_prompt():

# --- Lists Theme: SCIENCE-FICTION (Standard & Dark) ---

    sujets_sf = [
        "a weary starship captain",
        "a rogue android assassin",
        "a cyborg bounty hunter",
        "an alien ambassador",
        "a mech pilot ",
        "a scientist",
        "a deep-space smuggler",
        "an artificial intelligence",
        "a colonist",
        "a xeno-archaeologist ",
        "a heavily augmented corporate enforcer",
        "a mutant scavenger",
        "a bio-engineer",
        "an explorer",
        "a tech-priest",
        "a data-thief",
        "a lone survivor",
        "a mind-wiped agent ",
        "an alien entity"
    ]

    actions_sf = [
        "hacking into a corrupted corporate datastream",
        "piloting a battered starfighter through wreckage fields",
        "performing emergency repairs on a failing life support system",
        "navigating treacherous, decaying urban underlevels",
        "activating an unstable, forbidden alien device",
        "analyzing a disturbing, non-Euclidean artifact",
        "evading relentless security drones in zero-gravity combat",
        "making a desperate plea to an uncaring alien hive mind",
        "scanning a planet scarred by orbital bombardment",
        "fleeing from grotesque, bio-engineered monstrosities",
        "interfacing with a dying ship's corrupted AI core",
        "deploying a nanobot swarm that consumes organic matter",
        "witnessing the terrifying spectacle of a warp drive malfunction",
        "monitoring flickering screens showing catastrophic data",
        "plugging into a dangerous, unregulated virtual reality",
        "receiving painful, involuntary cybernetic augmentation",
        "escaping a containment breach in a research facility",
        "scavenging vital supplies from derelict spacecraft",
        "decrypting a transmission foretelling cosmic doom",
        "battling malfunctioning security robots in dark corridors"
    ]

    lieux_sf = [
        "bridge of a ghost starship",
        "alley in a cyberpunk megalopolis",
        "orbital station",
        "toxic alien jungle",
        "interior of a planet-sized supercomputer",
        "mining colony on a desolate moon",
        "bio-engineering lab",
        "ruins of a city",
        "black market bazaar in a space hulk",
        "core of a Doomsday machine",
        "underwater research facility",
        "landscape within virtual reality",
        "graveyard of war machines",
        "cryo-storage facility",
        "desert planet",
        "interior of an alien vessel",
        "quarantine zone",
        "corporate arcology",
        "alien city",
        "the void near a black hole's event horizon"
    ]

    vetements_sf = [
        "a sleek, black environmental suit, subtly damaged",
        "a heavy combat exoskeleton stained with alien ichor",
        "crude, visible cybernetic limbs sparking intermittently",
        "glitching holographic clothing displaying corrupted ads",
        "ragged scavenger gear patched with scrap metal and bio-fiber",
        "a long, stained trench coat concealing multiple weapons",
        "a minimalist, utilitarian uniform of a dystopian regime",
        "dark, form-fitting stealth suit with optical camouflage",
        "a sterile, blood-spattered hazard suit from a lab outbreak",
        "flowing, tattered robes of a void cultist leader",
        "a pilot's G-suit, torn and stained with hydraulic fluid",
        "exposed, crude cybernetics replacing missing body parts",
        "a grimy virtual reality interface suit covered in wires",
        "heavy, scarred power armor marked with kill counts",
        "patched, mismatched clothing of a desperate survivor",
        "angular, intimidating armor of corporate security forces",
        "a bulky, damaged EVA spacesuit leaking oxygen",
        "augmented reality goggles displaying ominous warnings",
        "adaptive camouflage fatigues flickering erratically",
        "bio-luminescent symbiotic plating fused to the skin"
    ]

    ambiances_sf = [
        "cold, sterile fluorescent lighting casting harsh shadows",
        "flickering emergency lights bathing corridors in red",
        "the oppressive silence of a vacuum or dead station",
        "lens flares from harsh, industrial spotlights",
        "dense, acidic rain under a perpetually overcast sky",
        "eerie bioluminescent glow from toxic alien fungi",
        "oppressive, sterile white light of a sinister medical bay",
        "the disturbing green glow of unknown energy fields",
        "constant blaring of distant, ignored warning sirens",
        "artificial, sickly yellow sunlight in a polluted biodome",
        "disorienting strobe lights from malfunctioning equipment",
        "the cold, pale blue glow from countless data screens",
        "absolute, terrifying darkness swallowing all light",
        "thick, choking smog obscuring visibility in a dense city",
        "electrical arcing illuminating scenes in brief, violent flashes",
        "the blinding, unforgiving glare of a nearby binary star",
        "a gritty, noir atmosphere with deep shadows and high contrast",
        "shimmering heat haze over irradiated tech ruins",
        "holographic projections glitching, showing disturbing images",
        "an unsettling sense of being watched or hunted"
    ]

    compositions_sf = [
        "extreme close-up",
        "wide shot",
        "low angle shot",
        "centered shot",
        "over-the-shoulder shot",
        "dutch angle",
        "symmetrical shot",
        "tracking shot",
        "fisheye lens",
        "long shot",
        "split diopter",
        "high angle",
        "first-person POV",
        "rule of thirds",
        "rack focus",
        "silhouette",
        "tight framing",
        "macro shot",
        "worm's-eye view",
        "cinematic widescreen"
    ]

    details_sf = [
        "flickering neon signs casting long, dancing shadows",
        "visible streams of corrupted data code glitching in the air",
        "puddles of iridescent chemical waste bubbling slightly",
        "discarded, damaged cybernetic limbs lying in alleys",
        "distant, muffled warning klaxons echoing constantly",
        "pressurized steam hissing menacingly from broken vents",
        "patches of invasive, pulsating alien bio-mold",
        "small metallic debris gently floating in zero-gravity",
        "smashed security monitors displaying only static or errors",
        "glitching holographic 'Wanted' posters showing grim faces",
        "visible ripples or distortions from strange energy fluctuations",
        "pools of leaking, luminous coolant dripping from machinery",
        "scattered, empty nutrient paste tubes and ration packs",
        "exposed, sparking electrical wiring panels hanging loose",
        "a severed, malfunctioning robotic arm twitching erratically",
        "silent, ominous surveillance drones drifting slowly overhead",
        "glowing, cryptic graffiti tags warning of danger",
        "open, ice-covered cryogenic suspension pods, contents unknown",
        "scattered brass bullet casings glinting under harsh light",
        "trails of viscous, black unidentified slime on floors"
    ]

    styles_sf = [
        "gritty, dystopian cyberpunk aesthetic (style of Blade Runner 2049)",
        "dark industrial sci-fi (style of Alien, Event Horizon)",
        "retro-futurism noir (style of Bioshock, Dark City)",
        "bio-punk horror emphasizing grotesque body modification",
        "hard science fiction realism with a sense of dread",
        "cosmic horror sci-fi (style of H.P. Lovecraft, Prometheus)",
        "anime mech design with dark, psychological themes (style of Evangelion)",
        "dieselpunk post-apocalypse (style of Mad Max)",
        "photorealistic concept art depicting oppressive futures",
        "glitch art aesthetics representing system corruption",
        "surreal bio-mechanical horror (style of H.R. Giger, Zdzisław Beksiński)",
        "found footage or security camera perspective",
        "cinematic sci-fi horror film look (style of John Carpenter)",
        "stark brutalist architectural focus, emphasizing scale and coldness",
        "monochromatic noir photography with high contrast",
        "Soviet-era brutalist retrofuturism",
        "detailed technical illustration of decaying machinery",
        "cell-shaded graphics with dark outlines and grim palettes",
        "abstract art depicting technological singularity or cosmic dread",
        "infra-red or thermal vision point-of-view"
    ]



# Lists for generating fantasy and science-fantasy prompts

    sujets_hf = [
        "a mystical dragon",
        "an ancient sorcerer",
        "a noble paladin",
        "a shadowy assassin",
        "a wise old sage",
        "a cursed knight",
        "a dark elf warlord",
        "a wandering bard",
        "a fierce barbarian",
        "a high priestess",
        "a forest druid",
        "a goblin chieftain",
        "a fallen angel",
        "a royal heir in exile",
        "a necromancer",
        "a dwarven king",
        "a battle-hardened ranger",
        "a witch-queen",
        "a beastmaster with his companion",
        "a lone adventurer"
    ]
    
    actions_hf = [
        "casting a powerful incantation of fire",
        "wielding an enchanted sword against foes",
        "summoning a creature from another plane",
        "sneaking silently through torchlit corridors",
        "performing a forbidden ritual under moonlight",
        "leading soldiers into a desperate battle",
        "exploring ancient, crumbling ruins",
        "riding a mighty griffon through the skies",
        "calling upon ancestral spirits for aid",
        "dueling a rival in a sacred arena",
        "healing the wounded with divine magic",
        "searching for a legendary artifact",
        "confronting a monstrous guardian",
        "protecting a sacred grove from invaders",
        "marching across a battlefield of corpses",
        "deciphering glowing, cryptic runes",
        "kneeling before a godlike apparition",
        "drinking from a cursed chalice",
        "commanding undead legions from a dark citadel",
        "whispering secrets to demonic forces"
    ]
    
    lieux_hf = [
        "a dense, enchanted forest filled with whispers",
        "a towering, ancient castle shrouded in fog",
        "a vast battlefield littered with bones",
        "a hidden elven sanctuary in twilight",
        "a grand, gothic cathedral of forgotten gods",
        "a misty mountain pass above the clouds",
        "a mystical crystal cavern glowing faintly",
        "a dark, underground dwarven fortress",
        "a haunted graveyard under a blood moon",
        "a sacred druidic stone circle",
        "a storm-lashed cliff overlooking the sea",
        "a royal throne room illuminated by torches",
        "a cursed swamp with twisted trees",
        "a ruined temple swallowed by the jungle",
        "a frozen tundra under aurora skies",
        "a labyrinthine dungeon carved in stone",
        "a fiery volcanic wasteland",
        "a sunlit meadow hiding ancient ruins",
        "a war-torn village reduced to ashes",
        "a mystical floating island drifting in clouds"
    ]
    
    vetements_hf = [
        "ornate robes embroidered with glowing runes",
        "battle-scarred plate armor bearing heraldic sigils",
        "dark leather assassin garb with hidden daggers",
        "elegant elven attire woven with silver thread",
        "a hooded cloak concealing a scarred face",
        "mystical robes lined with golden trim",
        "ceremonial regalia of a forgotten cult",
        "a suit of dwarven-forged armor covered in soot",
        "a ragged cloak stitched with charms and bones",
        "simple monk’s robes of coarse fabric",
        "gleaming armor polished for royal ceremonies",
        "tattered garments soaked in dried blood",
        "fur-lined leathers suited for frozen tundras",
        "robes of a necromancer adorned with skulls",
        "a crown set with cracked gemstones",
        "an enchanted chainmail shirt that glows faintly",
        "leather armor reinforced with dragon scales",
        "a druid’s outfit covered in living vines",
        "noble garments decorated with golden embroidery",
        "a witch’s wide-brimmed hat and shadowy cloak"
    ]
    
    ambiances_hf = [
        "mystical and ethereal moonlight",
        "dark and foreboding shadows",
        "ancient, timeless atmosphere heavy with secrets",
        "eerie and haunting silence broken by whispers",
        "vibrant and otherworldly magical glow",
        "gothic and moody candlelight",
        "heroic and inspiring, bathed in sunlight",
        "melancholic and somber twilight skies",
        "chaotic and intense battlefield tension",
        "serene and tranquil pastoral setting",
        "majestic and awe-inspiring divine presence",
        "apocalyptic and desolate wastelands",
        "whimsical and enchanted woodland charm",
        "dramatic and tense standoff",
        "shadowy and ominous corridors",
        "mysterious and intriguing ruins",
        "grand and epic landscapes of mountains and castles",
        "fiery and destructive volcanic light",
        "sacred and solemn holy ground",
        "unsettling silence before an ambush"
    ]
    
    compositions_hf = [
        "close-up portrait with intense expression",
        "wide, sweeping landscape view",
        "low-angle heroic shot emphasizing power",
        "dramatic silhouette against glowing skies",
        "symmetrical framing with divine balance",
        "dynamic action pose mid-battle",
        "crowded and chaotic battle composition",
        "isolated lone figure in vast wilderness",
        "high-angle diminishing perspective",
        "rule of thirds for dramatic balance",
        "natural framing with branches or ruins",
        "deep atmospheric perspective through mist",
        "shallow depth of field on mystical symbols",
        "panoramic mountain range with castles",
        "intimate close-up of spellcasting hands",
        "monumental scale with towering structures",
        "framed through archways or ruins",
        "bird’s-eye view over battlefield",
        "intense duel in focused foreground",
        "grand tableau with multiple characters posed"
    ]
    
    details_hf = [
        "floating crystal shards glowing faintly",
        "glowing arcane runes etched into stone",
        "patches of luminescent fungi on walls",
        "wisps of spectral energy drifting slowly",
        "ancient banners torn and fluttering",
        "a sword embedded in cracked earth",
        "a chalice spilling glowing liquid",
        "a shattered crown lying forgotten",
        "carved statues eroded by time",
        "motes of magical dust drifting in air",
        "a burning brazier casting long shadows",
        "shattered shields and rusted weapons",
        "a pool reflecting eerie moonlight",
        "vines entangling old ruins",
        "skulls arranged in ritual patterns",
        "a grimoire open on a pedestal",
        "a spectral animal companion lurking nearby",
        "storm clouds swirling ominously overhead",
        "a shattered stained-glass window glowing faintly",
        "a circle of candles flickering in the wind"
    ]
    
    styles_hf = [
        "dark, gothic fantasy (style of Dark Souls, Diablo)",
        "high fantasy epic (style of The Lord of the Rings)",
        "grimdark medieval realism (style of The Witcher)",
        "mythological and heroic (style of ancient epics)",
        "romantic fantasy painting (style of John William Waterhouse)",
        "ethereal and dreamlike illustration",
        "baroque and ornate fantasy art",
        "folkloric fairy-tale atmosphere",
        "epic fantasy concept art",
        "whimsical and enchanted storybook",
        "sword-and-sorcery pulp aesthetic",
        "renaissance-inspired high fantasy painting",
        "dark ritualistic horror",
        "majestic divine grandeur",
        "expressionistic fantasy art",
        "celestial and angelic themes",
        "arcane and mysterious symbolism",
        "battlefield fantasy realism",
        "storybook illustration with bright palettes",
        "otherworldly surrealist fantasy"
    ]



# --- Lists Theme: NOIR/POLAR ---

    sujets_np = [
        "un détective privé cynique",
        "une femme fatale énigmatique",
        "un flic corrompu",
        "un baron du crime",
        "un indic nerveux",
        "un journaliste d'investigation tenace"
    ]

    actions_np = [
        "enquêtant sur une disparition mystérieuse",
        "surveillant une ruelle sombre depuis une voiture",
        "interrogeant un suspect sous une lumière blafarde",
        "fuyant des tueurs à gages dans la nuit",
        "découvrant une preuve compromettante",
        "recevant un pot-de-vin dans un bar enfumé"
    ]

    lieux_np = [
        "un bureau de détective privé miteux",
        "une ruelle sombre et pluvieuse",
        "un bar de jazz enfumé",
        "un entrepôt désaffecté sur les quais",
        "un appartement de luxe avec un sombre secret",
        "une morgue froide et silencieuse"
    ]

    vetements_np = [
        "un trench-coat et un chapeau fedora",
        "une robe de soirée élégante et un collier de perles",
        "un costume mal ajusté",
        "des vêtements de travail usés",
        "un uniforme de police",
        "un manteau de fourrure luxueux"
    ]

    ambiances_np = [
        "une pluie battante incessante",
        "des ombres profondes et des contrastes élevés",
        "la fumée de cigarette flottant dans l'air",
        "le son lointain d'une sirène de police",
        "une tension palpable",
        "un sentiment de paranoïa et de méfiance"
    ]

    compositions_np = [
        "plan rapproché sur un visage anxieux",
        "grand angle sur une ville nocturne",
        "contre-plongée pour accentuer le pouvoir",
        "silhouette se découpant dans un encadrement de porte",
        "reflet dans une flaque d'eau",
        "angle hollandais pour créer un malaise"
    ]

    details_np = [
        "un verre de whisky posé sur un bureau",
        "un store vénitien projetant des ombres en bandes",
        "un mégot de cigarette écrasé dans un cendrier",
        "une tache de sang sur le trottoir",
        "un néon clignotant à l'extérieur",
        "une photo en noir et blanc sur un mur"
    ]

    styles_np = [
        "style film noir classique (style de Le Faucon Maltais)",
        "esthétique néo-noir (style de Blade Runner, Sin City)",
        "photographie en noir et blanc à fort contraste",
        "cinématographie avec beaucoup d'ombres (clair-obscur)",
        "atmosphère sombre et pessimiste",
        "réalisme granuleux"
    ]


# --- Lists Theme: HORREUR/DARK HORREUR ---

    sujets_hd = [
        "une créature cauchemardesque",
        "un survivant terrifié",
        "un cultiste dément",
        "un fantôme vengeur",
        "un savant fou",
        "une poupée possédée"
    ]

    actions_hd = [
        "fuyant une menace invisible dans un couloir sombre",
        "se cachant dans un placard en retenant sa respiration",
        "lisant un grimoire interdit à la lueur d'une bougie",
        "assistant à un rituel blasphématoire",
        "étant traqué par une entité malveillante",
        "se réveillant dans un lieu inconnu et macabre"
    ]

    lieux_hd = [
        "un asile abandonné",
        "une maison hantée au sommet d'une colline",
        "une forêt sombre et silencieuse",
        "un cimetière brumeux à minuit",
        "un laboratoire souterrain secret",
        "une église désacralisée"
    ]

    vetements_hd = [
        "des haillons sales et déchirés",
        "une chemise de nuit blanche tachée de sang",
        "une robe de cérémonie de culte avec des symboles étranges",
        "des bandages recouvrant des blessures horribles",
        "une blouse de médecin souillée",
        "des vêtements d'enfants démodés"
    ]

    ambiances_hd = [
        "une obscurité quasi totale",
        "un silence de mort oppressant",
        "des murmures incompréhensibles",
        "une sensation d'être observé",
        "une lumière vacillante",
        "un froid glacial et anormal"
    ]

    compositions_hd = [
        "très gros plan sur un œil terrifié",
        "plan en vue subjective (POV) du monstre",
        "silhouette menaçante se dessinant au loin",
        "cadrage serré dans un espace confiné",
        "plongée sur une victime impuissante",
        "image déformée comme vue à travers un judas"
    ]

    details_hd = [
        "des rayures sur les murs",
        "des empreintes de pas ensanglantées",
        "une porte qui grince lentement",
        "des jouets d'enfants abandonnés",
        "des symboles occultes dessinés sur le sol",
        "des ombres qui bougent toutes seules"
    ]

    styles_hd = [
        "horreur gothique (style de Dracula de Bram Stoker)",
        "horreur cosmique (style de H.P. Lovecraft)",
        "body horror (style de David Cronenberg)",
        "found footage (style de Le Projet Blair Witch)",
        "horreur psychologique (style de The Shining)",
        "art surréaliste et macabre (style de Zdzisław Beksiński)"
    ]


    Themes = [ "SF","HF", "NP", "HD" ]

    theme = random.choice(Themes)

    if theme == "SF" :
        print("SF")
        sujet = random.choice(sujets_sf)
        action = random.choice(actions_sf)
        lieu = random.choice(lieux_sf)
        vetement = random.choice(vetements_sf)
        ambiance = random.choice(ambiances_sf)
        composition = random.choice(compositions_sf)
        style = random.choice(styles_sf)

        # Choisir 2 ou 3 détails distincts
        nb_details = random.randint(2, 3)
        details_choisis = random.sample(details_sf, nb_details)
        details_str = ", ".join(details_choisis) # Les sépare par une virgule

        # Assembler le prompt brut
        # Vous pouvez varier la structure ici
        # random_prompt = f"{composition} d'un(e) {sujet} {vetement}, {action} dans un(e) {lieu}. {details_str}. Ambiance {ambiance}. Style {style}."
        random_prompt = f"Science-fiction, {composition}, {sujet}, {vetement}, {action}, {lieu}, {details_str}, {ambiance}, {style}."
    elif theme == "HF" :
        print("HF")
        sujet = random.choice(sujets_hf)
        action = random.choice(actions_hf)
        lieu = random.choice(lieux_hf)
        vetement = random.choice(vetements_hf)
        ambiance = random.choice(ambiances_hf)
        composition = random.choice(compositions_hf)
        style = random.choice(styles_hf)

        # Choisir 2 ou 3 détails distincts
        nb_details = random.randint(2, 3)
        details_choisis = random.sample(details_hf, nb_details)
        details_str = ", ".join(details_choisis) # Les sépare par une virgule

        # Assembler le prompt brut
        # Vous pouvez varier la structure ici
        # random_prompt = f"{composition} d'un(e) {sujet} {vetement}, {action} dans un(e) {lieu}. {details_str}. Ambiance {ambiance}. Style {style}."
        random_prompt = f"Heroic-Fantasy, {composition}, {sujet}, {vetement}, {action}, {lieu}, {details_str}, {ambiance}, {style}."
    elif theme == "NP":
        print("NP")
        sujet = random.choice(sujets_np)
        action = random.choice(actions_np)
        lieu = random.choice(lieux_np)
        vetement = random.choice(vetements_np)
        ambiance = random.choice(ambiances_np)
        composition = random.choice(compositions_np)
        style = random.choice(styles_np)

        nb_details = random.randint(2, 3)
        details_choisis = random.sample(details_np, nb_details)
        details_str = ", ".join(details_choisis)

        random_prompt = f"Noir/Polar, {composition}, {sujet}, {vetement}, {action}, {lieu}, {details_str}, {ambiance}, {style}."
    elif theme == "HD":
        print("HD")
        sujet = random.choice(sujets_hd)
        action = random.choice(actions_hd)
        lieu = random.choice(lieux_hd)
        vetement = random.choice(vetements_hd)
        ambiance = random.choice(ambiances_hd)
        composition = random.choice(compositions_hd)
        style = random.choice(styles_hd)

        nb_details = random.randint(2, 3)
        details_choisis = random.sample(details_hd, nb_details)
        details_str = ", ".join(details_choisis)

        random_prompt = f"Horreur/Dark Horreur, {composition}, {sujet}, {vetement}, {action}, {lieu}, {details_str}, {ambiance}, {style}."



    # Ici, vous enverriez prompt_brut à votre LLM pour l'améliorer
    # prompt_final = appeler_llm(prompt_brut)
    # return prompt_final

    return random_prompt # Pour l'instant, on retourne le prompt brut
