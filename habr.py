import requests
from bs4 import BeautifulSoup

KEYWORDS = {'дизайн', 'фото', 'web', 'python'}


def get_page(url):
    ret = requests.get(url)
    page = BeautifulSoup(ret.text, 'html.parser')
    return page


def get_desired_article(page):
    posts = page.find_all('article', class_='post')

    for post in posts:
        read_more = post.find('a', class_='btn btn_x-large btn_outline_blue post__habracut-btn')
        link_post = read_more.attrs.get('href').replace('#habracut', '')
        new_page = get_page(link_post)

        post_text = new_page.find_all('div', class_='post__text post__text-html post__text_v1')

        for text in post_text:
            text_lower = set(text.text.lower().split())

            if KEYWORDS.intersection(text_lower):
                post_time = post.find('span', class_='post__time')
                title_element = post.find('a', class_='post__title_link')
                print(f'{post_time.text} - {title_element.text} - {link_post}')
                break


if __name__ == '__main__':
    get_desired_article(get_page('https://habr.com/ru/all/'))
