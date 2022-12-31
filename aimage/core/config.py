MODEL = "text-davinci-002"

TEMPERATURE = 0.9

MAX_TOKENS = 200

IMAGE_SIZE = "1024x1024"

IMAGES_COUNT = 1

CHARACTERISTICS = [
    "bizarre",
    "curious",
    "odd",
    "peculiar",
    "strange",
    "magician",
    "fairy-tale",
    "strange",
    "uncommon",
    "unfamiliar",
    "unusual",
    "weird",
    "wonderful",
]

CHARACTERS = [
    "alien",
    "angel",
    "animal",
    "ape",
    "bird",
    "cat",
    "crow",
    "dog",
    "dragon",
    "devil",
    "dwarf",
    "elf",
    "fairy",
    "feline",
    "fish",
    "giant",
    "goblin",
    "golem",
    "gorgon",
    "gryphon",
    "human",
    "hydra",
    "knight",
    "mermaid",
    "monster",
]

STYLES = [
    "abstract",
    "cartoon",
    "cubism",
    "cyberpunk",
    "digital art",
    "expressionism",
    "figurative",
    "impressionism",
    "pastel drawing",
    "pop art",
    "vaporwave",
    "watercolor",
    "woodcut"
]


ENTITIES = {
    "landscape": {
        "type": "landscape",
        "context": [
            "beach",
            "canyon",
            "cave",
            "desert",
            "forest",
            "island",
            "lake",
            "mountain",
            "ocean",
            "river",
            "valley",
            "volcano",
            "waterfall",
        ],
        "characters": (None, None, 1, 2)
    },
    "character": {
        "type": "character",
        "characters": (1, 1, 2, 2, 3)
    },
    "item": {
        "type": "item",
        "context": [
            "armor",
            "book",
            "bottle",
            "bow",
            "candle",
            "crown",
            "dagger",
            "doll",
            "manuscript",
            "mask",
            "medallion",
            "mirror",
            "orb",
            "potion",
            "ring",
            "scroll",
            "shield",
            "spear",
            "sword",
            "tome",
            "treasure",
            "wand",
            "weapon",
        ]
    }
}
