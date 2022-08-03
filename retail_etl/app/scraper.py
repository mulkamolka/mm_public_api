import os
import sys
import csv
import argparse
import requests
import pandas as pd
import time
from typing import Dict, List, Tuple
from requests_html import HTMLSession
from dotenv import load_dotenv


class PublicApiScraper:

    def __init__(self):
        self._url: str = self._set_url()
        self._prev_lastitem_idx: int = self._set_prev_lastitem_idx()
        self._curr_lastitem_idx: int = None
        self._connection: bool = False
        self._output_path: str = None


    def _set_url(self) -> None:
        """
        baseurl: API_KEY=4c63564f71726c6136384147526f4d
        BASE_URL=http://openapi.seoul.go.kr:8088/
        """
        # load .env
        load_dotenv()

        API_BASE_URL: str = os.getenv('API_BASE_URL')
        API_KEY: str = os.getenv('API_KEY')
        
        return API_BASE_URL + API_KEY + "/" + \
                    "json/" + \
                    "ListNecessariesPricesService/"
    

    def _set_prev_lastitem_idx(dirpath: str="./data"):
    
        # filepath = os.path.join(dirpath, "idx_history.csv")
        filepath = "C:/Users/l2t/Documents/GitHub/mm_public_api/retail_etl/app/data/idx_history.csv"
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                lastitem_idx = f.read() 
            return lastitem_idx

        except FileNotFoundError:
            with open(filepath, 'w', encoding='utf-8') as f:
                lastitem_idx = "0"
                f.write(lastitem_idx)
            return lastitem_idx


    def get_session(self) -> str:

        with HTMLSession() as s:
            try:
                url: str = self._url + "1/1" # 
                res = s.get(url, timeout=5)
                
                self._set_curr_lastitem_idx(res)
                self._connection = True
                return "Session Connected"

            except Exception as e:
                # logging ERROR
                print(f"{res.status_code}, requests error: {e}")
                return "Connection Error"


    def _set_curr_lastitem_idx(self, res) -> int:
        """
        현재 시점 API 호출 시 마지막 아이템 인덱스
        """
        
        results = res.json()
        self._curr_lastitem_idx: int = int(results.get('ListNecessariesPricesService').get('list_total_count'))


    def _save_lastitem_idx(self, lastitem_idx: int, dirpath: str="./data") -> None:

        """교체"""

        filepath = os.path.join(dirpath, "idx_history.csv")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(lastitem_idx)


    def _save_results_to_csv(data: List[Dict], output_path: str):
        """
        데이터를 CSV 파일로 저장하는 함수

        :param data: 수집한 딕셔너리 데이터를 저장하는 리스트
        :param output_path: csv 파일을 저장할 경로
        """

        df = pd.DataFrame(data)
        df.to_csv(output_path, index=False)


    def get_items_from_api(self, start_idx: int, end_idx: int):
        """
        공공 API에 데이터를 요청하는 함수

        예시)

        샘플 URL	생필품가격
        http://openAPI.seoul.go.kr:8088/(인증키)/xml/ListNecessariesPricesService/(시작인덱스)/(마지막인덱스)/

        :param start_idx: 요청 시작 인덱스
        :param end_idx: 요청 마지막 인덱스

        :return: 상품 정보를 담은 리스트
        """    
        try:
            if self._connection and self._url:
                url = self._url + f"{start_idx}/{end_idx}" 
                res = requests.get(url, timeout=10)

        except Exception as e:
            # logging ERROR
            print(f"{res.status_code}, requests error: {e}")
            return False

        yield res.json().get('ListNecessariesPricesService').get('row')


    def get_all_items(self, step=1000) -> List[Dict]:

        """ 
        모든 아이템을 수집하는 함수
        :param start: 시작 인덱스, default=1

        :return: 수집한 데이터 리스트
        """    
        all_items = []
        curr_idx = self._prev_lastitem_idx


        while curr_idx <= self._curr_lastitem_idx:

            items = self.get_data_from_api(curr_idx, step) # default: 1000개씩 데이터 수집
            all_items.extend(items)
            print(f"----------------------------------{curr_idx} / {self._curr_lastitem_idx} ingestion finished--------------------------------------------")

            if curr_idx + step > self._curr_lastitem_idx:
                items = self.get_data_from_api(curr_idx, self._curr_lastitem_id)
                all_items.extend(items)
                return all_items

            curr_idx = curr_idx + step
            time.sleep(2)

        return all_items


def main():


    API_KEY = os.environ.get('API_KEY')

    parser = argparse.ArgumentParser(description="공공 API 소매 데이터 수집 코드")

    # 입력받을 인자값 설정
    parser.add_argument('--start', type=int)

    # data = get_all_data(1, list_total_count)
    parser.add_argument('--end', type=int)

    # output_path

    parser.add_argument()
    ## 한번에 몇개 호출할 것인지 /1/1000
    args = parser.parse_args()
    
    args.start
    args.end
    get_json_from_api
    print(API_URL)


if __name__ == "__main__":
    main()
