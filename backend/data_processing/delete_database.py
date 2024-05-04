import requests


def delete_database():
    """
    DELETE Request: http://127.0.0.1:5000/ingredient

    Body:
        {
            "id": 1
        }
    """
    # continue to delete until there are no more ingredients
    idx = 1
    while True:
        ingredient = {
            "id": idx
        }
        response = requests.delete(f'http://127.0.0.1:5000/ingredient', json=ingredient)

        if response.status_code != 200:
            print('No more ingredients to delete')
            break
        else:
            print('Deleted ingredient')
            print(response.json())
            idx += 1

if __name__ == "__main__":
    delete_database()