# -*- coding:utf-8 -*-
import logging
import requests

from retrying import retry

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def get_ua():
    try:
        from fake_useragent import UserAgent
        return {'User-Agent': UserAgent().random}
    except:
        return {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}


@retry(stop_max_attempt_number=10, wait_random_min=4000, wait_random_max=9000)
def request(url):
    logger.info(url)
    response = requests.get(url, headers=get_ua(), timeout=10)
    if response.status_code != 200:
        raise Exception('unexpected status_code %s ' % response.status_code)
    return response.json()


def get_one_page(url):
    try:
        return request(url)
    except Exception as e:
        logger.error(f'{url}\n{e}')
        return []
