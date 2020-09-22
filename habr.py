import requests
from bs4 import BeautifulSoup

DESIRED_HUBS = ['дизайн', 'фото', 'web', 'python']


def get_page():
    ret = requests.get('https://habr.com/ru/all/')
    page = BeautifulSoup(ret.text, 'html.parser')
    return page


def get_desired_article(page):
    posts = page.find_all('article', class_='post')
    for post in posts:
        hubs = post.find_all('a', class_='hub-link')

        for hub in hubs:
            hub_lower = hub.text.lower()

            if any([hub_lower in desired for desired in DESIRED_HUBS]):
                post_time = post.find('span', class_='post__time')
                title_element = post.find('a', class_='post__title_link')
                print(f'{post_time.text} - {title_element.text} - {title_element.attrs.get("href")}')
                break


if __name__ == '__main__':
    get_desired_article(get_page())
