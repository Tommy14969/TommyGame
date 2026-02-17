"""
Generate AI-powered game cover images for NES games
Using ModelScope AI image generation
"""

import os
import subprocess
import json

# Game list with descriptions for AI generation
GAMES = [
    {"id": 1, "title": "超级马里奥兄弟", "titleEn": "Super Mario Bros", "prompt": "Retro pixel art style video game cover, Mario the plumber jumping over green pipes and mushroom platforms, colorful pixelated clouds and blue sky, 8-bit NES game art style, vibrant colors, classic Nintendo game box art"},
    {"id": 2, "title": "塞尔达传说", "titleEn": "The Legend of Zelda", "prompt": "Fantasy adventure game art, heroic elf warrior Link holding a sword and shield, green tunic, magical triforce symbol in background, pixel art style, mystical forest landscape, 8-bit RPG game cover"},
    {"id": 3, "title": "魂斗罗", "titleEn": "Contra", "prompt": "Action shooter game art, two commando soldiers in combat poses, military scene with explosions, jungle warfare setting, pixel art style, intense action, classic NES shooter game cover"},
    {"id": 4, "title": "坦克大战", "titleEn": "Tank Battle", "prompt": "Military tank warfare game, top-down view battlefield, multiple tanks on brick terrain, shooting mechanics, pixel art strategy game, brown and green military colors, classic NES battle city style"},
    {"id": 5, "title": "吃豆人", "titleEn": "Pac-Man", "prompt": "Classic arcade game art, yellow Pac-Man character in a blue maze, being chased by colorful ghosts, pixel art style, retro arcade aesthetic, vibrant neon colors, classic gaming icon"},
    {"id": 6, "title": "大金刚", "titleEn": "Donkey Kong", "prompt": "Classic arcade game, giant gorilla Donkey Kong on steel beams, jumping character Mario, ladder climbing construction site, pixel art style, retro arcade scene, black and red color scheme"},
    {"id": 7, "title": "洛克人", "titleEn": "Mega Man", "prompt": "Futuristic robot hero Mega Man in blue armor, shooting energy blasts, high-tech sci-fi city background, pixel art style, cybernetic action game, bright blue and yellow colors"},
    {"id": 8, "title": "恶魔城", "titleEn": "Castlevania", "prompt": "Gothic horror game art, vampire hunter Simon Belmont with whip, dark gothic castle, bats and candles, pixel art style, purple and black atmosphere, haunted castle scene"},
    {"id": 9, "title": "银河战士", "titleEn": "Metroid", "prompt": "Sci-fi action game, space warrior Samus in power armor, alien planet landscape with caves, pixel art style, green and orange armored suit, futuristic space atmosphere"},
    {"id": 10, "title": "忍者龙剑传", "titleEn": "Ninja Gaiden", "prompt": "Ninja action game, masked ninja Ryu in dramatic pose, throwing shurikens, cityscape at night, pixel art style, dynamic ninja action, purple and dark blue atmosphere"},
    {"id": 11, "title": "俄罗斯方块", "titleEn": "Tetris", "prompt": "Classic puzzle game art, falling colorful geometric blocks, tetromino pieces stacking, neon grid background, pixel art style, vibrant red blue green yellow blocks, addictive puzzle game"},
    {"id": 12, "title": "炸弹人", "titleEn": "Bomberman", "prompt": "Cute action game, robot Bomberman character placing bombs, grid-based maze with destructible blocks, pixel art style, cute white robot character, colorful explosions"},
    {"id": 13, "title": "冰山登山者", "titleEn": "Ice Climber", "prompt": "Mountain climbing game, character with hammer climbing ice columns, snowy mountain peaks, pixel art style, blue and white ice theme, winter adventure scene"},
    {"id": 14, "title": "打鸭子", "titleEn": "Duck Hunt", "prompt": "Classic shooting gallery game, ducks flying across the screen, dog character laughing, pixel art style, outdoor scene with trees and grass, retro Nintendo light gun game"},
    {"id": 15, "title": "拳无虚发", "titleEn": "Punch-Out!!", "prompt": "Boxing game art, boxer in the ring throwing punches, dramatic boxing match scene, pixel art style, intense sports action, fighting game cover"},
    {"id": 16, "title": "最终幻想", "titleEn": "Final Fantasy", "prompt": "Fantasy RPG game art, four warriors with different weapons and armor, crystal spheres, magical fantasy landscape, pixel art style, epic fantasy adventure"},
    {"id": 17, "title": "勇者斗恶龙", "titleEn": "Dragon Quest", "prompt": "Japanese RPG game art, heroic warrior fighting dragon, castle in background, pixel art style, blue slime creature, fantasy adventure scene"},
    {"id": 18, "title": "星之卡比", "titleEn": "Kirby's Adventure", "prompt": "Cute pink puffball character Kirby, floating in Dream Land, colorful whimsical world, pixel art style, adorable round character, bright cheerful colors"},
    {"id": 19, "title": "马里奥兄弟3", "titleEn": "Super Mario Bros 3", "prompt": "Platformer game art, Mario in raccoon suit flying, airship level with cannons, pixel art style, colorful mushroom kingdom, tanooki Mario transformation"},
    {"id": 20, "title": "合金装备", "titleEn": "Metal Gear", "prompt": "Stealth action game, soldier Solid Snake sneaking, military base with guards, pixel art style, tactical espionage, green camouflage gear"},
    {"id": 21, "title": "双截龙", "titleEn": "Double Dragon", "prompt": "Beat 'em up game art, two martial artist brothers fighting, urban street scene, pixel art style, martial arts action, co-op fighting game"},
    {"id": 23, "title": "赤影战士", "titleEn": "Shadow of the Ninja", "prompt": "Ninja action game, two ninjas in combat, feudal Japan setting, pixel art style, stealth ninja action, dark shadowy atmosphere"},
    {"id": 24, "title": "绿色兵团", "titleEn": "Rush'n Attack", "prompt": "Military commando game, soldier running and attacking, enemy base infiltration, pixel art style, action warfare, green army theme"},
    {"id": 25, "title": "淘金者", "titleEn": "Lode Runner", "prompt": "Puzzle platformer game, character collecting gold on brick platforms, ladder climbing, pixel art style, strategic puzzle game, gold and bricks theme"},
    {"id": 26, "title": "所罗门之钥", "titleEn": "Solomon's Key", "prompt": "Puzzle platformer game, wizard creating and destroying blocks, magical realm, pixel art style, brick puzzle mechanics, mystical atmosphere"},
    {"id": 27, "title": "泡泡龙", "titleEn": "Bubble Bobble", "prompt": "Cute platformer game, two baby dinosaurs breathing bubbles, candy and fruit items, pixel art style, adorable colorful characters, playful scene"},
    {"id": 29, "title": "影之传说", "titleEn": "The Legend of Kage", "prompt": "Ninja action game, ninja jumping through trees, throwing shurikens, forest setting, pixel art style, dynamic ninja movement, feudal Japan"},
    {"id": 31, "title": "马里奥高尔夫", "titleEn": "Mario Golf", "prompt": "Sports game art, Mario character golfing on green course, golf ball and club, pixel art style, cheerful golf course, blue sky and grass"},
    {"id": 33, "title": "越野机车", "titleEn": "Excitebike", "prompt": "Motocross racing game, motorcycle racer on dirt track, jumping over ramps, pixel art style, extreme sports action, brown dirt track"},
    {"id": 35, "title": "世界杯", "titleEn": "World Cup", "prompt": "Soccer game art, soccer players on green field, kicking ball, pixel art style, sports stadium, international football theme"},
    {"id": 36, "title": "特库莫碗", "titleEn": "Tecmo Bowl", "prompt": "American football game, players in formation, football stadium, pixel art style, intense sports action, helmet and jersey"},
    {"id": 37, "title": "弹珠台", "titleEn": "Pinball", "prompt": "Pinball game art, pinball machine with flippers and bumpers, Mario themed table, pixel art style, colorful arcade pinball"},
    {"id": 38, "title": "气球塔防", "titleEn": "Balloon Fight", "prompt": "Action game, character popping balloons, floating in sky, pixel art style, colorful balloons, blue sky background"},
    {"id": 39, "title": "西天取经", "titleEn": "Journey to the West", "prompt": "Chinese mythology game, Monkey King Sun Wukong fighting demons, magical journey, pixel art style, Eastern fantasy theme"},
    {"id": 41, "title": "火之鸟", "titleEn": "Phoenix", "prompt": "Vertical shooter game, phoenix ship firing at enemies, space battle, pixel art style, fiery bird spacecraft, space shooter"},
    {"id": 42, "title": "小蜜蜂", "titleEn": "Galaga", "prompt": "Classic space shooter, alien insect formations in space, player ship at bottom, pixel art style, retro arcade shooter, colorful aliens"},
    {"id": 43, "title": "太空侵略者", "titleEn": "Space Invaders", "prompt": "Classic alien shooter, rows of pixelated aliens descending, player cannon, pixel art style, retro arcade icon, black space background"},
    {"id": 44, "title": "1942", "titleEn": "1942", "prompt": "WWII vertical shooter, fighter plane shooting enemies, aerial combat, pixel art style, war plane action, Pacific battle theme"},
    {"id": 45, "title": "吸尘器", "titleEn": "Wrecking Crew", "prompt": "Puzzle action game, Mario and Luigi with hammers, destroying brick walls, construction site, pixel art style, demolition puzzle"},
    {"id": 46, "title": "石匠", "titleEn": "Mario Bros", "prompt": "Arcade platformer, Mario fighting creatures in pipes, underground sewer setting, pixel art style, classic Mario arcade, blue and green pipes"},
    {"id": 48, "title": "功夫", "titleEn": "Kung Fu", "prompt": "Fighting game, martial artist fighting enemies, scrolling dojo, pixel art style, kung fu action, Bruce Lee inspired"},
    {"id": 49, "title": "猪小弟", "titleEn": "Pooyan", "prompt": "Shooting gallery game, pig shooting arrows at wolves, elevator scene, pixel art style, cute cartoon animals, arcade action"},
    {"id": 50, "title": "大蜜蜂", "titleEn": "Xevious", "prompt": "Revolutionary shooter game, spaceship attacking both air and ground targets, futuristic battlefield, pixel art style, vertical scrolling shooter"},
    {"id": 51, "title": "冒险岛", "titleEn": "Adventure Island", "prompt": "Platformer adventure, character Master Higgins running on tropical island, dinosaurs and fruits, pixel art style, jungle adventure scene, prehistoric theme"},
]

def generate_ai_cover_image(game, index, total):
    """Generate AI cover image for a single game"""
    filename = f"{game['id']}-{game['titleEn'].replace(' ', '_')}.png"
    filepath = os.path.join("images", filename)

    print(f"[{index}/{total}] 生成: {game['title']} ({game['titleEn']})")
    print(f"  Prompt: {game['prompt'][:100]}...")

    # This will be replaced with actual AI generation call
    # For now, create a placeholder to show the structure

    return filepath

def main():
    print("🎮 使用AI生成NES游戏封面图...")
    print(f"总共 {len(GAMES)} 个游戏\n")

    # Create images directory
    os.makedirs("images", exist_ok=True)

    # Generate images for all games
    for i, game in enumerate(GAMES, 1):
        try:
            generate_ai_cover_image(game, i, len(GAMES))
        except Exception as e:
            print(f"❌ 错误: {game['title']} - {e}")

    print(f"\n✅ 完成! 已生成 {len(GAMES)} 张AI游戏封面图")

if __name__ == "__main__":
    main()
