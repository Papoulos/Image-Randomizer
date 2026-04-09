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
        "a cynical private investigator",
        "an enigmatic femme fatale",
        "a corrupt cop",
        "a crime lord",
        "a nervous snitch",
        "a tenacious investigative journalist",
        "a crooked lawyer",
        "a prosecutor obsessed with the truth",
        "a fallen boxer turned bodyguard",
        "a taciturn taxi driver",
        "a curious crime photographer",
        "a cold and methodical hitman",
        "a cunning pickpocket",
        "a senator compromised in a scandal",
        "a broken war veteran",
        "an aging mafia godfather",
        "a melancholy jazz singer",
        "a banker with shady dealings",
        "an idealistic cop on the verge of a breakdown",
        "a drifter who knows too much"
    ]

    actions_np = [
        "investigating a mysterious disappearance",
        "watching a dark alley from a car",
        "interrogating a suspect under a dim light",
        "fleeing from hitmen in the night",
        "discovering compromising evidence",
        "receiving a bribe in a smoky bar",
        "hiding bundles of cash in a trunk",
        "knocking on a stranger's door in the rain",
        "writing an explosive article in an empty newsroom",
        "hiding a bloody weapon",
        "concealing a body in a car trunk",
        "following a silhouette through misty streets",
        "thwarting an ambush in an alley",
        "betraying an ally to save their own skin",
        "eavesdropping on a phone conversation",
        "being double-crossed by an accomplice",
        "witnessing a gangland hit",
        "handing over a mysterious briefcase",
        "drowning in alcohol in a deserted bar",
        "receiving an anonymous call late at night"
    ]

    lieux_np = [
        "a seedy private investigator's office",
        "a dark and rainy alleyway",
        "a smoky jazz bar",
        "a derelict warehouse on the docks",
        "a luxury apartment with a dark secret",
        "a cold and silent morgue",
        "a grimy flophouse",
        "a deserted parking lot lit by a neon sign",
        "a decrepit boxing gym",
        "a corrupt police station",
        "an underground casino",
        "a newsroom full of typewriters",
        "an exclusive club frequented by the underworld",
        "a hotel room with drawn curtains",
        "a deserted subway station",
        "a skyscraper rooftop in the rain",
        "a bourgeois house hiding secrets",
        "a mafia hideout",
        "a silent courtroom at night",
        "a dilapidated neighborhood cinema"
    ]

    vetements_np = [
        "a trench coat and a fedora hat",
        "an elegant evening dress and a pearl necklace",
        "an ill-fitting suit",
        "worn-out work clothes",
        "a police uniform",
        "a luxurious fur coat",
        "a white shirt stained with blood",
        "a faded tuxedo",
        "a bulletproof vest hidden under a jacket",
        "a rain-soaked raincoat",
        "shiny stilettos under a long coat",
        "a pinstripe three-piece suit",
        "a loosened tie",
        "a slit cocktail dress",
        "an elegant cloche hat",
        "a dark overcoat that is too large",
        "sunglasses worn at night",
        "a worn police armband",
        "black leather gloves",
        "a scarf stained with lipstick"
    ]
    
    ambiances_np = [
        "incessant heavy rain",
        "deep shadows and high contrast",
        "cigarette smoke wafting through the air",
        "distant sound of a police siren",
        "palpable tension",
        "a sense of paranoia and mistrust",
        "a heavy silence before a betrayal",
        "harsh, artificial lighting",
        "stifling heat in a windowless room",
        "a radio crackling an old jazz standard",
        "a sticky and damp atmosphere",
        "the steady sound of dripping water",
        "whispered conversations in dark corners",
        "a smoky atmosphere saturated with whiskey",
        "the dim light of an isolated lamppost",
        "a mix of desire and danger",
        "the muffled tumult of a city at night",
        "a constant impression of being followed",
        "the steady clacking of a typewriter",
        "a dramatic tension ready to explode"
    ]

    compositions_np = [
        "close-up on an anxious face",
        "wide shot of a nocturnal city",
        "low-angle shot to accentuate power",
        "silhouette outlined in a doorway",
        "reflection in a puddle",
        "dutch angle to create unease",
        "tight shot on a hand holding a weapon",
        "shot-reverse shot between two characters in conflict",
        "shadow cast on a decrepit wall",
        "lighted window in a pitch-black night",
        "view through venetian blinds",
        "focus on a compromising object",
        "blurred silhouette at the end of an alley",
        "high-angle view of a messy office",
        "dramatic backlighting in the smoke",
        "slow panoramic of a crime scene",
        "progressive zoom on a worried face",
        "static shot in a silent room",
        "asymmetric framing reinforcing the malaise",
        "tracking shot following a suspect in the street"
    ]

    details_np = [
        "a glass of whiskey on a desk",
        "a venetian blind casting striped shadows",
        "a cigarette butt crushed in an ashtray",
        "a blood stain on the sidewalk",
        "a blinking neon sign outside",
        "a black and white photo on a wall",
        "a revolver on a table",
        "a rotary phone off the hook",
        "an abandoned typewriter",
        "crumpled bills scattered on the floor",
        "a pair of half-opened handcuffs",
        "a lighter engraved with initials",
        "empty bottles lined up behind a bar",
        "a rusty key forgotten in a lock",
        "scattered playing cards",
        "a hat fallen in a puddle",
        "a crumpled letter stained with tears",
        "muddy footprints leading to a door",
        "a cracked mirror reflecting a disturbing image",
        "a curtain swaying in the draft"
    ]

    styles_np = [
        "classic film noir style (The Maltese Falcon, Double Indemnity)",
        "neo-noir aesthetic (Blade Runner, Sin City, L.A. Confidential)",
        "high contrast black and white photography",
        "German expressionist cinematography (distorted shadows, chiaroscuro)",
        "dark and pessimistic atmosphere inspired by Raymond Chandler",
        "gritty realism of the 70s",
        "French polar style (Jean-Pierre Melville, Jacques Becker)",
        "pulp aesthetic with illustrated magazine covers",
        "modern urban noir with neons and rain",
        "dramatic theatrical composition inspired by Kabuki theater",
        "minimalist and cold staging",
        "black and white graphic novel style",
        "documentary atmosphere of the underworld",
        "Hitchcockian influence, psychological suspense",
        "dark watercolors evoking nightmares",
        "50s photojournalism style",
        "gritty vintage sepia images",
        "paranoiac thriller atmosphere",
        "low-key independent cinema aesthetic",
        "stylized black ink illustration"
    ]



# --- Lists Theme: HORREUR/DARK HORREUR ---

    sujets_hd = [
        "a nightmarish creature",
        "a terrified survivor",
        "a demented cultist",
        "a vengeful ghost",
        "a mad scientist",
        "a possessed doll",
        "a shapeshifting demon",
        "a tormented defrocked priest",
        "a spectral bride",
        "a raven with glowing eyes",
        "a reanimated corpse",
        "a sinister gravedigger",
        "a witch with gnarled fingers",
        "a child with empty eyes",
        "a hungry vampire",
        "a mutilated asylum patient",
        "an exhausted monster hunter",
        "an extraterrestrial parasite",
        "a demonic nun",
        "a necromancer"
    ]

    actions_hd = [
        "fleeing an invisible threat in a dark corridor",
        "hiding in a closet while holding their breath",
        "reading a forbidden grimoire by candlelight",
        "witnessing a blasphemous ritual",
        "being hunted by a malevolent entity",
        "waking up in an unknown and macabre place",
        "slowly opening a creaking door",
        "staring at a mirror that distorts the reflection",
        "screaming silently with no one to hear",
        "descending a staircase into a damp cellar",
        "digging a grave in the middle of the night",
        "holding a flickering lantern in the mist",
        "sacrificing an animal during an occult ceremony",
        "frantically scratching at the stone walls",
        "fleeing into a forest shrouded in fog",
        "listening to a voice whispering in their head",
        "opening an ancient coffin",
        "burning herbs to ward off a demon",
        "waking up with unexplained scars",
        "struggling against rusty chains"
    ]

    lieux_hd = [
        "an abandoned asylum",
        "a haunted house atop a hill",
        "a dark and silent forest",
        "a misty cemetery at midnight",
        "a secret underground laboratory",
        "a desecrated church",
        "a dusty attic filled with spiderwebs",
        "a ruined Victorian mansion",
        "a stagnant marsh covered in fog",
        "an underground crypt infested with rats",
        "a dilapidated roadside hotel",
        "an isolated cabin in the woods",
        "an abandoned theater",
        "a creaking old mill",
        "a disused operating room",
        "a convent in ruins",
        "a deserted subway tunnel",
        "a storm-lashed lighthouse",
        "a battlefield strewn with bones",
        "an abandoned circus"
    ]

    vetements_hd = [
        "dirty and torn rags",
        "a white nightgown stained with blood",
        "a cult ceremonial robe with strange symbols",
        "bandages covering horrific wounds",
        "a soiled doctor's coat",
        "old-fashioned children's clothes",
        "a black hooded cape",
        "a bloody leather mask",
        "a yellowed asylum uniform",
        "a frayed cassock",
        "a coat soaked in rain and mud",
        "an apron stained with organs",
        "corroded ancient armor",
        "a macabre clown costume",
        "tattered funeral shrouds",
        "boots covered in mud and blood",
        "a broken rosary around the neck",
        "a yellowed bridal veil",
        "a psychiatric patient jumpsuit",
        "a mangy fur coat"
    ]
    
    ambiances_hd = [
        "near total darkness",
        "oppressive deathly silence",
        "incomprehensible whispers",
        "a feeling of being watched",
        "a flickering light",
        "an abnormal and icy cold",
        "distant and distorted laughter",
        "a smell of burning flesh",
        "thick and stifling fog",
        "heavy rain on a tin roof",
        "heartbeats echoing in the silence",
        "a constant echo of invisible footsteps",
        "incessant creaking",
        "an icy breath on the neck",
        "an oppressive sound distortion",
        "a scent of wilted flowers",
        "the irregular blinking of a light",
        "a suffocating and unhealthy heat",
        "a dull vibration from the ground",
        "a choir of inhuman voices"
    ]

    compositions_hd = [
        "extreme close-up on a terrified eye",
        "point-of-view (POV) shot of the monster",
        "threatening silhouette appearing in the distance",
        "tight framing in a confined space",
        "high-angle shot on a helpless victim",
        "distorted image as if seen through a peephole",
        "backlighting of a monstrous figure",
        "static shot on a half-open door",
        "shaky camera following a flight",
        "silhouette appearing in a mirror",
        "wide shot of a desolate landscape",
        "moving shadow cast on a wall",
        "high-angle view of an occult ritual",
        "composition centered on a ritual circle",
        "tracking shot through an endless corridor",
        "macro on a bloody object",
        "split screen between victim and executioner",
        "off-center shot reinforcing the malaise",
        "back view of a still silhouette",
        "frozen shot of a face frozen in horror"
    ]

    details_hd = [
        "scratches on the walls",
        "bloody footprints",
        "a door creaking slowly",
        "abandoned children's toys",
        "occult symbols drawn on the ground",
        "shadows that move on their own",
        "overturned candlesticks",
        "scattered bones",
        "a clock stopped at midnight",
        "chains hanging from the ceiling",
        "cracked mirrors",
        "a rusty knife stuck in the wood",
        "broken stained glass windows letting in a strange light",
        "a stained diary",
        "a barricaded door",
        "statues with distorted faces",
        "a stuffed raven covered in dust",
        "claw marks on the ground",
        "a half-open coffin",
        "thick spiderwebs"
    ]

    styles_hd = [
        "gothic horror (style of Dracula, Crimson Peak)",
        "cosmic horror (style of H.P. Lovecraft)",
        "body horror (style of David Cronenberg, The Thing)",
        "found footage (style of The Blair Witch Project, REC)",
        "psychological horror (style of The Shining, Hereditary)",
        "surreal and macabre art (style of Zdzisław Beksiński)",
        "80s slasher (style of Halloween, Friday the 13th)",
        "Japanese horror (style of Ringu, Ju-On)",
        "illustrated macabre tale",
        "German expressionist film (Nosferatu, The Cabinet of Dr. Caligari)",
        "religious horror (style of The Exorcist, The Nun)",
        "extreme gore cinema",
        "folk horror (style of The Witch, Midsommar)",
        "retro VHS aesthetic",
        "lovecraftian ink illustration",
        "dark and baroque painting",
        "post-apocalyptic horror",
        "surreal nightmare style",
        "urban nightmare aesthetic (Silent Hill)",
        "horror film noir"
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

        random_prompt = f"""Subject: {sujet} wearing {vetement}
Action: {action}
Location: {lieu}
Atmosphere/Mood: {ambiance}
Technical/Style: {composition}, {style}
Additional Detail: {details_str}"""
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

        random_prompt = f"""Subject: {sujet} wearing {vetement}
Action: {action}
Location: {lieu}
Atmosphere/Mood: {ambiance}
Technical/Style: {composition}, {style}
Additional Detail: {details_str}"""
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

        random_prompt = f"""Subject: {sujet} wearing {vetement}
Action: {action}
Location: {lieu}
Atmosphere/Mood: {ambiance}
Technical/Style: {composition}, {style}
Additional Detail: {details_str}"""
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

        random_prompt = f"""Subject: {sujet} wearing {vetement}
Action: {action}
Location: {lieu}
Atmosphere/Mood: {ambiance}
Technical/Style: {composition}, {style}
Additional Detail: {details_str}"""
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

        random_prompt = f"""Subject: {sujet} wearing {vetement}
Action: {action}
Location: {lieu}
Atmosphere/Mood: {ambiance}
Technical/Style: {composition}, {style}
Additional Detail: {details_str}"""
        return random_prompt, theme
