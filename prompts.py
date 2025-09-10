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
        "A mystical dragon", "An ancient sorcerer", "A cybernetic knight", "A rogue assassin",
        "A wise old sage", "A futuristic bounty hunter", "A dark elf", "A noble paladin",
        "A steampunk inventor", "A ghostly apparition", "A celestial being", "A shadowy figure",
        "A time-traveling adventurer", "A cursed warrior", "A mystic seer", "A fallen angel",
        "A bio-engineered creature", "A holographic entity", "A sentient robot", "A vampire lord"
    ]

    actions_hf = [
        "Casting a powerful spell", "Wielding a legendary sword", "Flying through the sky",
        "Sneaking through shadows", "Summoning a magical creature", "Fighting a horde of enemies",
        "Exploring an ancient ruin", "Riding a mythical beast", "Inventing a magical device",
        "Performing a dark ritual", "Guarding a sacred artifact", "Traveling through time",
        "Battling a fierce dragon", "Channeling cosmic energy", "Uncovering a hidden secret",
        "Leading an army into battle", "Confronting a powerful foe", "Healing a wounded ally",
        "Seeking ancient knowledge", "Protecting a vulnerable village"
    ]

    lieux_hf = [
        "A dense, enchanted forest", "A towering, ancient castle", "A futuristic, neon-lit city",
        "A haunted, abandoned mansion", "A vast, otherworldly landscape", "A bustling, steampunk market",
        "A serene, mystical lake", "A dark, underground cavern", "A floating, sky island",
        "A post-apocalyptic wasteland", "A hidden, elven sanctuary", "A grand, gothic cathedral",
        "A lush, alien jungle", "A frozen, icy tundra", "A mystical, crystal cave",
        "A war-torn battlefield", "A tranquil, hidden grove", "A bustling, space station",
        "A eerie, ghostly graveyard", "A majestic, mountain peak"
    ]

    vetements_hf = [
        "Ornate, magical robes", "Futuristic, cybernetic armor", "Dark, leather assassin gear",
        "Elegant, elven attire", "Heavy, plate mail armor", "Mystical, rune-covered cloak",
        "Steampunk, goggle-adorned outfit", "Gothic, Victorian-era dress", "Ancient, ritualistic garb",
        "Light, ethereal fabric", "Shadowy, hooded cloak", "Bio-luminescent suit", "Holographic clothing",
        "Battle-scarred armor", "Ceremonial, royal regalia", "Time-traveler's eclectic outfit",
        "Cursed, enchanted armor", "Noble, knightly attire", "Alien, exosuit", "Vampiric, elegant wear"
    ]

    ambiances_hf = [
        "Mystical and ethereal", "Dark and foreboding", "Futuristic and sleek", "Ancient and timeless",
        "Eerie and haunting", "Vibrant and otherworldly", "Gothic and moody", "Heroic and inspiring",
        "Melancholic and somber", "Chaotic and intense", "Serene and tranquil", "Majestic and awe-inspiring",
        "Apocalyptic and desolate", "Whimsical and playful", "Dramatic and tense", "Enchanting and magical",
        "Cybernetic and cold", "Mysterious and intriguing", "Grand and epic", "Shadowy and ominous"
    ]

    compositions_hf = [
        "Close-up portrait", "Wide, sweeping landscape", "Bird's-eye view", "Dramatic silhouette",
        "Symmetrical and balanced", "Dynamic and action-packed", "Isolated and focused", "Crowded and chaotic",
        "Low-angle, heroic shot", "High-angle, diminishing perspective", "Dutch angle, disorienting",
        "Rule of thirds composition", "Leading lines drawing focus", "Frame within a frame",
        "Natural framing with environment", "Deep space with atmospheric effects",
        "Shallow depth of field, subject focus", "Panoramic and expansive", "Intimate and personal",
        "Monumental and grand"
    ]

    details_hf = [
        "floating crystal shards shimmering nearby",
        "glowing arcane runes carved into walls or stones",
        "patches of strange bioluminescent fungi on surfaces",
        "wisps of spectral energy drifting through the air",
        "scattered, broken mechanical parts on the ground",
        "a small, hovering, silent observation drone",
        "puddles of iridescent, unidentifiable liquid",
        "glowing cracks in the ground revealing energy/lava",
        "ancient, weathered carvings on nearby pillars",
        "swirling motes of magical dust in the light",
        "a flickering, damaged holographic advertisement",
        "thick, metallic vines snaking across structures",
        "a small pile of bleached, unidentified bones",
        "sparking, exposed power conduits arcing occasionally",
        "intricate, floating geometric energy patterns",
        "a shimmering heat haze distorting the background",
        "clumps of rare, unusually colored exotic flowers",
        "mysterious glowing symbols painted on surfaces",
        "a small, unattended bubbling cauldron or beaker",
        "discarded, faintly glowing energy cells littered about"
    ]

    styles_hf = [
        "Dark fantasy", "Cyberpunk", "Steampunk", "High fantasy", "Gothic horror", "Science fantasy",
        "Mythological", "Post-apocalyptic", "Ethereal and dreamlike", "Heroic and epic",
        "Mystical and enchanting", "Dystopian and grim", "Alien and otherworldly", "Ancient and mystical",
        "Futuristic and sleek", "Shadowy and ominous", "Vibrant and whimsical", "Melancholic and somber",
        "Grand and majestic", "Eerie and haunting"
    ]

    Themes = [ "SF","HF" ]

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



    # Ici, vous enverriez prompt_brut à votre LLM pour l'améliorer
    # prompt_final = appeler_llm(prompt_brut)
    # return prompt_final

    return random_prompt # Pour l'instant, on retourne le prompt brut
