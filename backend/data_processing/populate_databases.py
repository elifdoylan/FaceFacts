import requests

def create_data(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        data = {}
        key = ""
        for line in lines:
            if ":" in line:
                key = line.strip()
                key = key.replace(":", "")
                data[key] = []
            else:
                data[key].append(line.strip())
        print(f'Created data from {filename}')
        print(f'Keys: {data.keys()}')
        print(f'Ingredients for each key: {data.values()}')
        return data

def populate_database(data, db):
    """
    POST Request: http://127.0.0.1:5000/ingredient

    Body:
        {
            "name": "Sample Ingredient 2",
            "isHarmful": false
            "harmfulSkin": key value
        }
    """

    for key, values in data.items():
        for value in values:
            ingredient = {
                "name": value,
                "isHarmful": True,
                "harmfulSkin": key
            }
            response = requests.post(f'http://127.0.0.1:5000/ingredient', json=ingredient)
            print(f'Posted {value} to database')
            print(response.json())

if __name__ == "__main__":
    data = create_data("data/unprocessed_data.txt")
    populate_database(data, "ingredient")
