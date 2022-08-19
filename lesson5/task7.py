import json


def read_table_to_dict():
    with open("files/text_7.txt", 'r', encoding="utf-8") as source_file:
        profits = []
        profit_by_company = {}
        for cells in [raw.split() for raw in source_file]:
            profit = int(cells[2]) - int(cells[3])
            profit_by_company[cells[0]] = profit
            if profit > 0:
                profits.append(profit)
        return [profit_by_company, {'average_profit': sum(profits) / len(profits)}]


def write_dict_to_json(data):
    with open("files/text_7.json", "w", encoding="utf-8") as target_file:
        json.dump(data, target_file, indent=4, ensure_ascii=False, separators=(',', ': '))


write_dict_to_json(read_table_to_dict())
