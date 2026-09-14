import requests


while True:
    topic = input("Enter topic: ")

    if topic.lower() == "exit":
        print("Goodbye!")
        break

    response = requests.post(
        "http://127.0.0.1:8000/blog",
        json={"topic": topic},
    )

    print("\nResponse:")
    print(response.json())
    print("\n" + "-" * 50 + "\n")