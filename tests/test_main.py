import pytest
from typing import List, Tuple

def test_difference():
    numbers = [1, 2, 3, 4]
    result = [numbers[i] - numbers[i+1] for i in range(0, len(numbers), 2)]
    assert result == [-1, -1]

def test_student_info():
    names = ["Ali", "Vali"]
    scores = [90, 80]
    result = [f"{name} — {score} ball" for name, score in zip(names, scores)]
    assert result == ["Ali — 90 ball", "Vali — 80 ball"]

def test_discounted_price():
    prices = [100, 200]
    discounts = [10, 20]
    result = [price * (1 - discount / 100) for price, discount in zip(prices, discounts)]
    assert result == [90.0, 160.0]

def test_coordinate_sum():
    coordinates = [(1, 2), (3, 4)]
    result = [x + y for x, y in coordinates]
    assert result == [3, 7]

def test_string_formatting():
    strings = ["hello", "world"]
    lengths = [5, 10]
    result = [s.ljust(length) for s, length in zip(strings, lengths)]
    assert result == ["hello", "world     "]

def test_age_string():
    people = [("Ali", 25), ("Vali", 30)]
    result = [f"{name} {age} yoshda" for name, age in people]
    assert result == ["Ali 25 yoshda", "Vali 30 yoshda"]

def test_area():
    lengths = [10, 20]
    widths = [5, 10]
    result = [length * width for length, width in zip(lengths, widths)]
    assert result == [50, 200]

def test_backup_name():
    file_names = ["file1.txt", "file2.txt"]
    result = [name + ".bak" for name in file_names]
    assert result == ["file1.txt.bak", "file2.txt.bak"]

def test_dict_from_lists():
    keys = ["a", "b"]
    values = [1, 2]
    result = dict(zip(keys, values))
    assert result == {"a": 1, "b": 2}

def test_temperature_string():
    temperatures = [25, 30]
    cities = ["Tashkent", "Samarkand"]
    result = [f"{city}: {temp}.0 °C (Farengeyt: {(temp * 9/5) + 32:.1f} °F)" for city, temp in zip(cities, temperatures)]
    assert result == ["Tashkent: 25.0 °C (Farengeyt: 77.0 °F)", "Samarkand: 30.0 °C (Farengeyt: 86.0 °F)"]

def test_average():
    nested_list = [[1, 2, 3], [4, 5], [6]]
    result = [sum(inner_list) / len(inner_list) for inner_list in nested_list]
    assert result == [2.0, 4.5, 6.0]

def test_username():
    names = ["ali", "vali"]
    result = [f"@{name}_user" for name in names]
    assert result == ["@ali_user", "@vali_user"]

def test_product():
    numbers = [1, 2, 3, 4]
    result = [(numbers[i] * numbers[i+1]) / 10 for i in range(0, len(numbers), 2)]
    assert result == [0.2, 0.6]

def test_text_formatting():
    texts = ["hello123", "world456"]
    result = ["".join(filter(str.isalpha, text)).upper() for text in texts]
    assert result == ["HELLO", "WORLD"]

def test_rgb_to_hex():
    rgb_values = [(255, 0, 0), (0, 255, 0)]
    result = [f"#{r:02x}{g:02x}{b:02x}" for r, g, b in rgb_values]
    assert result == ["#ff0000", "#00ff00"]

def test_word_frequency():
    words = ["apple", "banana", "apple"]
    frequencies = [2, 1]
    result = [f"{word} ({frequency} marta)" for word, frequency in zip(words, frequencies)]
    assert result == ["apple (2 marta)", "banana (1 marta)"]

def test_element_type():
    elements = [1, "hello", 2.5]
    result = [type(element).__name__ for element in elements]
    assert result == ["int", "str", "float"]

def test_url_protocol():
    urls = ["https://example.com", "http://example.org"]
    result = [url.split("://")[0] for url in urls]
    assert result == ["https", "http"]

def test_grade():
    scores = [90, 80, 70]
    result = ["A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F" for score in scores]
    assert result == ["A", "B", "C"]

def test_full_name():
    first_names = ["Ali", "Vali"]
    last_names = ["Ivanov", "Petrov"]
    result = [f"{last_name}, {first_name}" for first_name, last_name in zip(first_names, last_names)]
    assert result == ["Ivanov, Ali", "Petrov, Vali"]

def test_bmi():
    weights = [70, 80]
    heights = [1.7, 1.8]
    result = [weight / (height ** 2) for weight, height in zip(weights, heights)]
    assert result == [24.22, 24.69]

def test_title_case():
    strings = ["hello world", "python programming"]
    result = [s.title() for s in strings]
    assert result == ["Hello World", "Python Programming"]

def test_max_element():
    nested_list = [[1, 2, 3], [4, 5], [6]]
    result = [max(inner_list) for inner_list in nested_list]
    assert result == [3, 5, 6]

def test_stock_status():
    product_names = ["Product1", "Product2"]
    stock_quantities = [5, 15]
    result = ["Kam stok" if quantity < 10 else "Normal" for quantity in stock_quantities]
    assert result == ["Kam stok", "Normal"]

def test_sum_of_squares():
    a = [1, 2]
    b = [3, 4]
    result = [x**2 + y**2 for x, y in zip(a, b)]
    assert result == [10, 20]

def test_domain_name():
    email_addresses = ["ali@example.com", "vali@example.org"]
    result = [address.split("@")[1] for address in email_addresses]
    assert result == ["example.com", "example.org"]

def test_digit_sum():
    numbers = [123, 456]
    result = [sum(int(digit) for digit in str(number)) for number in numbers]
    assert result == [6, 15]

def test_average_score():
    scores = [("Ali", 90, 80), ("Vali", 70, 60)]
    result = [(name, (score1 + score2) / 2) for name, score1, score2 in scores]
    assert result == [("Ali", 85.0), ("Vali", 65.0)]

def test_reversed_string():
    strings = ["hello", "world"]
    result = [s[::-1] + "!" for s in strings]
    assert result == ["olleh!", "dlrow!"]

def test_total_cost():
    prices = [10, 20]
    quantities = [2, 3]
    result = [price * quantity for price, quantity in zip(prices, quantities)]
    assert result == [20, 60]

def test_clamped_number():
    numbers = [150, -50]
    result = [min(100, max(0, number)) for number in numbers]
    assert result == [100, 0]

def test_name_length():
    names = ["Ali", "Alexander"]
    result = ["Qisqa ism" if len(name) < 10 else "Uzun ism" for name in names]
    assert result == ["Qisqa ism", "Uzun ism"]

def test_circle_area():
    coordinates = [(1, 2), (3, 4)]
    radii = [5, 10]
    result = [3.14 * radius ** 2 for radius in radii]
    assert result == [78.5, 314.0]

def test_space_count():
    strings = ["hello world", "python programming"]
    result = [s.count(" ") for s in strings]
    assert result == [1, 1]

def test_event_string():
    years = [2020, 2021]
    events = ["Event1", "Event2"]
    result = [f"{year} — {event}" for year, event in zip(years, events)]
    assert result == ["2020 — Event1", "2021 — Event2"]

def test_binary_number():
    numbers = [10, 20]
    result = [bin(number)[2:] for number in numbers]
    assert result == ["1010", "10100"]

def test_name_and_age():
    people = [{"name": "Ali", "age": 25}, {"name": "Vali", "age": 30}]
    result = [(person["name"], person["age"]) for person in people]
    assert result == [("Ali", 25), ("Vali", 30)]

def test_vowel_replacement():
    strings = ["hello", "world"]
    result = ["".join("*" if char in "aeiou" else char for char in s) for s in strings]
    assert result == ["h*ll*", "w*rld"]

def test_power():
    numbers = [2, 3]
    powers = [2, 3]
    result = [number ** power for number, power in zip(numbers, powers)]
    assert result == [4, 27]

def test_file_name():
    file_paths = ["/path/to/file1.txt", "/path/to/file2.txt"]
    result = [path.split("/")[-1] for path in file_paths]
    assert result == ["file1.txt", "file2.txt"]

def test_normalized_score():
    scores = [90, 80]
    result = [score / 10 for score in scores]
    assert result == [9.0, 8.0]

def test_title():
    names = ["Ali", "Vali"]
    genders = ["male", "female"]
    result = [f"Mr. {name}" if gender == "male" else f"Ms. {name}" for name, gender in zip(names, genders)]
    assert result == ["Mr. Ali", "Ms. Vali"]

def test_product_of_tuple():
    tuples = [(1, 2, 3), (4, 5, 6)]
    result = [t[0] * t[1] * t[2] for t in tuples]
    assert result == [6, 120]

def test_text_length():
    strings = ["hello", "hello world", "hello world again"]
    result = ["Qisqa" if len(s.split()) < 3 else "O‘rta" if len(s.split()) < 5 else "Uzun" for s in strings]
    assert result == ["Qisqa", "O‘rta", "Uzun"]

def test_gcd():
    numbers = [12, 15]
    result = [gcd(numbers[0], numbers[1])]
    assert result == [3]

def test_color_string():
    colors = ["red", "green"]
    rgb_values = [(255, 0, 0), (0, 255, 0)]
    result = [f"{color}: ({rgb[0]},{rgb[1]},{rgb[2]})" for color, rgb in zip(colors, rgb_values)]
    assert result == ["red: (255,0,0)", "green: (0,255,0)"]

def test_nearest_odd():
    numbers = [10, 20]
    result = [number + 1 if number % 2 == 0 else number for number in numbers]
    assert result == [11, 21]

def test_unicode_code():
    strings = ["hello", "world"]
    result = [ord(char) for s in strings for char in s]
    assert result == [104, 101, 108, 108, 111, 119, 111, 114, 108, 100]

def test_duration():
    start_times = [10, 20]
    end_times = [15, 25]
    result = [end - start for start, end in zip(start_times, end_times)]
    assert result == [5, 5]

def test_user_info():
    users = [["Ali", "Ivanov", 25], ["Vali", "Petrov", 30]]
    result = [f"{user[1]} {user[0]} — {user[2]} yosh" for user in users]
    assert result == ["Ivanov Ali — 25 yosh", "Petrov Vali — 30 yosh"]

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
