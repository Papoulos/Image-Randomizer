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
        "un journaliste d'investigation tenace",
        "un avocat véreux",
        "un procureur obsédé par la vérité",
        "un boxeur déchu reconverti en garde du corps",
        "un chauffeur de taxi taciturne",
        "un photographe de crime curieux",
        "un tueur à gages froid et méthodique",
        "un pickpocket rusé",
        "un sénateur compromis dans un scandale",
        "un vétéran de guerre brisé",
        "un parrain de la mafia vieillissant",
        "une chanteuse de jazz mélancolique",
        "un banquier aux affaires louches",
        "un flic idéaliste au bord de la chute",
        "un vagabond qui en sait trop"
    ]
    
    actions_np = [
        "enquêtant sur une disparition mystérieuse",
        "surveillant une ruelle sombre depuis une voiture",
        "interrogeant un suspect sous une lumière blafarde",
        "fuyant des tueurs à gages dans la nuit",
        "découvrant une preuve compromettante",
        "recevant un pot-de-vin dans un bar enfumé",
        "planquant des liasses de billets dans un coffre",
        "frappant à la porte d’un inconnu sous la pluie",
        "rédigeant un article explosif dans une salle de rédaction vide",
        "cachant une arme ensanglantée",
        "dissimulant un corps dans un coffre de voiture",
        "suivant une silhouette dans les rues embrumées",
        "déjouant une embuscade dans une ruelle",
        "trahissant un allié pour sauver sa peau",
        "espionnant une conversation téléphonique",
        "se faisant doubler par un complice",
        "assistant à un règlement de comptes",
        "remettant une mallette mystérieuse",
        "se noyant dans l’alcool dans un bar désert",
        "recevant un appel anonyme tard dans la nuit"
    ]
    
    lieux_np = [
        "un bureau de détective privé miteux",
        "une ruelle sombre et pluvieuse",
        "un bar de jazz enfumé",
        "un entrepôt désaffecté sur les quais",
        "un appartement de luxe avec un sombre secret",
        "une morgue froide et silencieuse",
        "un hôtel de passe crasseux",
        "un parking désert éclairé par un néon",
        "une salle de boxe décrépite",
        "un commissariat corrompu",
        "un casino clandestin",
        "une salle de rédaction pleine de machines à écrire",
        "un club sélect fréquenté par la pègre",
        "une chambre d’hôtel à rideaux tirés",
        "une station de métro déserte",
        "un toit de gratte-ciel sous la pluie",
        "une maison bourgeoise cachant des secrets",
        "une planque de mafieux",
        "un tribunal silencieux la nuit",
        "un cinéma de quartier délabré"
    ]
    
    vetements_np = [
        "un trench-coat et un chapeau fedora",
        "une robe de soirée élégante et un collier de perles",
        "un costume mal ajusté",
        "des vêtements de travail usés",
        "un uniforme de police",
        "un manteau de fourrure luxueux",
        "une chemise blanche tachée de sang",
        "un smoking défraîchi",
        "un gilet pare-balles dissimulé sous un veston",
        "un imperméable trempé de pluie",
        "des talons aiguilles brillants sous un manteau long",
        "un costume trois-pièces rayé",
        "une cravate desserrée",
        "une robe cocktail fendue",
        "un chapeau cloche élégant",
        "un pardessus sombre trop grand",
        "des lunettes de soleil portées la nuit",
        "un brassard de policier élimé",
        "des gants en cuir noir",
        "un foulard taché de rouge à lèvres"
    ]
    
    ambiances_np = [
        "une pluie battante incessante",
        "des ombres profondes et des contrastes élevés",
        "la fumée de cigarette flottant dans l'air",
        "le son lointain d'une sirène de police",
        "une tension palpable",
        "un sentiment de paranoïa et de méfiance",
        "un silence pesant avant une trahison",
        "un éclairage artificiel trop cru",
        "une chaleur étouffante dans une pièce sans fenêtre",
        "une radio grésillant un vieux standard de jazz",
        "une atmosphère poisseuse et moite",
        "le bruit régulier d’une goutte d’eau",
        "des conversations chuchotées dans des recoins sombres",
        "une ambiance enfumée saturée de whisky",
        "la lumière blafarde d’un réverbère isolé",
        "un mélange de désir et de danger",
        "le tumulte étouffé d’une ville la nuit",
        "une impression constante d’être suivi",
        "le claquement régulier d’une machine à écrire",
        "une tension dramatique prête à exploser"
    ]
    
    compositions_np = [
        "plan rapproché sur un visage anxieux",
        "grand angle sur une ville nocturne",
        "contre-plongée pour accentuer le pouvoir",
        "silhouette se découpant dans un encadrement de porte",
        "reflet dans une flaque d'eau",
        "angle hollandais pour créer un malaise",
        "plan serré sur une main tenant une arme",
        "champ-contrechamp entre deux personnages en conflit",
        "ombre projetée sur un mur décrépi",
        "fenêtre éclairée dans une nuit noire",
        "vue à travers des stores vénitiens",
        "focus sur un objet compromettant",
        "silhouette floue au bout d’une ruelle",
        "vue en plongée d’un bureau en désordre",
        "contre-jour dramatique dans la fumée",
        "panoramique lent sur une scène de crime",
        "zoom progressif sur un visage inquiet",
        "plan fixe dans une pièce silencieuse",
        "cadrage asymétrique renforçant le malaise",
        "plan séquence suivant un suspect dans la rue"
    ]
    
    details_np = [
        "un verre de whisky posé sur un bureau",
        "un store vénitien projetant des ombres en bandes",
        "un mégot de cigarette écrasé dans un cendrier",
        "une tache de sang sur le trottoir",
        "un néon clignotant à l'extérieur",
        "une photo en noir et blanc sur un mur",
        "un revolver posé sur une table",
        "un téléphone à cadran décroché",
        "une machine à écrire abandonnée",
        "des billets froissés éparpillés sur le sol",
        "une paire de menottes entrouvertes",
        "un briquet gravé avec des initiales",
        "des bouteilles vides alignées derrière un bar",
        "une clé rouillée oubliée dans une serrure",
        "des cartes de jeu éparpillées",
        "un chapeau tombé dans une flaque",
        "une lettre froissée tachée de larmes",
        "des empreintes boueuses menant à une porte",
        "un miroir fissuré renvoyant un reflet troublant",
        "un rideau qui se balance dans le courant d’air"
    ]
    
    styles_np = [
        "style film noir classique (Le Faucon Maltais, Assurance sur la mort)",
        "esthétique néo-noir (Blade Runner, Sin City, L.A. Confidential)",
        "photographie en noir et blanc à fort contraste",
        "cinématographie expressionniste allemande (ombres déformées, clair-obscur)",
        "atmosphère sombre et pessimiste inspirée de Raymond Chandler",
        "réalisme granuleux des années 70",
        "style polar français (Jean-Pierre Melville, Jacques Becker)",
        "esthétique pulp avec couvertures de magazines illustrées",
        "noir urbain moderne avec néons et pluie",
        "composition théâtrale dramatique inspirée du théâtre kabuki",
        "mise en scène minimaliste et froide",
        "style graphic novel noir et blanc",
        "ambiance documentaire des bas-fonds",
        "influence hitchcockienne, suspense psychologique",
        "sombres aquarelles évoquant des cauchemars",
        "style photojournalisme années 50",
        "images sépia granuleuses d’époque",
        "atmosphère de thriller paranoïaque",
        "esthétique cinéma indépendant low-key",
        "illustration stylisée à l’encre noire"
    ]    



# --- Lists Theme: HORREUR/DARK HORREUR ---

    sujets_hd = [
        "une créature cauchemardesque",
        "un survivant terrifié",
        "un cultiste dément",
        "un fantôme vengeur",
        "un savant fou",
        "une poupée possédée",
        "un démon aux formes changeantes",
        "un prêtre défroqué tourmenté",
        "une mariée spectrale",
        "un corbeau aux yeux luisants",
        "un cadavre réanimé",
        "un fossoyeur sinistre",
        "une sorcière aux doigts tordus",
        "un enfant aux yeux vides",
        "un vampire affamé",
        "un patient d’asile mutilé",
        "un chasseur de monstres épuisé",
        "un parasite extraterrestre",
        "une nonne démoniaque",
        "un nécromancien"
    ]
    
    actions_hd = [
        "fuyant une menace invisible dans un couloir sombre",
        "se cachant dans un placard en retenant sa respiration",
        "lisant un grimoire interdit à la lueur d'une bougie",
        "assistant à un rituel blasphématoire",
        "étant traqué par une entité malveillante",
        "se réveillant dans un lieu inconnu et macabre",
        "ouvrant lentement une porte grinçante",
        "regardant fixement un miroir qui déforme le reflet",
        "hurlant silencieusement sans que personne n’entende",
        "descendant un escalier vers une cave humide",
        "creusant une tombe en pleine nuit",
        "tenant une lanterne vacillante dans la brume",
        "sacrifiant un animal lors d’une cérémonie occulte",
        "grattant frénétiquement les murs de pierre",
        "fuyant dans une forêt plongée dans le brouillard",
        "écoutant une voix qui chuchote dans sa tête",
        "ouvrant un cercueil ancien",
        "brûlant des herbes pour repousser un démon",
        "s’éveillant avec des cicatrices inexpliquées",
        "se débattant contre des chaînes rouillées"
    ]
    
    lieux_hd = [
        "un asile abandonné",
        "une maison hantée au sommet d'une colline",
        "une forêt sombre et silencieuse",
        "un cimetière brumeux à minuit",
        "un laboratoire souterrain secret",
        "une église désacralisée",
        "un grenier poussiéreux rempli de toiles d’araignée",
        "un manoir victorien en ruine",
        "un marais stagnant couvert de brouillard",
        "une crypte souterraine infestée de rats",
        "un hôtel délabré au bord de la route",
        "une cabane isolée dans les bois",
        "un théâtre abandonné",
        "un vieux moulin grinçant",
        "une salle d’opération désaffectée",
        "un couvent en ruines",
        "un tunnel de métro désert",
        "un phare battu par la tempête",
        "un champ de bataille jonché d’ossements",
        "un cirque abandonné"
    ]
    
    vetements_hd = [
        "des haillons sales et déchirés",
        "une chemise de nuit blanche tachée de sang",
        "une robe de cérémonie de culte avec des symboles étranges",
        "des bandages recouvrant des blessures horribles",
        "une blouse de médecin souillée",
        "des vêtements d'enfants démodés",
        "une cape noire à capuche",
        "un masque de cuir sanglant",
        "un uniforme d’asile jauni",
        "une soutane effilochée",
        "un manteau trempé de pluie et de boue",
        "un tablier taché d’organes",
        "une armure ancienne corrodée",
        "un costume de clown macabre",
        "des draps funéraires en lambeaux",
        "des bottes couvertes de boue et de sang",
        "un chapelet brisé autour du cou",
        "un voile de mariée jauni",
        "une combinaison de patient psychiatrique",
        "un manteau de fourrure miteux"
    ]
    
    ambiances_hd = [
        "une obscurité quasi totale",
        "un silence de mort oppressant",
        "des murmures incompréhensibles",
        "une sensation d'être observé",
        "une lumière vacillante",
        "un froid glacial et anormal",
        "des rires lointains et déformés",
        "une odeur de chair brûlée",
        "un brouillard épais et étouffant",
        "une pluie battante sur un toit en tôle",
        "des battements de cœur résonnant dans le silence",
        "un écho constant de pas invisibles",
        "des grincements incessants",
        "un souffle glacé dans la nuque",
        "une distorsion sonore oppressante",
        "un parfum de fleurs fanées",
        "le clignotement irrégulier d’une lumière",
        "une chaleur suffocante et malsaine",
        "une vibration sourde venue du sol",
        "un chœur de voix inhumaines"
    ]
    
    compositions_hd = [
        "très gros plan sur un œil terrifié",
        "plan en vue subjective (POV) du monstre",
        "silhouette menaçante se dessinant au loin",
        "cadrage serré dans un espace confiné",
        "plongée sur une victime impuissante",
        "image déformée comme vue à travers un judas",
        "contre-jour d’une figure monstrueuse",
        "plan fixe sur une porte entrouverte",
        "caméra tremblante suivant une fuite",
        "silhouette apparaissant dans un miroir",
        "plan large d’un paysage désolé",
        "ombre mouvante projetée sur un mur",
        "vue en plongée d’un rituel occulte",
        "composition centrée sur un cercle rituel",
        "plan séquence à travers un couloir sans fin",
        "macro sur un objet ensanglanté",
        "split screen entre victime et bourreau",
        "plan décentré renforçant le malaise",
        "vue de dos d’une silhouette immobile",
        "plan figé sur un visage figé dans l’horreur"
    ]
    
    details_hd = [
        "des rayures sur les murs",
        "des empreintes de pas ensanglantées",
        "une porte qui grince lentement",
        "des jouets d'enfants abandonnés",
        "des symboles occultes dessinés sur le sol",
        "des ombres qui bougent toutes seules",
        "des chandeliers renversés",
        "des ossements éparpillés",
        "une horloge arrêtée à minuit",
        "des chaînes suspendues au plafond",
        "des miroirs fissurés",
        "un couteau rouillé planté dans le bois",
        "des vitraux brisés laissant passer une lueur étrange",
        "un journal intime taché",
        "une porte barricadée",
        "des statues aux visages déformés",
        "un corbeau empaillé couvert de poussière",
        "des traces de griffes sur le sol",
        "un cercueil entrouvert",
        "des toiles d’araignée épaisses"
    ]
    
    styles_hd = [
        "horreur gothique (style Dracula, Crimson Peak)",
        "horreur cosmique (style H.P. Lovecraft)",
        "body horror (style David Cronenberg, The Thing)",
        "found footage (style Le Projet Blair Witch, REC)",
        "horreur psychologique (style The Shining, Hereditary)",
        "art surréaliste et macabre (style Zdzisław Beksiński)",
        "slasher des années 80 (style Halloween, Vendredi 13)",
        "horreur japonaise (style Ringu, Ju-On)",
        "conte macabre illustré",
        "film expressionniste allemand (Nosferatu, Le Cabinet du Dr Caligari)",
        "horreur religieuse (style L’Exorciste, The Nun)",
        "cinéma gore extrême",
        "horreur folklorique (style The Witch, Midsommar)",
        "esthétique VHS rétro",
        "illustration lovecraftienne à l’encre",
        "peinture sombre et baroque",
        "horreur post-apocalyptique",
        "style cauchemar surréaliste",
        "esthétique cauchemar urbain (Silent Hill)",
        "film noir horrifique"
    ]



    Themes = [ "SF","HF", "NP", "HD", "Mixed" ]
    Mixed_Themes = ["SF-NP", "HF-HD", "SF-HD"]

    theme = random.choice(Themes)

    if theme == "Mixed":
        mixed_theme_choice = random.choice(Mixed_Themes)
        theme1_str, theme2_str = mixed_theme_choice.split('-')

        print(f"Mixed Theme: {theme1_str}-{theme2_str}")

        theme_map = {
            "SF": (sujets_sf, actions_sf, lieux_sf, vetements_sf, ambiances_sf, compositions_sf, details_sf, styles_sf),
            "HF": (sujets_hf, actions_hf, lieux_hf, vetements_hf, ambiances_hf, compositions_hf, details_hf, styles_hf),
            "NP": (sujets_np, actions_np, lieux_np, vetements_np, ambiances_np, compositions_np, details_np, styles_np),
            "HD": (sujets_hd, actions_hd, lieux_hd, vetements_hd, ambiances_hd, compositions_hd, details_hd, styles_hd),
        }

        theme1_lists = theme_map[theme1_str]
        theme2_lists = theme_map[theme2_str]

        sujet = random.choice(random.choice([theme1_lists[0], theme2_lists[0]]))
        action = random.choice(random.choice([theme1_lists[1], theme2_lists[1]]))
        lieu = random.choice(random.choice([theme1_lists[2], theme2_lists[2]]))
        vetement = random.choice(random.choice([theme1_lists[3], theme2_lists[3]]))
        ambiance = random.choice(random.choice([theme1_lists[4], theme2_lists[4]]))
        composition = random.choice(random.choice([theme1_lists[5], theme2_lists[5]]))
        style = random.choice(random.choice([theme1_lists[7], theme2_lists[7]]))

        details_list = random.choice([theme1_lists[6], theme2_lists[6]])
        nb_details = random.randint(2, 3)
        details_choisis = random.sample(details_list, nb_details)
        details_str = ", ".join(details_choisis)

        random_prompt = f"Mixed Genre ({theme1_str}/{theme2_str}), {composition}, {sujet}, {vetement}, {action}, {lieu}, {details_str}, {ambiance}, {style}."
        return random_prompt, mixed_theme_choice

    elif theme == "SF" :
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
        return random_prompt, theme
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
        return random_prompt, theme
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
        return random_prompt, theme
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
        return random_prompt, theme
