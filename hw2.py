#hw 2_1
user = {"registered" : True,
        "user_name" : "VinniPooh",
        "password" : "Pyatach0k",
        "user_lvl" : "advanced"}
print(user)
sentence = {"user_lvl" : "advanced",
            "number_of_sentences" : 1,
            "word" : "word",
            "text" : "Sentence with my word"}
print(sentence)
print("--------------------------------------------")

#hw 2_2
#meganagibator_stats
player = {"name" : "Elf_Ranger",
          "lvl" : 54,
          "str" : 4,
          "dex" : 9,
          "con" : 6}
player_stats = {"attack" : player.get("str")*3,
                "crt_chance" : player.get("dex")*3,
                "hp" : player.get("con")*10}
armor_info = {"name" : "Elf light armor",
              "meel_def" : 40,
              "range_def" : 60,
              "mag_def" : 0,
              "evasion" : 30}
meel_weapon_info = {"name" : "War mace",
                    "pierce" : 5,
                    "min_dmg" : 12,
                    "max_dmg" : 20,
                    "mag_dmg" : False,
                    "crt_chance" : 10,
                    "crt_rate" : 1.5,
                    "type" : "blunt"}
range_weapon_info =  {"name" : "Elf translator",
                      "pierce" : 30,
                      "min_dmg" : 16,
                      "max_dmg" : 32,
                      "mag_dmg" : False,
                      "crt_chance" : 40,
                      "crt_rate" : 2.5,
                      "type" : "long bow"}
print(player)
print("--------------------------------------------")

#hw 2_3
player_info = {"name" : "Elf_Ranger",
                "lvl" : 54,
                "str" : 4,
                "dex" : 9,
                "con" : 6,
                "attack" : player["str"]*3,
                "crt_chance" : player["dex"]*3,
                "hp" : player["con"]*10,
                "armor" : {"name" : "Elf light armor",
                           "meel_def" : 40,
                           "range_def" : 60,
                           "mag_def" : 0,
                           "evasion" : 30},
                "weapons" :  {"weapon1" : meel_weapon_info,
                              "weapon2" : {"name" : range_weapon_info["name"],
                                           "pierce" : range_weapon_info["pierce"],
                                           "min_dmg" : range_weapon_info["min_dmg"],
                                           "max_dmg" : range_weapon_info["max_dmg"],
                                           "mag_dmg" : range_weapon_info["mag_dmg"],
                                           "crt_chance" : range_weapon_info["crt_chance"],
                                           "crt_rate" : range_weapon_info["crt_rate"],
                                           "type" : range_weapon_info["type"]}
                                }
                }
print(player_info)