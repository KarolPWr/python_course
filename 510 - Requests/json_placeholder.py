import requests
import curl


def get_posts():
    response  = requests.get(f"https://jsonplaceholder.typicode.com/posts")
    return response.json()


def get_post(post_id: int):
    r = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    print(r.json())
    return r.json()


def publish_post(title, body, user_id):
    data = {
        "title": f"{title}",
        "body": f"{body}",
        "userId": f"{user_id}",
    }
    response3 = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=data
    )
    print(curl.parse(response3))


def delete_post(post_id):
    requests.delete(f"https://jsonplaceholder.typicode.com/posts/{post_id}")


def get_user_posts(user_id: int):
    # response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{user_id}/posts")
    # return response.json()
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}/posts",
    )
    assert response.status_code == 200
    response_object = response.json()
    return response_object


if __name__ == "__main__":
    get_user_posts(1)

    all_posts = get_posts()
    post_one = get_post(1)
    assert post_one == {
        'userId': 1,
        'id': 1,
        'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit',
        'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\n'
                'reprehenderit molestiae ut ut quas totam\n'
                'nostrum rerum est autem sunt rem eveniet architecto'
    }
    publish_post("title", "Lore impsum", 1)
