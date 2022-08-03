from flask import Flask, jsonify, Response
from config import API_KEY
from update_info import api_call

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False # 한글 인코딩 깨짐 방지

API_URL = 'http://openapi.seoul.go.kr:8088/{}/json/ListNecessariesPricesService/1/1000/'.format(API_KEY)

def save_json(output_path: str) -> bool:
    """
    # TODO
    # json 데이터를 저장하는 함수
    """
    pass
    
@app.route('/', methods=['GET'])
def api() -> Response:
    
    # 공공 api 호출
    contents = api_call(API_URL)
    
    return jsonify(contents)

if __name__ == "__main__":
    # os.system("./run_sever.sh")
    app.run(debug=True)