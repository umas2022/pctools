import itertools

# 属性列表
types = [
    "普通", "火", "水", "电", "草", "冰", "格斗", "毒", "地面",
    "飞行", "超能力", "虫", "岩石", "鬼", "龙", "恶", "钢", "妖精"
]

# 属性克制关系

effectiveness = {
    ("普通", "岩石"): 0.5, ("普通", "鬼"): 0, ("普通", "钢"): 0.5,
    ("火", "火"): 0.5, ("火", "水"): 0.5, ("火", "草"): 2, ("火", "冰"): 2, ("火", "虫"): 2, ("火", "岩石"): 0.5, ("火", "龙"): 0.5, ("火", "钢"): 2,
    ("水", "火"): 2, ("水", "水"): 0.5, ("水", "草"): 0.5, ("水", "地面"): 2, ("水", "岩石"): 2, ("水", "龙"): 0.5, 

    ("电", "水"): 2, ("电", "电"): 0.5, ("电", "草"): 0.5, ("电", "地面"): 0, ("电", "飞行"): 2, ("电", "龙"): 0.5, 
    ("草", "火"): 0.5, ("草", "水"): 2, ("草", "草"): 0.5, ("草", "毒"): 0.5, ("草", "地面"): 2, ("草", "飞行"): 0.5, ("草", "虫"): 0.5, ("草", "岩石"): 2, ("草", "龙"): 0.5, ("草", "钢"): 0.5,
    ("冰", "火"): 0.5, ("冰", "水"): 0.5, ("冰", "草"): 2, ("冰", "地面"): 2, ("冰", "飞行"): 2, ("冰", "龙"): 2, ("冰", "钢"): 0.5,
    ("格斗", "普通"): 2, ("格斗", "冰"): 2, ("格斗", "毒"): 0.5, ("格斗", "飞行"): 0.5, ("格斗", "超能力"): 0.5, ("格斗", "虫"): 0.5, ("格斗", "岩石"): 2, ("格斗", "鬼"): 0, ("格斗", "钢"): 2, ("格斗", "妖精"): 0.5,
    ("毒", "草"): 2, ("毒", "毒"): 0.5, ("毒", "地面"): 0.5, ("毒", "岩石"): 0.5, ("毒", "鬼"): 0.5, ("毒", "钢"): 0, ("毒", "妖精"): 2,
    ("地面", "火"): 2, ("地面", "电"): 2, ("地面", "草"): 0.5, ("地面", "毒"): 2, ("地面", "飞行"): 0, ("地面", "虫"): 0.5, ("地面", "岩石"): 2, ("地面", "钢"): 2,
    ("飞行", "电"): 0.5, ("飞行", "草"): 2, ("飞行", "格斗"): 2, ("飞行", "岩石"): 0.5, ("飞行", "钢"): 0.5,
    ("超能力", "格斗"): 2, ("超能力", "毒"): 2, ("超能力", "恶"): 0, ("超能力", "钢"): 0.5,
    ("虫", "火"): 0.5, ("虫", "格斗"): 0.5, ("虫", "毒"): 0.5, ("虫", "地面"): 0.5, ("虫", "飞行"): 0.5, ("虫", "超能力"): 2, ("虫", "鬼"): 0.5, ("虫", "钢"): 0.5, ("虫", "妖精"): 0.5,
    ("岩石", "火"): 2, ("岩石", "冰"): 2, ("岩石", "格斗"): 0.5, ("岩石", "地面"): 0.5, ("岩石", "飞行"): 2, ("岩石", "虫"): 2, ("岩石", "钢"): 0.5,

    ("鬼", "普通"): 0, ("鬼", "超能力"): 2, ("鬼", "鬼"): 2, ("鬼", "恶"): 0.5, 
    ("龙", "龙"): 2, ("龙", "钢"): 0.5, ("龙", "妖精"): 0,
    ("恶", "超能力"): 2, ("恶", "鬼"): 2, ("恶", "恶"): 0.5, ("恶", "妖精"): 0.5,
    ("钢", "火"): 0.5, ("钢", "水"): 0.5, ("钢", "电"): 0.5, ("钢", "冰"): 2, ("钢", "岩石"): 2, ("钢", "妖精"): 2,
    ("妖精", "火"): 0.5, ("妖精", "格斗"): 2, ("妖精", "毒"): 0.5, ("妖精", "龙"): 2, ("妖精", "恶"): 2, ("妖精", "钢"): 0.5,
}





# 输出属性克制表
def print_type_chart():
    print("属性克制表：")
    print("攻击属性 ↓ \\ 防御属性 →", end=" ")
    for defender in types:
        print(defender, end=" ")
    print()

    for attacker in types:
        print(attacker, end=" ")
        for defender in types:
            key = (attacker, defender)
            value = effectiveness.get(key, 1)
            print(value, end=" ")
        print()

# print_type_chart()

from typing import List, Tuple

def recommend_best_types(boss_crystal_type: str, boss_move_types: List[str], type_chart: dict, types: List[str]) -> Tuple[str, str]:
    min_damage_taken = float("inf")
    best_types = ("", "")
    
    # 生成所有可能的属性组合（包括单属性和双属性）
    possible_type_combinations = list(itertools.combinations(types, 2))
    for type1 in types:
        possible_type_combinations.append((type1,))

    for type_combination in possible_type_combinations:
        total_damage_taken = 0
        total_damage_dealt = 0

        # 计算防守效果
        for move_type in boss_move_types:
            move_effectiveness = 1
            for t in type_combination:
                move_effectiveness *= type_chart.get((move_type, t), 1)
            total_damage_taken += move_effectiveness

        # 计算攻击效果
        for t in type_combination:
            attack_effectiveness = type_chart.get((t, boss_crystal_type), 1)
            total_damage_dealt += attack_effectiveness

        # 更新最佳属性组合
        if total_damage_taken < min_damage_taken:
            min_damage_taken = total_damage_taken
            best_types = type_combination

    return best_types

# 示例：假设 Boss 的太晶属性是 "火"，技能属性分别为 "火", "水", "草", "电"
boss_crystal_type = "火"
boss_move_types = ["火", "水", "草", "电"]

best_types = recommend_best_types(boss_crystal_type, boss_move_types, effectiveness, types)
print(f"推荐的最佳属性组合：{best_types}")


