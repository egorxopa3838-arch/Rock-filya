import random
import time
import json
import os
import atexit

SAVE_FILE = "filya_rockk_save.json"

# ===== LOAD / SAVE =====
def save_game():
    data = {
        "money": money,
        "fans": fans,
        "fame": fame,
        "guitar": guitar,
        "repertoire": repertoire,
        "location": location,
        "total_performances": total_performances,
        "perfect_games": perfect_games,
        "failures": failures,
        "albums_played": albums_played,
    }
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("💾 Saved!")


def load_game():
    global money, fans, fame, guitar, repertoire, location, total_performances, perfect_games, failures, albums_played
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        money = data.get("money", 0)
        fans = data.get("fans", 0)
        fame = data.get("fame", 0)
        guitar = data.get("guitar", "🪵 Wooden")
        repertoire = data.get("repertoire", ["🎵 Meow-meow"])
        location = data.get("location", "🏠 Yard")
        total_performances = data.get("total_performances", 0)
        perfect_games = data.get("perfect_games", 0)
        failures = data.get("failures", 0)
        albums_played = data.get("albums_played", 0)
        print("📂 Game loaded!")
    else:
        print("🆕 New game!")


atexit.register(save_game)

# ===== VARIABLES =====
money = 0
fans = 0
fame = 0
energy = 100
guitar = "🪵 Wooden"
repertoire = ["🎵 Meow-meow"]
location = "🏠 Yard"
total_performances = 0
perfect_games = 0
failures = 0
albums_played = 0


# ===== SONGS (difficulty from 0 to 1) =====
SONGS = {
    # EASY
    "🎵 Meow-meow": {
        "difficulty": 0.9, "fame": 5, "money": 100,
        "description": "⭐ Easy — a simple cat song",
        "band": "Filya",
    },
    "🎵 I'm a Kitten": {
        "difficulty": 0.8, "fame": 8, "money": 200,
        "description": "⭐⭐ Easy — a fun little song",
        "band": "Filya",
    },
    # MEDIUM
    "🎵 Paranoid (Black Sabbath)": {
        "difficulty": 0.6, "fame": 15, "money": 600,
        "description": "⭐⭐⭐ Medium — rock classic",
        "band": "Black Sabbath",
    },
    "🎵 Back in Black (AC/DC)": {
        "difficulty": 0.55, "fame": 18, "money": 700,
        "description": "⭐⭐⭐ Medium — AC/DC hit",
        "band": "AC/DC",
    },
    "🎵 Smells Like Teen Spirit (Nirvana)": {
        "difficulty": 0.5, "fame": 20, "money": 800,
        "description": "⭐⭐⭐ Medium — anthem of the 90s",
        "band": "Nirvana",
    },
    "🎵 Tail Up High": {
        "difficulty": 0.6, "fame": 12, "money": 400,
        "description": "⭐⭐⭐ Medium — rhythmic",
        "band": "Filya",
    },
    "🎵 Walk (Pantera)": {
        "difficulty": 0.45, "fame": 25, "money": 1000,
        "description": "⭐⭐⭐ Medium — Pantera groove",
        "band": "Pantera",
    },
    # HARD
    "🎵 Master of Puppets (Metallica)": {
        "difficulty": 0.3, "fame": 25, "money": 1500,
        "description": "⭐⭐⭐⭐ Hard — metal classic!",
        "band": "Metallica",
    },
    "🎵 The Trooper (Iron Maiden)": {
        "difficulty": 0.25, "fame": 35, "money": 2500,
        "description": "⭐⭐⭐⭐ Hard — Iron Maiden gallop!",
        "band": "Iron Maiden",
    },
    "🎵 Holy Wars (Megadeth)": {
        "difficulty": 0.20, "fame": 45, "money": 3500,
        "description": "⭐⭐⭐⭐ Hard — Megadeth speed!",
        "band": "Megadeth",
    },
    "🎵 Raining Blood (Slayer)": {
        "difficulty": 0.15, "fame": 60, "money": 5000,
        "description": "⭐⭐⭐⭐ Hard — thrash metal!",
        "band": "Slayer",
    },
    "🎵 Bodom After Midnight (Children of Bodom)": {
        "difficulty": 0.12, "fame": 70, "money": 6000,
        "description": "⭐⭐⭐⭐ Hard — Finnish metal!",
        "band": "Children of Bodom",
    },
    # EPIC
    "🎵 Stairway to Heaven (Led Zeppelin)": {
        "difficulty": 0.10, "fame": 80, "money": 8000,
        "description": "⭐⭐⭐⭐⭐ EPIC — 10% chance! A legend!",
        "band": "Led Zeppelin",
    },
    "🎵 Dominator (DragonForce)": {
        "difficulty": 0.05, "fame": 100, "money": 10000,
        "description": "⭐⭐⭐⭐⭐ EPIC — 5% chance! A legend!",
        "band": "DragonForce",
    },
    "🎵 Through the Fire and Flames (DragonForce)": {
        "difficulty": 0.03, "fame": 200, "money": 50000,
        "description": "⭐⭐⭐⭐⭐⭐ LEGEND — 3% chance! INCREDIBLE!",
        "band": "DragonForce",
    },
}

# ===== ALBUMS (3 songs each) =====
ALBUMS = {
    "📀 Filya — Debut": {
        "songs": ["🎵 Meow-meow", "🎵 I'm a Kitten", "🎵 Tail Up High"],
        "bonus_fame": 20,
        "bonus_money": 500,
        "description": "Filya's first album",
    },
    "📀 Rock Classics": {
        "songs": ["🎵 Paranoid (Black Sabbath)", "🎵 Back in Black (AC/DC)", "🎵 Smells Like Teen Spirit (Nirvana)"],
        "bonus_fame": 50,
        "bonus_money": 2000,
        "description": "Hits of the 70s-90s",
    },
    "📀 Metal Mania": {
        "songs": ["🎵 Master of Puppets (Metallica)", "🎵 The Trooper (Iron Maiden)", "🎵 Holy Wars (Megadeth)"],
        "bonus_fame": 100,
        "bonus_money": 8000,
        "description": "Heavy classics",
    },
    "📀 Extreme Metal": {
        "songs": ["🎵 Raining Blood (Slayer)", "🎵 Bodom After Midnight (Children of Bodom)", "🎵 Walk (Pantera)"],
        "bonus_fame": 150,
        "bonus_money": 12000,
        "description": "For true metalheads",
    },
    "📀 Legends of Speed": {
        "songs": ["🎵 Stairway to Heaven (Led Zeppelin)", "🎵 Dominator (DragonForce)", "🎵 Through the Fire and Flames (DragonForce)"],
        "bonus_fame": 300,
        "bonus_money": 50000,
        "description": "EPIC ALBUM — only for legends!",
    },
}

# ===== INSTRUMENTS =====
INSTRUMENTS = {
    "🪵 Wooden": {"price": 0, "bonus": 1},
    "🎸 Electric Guitar": {"price": 500, "bonus": 3},
    "🎸 Cool Guitar": {"price": 5000, "bonus": 10},
    "🎸 Golden Guitar": {"price": 50000, "bonus": 30},
}

# ===== LOCATIONS =====
LOCATIONS = {
    "🏠 Yard": {"fans_needed": 0, "income": 10},
    "☕ Cafe": {"fans_needed": 20, "income": 50},
    "🎤 Club": {"fans_needed": 100, "income": 200},
    "🏟️ Stadium": {"fans_needed": 1000, "income": 1000},
    "🌍 World Tour": {"fans_needed": 10000, "income": 5000},
}


# ===== DISPLAY =====
def show_status():
    print(f"\n{'=' * 50}")
    print(f"🎸 Guitar: {guitar}")
    print(f"💰 Money: {money}")
    print(f"👥 Fans: {fans}")
    print(f"⭐ Fame: {fame}")
    print(f"⚡ Energy: {energy}")
    print(f"📍 Location: {location}")
    print(f"🎵 Repertoire: {len(repertoire)} songs")
    print(f"📀 Albums played: {albums_played}")
    print(f"{'=' * 50}")


def show_repertoire():
    print("\n🎵 YOUR REPERTOIRE:")
    for i, song in enumerate(repertoire, 1):
        data = SONGS.get(song, {})
        description = data.get("description", "A regular song")
        print(f"  {i}. {song}")
        print(f"     {description}")
    print("  0. Back")


# ===== PERFORM =====
def perform():
    global money, fans, fame, energy, total_performances, perfect_games, failures

    if energy < 20:
        print("❌ Filya is tired! He needs rest!")
        return

    if not repertoire:
        print("❌ Filya has no songs! Write a song (option 5)!")
        return

    print("\n🎤 WHICH SONG TO PLAY?")
    for i, song in enumerate(repertoire, 1):
        data = SONGS.get(song, {})
        difficulty = data.get("difficulty", 0.5)
        print(f"  {i}. {song}")
        print(f"     Difficulty: {int(difficulty * 100)}% | Fame: +{data.get('fame', 5)}")

    try:
        choice = int(input("\nWhich one to play? (0 - cancel): "))
        if choice == 0:
            return
        song = repertoire[choice - 1]
    except:
        print("❌ Error!")
        return

    data = SONGS.get(song, {"difficulty": 0.5, "fame": 5, "money": 100})
    difficulty = data["difficulty"]

    print(f"\n🎤 Filya plays: {song}...")
    time.sleep(2)

    guitar_bonus = INSTRUMENTS[guitar]["bonus"]
    chance = min(0.95, difficulty + (guitar_bonus - 1) * 0.05)

    success = random.random()
    total_performances += 1

    location_income = LOCATIONS[location]["income"]
    fame_bonus = data["fame"]
    base_income = data["money"]

    if success < chance * 0.3:
        print("🎉🎉🎉 PERFECT PERFORMANCE! 🎉🎉🎉")
        income = int((base_income + location_income) * guitar_bonus * (1 + fame * 0.1))
        new_fans = random.randint(10, 30) * guitar_bonus
        money += income
        fans += new_fans
        fame += fame_bonus * 2
        perfect_games += 1
        print(f"💰 +{income} money")
        print(f"👥 +{new_fans} fans")
        print(f"⭐ +{fame_bonus * 2} fame (double!)")
        if "Dominator" in song or "Through the Fire" in song:
            print("\n🔥🔥🔥 YOU PLAYED AN EPIC PERFECTLY! 🔥🔥🔥")
            print("🏆 ACHIEVEMENT: Guitar Legend!")
    elif success < chance:
        print("🎉 SUCCESSFUL PERFORMANCE!")
        income = int((base_income + location_income) * guitar_bonus * (1 + fame * 0.1) // 2)
        new_fans = random.randint(5, 20) * guitar_bonus
        money += income
        fans += new_fans
        fame += fame_bonus
        print(f"💰 +{income} money")
        print(f"👥 +{new_fans} fans")
        print(f"⭐ +{fame_bonus} fame")
    elif success < chance + 0.15:
        print("😐 An ordinary performance")
        income = int((base_income + location_income) * guitar_bonus // 3)
        money += income
        fans += 2
        print(f"💰 +{income} money")
        print(f"👥 +2 fans")
    else:
        print("😱 FAILURE! Filya forgot the lyrics!")
        fans = max(0, fans - 10)
        failures += 1
        print(f"👥 -10 fans")

    energy -= 20


# ===== PLAY ALBUM =====
def play_album():
    global money, fans, fame, energy, total_performances, perfect_games, failures, albums_played

    if energy < 50:
        print("❌ Filya is tired! 50 energy needed!")
        return

    # filter albums where all songs are learned
    available = {}
    for name, data in ALBUMS.items():
        if all(s in repertoire for s in data["songs"]):
            available[name] = data

    if not available:
        print("❌ No albums available! Learn all the songs from an album!")
        return

    print("\n📀 AVAILABLE ALBUMS:")
    for i, (name, data) in enumerate(available.items(), 1):
        print(f"  {i}. {name}")
        print(f"     {data['description']}")
        print(f"     Songs: {', '.join(data['songs'])}")
        print(f"     Bonus: +{data['bonus_fame']} fame, +{data['bonus_money']} money")

    try:
        choice = int(input("\nWhich album? (0 - cancel): "))
        if choice == 0:
            return
        album_name = list(available.keys())[choice - 1]
    except:
        print("❌ Error!")
        return

    album = available[album_name]

    print(f"\n📀 FILYA PLAYS THE ALBUM: {album_name}")
    print("=" * 50)
    time.sleep(2)

    successful = 0
    perfect = 0

    for song in album["songs"]:
        data = SONGS[song]
        difficulty = data["difficulty"]
        guitar_bonus = INSTRUMENTS[guitar]["bonus"]
        chance = min(0.95, difficulty + (guitar_bonus - 1) * 0.05)

        print(f"\n🎵 Playing: {song}...")
        time.sleep(1)

        success = random.random()
        total_performances += 1

        if success < chance * 0.3:
            print("  🎉🎉🎉 PERFECT! 🎉🎉🎉")
            perfect += 1
            successful += 1
        elif success < chance:
            print("  🎉 Success!")
            successful += 1
        else:
            print("  😱 Failure!")
            failures += 1

    print(f"\n{'=' * 50}")
    print(f"📀 ALBUM RESULT: {successful}/{len(album['songs'])} successful, {perfect} perfect")

    if successful == len(album["songs"]):
        print("🎉🎉🎉 THE WHOLE ALBUM IS PLAYED! 🎉🎉🎉")
        bonus_money = album["bonus_money"] * INSTRUMENTS[guitar]["bonus"]
        money += bonus_money
        fans += 50 * INSTRUMENTS[guitar]["bonus"]
        fame += album["bonus_fame"]
        albums_played += 1
        print(f"💰 +{bonus_money} money (album bonus!)")
        print(f"👥 +{50 * INSTRUMENTS[guitar]['bonus']} fans")
        print(f"⭐ +{album['bonus_fame']} fame")
        print(f"🏆 ACHIEVEMENT: Album {album_name} played!")
    else:
        print(f"😐 The album wasn't played completely. Try again!")

    energy -= 50


# ===== REST =====
def rest():
    global energy
    print("\n😴 Filya is resting...")
    time.sleep(1)
    energy = min(100, energy + 50)
    print(f"⚡ Energy restored: {energy}")


# ===== SHOP =====
def shop():
    global money, guitar

    print("\n🛒 GUITAR SHOP:")
    for i, (name, data) in enumerate(INSTRUMENTS.items(), 1):
        status = "✅" if guitar == name else "💰"
        print(f"{status} {i}. {name} — {data['price']} (bonus x{data['bonus']})")
    print("0. Back")

    try:
        choice = int(input("What to buy? "))
        if choice == 0:
            return
        name = list(INSTRUMENTS.keys())[choice - 1]
        if guitar == name:
            print("✅ You already have this guitar!")
            return
        price = INSTRUMENTS[name]["price"]
        if money >= price:
            money -= price
            guitar = name
            print(f"🎸 Purchased: {name}!")
        else:
            print(f"❌ You're short {price - money} money!")
    except:
        print("❌ Error!")


# ===== CHANGE LOCATION =====
def change_location():
    global location

    print("\n📍 AVAILABLE LOCATIONS:")
    available = []
    for loc, data in LOCATIONS.items():
        if fans >= data["fans_needed"]:
            available.append(loc)
            status = "✅" if loc == location else "  "
            print(f"{status} {loc} — needs {data['fans_needed']} fans, income {data['income']}")

    print("0. Back")
    try:
        choice = int(input("Where to go? "))
        if choice == 0:
            return
        location = available[choice - 1]
        print(f"📍 Filya now performs at: {location}")
    except:
        print("❌ Error!")


# ===== LEARN SONG =====
def write_song():
    global fame, energy, repertoire

    if energy < 30:
        print("❌ Filya is tired!")
        return

    available = [s for s in SONGS.keys() if s not in repertoire]

    if not available:
        print("🎵 All songs are already in the repertoire!")
        return

    print("\n🎵 SONGS AVAILABLE TO LEARN:")
    for i, song in enumerate(available, 1):
        data = SONGS[song]
        print(f"  {i}. {song}")
        print(f"     {data['description']}")

    try:
        choice = int(input("\nWhich song to learn? (0 - cancel): "))
        if choice == 0:
            return
        song = available[choice - 1]
        data = SONGS[song]

        if random.random() < data["difficulty"]:
            repertoire.append(song)
            fame += data["fame"] // 2
            print(f"\n🎉 Filya learned: {song}!")
            print(f"⭐ +{data['fame'] // 2} fame")
        else:
            print(f"\n😓 Filya couldn't learn {song}...")
    except:
        print("❌ Error!")

    energy -= 30


# ===== STATISTICS =====
def show_statistics():
    print("\n📊 STATISTICS:")
    print(f"  🎤 Total performances: {total_performances}")
    print(f"  🎉 Perfect games: {perfect_games}")
    print(f"  ❌ Failures: {failures}")
    print(f"  📀 Albums played: {albums_played}")
    print(f"  ⭐ Fame: {fame}")
    print(f"  👥 Fans: {fans}")
    print(f"  💰 Money: {money}")
    print(f"  🎵 Songs: {len(repertoire)}/{len(SONGS)}")
    if total_performances > 0:
        print(f"  🔥 Perfect percentage: {int(perfect_games / total_performances * 100)}%")


# ===== MAIN LOOP =====
print("=" * 50)
print("   🎸 FILYA — ROCK STAR v3.0")
print("=" * 50)

load_game()

while True:
    show_status()
    print("\n1. 🎤 Perform (one song)")
    print("2. 📀 Play album (3 songs)")
    print("3. 😴 Rest")
    print("4. 🛒 Guitar shop")
    print("5. 📍 Change location")
    print("6. 🎵 Learn a song")
    print("7. 📊 Statistics")
    print("8. 📜 Repertoire")
    print("9. 💾 Save")
    print("10. 🚪 Exit")

    choice = input("\nYour choice: ").strip()

    if choice == "1":
        perform()
    elif choice == "2":
        play_album()
    elif choice == "3":
        rest()
    elif choice == "4":
        shop()
    elif choice == "5":
        change_location()
    elif choice == "6":
        write_song()
    elif choice == "7":
        show_statistics()
    elif choice == "8":
        show_repertoire()
    elif choice == "9":
        save_game()
    elif choice == "10":
        save_game()
        print(f"\n🎸 Filya earned {money} money and {fans} fans!")
        print(f"⭐ Fame: {fame}")
        print("🐱 Filya: Meow! Thank you!")
        break
    else:
        print("❌ Unknown command!")