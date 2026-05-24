COFFEE_DATA = {
    "Double Espresso": {
        "caffeine": 160,
        "kaomoji": "(＠_＠;)",
        "description": "A strong choice for a tired but intense coffee personality."
    },
    "Flat White": {
        "caffeine": 140,
        "kaomoji": "(－_－) zzZ",
        "description": "A smooth but effective drink to help you wake up."
    },
    "Mocha": {
        "caffeine": 100,
        "kaomoji": "(´;ω;`)",
        "description": "A sweet and comforting drink for a low-energy mood."
    },
    "Long Black": {
        "caffeine": 120,
        "kaomoji": "இдஇ",
        "description": "Strong, but lighter than espresso. Good for focus without too much heaviness."
    },
    "Cappuccino": {
        "caffeine": 75,
        "kaomoji": "(´Ａ｀。)",
        "description": "A balanced coffee for a stressful day."
    },
    "Latte": {
        "caffeine": 70,
        "kaomoji": "(๑•́ ₃ •̀๑)",
        "description": "A gentle option for comfort and calm."
    },
    "Cold Brew": {
        "caffeine": 150,
        "kaomoji": "ヽ(●´∀`●)ﾉ",
        "description": "A strong but smooth drink for a calm and focused mood."
    },
    "Caramel Macchiato": {
        "caffeine": 75,
        "kaomoji": "(๑´ㅂ`๑)",
        "description": "A soft and cosy drink for a calm mood."
    },
    "Espresso": {
        "caffeine": 80,
        "kaomoji": "✧(•̀ᴗ•́)و",
        "description": "A quick and sharp drink for high energy."
    },
    "Iced Latte": {
        "caffeine": 75,
        "kaomoji": "٩(ˊᗜˋ*)و",
        "description": "A refreshing drink for an active mood."
    },
    "Matcha Latte": {
        "caffeine": 70,
        "kaomoji": "๑⃙⃘´༥`๑⃙⃘",
        "description": "A soft alternative for a light and positive mood."
    }
}


RECOMMENDATION_MAP = {
    ("tired", "intense"): "Double Espresso",
    ("tired", "balanced"): "Flat White",
    ("tired", "soft"): "Mocha",

    ("stressed", "intense"): "Long Black",
    ("stressed", "balanced"): "Cappuccino",
    ("stressed", "soft"): "Latte",

    ("calm", "intense"): "Cold Brew",
    ("calm", "balanced"): "Flat White",
    ("calm", "soft"): "Caramel Macchiato",

    ("energetic", "intense"): "Espresso",
    ("energetic", "balanced"): "Iced Latte",
    ("energetic", "soft"): "Matcha Latte"
}
