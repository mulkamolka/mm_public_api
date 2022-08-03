import requests
import pandas as pd
import time
from typing import Dict, List
from config import API_KEY

def get_json_from_api(start_idx: int, end_idx: int) -> List[Dict]:
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
        API_URL = f'http://openapi.seoul.go.kr:8088/{API_KEY}/json/ListNecessariesPricesService/{start_idx}/{end_idx}/'
        res = requests.get(API_URL, timeout=10)

    except Exception as e:
        # logging ERROR
        print(f"{res.status_code}, requests error: {e}")
        return False

    results = res.json()
    results = results.get('ListNecessariesPricesService').get('row', [])

    return results


def save_to_csv(data: List[Dict], output_path: str) -> pd.DataFrame:
    """
    데이터를 CSV 파일로 저장하는 함수

    :param data: 수집한 딕셔너리 데이터를 저장하는 리스트
    :param output_path: csv 파일을 저장할 경로

    :return: pandas dataframe으로 변환 후 리턴
    """

    df = pd.DataFrame(data)
    df.to_csv(output_path, index=False)
    return df


def get_all_data(start: int, end: int) -> List[Dict]:

    assert start >= 1 and end <= 379194

    """
    API가 제공하는 모든 데이터를 수집하여 리스트에 저장

    :param start: 시작 인덱스
    :param end: 마지막 인덱스

    :return: 수집한 데이터 리스트
    """    
    total_data = []
    call_cnt = 0 # API 요청 횟수

    while start + 999 <= end:
        
        try:
            curr_data = get_json_from_api(start, start + 999)

            if curr_data: # 성공   
                total_data.extend(curr_data)
                print(f"{start}/{start + 999} data ingestion finished")
            else: # 실패
                print(f"{start}/{start + 999} data ingestion failed")

        except Exception as e:
            print(e)

        finally:
            call_cnt += 1
            start += 1000 # 한번에 1000개의 데이터 호출 가능
            time.sleep(2)
            print(f"----------------------------------API 요청 횟수 {call_cnt}--------------------------------------------")
    
    return total_data


if __name__ == "__main__":
    
    list_total_count = 379194
    output_path = './data/master.csv'
    data = get_all_data(1, list_total_count)
    save_to_csv(data, output_path)