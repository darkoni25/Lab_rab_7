import sys
import io
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
def main():
    countries = {
        "Україна": {"площа": 56000, "населення": 23100, "континент": "Європа"},
        "Єгипет": {"площа": 25000, "населення": 206000, "континент": "Африка"},
        "Китай": {"площа": 25000, "населення": 206000, "континент": "Азія"},
        "Індія": {"площа": 56000, "населення": 23100, "континент": "Азія"},
        "Нігерія": {"площа": 25000, "населення": 206000, "континент": "Африка"},
        "Німеччина": {"площа": 23100, "населення": 56000, "континент": "Європа"},
        "Японія": {"площа": 56000, "населення": 23100, "континент": "Азія"},
        "Кенія": {"площа": 25000, "населення": 206000, "континент": "Африка"},
        "Бразилія": {"площа": 56000, "населення": 23100, "континент": "Південна Америка"},
        "США": {"площа": 23100, "населення": 56000, "континент": "Північна Америка"}
    }
    def print_countries(countries_dict):
        print("\nВсі країни та їх дані:")
        for country, info in countries_dict.items():
            print(f"{country}: {info}")
    def add_country(countries_dict):
        name = input("Введіть назву країни: ").strip()
        area = int(input("Введіть площу країни: ").strip())
        population = int(input("Введіть населення країни: ").strip())
        continent = input("Введіть континент країни: ").strip()
        countries_dict[name] = {"площа": area, "населення": population, "континент": continent}
        print(f"Країну '{name}' було додано.")
    def remove_country(countries_dict):
        name = input("Введіть назву країни для видалення: ").strip()
        if name in countries_dict:
            del countries_dict[name]
            print(f"Країну '{name}' було видалено.")
        else:
            print(f"Країну '{name}' не знайдено.")
    print_countries(countries)
    while True:
        action = input("\nВведіть 'додати' для додавання країни, 'видалити' для видалення, 'список' для перегляду країн, або 'вихід' для завершення: ").strip().lower()
        if action == "додати":
            add_country(countries)
        elif action == "видалити":
            remove_country(countries)
        elif action == "список":
            print_countries(countries)
        elif action == "вихід":
            break
        else:
            print("Невірна команда, спробуйте ще раз.")
    print("\nСписок країн у алфавітному порядку:")
    for country in sorted(countries.keys()):
        print(country)
    africa_asia_countries = [country for country, info in countries.items() 
                             if info["континент"] in {"Африка", "Азія"}]
    if africa_asia_countries:
        print("\nКраїни, що знаходяться в Африці або Азії:")
        for country in africa_asia_countries:
            print("-", country)
    else:
        print("Серед заданих країн немає тих, що знаходяться в Африці або Азії.")
main()