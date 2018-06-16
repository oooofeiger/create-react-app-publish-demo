from flask import Flask, request, abort
from flask import jsonify
from flask_cors import *

app = Flask(__name__)
# CORS(app, supports_credentials=True)

"""
http://127.0.0.1:3000/api/list?page_number=1
http://127.0.0.1:5000/api/baseInfo?key=sdfsdfyhut478h654j
http://127.0.0.1:5000/api/showInvest?key=sdfsdfyhut478h654j
"""

@app.route('/api/list')
def list_info():
    # try:
    obj = {"name": "上海嘉定公路建设发展有限公司", "type": "有限责任公司(自然人投资或控股)",
           "scope": "塑料制品制造、加工", "establishTime": "2007-03-23",
           "conCapital": "60万人民币元", "regCapital": "60万人民币元", "status": "存续"}
    items = []
    for i in range(20):
        items.append(obj)

    page_number = request.args.get('page_number')
    if page_number:
        try:
            page_number = int(page_number)
        except TypeError:
            abort(404)
        return jsonify(items)
    else:
        abort(404)


@app.route('/api/baseInfo')
def base_info():
    key = request.args.get('key')
    if key:
        dic = {"base": {"公司名称": "上海嘉定公路建设发展有限公司", "公司类型": "有限责任公司(自然人投资或控股)",
                        "经营范围": "塑料制品制造、加工", "成立日期": "2007-03-23",
                        "登记机关": "象山县市场监督管理局", "曾用名": "-", "企业地址": "浙江省象山县茅洋乡白岩下村",
                        "核准日期": "2016-12-06", "实缴资本": "60万人民币元", "注册资本": "60万人民币元", "法人": "胡明良",
                        "所属地区": "浙江省", "注册号": "330225000054995", "纳税人识别号": "913302257995213595",
                        "统一社会信用代码": "913302257995213595", "法人链接": "/pl_p62db6b6e680727795abfdd8a4409d92.html",
                        "英文名": "-", "营业期限": "2007-03-23 至 无固定期限", "人员规模": "-", "所属行业": "制造业",
                        "经营方式": "-", "组织机构代码": "79952135-9", "经营状态": "存续"},
               "gudong": [
                    {"number": "1", "name": "第一拖拉机股份有限公司", "rate": "51.00%", "money": "1020", "date": "-"},
                    {"number": "2", "name": "黑龙江省农业机械有限责任公司", "rate": "49.00%", "money": "980", "date": "-"}
               ],
               "employ": [
                   {"number": "1", "name": "尚书志", "duty": "董事"},
                   {"number": "2", "name": "詹灵芝", "duty": "监事"},
                   {"number": "3", "name": "程怀远", "duty": "总经理"},
                   {"number": "4", "name": "李秀林", "duty": "董事长"},
               ],
               "branches": [
                   {"number": "1", "name": "广发证券股份有限公司东莞东城证券营业部"},
                   {"number": "2", "name": "广发证券股份有限公司北京广安门内大街证券营业部"},
                   {"number": "3", "name": "广发证券股份有限公司清远英德浈阳东路证券营业部"},
               ]
               }
        return jsonify(dic)
    else:
        abort(404)


@app.route('/api/showInvest')
def img_show():
    key = request.args.get('key')
    if key:
        dic ={
        	"success": {
        		"results": [{
        			"columns": ["value"],
        			"data": [{
        				"graph": {
        					"nodes": [{
        						"id": "30841307",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "8aca3b9c9b79671b6d221dba30cbfa3b",
        							"registCapi": "350000.0",
        							"name": "美的金融控股(深圳)有限公司",
        							"econKind": "有限责任公司（法人独资）",
        							"status": "存续"
        						}
        					}, {
        						"id": "51868419",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "e9037d8318f7d6893f82f580e9e9fc1b",
        							"registCapi": "34596.0",
        							"name": "北京新尚品科技发展有限公司",
        							"econKind": "有限责任公司(中外合资)",
        							"status": "在业"
        						}
        					}, {
        						"id": "23304514",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "69369eb97345e2e5185b7368de945ab4",
        							"registCapi": "19804.8",
        							"name": "珠海金山数码科技有限公司",
        							"econKind": "有限责任公司(台港澳法人独资)",
        							"status": "存续"
        						}
        					}, {
        						"id": "16648410",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "4b652402737f0d7d60271115cff33a58",
        							"registCapi": "2326.9958",
        							"name": "上海商米科技有限公司",
        							"econKind": "有限责任公司（自然人投资或控股）",
        							"status": "存续"
        						}
        					}, {
        						"id": "10336442",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "2ed06d06417125305330740513a5fb63",
        							"registCapi": "0.0",
        							"name": "天津玖米企业管理合伙企业(有限合伙)",
        							"econKind": "有限合伙企业",
        							"status": "存续"
        						}
        					}, {
        						"id": "29841901",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "864fa2bf79d4c90a2f81928edd07c643",
        							"registCapi": "10000.0",
        							"name": "广州华多网络科技有限公司",
        							"econKind": "其他有限责任公司",
        							"status": "存续"
        						}
        					}, {
        						"id": "781373",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "03908d14e1694b39654862a1ad894e37",
        							"registCapi": "5000.0",
        							"name": "重庆美的制冷设备有限公司",
        							"econKind": "有限责任公司",
        							"status": "存续"
        						}
        					}, {
        						"id": "102647336",
        						"labels": ["Person"],
        						"properties": {
        							"keyNo": "p843138812fbff4fef920653cdfd970b",
        							"role": "",
        							"name": "方洪波"
        						}
        					}, {
        						"id": "34862636",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "9cce0780ab7644008b73bc2120479d31",
        							"registCapi": "185000.0",
        							"name": "小米科技有限责任公司",
        							"econKind": "有限责任公司(自然人投资或控股)",
        							"status": "在业"
        						}
        					}, {
        						"id": "84306247",
        						"labels": ["Person"],
        						"properties": {
        							"keyNo": "p4c25ab66114eb92232de453dfcc05c1",
        							"role": "董事",
        							"name": "刘芹"
        						}
        					}, {
        						"id": "38347294",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "ac66f9d18c12d884e23b7c83bbad1c6b",
        							"registCapi": "3000.0",
        							"name": "北京顺为创业投资有限公司",
        							"econKind": "有限责任公司(自然人投资或控股)",
        							"status": "在业"
        						}
        					}, {
        						"id": "15868072",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "47ea1501769cfab0a28bfc0971d60db0",
        							"registCapi": "200000.0",
        							"name": "佛山市美的日用家电集团有限公司",
        							"econKind": "有限责任公司(法人独资)",
        							"status": "注销"
        						}
        					}, {
        						"id": "6564926",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "1dac5c8be14a5cf94a4c6ca3ae4876d3",
        							"registCapi": "1000.0",
        							"name": "上海汉涛信息咨询有限公司",
        							"econKind": "有限责任公司（自然人投资或控股）",
        							"status": "存续"
        						}
        					}, {
        						"id": "1481843",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "06c739fdd7af2d3a52139a939196165f",
        							"registCapi": "50.0",
        							"name": "深圳英鹏玩聚互娱科技有限公司",
        							"econKind": "有限责任公司",
        							"status": "注销"
        						}
        					}, {
        						"id": "20919641",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "5e965bd7f9fc0560d474efed6710bcff",
        							"registCapi": "1000.0",
        							"name": "上海兴畔投资管理咨询有限公司",
        							"econKind": "有限责任公司（自然人投资或控股）",
        							"status": "存续"
        						}
        					}, {
        						"id": "42704608",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "bfeb8fa5f2ef0a07606c0a7aa4253621",
        							"registCapi": "8000.0",
        							"name": "邯郸美的制冷设备有限公司",
        							"econKind": "其他有限责任公司",
        							"status": "存续"
        						}
        					}, {
        						"id": "31039917",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "8bae20d34ab99d9f07d046caa4d422d3",
        							"registCapi": "120000.0",
        							"name": "天津金星投资有限公司",
        							"econKind": "有限责任公司(法人独资)",
        							"status": "存续"
        						}
        					}, {
        						"id": "9097458",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "29328112375d07205ab125dcb575d59b",
        							"registCapi": "1000.0",
        							"name": "图扑尚贸易(上海)有限公司",
        							"econKind": "有限责任公司（自然人投资或控股）",
        							"status": "存续"
        						}
        					}, {
        						"id": "26798560",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "78bd7f41ad3bd438e8b63e2a2b5ae644",
        							"registCapi": "1135.9266",
        							"name": "舒可士(深圳)科技有限公司",
        							"econKind": "有限责任公司（台港澳与境内合资）外资比例低于25%",
        							"status": "存续"
        						}
        					}, {
        						"id": "17559925",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "4f767dcd1ae6ac59ded93351164a841a",
        							"registCapi": "25.0",
        							"name": "深圳超好玩互动娱乐企业(有限合伙)",
        							"econKind": "合伙企业",
        							"status": "存续"
        						}
        					}, {
        						"id": "25368839",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "72654c80c53f506443a8d741ad354a2b",
        							"registCapi": "1000.0",
        							"name": "成都西山居世游科技有限公司",
        							"econKind": "有限责任公司（自然人投资或控股的法人独资）",
        							"status": "存续"
        						}
        					}, {
        						"id": "16152702",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "492ed301d569a5e1c5e37560b8887cb5",
        							"registCapi": "0.0",
        							"name": "拉萨经济技术开发区顺为科技创业投资合伙企业(有限合伙)",
        							"econKind": "有限合伙企业",
        							"status": "存续"
        						}
        					}, {
        						"id": "47698527",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "d64da78333777354bf3634e371d736a6",
        							"registCapi": "0.0",
        							"name": "上海晨熹创业投资中心(有限合伙)",
        							"econKind": "有限合伙企业",
        							"status": "存续"
        						}
        					}, {
        						"id": "6015168",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "1b2cd9e9cae92579e2467c1973877730",
        							"registCapi": "207100.1956",
        							"name": "北京小米电子软件技术有限公司",
        							"econKind": "有限责任公司(自然人投资或控股)",
        							"status": "在业"
        						}
        					}, {
        						"id": "24465896",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "6e62fda57887baa0909cb79bef96b07c",
        							"registCapi": "5000.0",
        							"name": "小米影业有限责任公司",
        							"econKind": "有限责任公司(自然人投资或控股)",
        							"status": "在业"
        						}
        					}, {
        						"id": "101372578",
        						"labels": ["Person"],
        						"properties": {
        							"keyNo": "p804a400c7a446c6eb28cfa455ffc91f",
        							"role": "",
        							"name": "张震阳"
        						}
        					}, {
        						"id": "101171886",
        						"labels": ["Person"],
        						"properties": {
        							"keyNo": "p7fad99cad9ca21f528b59e0905eaeb5",
        							"role": "自然人股东",
        							"name": "林军"
        						}
        					}, {
        						"id": "26802477",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "78c200dd24178853e4a985d918c6bc2e",
        							"registCapi": "500000.0",
        							"name": "中央汇金资产管理有限责任公司",
        							"econKind": "有限责任公司(法人独资)",
        							"status": "在业"
        						}
        					}, {
        						"id": "95221018",
        						"labels": ["Person"],
        						"properties": {
        							"keyNo": "p6d7e0b8f1d5f085cef08c25afc20309",
        							"role": "董事",
        							"name": "刘德"
        						}
        					}, {
        						"id": "111494674",
        						"labels": ["Person"],
        						"properties": {
        							"keyNo": "p9f4717323a4b8cb7fd8488942d4ab96",
        							"role": "董事长",
        							"name": "邹涛"
        						}
        					}, {
        						"id": "121297792",
        						"labels": ["Person"],
        						"properties": {
        							"keyNo": "pbd53dfed80ff7ab8f71898c13c960cf",
        							"role": "监事",
        							"name": "杨勇"
        						}
        					}, {
        						"id": "657610",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "02ff6e6bed57a655db1bc67dfa829984",
        							"registCapi": "100000.0",
        							"name": "广东小米科技有限责任公司",
        							"econKind": "有限责任公司(法人独资)",
        							"status": "存续"
        						}
        					}, {
        						"id": "61964144",
        						"labels": ["Person"],
        						"properties": {
        							"keyNo": "p081b609f81220f87cd46edbd7b9f022",
        							"role": "董事",
        							"name": "尚进"
        						}
        					}, {
        						"id": "17222095",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "4df48f20fd5c568ec641748320400fcf",
        							"registCapi": "200.0",
        							"name": "成都西米互动科技有限公司",
        							"econKind": "其他有限责任公司",
        							"status": "存续"
        						}
        					}, {
        						"id": "101181150",
        						"labels": ["Person"],
        						"properties": {
        							"keyNo": "p7fb4c0e31a086dcdb3127571632ef31",
        							"role": "自然人股东",
        							"name": "谢阗地"
        						}
        					}, {
        						"id": "17917391",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "510e52c6f0b95cfb1aaea63bbca6d7dd",
        							"registCapi": "150.0",
        							"name": "北京金山奇剑数码科技有限公司",
        							"econKind": "有限责任公司(自然人投资或控股)",
        							"status": "在业"
        						}
        					}, {
        						"id": "26278264",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "766f04948eaedb5aeedbe2775266ed82",
        							"registCapi": "30000.0",
        							"name": "广东美的暖通设备有限公司",
        							"econKind": "其他有限责任公司",
        							"status": "存续"
        						}
        					}, {
        						"id": "130712376",
        						"labels": ["Person"],
        						"properties": {
        							"keyNo": "pda37a1557f8fe342fb47f7015b31b23",
        							"role": "负责人",
        							"name": "曲德君"
        						}
        					}, {
        						"id": "36973248",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "a63fcd4a4ae1ff0610a1991a821621ec",
        							"registCapi": "100.0",
        							"name": "西藏紫米通讯技术有限公司",
        							"econKind": "有限责任公司（非自然人投资或控股的法人独资）",
        							"status": "存续"
        						}
        					}, {
        						"id": "52260843",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "eac35f7cb2922037a2f7e0525d8cf0cb",
        							"registCapi": "658402.2574",
        							"name": "美的集团股份有限公司",
        							"econKind": "股份有限公司(上市、自然人投资或控股)",
        							"status": "存续"
        						}
        					}, {
        						"id": "16967162",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "4cd1d517db1980efb0e0186c382c6ee9",
        							"registCapi": "199.0",
        							"name": "北京太火红鸟科技有限公司",
        							"econKind": "有限责任公司(自然人投资或控股)",
        							"status": "在业"
        						}
        					}, {
        						"id": "94456",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "006f4aa686287cb359b449ce6ce347d1",
        							"registCapi": "200000.0",
        							"name": "四川银米科技有限责任公司",
        							"econKind": "有限责任公司（非自然人投资或控股的法人独资）",
        							"status": "存续"
        						}
        					}, {
        						"id": "52156389",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "ea4c0091715e60a24ba890282d026c6d",
        							"registCapi": "5000.0",
        							"name": "美的创新投资有限公司",
        							"econKind": "有限责任公司",
        							"status": "存续"
        						}
        					}, {
        						"id": "31098074",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "8bf10fde18745810db9ab3e5856746af",
        							"registCapi": "1000.0",
        							"name": "江苏紫米软件技术有限公司",
        							"econKind": "有限责任公司（法人独资）",
        							"status": "在业"
        						}
        					}, {
        						"id": "17083398",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "4d55c4c5d375cfc2adf70601ae7004b6",
        							"registCapi": "1000.0",
        							"name": "佛山市顺德区美的电子科技有限公司",
        							"econKind": "有限责任公司(自然人投资或控股)",
        							"status": "存续"
        						}
        					}, {
        						"id": "27382946",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "7b56d0143ada62ce06989e7c31e98497",
        							"registCapi": "38.5154",
        							"name": "北京拜克洛克科技有限公司",
        							"econKind": "其他有限责任公司",
        							"status": "在业"
        						}
        					}, {
        						"id": "38566723",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "ad622acd512e8f07fb287627b6901a7d",
        							"registCapi": "100.0",
        							"name": "西藏小米科技有限责任公司",
        							"econKind": "有限责任公司（自然人投资或控股的法人独资）",
        							"status": "注销"
        						}
        					}, {
        						"id": "53670436",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "f1141d6decb76ff22e70e5f8b656b68c",
        							"registCapi": "2700.0",
        							"name": "北京小米电子产品有限公司",
        							"econKind": "有限责任公司(台港澳法人独资)",
        							"status": "在业"
        						}
        					}, {
        						"id": "41428834",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "ba32be3a579bd641ca7c48b019462b8b",
        							"registCapi": "2750.5817",
        							"name": "上海迈外迪网络科技有限公司",
        							"econKind": "有限责任公司（自然人投资或控股）",
        							"status": "存续"
        						}
        					}, {
        						"id": "14890432",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "438f6b1882f44c8aa2adb2887229456f",
        							"registCapi": "10000.0",
        							"name": "成都金山互动娱乐科技有限公司",
        							"econKind": "有限责任公司(台港澳法人独资)",
        							"status": "存续"
        						}
        					}, {
        						"id": "70995224",
        						"labels": ["Person"],
        						"properties": {
        							"keyNo": "p2393bb965909d80fbdc6db7bcbf428a",
        							"role": "自然人股东",
        							"name": "张程"
        						}
        					}, {
        						"id": "50512428",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "e2f02283910a7f2c6759440681edf7eb",
        							"registCapi": "534.4822",
        							"name": "西安蜂语信息科技有限公司",
        							"econKind": "有限责任公司(自然人投资或控股)",
        							"status": "在业"
        						}
        					}, {
        						"id": "40646485",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "b6b1f03e058671c2738b4a569bfd2f21",
        							"registCapi": "63248.7764",
        							"name": "无锡小天鹅股份有限公司",
        							"econKind": "股份有限公司(上市)",
        							"status": "在业"
        						}
        					}, {
        						"id": "76032435",
        						"labels": ["Person"],
        						"properties": {
        							"keyNo": "p32ebd387e482098cf180863f7361007",
        							"role": "",
        							"name": "丁鹏飞"
        						}
        					}, {
        						"id": "29507713",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "84d05f991ede38ae5b2a74cc1e21ba51",
        							"registCapi": "10000.0",
        							"name": "广东美的日用电器进出口贸易有限公司",
        							"econKind": "有限责任公司(法人独资)",
        							"status": "存续"
        						}
        					}, {
        						"id": "17149007",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "4da107bbc5fe0e8939c0f8dbf63ec1b1",
        							"registCapi": "38000.0",
        							"name": "广东美的环境电器制造有限公司",
        							"econKind": "有限责任公司(中外合资)",
        							"status": "存续"
        						}
        					}, {
        						"id": "24315942",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "6db875a2f16bf13ca0b96c5d44fd1065",
        							"registCapi": "100.0",
        							"name": "广州小米信息服务有限公司",
        							"econKind": "有限责任公司(法人独资)",
        							"status": "存续"
        						}
        					}, {
        						"id": "4130136",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "12b7198ae8e5d2a908f2d00573e1d9ca",
        							"registCapi": "20000.0",
        							"name": "佛山市美的开利制冷设备有限公司",
        							"econKind": "有限责任公司(台港澳与境内合资)",
        							"status": "存续"
        						}
        					}, {
        						"id": "38514470",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "ad2694b03a4f32e4703568147a438c49",
        							"registCapi": "0.0",
        							"name": "天津拾米企业管理合伙企业(有限合伙)",
        							"econKind": "有限合伙企业",
        							"status": "存续"
        						}
        					}, {
        						"id": "45124547",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "cac4c7d67320964eddebc475fa66d3f9",
        							"registCapi": "1000.0",
        							"name": "北京金山数字娱乐科技有限公司",
        							"econKind": "有限责任公司(法人独资)",
        							"status": "在业"
        						}
        					}, {
        						"id": "3802438",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "113e5fdbe39a5a90f3c5d5a0902418da",
        							"registCapi": "200.0",
        							"name": "天津迈博远瞻科技有限公司",
        							"econKind": "有限责任公司(法人独资)",
        							"status": "存续"
        						}
        					}, {
        						"id": "19106983",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "565ed1dbf641ccd23989d3111d46286c",
        							"registCapi": "0.0",
        							"name": "天津金米投资合伙企业(有限合伙)",
        							"econKind": "有限合伙企业",
        							"status": "存续"
        						}
        					}, {
        						"id": "42411778",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "be99a4abfa65352286af89d0e9bce7ef",
        							"registCapi": "5000.0",
        							"name": "小米产业投资管理有限公司",
        							"econKind": "有限责任公司（非自然人投资或控股的法人独资）",
        							"status": "存续"
        						}
        					}, {
        						"id": "49332088",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "dda33f83062154c9c8a5570629b6f099",
        							"registCapi": "85400.0",
        							"name": "广东美的制冷设备有限公司",
        							"econKind": "有限责任公司(中外合资)",
        							"status": "存续"
        						}
        					}, {
        						"id": "11449639",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "33e17607404769ee18cd72338f4c5bd3",
        							"registCapi": "200.0",
        							"name": "北京小米影业投资有限公司",
        							"econKind": "有限责任公司(法人独资)",
        							"status": "在业"
        						}
        					}, {
        						"id": "20076707",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "5abe7edd9f06420784119ad621f80efc",
        							"registCapi": "10.0",
        							"name": "深圳英鹏数据信息有限公司",
        							"econKind": "有限责任公司",
        							"status": "存续"
        						}
        					}, {
        						"id": "26468356",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "77472fbe731c1b8f4bfc2723f3b65415",
        							"registCapi": "21550.0",
        							"name": "珠海金山软件有限公司",
        							"econKind": "有限责任公司(法人独资)",
        							"status": "存续"
        						}
        					}, {
        						"id": "25955383",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "75000249dc619c03cac6599928003df1",
        							"registCapi": "0.0",
        							"name": "湖北小米长江产业基金合伙企业(有限合伙)",
        							"econKind": "有限合伙企业",
        							"status": "存续"
        						}
        					}, {
        						"id": "3370376",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "0f4c469148a7b87a57e30425f0f40f31",
        							"registCapi": "2000.0",
        							"name": "上海步锵信息科技有限公司",
        							"econKind": "有限责任公司（自然人投资或控股）",
        							"status": "存续"
        						}
        					}, {
        						"id": "9386315",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "2a821429194d8afebf174c226dee21bb",
        							"registCapi": "560.0",
        							"name": "珠海金山快快科技有限公司",
        							"econKind": "其他有限责任公司",
        							"status": "注销"
        						}
        					}, {
        						"id": "55105166",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "f7807236936a27b6719e2ca626b6b55a",
        							"registCapi": "1650.0",
        							"name": "紫米通讯技术(江苏)有限公司",
        							"econKind": "有限责任公司(台港澳法人独资)",
        							"status": "在业"
        						}
        					}, {
        						"id": "31157266",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "8c3516cd93679b88af8eb26e8ec8e86b",
        							"registCapi": "1000.0",
        							"name": "北京金山软件有限公司",
        							"econKind": "其他有限责任公司",
        							"status": "在业"
        						}
        					}, {
        						"id": "7270847",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "20e0d9fcf7b3c7bc49098b1465dfbb01",
        							"registCapi": "10000.0",
        							"name": "小米之家商业有限公司",
        							"econKind": "有限责任公司(外商投资企业法人独资)",
        							"status": "存续"
        						}
        					}, {
        						"id": "53692134",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "f12d1a87544d51aa88cd6bb8d1f1ffa8",
        							"registCapi": "1200.0",
        							"name": "深圳杰睿联科技有限公司",
        							"econKind": "有限责任公司",
        							"status": "存续"
        						}
        					}, {
        						"id": "70814180",
        						"labels": ["Person"],
        						"properties": {
        							"keyNo": "p2306624640da02c003e5a2a77ffca67",
        							"role": "",
        							"name": "张峰"
        						}
        					}, {
        						"id": "2810359",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "0cc68eb8e8f9d0445d1916a9872d207c",
        							"registCapi": "6926.0",
        							"name": "广东美的生活电器制造有限公司",
        							"econKind": "有限责任公司(台港澳与境内合资)",
        							"status": "存续"
        						}
        					}, {
        						"id": "5189027",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "17773b52b0164d5d0c39a14cbc1d12c8",
        							"registCapi": "28800.0",
        							"name": "北京小米移动软件有限公司",
        							"econKind": "有限责任公司(法人独资)",
        							"status": "在业"
        						}
        					}, {
        						"id": "14049595",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "3fc8e6b450a351dffaf97ebba7bd5675",
        							"registCapi": "21000.0",
        							"name": "小米科技(武汉)有限公司",
        							"econKind": "有限责任公司(外商投资企业法人独资)",
        							"status": "存续"
        						}
        					}, {
        						"id": "26470526",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "77499fe96cd875f3ed66235fba82d61c",
        							"registCapi": "1367.6846",
        							"name": "杭州玺匠文化创意股份有限公司",
        							"econKind": "股份有限公司(非上市、外商投资企业投资)",
        							"status": "存续"
        						}
        					}, {
        						"id": "51048164",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "e558d7a7bf37fc3b8ccfcd7e7a85b7cc",
        							"registCapi": "42000.0",
        							"name": "广东美的微波炉制造有限公司",
        							"econKind": "有限责任公司(法人独资)",
        							"status": "存续"
        						}
        					}, {
        						"id": "21444787",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "60ee32febb98e1fa4628d59f8af8bea3",
        							"registCapi": "10.0",
        							"name": "南京酷科电子科技有限公司",
        							"econKind": "有限责任公司(台港澳与境内合资)",
        							"status": "在业"
        						}
        					}, {
        						"id": "30814253",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "8aab7f9b6a41da4aba1fed32acd85cee",
        							"registCapi": "1000.0",
        							"name": "湖北小米长江产业投资基金管理有限公司",
        							"econKind": "其他有限责任公司",
        							"status": "存续"
        						}
        					}, {
        						"id": "23436441",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "69cd1128903fa57b05e0b4d9b005d601",
        							"registCapi": "36000.0",
        							"name": "北京金山办公软件股份有限公司",
        							"econKind": "股份有限公司(中外合资、未上市)",
        							"status": "在业"
        						}
        					}, {
        						"id": "87093455",
        						"labels": ["Person"],
        						"properties": {
        							"keyNo": "p54a68df4d8a0ecf9ba5819df7851299",
        							"role": "总经理",
        							"name": "麦广炜"
        						}
        					}, {
        						"id": "72021583",
        						"labels": ["Person"],
        						"properties": {
        							"keyNo": "p26b3775f4ea1307e28aef63a6cf2cb8",
        							"role": "董事",
        							"name": "刘敏"
        						}
        					}, {
        						"id": "19616549",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "58a599fc62e3d36f3b111e35d79d5cb6",
        							"registCapi": "2320.0",
        							"name": "佛山市美的空调工业投资有限公司",
        							"econKind": "有限责任公司(法人独资)",
        							"status": "存续"
        						}
        					}, {
        						"id": "48932091",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "dbd7dbf53b862df3e288a1a42d473519",
        							"registCapi": "100000.0",
        							"name": "美的机器人产业发展有限公司",
        							"econKind": "其他有限责任公司",
        							"status": "存续"
        						}
        					}, {
        						"id": "40448122",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "b5cede7322c0f76d5adfe81632de5d21",
        							"registCapi": "44000.0",
        							"name": "上海新飞凡电子商务有限公司",
        							"econKind": "有限责任公司（自然人投资或控股的法人独资）",
        							"status": "存续"
        						}
        					}, {
        						"id": "5773895",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "1a15b53dcd65b1375bcc2378b43dafee",
        							"registCapi": "6000.0",
        							"name": "佛山市美的智荟房地产开发有限公司",
        							"econKind": "其他有限责任公司",
        							"status": "存续"
        						}
        					}, {
        						"id": "47032548",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "d351b2fa9881469bd1cabc0b55ddd3cf",
        							"registCapi": "83000.0",
        							"name": "芜湖美智空调设备有限公司",
        							"econKind": "其他有限责任公司",
        							"status": "存续"
        						}
        					}, {
        						"id": "21912320",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "630537e4747092679451cea00432584b",
        							"registCapi": "67650.0",
        							"name": "安得智联科技股份有限公司",
        							"econKind": "股份有限公司(台港澳与境内合资、未上市)",
        							"status": "存续"
        						}
        					}, {
        						"id": "138059368",
        						"labels": ["Person"],
        						"properties": {
        							"keyNo": "pf0cfb34822211ad0069e4008c849268",
        							"role": "",
        							"name": "殷必彤"
        						}
        					}, {
        						"id": "16515752",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "4acdaf5e031fc214abdb6287e9a9276f",
        							"registCapi": "45000.0",
        							"name": "重庆市小米小额贷款有限公司",
        							"econKind": "有限责任公司(台港澳法人独资)",
        							"status": "存续"
        						}
        					}, {
        						"id": "28343271",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "7f9b5c51888236c91a1fade703554b38",
        							"registCapi": "3000.0",
        							"name": "上海小米金融信息服务有限公司",
        							"econKind": "有限责任公司（非自然人投资或控股的法人独资）",
        							"status": "存续"
        						}
        					}, {
        						"id": "105408528",
        						"labels": ["Person"],
        						"properties": {
        							"keyNo": "p8ca4283fb80cf988920545e99aef3a4",
        							"role": "",
        							"name": "黎万强"
        						}
        					}, {
        						"id": "38533138",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "ad3beb3625f1d896c13569e655cfae99",
        							"registCapi": "100.0",
        							"name": "海南棋妙互动科技有限公司",
        							"econKind": "有限责任公司（自然人投资或控股的法人独资）",
        							"status": "存续"
        						}
        					}, {
        						"id": "33491868",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "96a96880169f224489579622628155dc",
        							"registCapi": "5000.0",
        							"name": "广东美的智联家居科技有限公司",
        							"econKind": "有限责任公司(自然人投资或控股)",
        							"status": "存续"
        						}
        					}, {
        						"id": "32117662",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "9081334ab227c34556e8fd88491c7f0f",
        							"registCapi": "20000.0",
        							"name": "珠海淇澳游艇会有限公司",
        							"econKind": "有限责任公司(自然人投资或控股)",
        							"status": "存续"
        						}
        					}, {
        						"id": "15162011",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "44c465ca815cf33b556d86577d364c92",
        							"registCapi": "10000.0",
        							"name": "重庆小米商业保理有限公司",
        							"econKind": "有限责任公司(法人独资)",
        							"status": "存续"
        						}
        					}, {
        						"id": "9358855",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "2a620cfbe8a8678ce9bb3312da633871",
        							"registCapi": "931250.6158",
        							"name": "上海万达网络金融服务有限公司",
        							"econKind": "其他有限责任公司",
        							"status": "存续"
        						}
        					}, {
        						"id": "53110181",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "ee92647afee609db9b431e4234557374",
        							"registCapi": "200.0",
        							"name": "北京创派力量科技有限公司",
        							"econKind": "有限责任公司(自然人投资或控股)",
        							"status": "在业"
        						}
        					}, {
        						"id": "21135315",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "5f8cd46f48690897a21e1db8f4fa3634",
        							"registCapi": "100.0",
        							"name": "广州小米通讯技术有限公司",
        							"econKind": "有限责任公司(外商投资企业法人独资)",
        							"status": "存续"
        						}
        					}, {
        						"id": "48640116",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "da88ade11ea1a161cf31cb82ec7730f1",
        							"registCapi": "300.0",
        							"name": "北京小米软件技术有限公司",
        							"econKind": "有限责任公司(台港澳法人独资)",
        							"status": "在业"
        						}
        					}, {
        						"id": "34862212",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "9ccd82113ca975c74dc6539c238d1256",
        							"registCapi": "392.16",
        							"name": "深圳市英鹏聚客网络科技有限责任公司",
        							"econKind": "有限责任公司",
        							"status": "存续"
        						}
        					}, {
        						"id": "111454216",
        						"labels": ["Person"],
        						"properties": {
        							"keyNo": "p9f2743c5058af08e2e451e3d099c542",
        							"role": "监事",
        							"name": "洪锋"
        						}
        					}, {
        						"id": "29514605",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "84d8302d3f1eb3f92d3aba2979d1fd47",
        							"registCapi": "25420.0",
        							"name": "北京赫美尚品科技有限公司",
        							"econKind": "有限责任公司(外商投资企业法人独资)",
        							"status": "在业"
        						}
        					}, {
        						"id": "27906841",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "7dab3f7324688b072949d6371a9026b0",
        							"registCapi": "705.88",
        							"name": "江苏紫米电子技术有限公司",
        							"econKind": "有限责任公司",
        							"status": "在业"
        						}
        					}, {
        						"id": "31403886",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "8d4f288caa104f94ba4df5ce4d72ec15",
        							"registCapi": "800.0",
        							"name": "美的集团武汉制冷设备有限公司",
        							"econKind": "有限责任公司(中外合资)",
        							"status": "存续"
        						}
        					}, {
        						"id": "67821232",
        						"labels": ["Person"],
        						"properties": {
        							"keyNo": "p19eba9bad4c00591015be72b57aa953",
        							"role": "董事",
        							"name": "李飞德"
        						}
        					}, {
        						"id": "125265334",
        						"labels": ["Person"],
        						"properties": {
        							"keyNo": "pc97f07e63872b0e1974c9c0aaec7aa7",
        							"role": "董事",
        							"name": "朱啸虎"
        						}
        					}, {
        						"id": "41727146",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "bb88746a494260f97d30c5c4c8343298",
        							"registCapi": "10.0",
        							"name": "西藏达孜金沙互联创业投资管理有限公司",
        							"econKind": "有限责任公司(自然人投资或控股)",
        							"status": "存续"
        						}
        					}, {
        						"id": "46630928",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "d185a7746d6f0309a9621eac297bacb5",
        							"registCapi": "30000.0",
        							"name": "珠海小米金融科技有限公司",
        							"econKind": "有限责任公司(法人独资)",
        							"status": "存续"
        						}
        					}, {
        						"id": "10062407",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "2d916ad7d280f663fdb24c9d58938418",
        							"registCapi": "774.0097",
        							"name": "广东美芝精密制造有限公司",
        							"econKind": "有限责任公司(中外合资)",
        							"status": "存续"
        						}
        					}, {
        						"id": "56441273",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "fd8c28225e351828515b5eed6ed4384d",
        							"registCapi": "222.2222",
        							"name": "深圳英鹏互娱科技有限公司",
        							"econKind": "有限责任公司",
        							"status": "存续"
        						}
        					}, {
        						"id": "12273234",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "37a2e1032399ec9068c5e5d003c62951",
        							"registCapi": "5527.0",
        							"name": "广东美芝制冷设备有限公司",
        							"econKind": "有限责任公司(中外合资)",
        							"status": "存续"
        						}
        					}, {
        						"id": "74767000",
        						"labels": ["Person"],
        						"properties": {
        							"keyNo": "p2f10e89de841bdc628df613420b0040",
        							"role": "",
        							"name": "朱凤涛"
        						}
        					}, {
        						"id": "46889411",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "d2adf1c22178335067fa214da6cffab5",
        							"registCapi": "5000.0",
        							"name": "小米信用管理有限公司",
        							"econKind": "有限责任公司(法人独资)",
        							"status": "在业"
        						}
        					}, {
        						"id": "9752450",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "2c2a4a5d83f570b42fc9a5b92a0dbe75",
        							"registCapi": "8000.0",
        							"name": "小米之家科技有限公司",
        							"econKind": "有限责任公司(外商投资企业法人独资)",
        							"status": "在业"
        						}
        					}, {
        						"id": "53815336",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "f1ba2f7dfcecba582edbf89b03009980",
        							"registCapi": "43757.56",
        							"name": "广州华凌空调设备有限公司",
        							"econKind": "其他有限责任公司",
        							"status": "存续"
        						}
        					}, {
        						"id": "91776593",
        						"labels": ["Person"],
        						"properties": {
        							"keyNo": "p62f65fb92140c5dac3878bb2e5ef0d9",
        							"role": "",
        							"name": "CHEW SHOU ZI"
        						}
        					}, {
        						"id": "49801690",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "dfc12f08a1e33388a7444803a2038595",
        							"registCapi": "0.0",
        							"name": "上海景林创业投资中心(有限合伙)",
        							"econKind": "有限合伙企业",
        							"status": "存续"
        						}
        					}, {
        						"id": "13487102",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "3d38cf313265f72e936e857ea628caab",
        							"registCapi": "50.0",
        							"name": "上海英鹏网络科技有限公司",
        							"econKind": "有限责任公司（自然人投资或控股的法人独资）",
        							"status": "注销"
        						}
        					}, {
        						"id": "33667381",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "9772fb898ce0113770c59edb21b9ef80",
        							"registCapi": "6000.0",
        							"name": "佛山市美的材料供应有限公司",
        							"econKind": "有限责任公司(自然人投资或控股)",
        							"status": "存续"
        						}
        					}, {
        						"id": "6778704",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "1ea557c511d6c06423d0519a364ae0a5",
        							"registCapi": "0.0",
        							"name": "天津众米企业管理合伙企业(有限合伙)",
        							"econKind": "有限合伙企业",
        							"status": "存续"
        						}
        					}, {
        						"id": "30051058",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "873fe8132ef18bb9bbd1f4cad6c4837c",
        							"registCapi": "250000.0",
        							"name": "佛山市顺德区美的家电实业有限公司",
        							"econKind": "有限责任公司(法人独资)",
        							"status": "存续"
        						}
        					}, {
        						"id": "56017001",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "fb9c28e66da9cf101cd174bf27c97b3a",
        							"registCapi": "10000.0",
        							"name": "捷付睿通股份有限公司",
        							"econKind": "其他股份有限公司(非上市)(1229)",
        							"status": "存续"
        						}
        					}, {
        						"id": "61750511",
        						"labels": ["Person"],
        						"properties": {
        							"keyNo": "p077472cd738bf6c70d757a42c6acaf4",
        							"role": "董事",
        							"name": "林斌"
        						}
        					}, {
        						"id": "28584701",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "80af5085726bb6b9c7770f1e4d0580f4",
        							"registCapi": "13000.0",
        							"name": "小米通讯技术有限公司",
        							"econKind": "有限责任公司(台港澳法人独资)",
        							"status": "在业"
        						}
        					}, {
        						"id": "46906758",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "d2c1f7ff860dd66ced5a2416c762be7d",
        							"registCapi": "0.0",
        							"name": "天津拾贰米企业管理合伙企业(有限合伙)",
        							"econKind": "有限合伙企业",
        							"status": "存续"
        						}
        					}, {
        						"id": "38668570",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "add69f81b86b006897fa3d6d90e97fed",
        							"registCapi": "1000.0",
        							"name": "英鹏互娱科技(北京)有限公司",
        							"econKind": "有限责任公司(自然人投资或控股)",
        							"status": "注销"
        						}
        					}, {
        						"id": "27426550",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "7b88b2641796b82c215433a1693354b1",
        							"registCapi": "1000.0",
        							"name": "北京尚品百姿电子商务有限公司",
        							"econKind": "有限责任公司(外商投资企业法人独资)",
        							"status": "在业"
        						}
        					}, {
        						"id": "44697085",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "c8dafdec7b4b5251309eaa03f2b7a214",
        							"registCapi": "1263.1579",
        							"name": "深圳英鹏信息技术股份有限公司",
        							"econKind": "非上市股份有限公司",
        							"status": "存续"
        						}
        					}, {
        						"id": "34470228",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "9b0c52e7af1ee199857b94bc3ea6be3d",
        							"registCapi": "275799.2863",
        							"name": "北京掌趣科技股份有限公司",
        							"econKind": "股份有限公司(上市、自然人投资或控股)",
        							"status": "在业"
        						}
        					}, {
        						"id": "25141798",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "7162d59044e687ea8f6bbf1670c6253b",
        							"registCapi": "153.8462",
        							"name": "深圳市一零二四信息技术有限公司",
        							"econKind": "有限责任公司",
        							"status": "存续"
        						}
        					}, {
        						"id": "35384641",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "9f2417970d571bb69c43d39de19d24ba",
        							"registCapi": "375.0",
        							"name": "深圳英鹏未来科技有限公司",
        							"econKind": "有限责任公司",
        							"status": "存续"
        						}
        					}, {
        						"id": "50514016",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "e2f1fa5a804f586366cab468d2895de7",
        							"registCapi": "2000.0",
        							"name": "上海小米慧科信息技术服务有限公司",
        							"econKind": "有限责任公司（外商投资企业法人独资）",
        							"status": "存续"
        						}
        					}, {
        						"id": "136011627",
        						"labels": ["Person"],
        						"properties": {
        							"keyNo": "pea83003052147075d5de0318be9e70f",
        							"role": "董事",
        							"name": "顾炎民"
        						}
        					}, {
        						"id": "23919128",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "6bf3741229b0bb3f9f16d6a1623ebf8a",
        							"registCapi": "692.8",
        							"name": "广东美的集团芜湖制冷设备有限公司",
        							"econKind": "有限责任公司(中外合资)",
        							"status": "存续"
        						}
        					}, {
        						"id": "8067068",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "247fabd4df39c3d4d822f3c00aa0b676",
        							"registCapi": "1500.0",
        							"name": "广东美的厨卫电器制造有限公司",
        							"econKind": "有限责任公司(中外合资)",
        							"status": "存续"
        						}
        					}, {
        						"id": "53842109",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "f1d8b7172af4e0d38d790a7c71daed8e",
        							"registCapi": "50.0",
        							"name": "深圳市英鹏兰德管理咨询有限公司",
        							"econKind": "有限责任公司",
        							"status": "存续"
        						}
        					}, {
        						"id": "20729514",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "5dbc2f59bf389bca62103ae7a9b2ff5c",
        							"registCapi": "30000.0",
        							"name": "珠海小米小额贷款有限公司",
        							"econKind": "有限责任公司(法人独资)",
        							"status": "存续"
        						}
        					}, {
        						"id": "27983365",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "7e023446a248dd2e873ede3a08eeadc5",
        							"registCapi": "5000.0",
        							"name": "成都倍达资产管理有限公司",
        							"econKind": "有限责任公司（非自然人投资或控股的法人独资）",
        							"status": "存续"
        						}
        					}, {
        						"id": "48014695",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "d7b8f0acc4c5d99cf900da00b2cd64de",
        							"registCapi": "66000.0",
        							"name": "广东美的商用空调设备有限公司",
        							"econKind": "有限责任公司(中外合资)",
        							"status": "存续"
        						}
        					}, {
        						"id": "14121832",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "401bd1aba720df2dc5f08c7dc8a594f7",
        							"registCapi": "1000.0",
        							"name": "珠海西山居世游科技有限公司",
        							"econKind": "有限责任公司(自然人投资或控股)",
        							"status": "存续"
        						}
        					}, {
        						"id": "132887594",
        						"labels": ["Person"],
        						"properties": {
        							"keyNo": "pe0e73ab3e840432797a2fdbaf7c544b",
        							"role": "监事",
        							"name": "华来银"
        						}
        					}, {
        						"id": "37359097",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "a7fa0ea25aac674b1501088a1bb12773",
        							"registCapi": "5000.0",
        							"name": "芜湖小天鹅制冷设备有限公司",
        							"econKind": "其他有限责任公司",
        							"status": "存续"
        						}
        					}, {
        						"id": "929751",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "043f45f8604ef6d9de115c400648fb58",
        							"registCapi": "1000.0",
        							"name": "北京金山志远技术有限公司",
        							"econKind": "有限责任公司(法人独资)",
        							"status": "在业"
        						}
        					}, {
        						"id": "13569812",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "3d9a2d02379f9ae6d16db49c3472f286",
        							"registCapi": "231363.0",
        							"name": "北京小米支付技术有限公司",
        							"econKind": "有限责任公司(外商投资企业法人独资)",
        							"status": "在业"
        						}
        					}, {
        						"id": "41067921",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "b894dee03e3d201af50ab60638820740",
        							"registCapi": "2592.0",
        							"name": "合肥荣事达洗衣机有限公司",
        							"econKind": "有限责任公司(中外合资)",
        							"status": "存续"
        						}
        					}, {
        						"id": "22793897",
        						"labels": ["Company"],
        						"properties": {
        							"keyNo": "66f17bf9eebdb4ab018709ecc76c3577",
        							"registCapi": "200.0",
        							"name": "珠海小米通讯技术有限公司",
        							"econKind": "有限责任公司(法人独资)",
        							"status": "存续"
        						}
        					}, {
        						"id": "67539962",
        						"labels": ["Person"],
        						"properties": {
        							"keyNo": "p1910534b4ae98fea35ddbeb1d61cd44",
        							"role": "董事",
        							"name": "雷军"
        						}
        					}],
        					"relationships": [{
        						"id": "51690263",
        						"type": "INVEST",
        						"startNode": "111494674",
        						"endNode": "16152702",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 0.274,
        							"shouldCapi": 100
        						}
        					}, {
        						"id": "51690257",
        						"type": "INVEST",
        						"startNode": "95221018",
        						"endNode": "16152702",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 0.5479,
        							"shouldCapi": 200
        						}
        					}, {
        						"id": "51690259",
        						"type": "INVEST",
        						"startNode": "111454216",
        						"endNode": "16152702",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 0.274,
        							"shouldCapi": 100
        						}
        					}, {
        						"id": "1208346",
        						"type": "INVEST",
        						"startNode": "41727146",
        						"endNode": "56441273",
        						"properties": {
        							"role": "有限责任",
        							"stockPercent": 18,
        							"shouldCapi": 40
        						}
        					}, {
        						"id": "3954742",
        						"type": "INVEST",
        						"startNode": "26468356",
        						"endNode": "31157266",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 80,
        							"shouldCapi": 800
        						}
        					}, {
        						"id": "1208345",
        						"type": "INVEST",
        						"startNode": "34862636",
        						"endNode": "56441273",
        						"properties": {
        							"role": "有限责任",
        							"stockPercent": 20.16,
        							"shouldCapi": 44.8
        						}
        					}, {
        						"id": "1208348",
        						"type": "INVEST",
        						"startNode": "17559925",
        						"endNode": "56441273",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 9,
        							"shouldCapi": 20
        						}
        					}, {
        						"id": "1208349",
        						"type": "INVEST",
        						"startNode": "49801690",
        						"endNode": "56441273",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 5.67,
        							"shouldCapi": 12.6
        						}
        					}, {
        						"id": "190309191",
        						"type": "EMPLOY",
        						"startNode": "130712376",
        						"endNode": "41428834",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "51690241",
        						"type": "INVEST",
        						"startNode": "102647336",
        						"endNode": "16152702",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 8.219,
        							"shouldCapi": 3000
        						}
        					}, {
        						"id": "222629203",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "14049595",
        						"properties": {
        							"role": "执行董事兼总经理"
        						}
        					}, {
        						"id": "222629202",
        						"type": "EMPLOY",
        						"startNode": "95221018",
        						"endNode": "14049595",
        						"properties": {
        							"role": "监事"
        						}
        					}, {
        						"id": "239167066",
        						"type": "EMPLOY",
        						"startNode": "102647336",
        						"endNode": "4130136",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "190309193",
        						"type": "EMPLOY",
        						"startNode": "70995224",
        						"endNode": "41428834",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "190309192",
        						"type": "EMPLOY",
        						"startNode": "121297792",
        						"endNode": "41428834",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "25143647",
        						"type": "INVEST",
        						"startNode": "31039917",
        						"endNode": "34470228",
        						"properties": {
        							"stockPercent": 0.75
        						}
        					}, {
        						"id": "239167072",
        						"type": "EMPLOY",
        						"startNode": "136011627",
        						"endNode": "4130136",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "25143645",
        						"type": "INVEST",
        						"startNode": "26802477",
        						"endNode": "34470228",
        						"properties": {
        							"stockPercent": 0.89
        						}
        					}, {
        						"id": "239167074",
        						"type": "EMPLOY",
        						"startNode": "138059368",
        						"endNode": "4130136",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "2963470",
        						"type": "INVEST",
        						"startNode": "51868419",
        						"endNode": "29514605",
        						"properties": {
        							"role": "法人股东",
        							"stockPercent": 100,
        							"shouldCapi": 25420
        						}
        					}, {
        						"id": "25143644",
        						"type": "INVEST",
        						"startNode": "34470228",
        						"endNode": "34470228",
        						"properties": {
        							"stockPercent": 2
        						}
        					}, {
        						"id": "3817502",
        						"type": "INVEST",
        						"startNode": "27906841",
        						"endNode": "50512428",
        						"properties": {
        							"role": "法人股东",
        							"stockPercent": 8.29,
        							"shouldCapi": 44.284
        						}
        					}, {
        						"id": "250722007",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "9752450",
        						"properties": {
        							"role": "执行董事"
        						}
        					}, {
        						"id": "3817500",
        						"type": "INVEST",
        						"startNode": "19106983",
        						"endNode": "50512428",
        						"properties": {
        							"role": "法人股东",
        							"stockPercent": 8.29,
        							"shouldCapi": 44.284
        						}
        					}, {
        						"id": "135483444",
        						"type": "LEGAL",
        						"startNode": "111454216",
        						"endNode": "46630928",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "250722006",
        						"type": "EMPLOY",
        						"startNode": "61750511",
        						"endNode": "9752450",
        						"properties": {
        							"role": "经理"
        						}
        					}, {
        						"id": "97324518",
        						"type": "LEGAL",
        						"startNode": "70814180",
        						"endNode": "55105166",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "944188",
        						"type": "INVEST",
        						"startNode": "52260843",
        						"endNode": "10062407",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 60,
        							"shouldCapi": 464.4058
        						}
        					}, {
        						"id": "132458454",
        						"type": "LEGAL",
        						"startNode": "111494674",
        						"endNode": "45124547",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "2527250",
        						"type": "INVEST",
        						"startNode": "26802477",
        						"endNode": "40646485",
        						"properties": {
        							"stockPercent": 1.61
        						}
        					}, {
        						"id": "50432833",
        						"type": "INVEST",
        						"startNode": "105408528",
        						"endNode": "26470526",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 0,
        							"shouldCapi": 0
        						}
        					}, {
        						"id": "214705295",
        						"type": "EMPLOY",
        						"startNode": "102647336",
        						"endNode": "40646485",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "217453745",
        						"type": "EMPLOY",
        						"startNode": "105408528",
        						"endNode": "6015168",
        						"properties": {
        							"role": "监事"
        						}
        					}, {
        						"id": "112090849",
        						"type": "LEGAL",
        						"startNode": "70814180",
        						"endNode": "31098074",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "217453742",
        						"type": "EMPLOY",
        						"startNode": "95221018",
        						"endNode": "6015168",
        						"properties": {
        							"role": "经理"
        						}
        					}, {
        						"id": "217453743",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "6015168",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "217453741",
        						"type": "EMPLOY",
        						"startNode": "61750511",
        						"endNode": "6015168",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "50432861",
        						"type": "INVEST",
        						"startNode": "76032435",
        						"endNode": "26470526",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 0,
        							"shouldCapi": 0
        						}
        					}, {
        						"id": "14092471",
        						"type": "INVEST",
        						"startNode": "70814180",
        						"endNode": "27906841",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 49.58,
        							"shouldCapi": 69.996
        						}
        					}, {
        						"id": "121343832",
        						"type": "LEGAL",
        						"startNode": "102647336",
        						"endNode": "40646485",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "98801029",
        						"type": "LEGAL",
        						"startNode": "102647336",
        						"endNode": "33667381",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "20871512",
        						"type": "INVEST",
        						"startNode": "87093455",
        						"endNode": "56441273",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 1.9,
        							"shouldCapi": 4.2222
        						}
        					}, {
        						"id": "20871513",
        						"type": "INVEST",
        						"startNode": "101372578",
        						"endNode": "56441273",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 1.58,
        							"shouldCapi": 3.5
        						}
        					}, {
        						"id": "20871510",
        						"type": "INVEST",
        						"startNode": "101171886",
        						"endNode": "56441273",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 28.4,
        							"shouldCapi": 63.1
        						}
        					}, {
        						"id": "20871511",
        						"type": "INVEST",
        						"startNode": "132887594",
        						"endNode": "56441273",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 2.8,
        							"shouldCapi": 6.2222
        						}
        					}, {
        						"id": "106458675",
        						"type": "LEGAL",
        						"startNode": "102647336",
        						"endNode": "17149007",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "14092472",
        						"type": "INVEST",
        						"startNode": "67539962",
        						"endNode": "27906841",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 15,
        							"shouldCapi": 21.176
        						}
        					}, {
        						"id": "52175724",
        						"type": "INVEST",
        						"startNode": "105408528",
        						"endNode": "34862636",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 10.12,
        							"shouldCapi": 18724.357
        						}
        					}, {
        						"id": "203639891",
        						"type": "EMPLOY",
        						"startNode": "132887594",
        						"endNode": "1481843",
        						"properties": {
        							"role": "总经理"
        						}
        					}, {
        						"id": "52175725",
        						"type": "INVEST",
        						"startNode": "111454216",
        						"endNode": "34862636",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 10.07,
        							"shouldCapi": 18623.1
        						}
        					}, {
        						"id": "203639890",
        						"type": "EMPLOY",
        						"startNode": "132887594",
        						"endNode": "1481843",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "52175726",
        						"type": "INVEST",
        						"startNode": "95221018",
        						"endNode": "34862636",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 2.01,
        							"shouldCapi": 3718.4963
        						}
        					}, {
        						"id": "203639895",
        						"type": "EMPLOY",
        						"startNode": "101171886",
        						"endNode": "1481843",
        						"properties": {
        							"role": "清算组负责人"
        						}
        					}, {
        						"id": "86756702",
        						"type": "LEGAL",
        						"startNode": "138059368",
        						"endNode": "29507713",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "203639894",
        						"type": "EMPLOY",
        						"startNode": "101171886",
        						"endNode": "1481843",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "52175723",
        						"type": "INVEST",
        						"startNode": "67539962",
        						"endNode": "34862636",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 77.8,
        							"shouldCapi": 143934.05
        						}
        					}, {
        						"id": "221969741",
        						"type": "EMPLOY",
        						"startNode": "72021583",
        						"endNode": "5773895",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "117899135",
        						"type": "LEGAL",
        						"startNode": "111494674",
        						"endNode": "31157266",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "203639897",
        						"type": "EMPLOY",
        						"startNode": "132887594",
        						"endNode": "1481843",
        						"properties": {
        							"role": "清算组成员"
        						}
        					}, {
        						"id": "6502625",
        						"type": "INVEST",
        						"startNode": "13569812",
        						"endNode": "27983365",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 100,
        							"shouldCapi": 5000
        						}
        					}, {
        						"id": "185498509",
        						"type": "EMPLOY",
        						"startNode": "111494674",
        						"endNode": "25368839",
        						"properties": {
        							"role": "董事兼总经理"
        						}
        					}, {
        						"id": "250992255",
        						"type": "EMPLOY",
        						"startNode": "111454216",
        						"endNode": "27983365",
        						"properties": {
        							"role": "经理"
        						}
        					}, {
        						"id": "153254313",
        						"type": "EMPLOY",
        						"startNode": "95221018",
        						"endNode": "3370376",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "250992254",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "27983365",
        						"properties": {
        							"role": "执行董事"
        						}
        					}, {
        						"id": "174367465",
        						"type": "EMPLOY",
        						"startNode": "61964144",
        						"endNode": "31039917",
        						"properties": {
        							"role": "监事"
        						}
        					}, {
        						"id": "153254316",
        						"type": "EMPLOY",
        						"startNode": "111454216",
        						"endNode": "3370376",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "90279409",
        						"type": "LEGAL",
        						"startNode": "70814180",
        						"endNode": "27906841",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "4690134",
        						"type": "INVEST",
        						"startNode": "31039917",
        						"endNode": "10336442",
        						"properties": {
        							"role": "",
        							"stockPercent": 0,
        							"shouldCapi": 0
        						}
        					}, {
        						"id": "16814481",
        						"type": "INVEST",
        						"startNode": "101171886",
        						"endNode": "25141798",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 6.5,
        							"shouldCapi": 10
        						}
        					}, {
        						"id": "88378833",
        						"type": "LEGAL",
        						"startNode": "102647336",
        						"endNode": "48014695",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "98911609",
        						"type": "LEGAL",
        						"startNode": "67539962",
        						"endNode": "657610",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "91839975",
        						"type": "LEGAL",
        						"startNode": "102647336",
        						"endNode": "23919128",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "185498513",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "25368839",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "98723136",
        						"type": "LEGAL",
        						"startNode": "102647336",
        						"endNode": "52260843",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "117245531",
        						"type": "LEGAL",
        						"startNode": "101171886",
        						"endNode": "17559925",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "124876762",
        						"type": "LEGAL",
        						"startNode": "130712376",
        						"endNode": "9358855",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "190792691",
        						"type": "EMPLOY",
        						"startNode": "138059368",
        						"endNode": "53815336",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "192369607",
        						"type": "EMPLOY",
        						"startNode": "67821232",
        						"endNode": "15868072",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "4829432",
        						"type": "INVEST",
        						"startNode": "34862636",
        						"endNode": "38566723",
        						"properties": {
        							"role": "法人股东",
        							"stockPercent": 100,
        							"shouldCapi": 100
        						}
        					}, {
        						"id": "192369606",
        						"type": "EMPLOY",
        						"startNode": "102647336",
        						"endNode": "15868072",
        						"properties": {
        							"role": "董事长,经理"
        						}
        					}, {
        						"id": "243570230",
        						"type": "EMPLOY",
        						"startNode": "111494674",
        						"endNode": "929751",
        						"properties": {
        							"role": "经理"
        						}
        					}, {
        						"id": "243570231",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "929751",
        						"properties": {
        							"role": "执行董事"
        						}
        					}, {
        						"id": "109397558",
        						"type": "LEGAL",
        						"startNode": "70995224",
        						"endNode": "41428834",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "2963601",
        						"type": "INVEST",
        						"startNode": "52260843",
        						"endNode": "53815336",
        						"properties": {
        							"role": "法人股东",
        							"stockPercent": 90,
        							"shouldCapi": 39381.805
        						}
        					}, {
        						"id": "2963602",
        						"type": "INVEST",
        						"startNode": "19616549",
        						"endNode": "53815336",
        						"properties": {
        							"role": "法人股东",
        							"stockPercent": 10,
        							"shouldCapi": 4375.756
        						}
        					}, {
        						"id": "5470356",
        						"type": "INVEST",
        						"startNode": "52260843",
        						"endNode": "30051058",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 100,
        							"shouldCapi": 250000
        						}
        					}, {
        						"id": "151521731",
        						"type": "EMPLOY",
        						"startNode": "102647336",
        						"endNode": "2810359",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "151521733",
        						"type": "EMPLOY",
        						"startNode": "67821232",
        						"endNode": "2810359",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "115828228",
        						"type": "LEGAL",
        						"startNode": "102647336",
        						"endNode": "48932091",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "121778086",
        						"type": "LEGAL",
        						"startNode": "111454216",
        						"endNode": "15162011",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "157135290",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "51868419",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "13654071",
        						"type": "INVEST",
        						"startNode": "111494674",
        						"endNode": "14121832",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 20,
        							"shouldCapi": 200
        						}
        					}, {
        						"id": "228803913",
        						"type": "EMPLOY",
        						"startNode": "111494674",
        						"endNode": "23304514",
        						"properties": {
        							"role": "总经理"
        						}
        					}, {
        						"id": "228803912",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "23304514",
        						"properties": {
        							"role": "执行董事"
        						}
        					}, {
        						"id": "157135286",
        						"type": "EMPLOY",
        						"startNode": "84306247",
        						"endNode": "51868419",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "111671209",
        						"type": "LEGAL",
        						"startNode": "102647336",
        						"endNode": "31403886",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "161263752",
        						"type": "EMPLOY",
        						"startNode": "61750511",
        						"endNode": "28584701",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "138940766",
        						"type": "LEGAL",
        						"startNode": "61750511",
        						"endNode": "9752450",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "161263748",
        						"type": "EMPLOY",
        						"startNode": "105408528",
        						"endNode": "28584701",
        						"properties": {
        							"role": "经理"
        						}
        					}, {
        						"id": "161263749",
        						"type": "EMPLOY",
        						"startNode": "84306247",
        						"endNode": "28584701",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "161263750",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "28584701",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "1872188",
        						"type": "INVEST",
        						"startNode": "9358855",
        						"endNode": "40448122",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 100,
        							"shouldCapi": 44000
        						}
        					}, {
        						"id": "65796808",
        						"type": "INVEST",
        						"startNode": "95221018",
        						"endNode": "27382946",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 1.84,
        							"shouldCapi": 0.7098
        						}
        					}, {
        						"id": "73899332",
        						"type": "INVEST",
        						"startNode": "67539962",
        						"endNode": "29841901",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 0.44,
        							"shouldCapi": 43.71
        						}
        					}, {
        						"id": "190790266",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "29514605",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "190790265",
        						"type": "EMPLOY",
        						"startNode": "84306247",
        						"endNode": "29514605",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "203433222",
        						"type": "EMPLOY",
        						"startNode": "67821232",
        						"endNode": "48932091",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "203433223",
        						"type": "EMPLOY",
        						"startNode": "102647336",
        						"endNode": "48932091",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "405806",
        						"type": "INVEST",
        						"startNode": "52260843",
        						"endNode": "48014695",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 73,
        							"shouldCapi": 48180
        						}
        					}, {
        						"id": "6070636",
        						"type": "INVEST",
        						"startNode": "34862636",
        						"endNode": "46630928",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 100,
        							"shouldCapi": 30000
        						}
        					}, {
        						"id": "125224514",
        						"type": "LEGAL",
        						"startNode": "67539962",
        						"endNode": "14049595",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "89289830",
        						"type": "LEGAL",
        						"startNode": "101171886",
        						"endNode": "35384641",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "6066534",
        						"type": "INVEST",
        						"startNode": "14890432",
        						"endNode": "929751",
        						"properties": {
        							"role": "法人股东",
        							"stockPercent": 100,
        							"shouldCapi": 1000
        						}
        					}, {
        						"id": "2679150",
        						"type": "INVEST",
        						"startNode": "52260843",
        						"endNode": "33491868",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 90,
        							"shouldCapi": 4500
        						}
        					}, {
        						"id": "2679151",
        						"type": "INVEST",
        						"startNode": "19616549",
        						"endNode": "33491868",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 10,
        							"shouldCapi": 500
        						}
        					}, {
        						"id": "3207545",
        						"type": "INVEST",
        						"startNode": "52260843",
        						"endNode": "31403886",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 73,
        							"shouldCapi": 584
        						}
        					}, {
        						"id": "130492044",
        						"type": "LEGAL",
        						"startNode": "102647336",
        						"endNode": "30051058",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "2634104",
        						"type": "INVEST",
        						"startNode": "28584701",
        						"endNode": "22793897",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 100,
        							"shouldCapi": 200
        						}
        					}, {
        						"id": "2871678",
        						"type": "INVEST",
        						"startNode": "19616549",
        						"endNode": "17083398",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 10,
        							"shouldCapi": 100
        						}
        					}, {
        						"id": "2871677",
        						"type": "INVEST",
        						"startNode": "52260843",
        						"endNode": "17083398",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 90,
        							"shouldCapi": 900
        						}
        					}, {
        						"id": "4776235",
        						"type": "INVEST",
        						"startNode": "52260843",
        						"endNode": "26278264",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 90,
        							"shouldCapi": 27000
        						}
        					}, {
        						"id": "4776236",
        						"type": "INVEST",
        						"startNode": "19616549",
        						"endNode": "26278264",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 10,
        							"shouldCapi": 3000
        						}
        					}, {
        						"id": "128384719",
        						"type": "LEGAL",
        						"startNode": "67539962",
        						"endNode": "32117662",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "985441",
        						"type": "INVEST",
        						"startNode": "38347294",
        						"endNode": "51868419",
        						"properties": {
        							"role": "法人股东",
        							"stockPercent": 2.24,
        							"shouldCapi": 775.9046
        						}
        					}, {
        						"id": "168582010",
        						"type": "EMPLOY",
        						"startNode": "102647336",
        						"endNode": "33667381",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "168582011",
        						"type": "EMPLOY",
        						"startNode": "67821232",
        						"endNode": "33667381",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "100574335",
        						"type": "LEGAL",
        						"startNode": "130712376",
        						"endNode": "40448122",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "6414788",
        						"type": "INVEST",
        						"startNode": "52260843",
        						"endNode": "30841307",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 100,
        							"shouldCapi": 350000
        						}
        					}, {
        						"id": "1024420",
        						"type": "INVEST",
        						"startNode": "41428834",
        						"endNode": "3802438",
        						"properties": {
        							"role": "法人股东",
        							"stockPercent": 100,
        							"shouldCapi": 200
        						}
        					}, {
        						"id": "203414961",
        						"type": "EMPLOY",
        						"startNode": "111454216",
        						"endNode": "46889411",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "183602014",
        						"type": "EMPLOY",
        						"startNode": "84306247",
        						"endNode": "20919641",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "203414960",
        						"type": "EMPLOY",
        						"startNode": "61750511",
        						"endNode": "46889411",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "203414959",
        						"type": "EMPLOY",
        						"startNode": "111454216",
        						"endNode": "46889411",
        						"properties": {
        							"role": "经理"
        						}
        					}, {
        						"id": "203414958",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "46889411",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "203414957",
        						"type": "EMPLOY",
        						"startNode": "95221018",
        						"endNode": "46889411",
        						"properties": {
        							"role": "监事"
        						}
        					}, {
        						"id": "5612007",
        						"type": "INVEST",
        						"startNode": "19616549",
        						"endNode": "47032548",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 12.53,
        							"shouldCapi": 10400
        						}
        					}, {
        						"id": "5612006",
        						"type": "INVEST",
        						"startNode": "52260843",
        						"endNode": "47032548",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 87.47,
        							"shouldCapi": 72600
        						}
        					}, {
        						"id": "5794275",
        						"type": "INVEST",
        						"startNode": "52260843",
        						"endNode": "49332088",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 73,
        							"shouldCapi": 62342
        						}
        					}, {
        						"id": "143073615",
        						"type": "EMPLOY",
        						"startNode": "105408528",
        						"endNode": "5189027",
        						"properties": {
        							"role": "经理"
        						}
        					}, {
        						"id": "143073614",
        						"type": "EMPLOY",
        						"startNode": "105408528",
        						"endNode": "5189027",
        						"properties": {
        							"role": "执行董事"
        						}
        					}, {
        						"id": "95224935",
        						"type": "LEGAL",
        						"startNode": "105408528",
        						"endNode": "28584701",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "133977645",
        						"type": "LEGAL",
        						"startNode": "105408528",
        						"endNode": "36973248",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "655839",
        						"type": "INVEST",
        						"startNode": "52260843",
        						"endNode": "2810359",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 75,
        							"shouldCapi": 5194.5
        						}
        					}, {
        						"id": "143073616",
        						"type": "EMPLOY",
        						"startNode": "111454216",
        						"endNode": "5189027",
        						"properties": {
        							"role": "监事"
        						}
        					}, {
        						"id": "125169299",
        						"type": "LEGAL",
        						"startNode": "67539962",
        						"endNode": "38566723",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "111755077",
        						"type": "LEGAL",
        						"startNode": "67539962",
        						"endNode": "38347294",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "2521557",
        						"type": "INVEST",
        						"startNode": "52260843",
        						"endNode": "40646485",
        						"properties": {
        							"stockPercent": 37.78
        						}
        					}, {
        						"id": "119377633",
        						"type": "LEGAL",
        						"startNode": "138059368",
        						"endNode": "781373",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "215410388",
        						"type": "EMPLOY",
        						"startNode": "102647336",
        						"endNode": "8067068",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "110654623",
        						"type": "LEGAL",
        						"startNode": "102647336",
        						"endNode": "41067921",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "215410385",
        						"type": "EMPLOY",
        						"startNode": "67821232",
        						"endNode": "8067068",
        						"properties": {
        							"role": "副董事长"
        						}
        					}, {
        						"id": "2507310",
        						"type": "INVEST",
        						"startNode": "52260843",
        						"endNode": "21912320",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 55,
        							"shouldCapi": 37207.5
        						}
        					}, {
        						"id": "233625597",
        						"type": "EMPLOY",
        						"startNode": "91776593",
        						"endNode": "7270847",
        						"properties": {
        							"role": "监事"
        						}
        					}, {
        						"id": "233625595",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "7270847",
        						"properties": {
        							"role": "执行董事"
        						}
        					}, {
        						"id": "175751265",
        						"type": "EMPLOY",
        						"startNode": "61750511",
        						"endNode": "16515752",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "40056955",
        						"type": "INVEST",
        						"startNode": "101372578",
        						"endNode": "38668570",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 0.31,
        							"shouldCapi": 3.065
        						}
        					}, {
        						"id": "40056954",
        						"type": "INVEST",
        						"startNode": "101171886",
        						"endNode": "38668570",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 97.27,
        							"shouldCapi": 972.655
        						}
        					}, {
        						"id": "175751266",
        						"type": "EMPLOY",
        						"startNode": "95221018",
        						"endNode": "16515752",
        						"properties": {
        							"role": "监事"
        						}
        					}, {
        						"id": "175751268",
        						"type": "EMPLOY",
        						"startNode": "111454216",
        						"endNode": "16515752",
        						"properties": {
        							"role": "董事兼总经理"
        						}
        					}, {
        						"id": "40056958",
        						"type": "INVEST",
        						"startNode": "87093455",
        						"endNode": "38668570",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 0.05,
        							"shouldCapi": 0.5
        						}
        					}, {
        						"id": "40056957",
        						"type": "INVEST",
        						"startNode": "132887594",
        						"endNode": "38668570",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 0.1,
        							"shouldCapi": 0
        						}
        					}, {
        						"id": "237292603",
        						"type": "EMPLOY",
        						"startNode": "87093455",
        						"endNode": "44697085",
        						"properties": {
        							"role": "总经理"
        						}
        					}, {
        						"id": "3056143",
        						"type": "INVEST",
        						"startNode": "52260843",
        						"endNode": "15868072",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 100,
        							"shouldCapi": 200000
        						}
        					}, {
        						"id": "4797035",
        						"type": "INVEST",
        						"startNode": "52260843",
        						"endNode": "5773895",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 95,
        							"shouldCapi": 5700
        						}
        					}, {
        						"id": "120063243",
        						"type": "LEGAL",
        						"startNode": "111494674",
        						"endNode": "17917391",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "4797036",
        						"type": "INVEST",
        						"startNode": "19616549",
        						"endNode": "5773895",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 5,
        							"shouldCapi": 300
        						}
        					}, {
        						"id": "194953657",
        						"type": "EMPLOY",
        						"startNode": "67821232",
        						"endNode": "31403886",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "179882129",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "53670436",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "179882130",
        						"type": "EMPLOY",
        						"startNode": "105408528",
        						"endNode": "53670436",
        						"properties": {
        							"role": "监事"
        						}
        					}, {
        						"id": "194953652",
        						"type": "EMPLOY",
        						"startNode": "136011627",
        						"endNode": "31403886",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "179882131",
        						"type": "EMPLOY",
        						"startNode": "61750511",
        						"endNode": "53670436",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "179882132",
        						"type": "EMPLOY",
        						"startNode": "95221018",
        						"endNode": "53670436",
        						"properties": {
        							"role": "总经理"
        						}
        					}, {
        						"id": "194953650",
        						"type": "EMPLOY",
        						"startNode": "138059368",
        						"endNode": "31403886",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "179882133",
        						"type": "EMPLOY",
        						"startNode": "84306247",
        						"endNode": "53670436",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "194953651",
        						"type": "EMPLOY",
        						"startNode": "102647336",
        						"endNode": "31403886",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "185944376",
        						"type": "EMPLOY",
        						"startNode": "72021583",
        						"endNode": "33491868",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "6486604",
        						"type": "INVEST",
        						"startNode": "28584701",
        						"endNode": "9752450",
        						"properties": {
        							"role": "外国(地区)企业",
        							"stockPercent": 100,
        							"shouldCapi": 8000
        						}
        					}, {
        						"id": "188449033",
        						"type": "EMPLOY",
        						"startNode": "87093455",
        						"endNode": "34862212",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "1671722",
        						"type": "INVEST",
        						"startNode": "28584701",
        						"endNode": "657610",
        						"properties": {
        							"role": "法人股东",
        							"stockPercent": 100,
        							"shouldCapi": 100000
        						}
        					}, {
        						"id": "122688868",
        						"type": "LEGAL",
        						"startNode": "95221018",
        						"endNode": "6015168",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "1950300",
        						"type": "INVEST",
        						"startNode": "26802477",
        						"endNode": "52260843",
        						"properties": {
        							"stockPercent": 1.19
        						}
        					}, {
        						"id": "41195570",
        						"type": "INVEST",
        						"startNode": "70995224",
        						"endNode": "41428834",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 11.41,
        							"shouldCapi": 313.8438
        						}
        					}, {
        						"id": "41195571",
        						"type": "INVEST",
        						"startNode": "121297792",
        						"endNode": "41428834",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 0.96,
        							"shouldCapi": 26.308
        						}
        					}, {
        						"id": "238910581",
        						"type": "EMPLOY",
        						"startNode": "67821232",
        						"endNode": "49332088",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "234606514",
        						"type": "EMPLOY",
        						"startNode": "105408528",
        						"endNode": "48640116",
        						"properties": {
        							"role": "监事"
        						}
        					}, {
        						"id": "147251855",
        						"type": "EMPLOY",
        						"startNode": "138059368",
        						"endNode": "48014695",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "147251852",
        						"type": "EMPLOY",
        						"startNode": "67821232",
        						"endNode": "48014695",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "234606512",
        						"type": "EMPLOY",
        						"startNode": "84306247",
        						"endNode": "48640116",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "147251853",
        						"type": "EMPLOY",
        						"startNode": "102647336",
        						"endNode": "48014695",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "238910582",
        						"type": "EMPLOY",
        						"startNode": "138059368",
        						"endNode": "49332088",
        						"properties": {
        							"role": "董事,总经理"
        						}
        					}, {
        						"id": "238910577",
        						"type": "EMPLOY",
        						"startNode": "136011627",
        						"endNode": "49332088",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "184293553",
        						"type": "EMPLOY",
        						"startNode": "67821232",
        						"endNode": "17149007",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "184293554",
        						"type": "EMPLOY",
        						"startNode": "102647336",
        						"endNode": "17149007",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "18426696",
        						"type": "INVEST",
        						"startNode": "101181150",
        						"endNode": "53842109",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 3,
        							"shouldCapi": 1.5
        						}
        					}, {
        						"id": "238910575",
        						"type": "EMPLOY",
        						"startNode": "102647336",
        						"endNode": "49332088",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "147251860",
        						"type": "EMPLOY",
        						"startNode": "136011627",
        						"endNode": "48014695",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "53868896",
        						"type": "INVEST",
        						"startNode": "95221018",
        						"endNode": "46906758",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 0,
        							"shouldCapi": 0
        						}
        					}, {
        						"id": "234606510",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "48640116",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "59943370",
        						"type": "INVEST",
        						"startNode": "111454216",
        						"endNode": "6015168",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 10,
        							"shouldCapi": 20710.02
        						}
        					}, {
        						"id": "59943369",
        						"type": "INVEST",
        						"startNode": "67539962",
        						"endNode": "6015168",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 90,
        							"shouldCapi": 186390.17
        						}
        					}, {
        						"id": "84936524",
        						"type": "LEGAL",
        						"startNode": "30814253",
        						"endNode": "25955383",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "18426693",
        						"type": "INVEST",
        						"startNode": "87093455",
        						"endNode": "53842109",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 27,
        							"shouldCapi": 13.5
        						}
        					}, {
        						"id": "18426692",
        						"type": "INVEST",
        						"startNode": "101171886",
        						"endNode": "53842109",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 46,
        							"shouldCapi": 23
        						}
        					}, {
        						"id": "108600345",
        						"type": "LEGAL",
        						"startNode": "101171886",
        						"endNode": "38668570",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "237292612",
        						"type": "EMPLOY",
        						"startNode": "101171886",
        						"endNode": "44697085",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "14973573",
        						"type": "INVEST",
        						"startNode": "105408528",
        						"endNode": "16967162",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 3.06,
        							"shouldCapi": 6.0946
        						}
        					}, {
        						"id": "237292608",
        						"type": "EMPLOY",
        						"startNode": "87093455",
        						"endNode": "44697085",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "133301653",
        						"type": "LEGAL",
        						"startNode": "138059368",
        						"endNode": "4130136",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "131667370",
        						"type": "LEGAL",
        						"startNode": "138059368",
        						"endNode": "47032548",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "102104162",
        						"type": "LEGAL",
        						"startNode": "102647336",
        						"endNode": "12273234",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "209535",
        						"type": "INVEST",
        						"startNode": "52260843",
        						"endNode": "29507713",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 100,
        							"shouldCapi": 10000
        						}
        					}, {
        						"id": "199649638",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "30814253",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "199649637",
        						"type": "EMPLOY",
        						"startNode": "91776593",
        						"endNode": "30814253",
        						"properties": {
        							"role": "董事兼总经理"
        						}
        					}, {
        						"id": "2106034",
        						"type": "INVEST",
        						"startNode": "52260843",
        						"endNode": "37359097",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 95,
        							"shouldCapi": 4750
        						}
        					}, {
        						"id": "2106035",
        						"type": "INVEST",
        						"startNode": "19616549",
        						"endNode": "37359097",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 5,
        							"shouldCapi": 250
        						}
        					}, {
        						"id": "130843990",
        						"type": "LEGAL",
        						"startNode": "91776593",
        						"endNode": "42411778",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "151143333",
        						"type": "EMPLOY",
        						"startNode": "70814180",
        						"endNode": "27906841",
        						"properties": {
        							"role": "总经理"
        						}
        					}, {
        						"id": "168421561",
        						"type": "EMPLOY",
        						"startNode": "67821232",
        						"endNode": "52260843",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "168421567",
        						"type": "EMPLOY",
        						"startNode": "74767000",
        						"endNode": "52260843",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "168421566",
        						"type": "EMPLOY",
        						"startNode": "136011627",
        						"endNode": "52260843",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "168421555",
        						"type": "EMPLOY",
        						"startNode": "72021583",
        						"endNode": "52260843",
        						"properties": {
        							"role": "监事长"
        						}
        					}, {
        						"id": "210652722",
        						"type": "EMPLOY",
        						"startNode": "138059368",
        						"endNode": "781373",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "168421557",
        						"type": "EMPLOY",
        						"startNode": "138059368",
        						"endNode": "52260843",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "168421556",
        						"type": "EMPLOY",
        						"startNode": "102647336",
        						"endNode": "52260843",
        						"properties": {
        							"role": "董事长,经理"
        						}
        					}, {
        						"id": "3705584",
        						"type": "INVEST",
        						"startNode": "52260843",
        						"endNode": "48932091",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 80,
        							"shouldCapi": 80000
        						}
        					}, {
        						"id": "3705585",
        						"type": "INVEST",
        						"startNode": "19616549",
        						"endNode": "48932091",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 20,
        							"shouldCapi": 20000
        						}
        					}, {
        						"id": "143565406",
        						"type": "EMPLOY",
        						"startNode": "138059368",
        						"endNode": "42704608",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "4246179",
        						"type": "INVEST",
        						"startNode": "6015168",
        						"endNode": "50514016",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 100,
        							"shouldCapi": 2000
        						}
        					}, {
        						"id": "5698226",
        						"type": "INVEST",
        						"startNode": "34862636",
        						"endNode": "44697085",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 0,
        							"shouldCapi": 289.7438
        						}
        					}, {
        						"id": "5698227",
        						"type": "INVEST",
        						"startNode": "49801690",
        						"endNode": "44697085",
        						"properties": {
        							"role": "其他投资者",
        							"stockPercent": 0,
        							"shouldCapi": 82.6199
        						}
        					}, {
        						"id": "3717835",
        						"type": "INVEST",
        						"startNode": "56441273",
        						"endNode": "1481843",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 51,
        							"shouldCapi": 25.5
        						}
        					}, {
        						"id": "5698218",
        						"type": "INVEST",
        						"startNode": "53842109",
        						"endNode": "44697085",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 0,
        							"shouldCapi": 76.4997
        						}
        					}, {
        						"id": "172224834",
        						"type": "EMPLOY",
        						"startNode": "130712376",
        						"endNode": "40448122",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "195813546",
        						"type": "EMPLOY",
        						"startNode": "70814180",
        						"endNode": "31098074",
        						"properties": {
        							"role": "执行董事"
        						}
        					}, {
        						"id": "195813548",
        						"type": "EMPLOY",
        						"startNode": "70814180",
        						"endNode": "31098074",
        						"properties": {
        							"role": "总经理"
        						}
        					}, {
        						"id": "92218993",
        						"type": "LEGAL",
        						"startNode": "111454216",
        						"endNode": "28343271",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "195987645",
        						"type": "EMPLOY",
        						"startNode": "70814180",
        						"endNode": "21444787",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "206225234",
        						"type": "EMPLOY",
        						"startNode": "61750511",
        						"endNode": "34862636",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "206225235",
        						"type": "EMPLOY",
        						"startNode": "105408528",
        						"endNode": "34862636",
        						"properties": {
        							"role": "监事"
        						}
        					}, {
        						"id": "206225232",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "34862636",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "206225236",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "34862636",
        						"properties": {
        							"role": "经理"
        						}
        					}, {
        						"id": "92872343",
        						"type": "LEGAL",
        						"startNode": "102647336",
        						"endNode": "10062407",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "206225237",
        						"type": "EMPLOY",
        						"startNode": "84306247",
        						"endNode": "34862636",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "240360818",
        						"type": "EMPLOY",
        						"startNode": "101181150",
        						"endNode": "20076707",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "234143440",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "42411778",
        						"properties": {
        							"role": "执行董事"
        						}
        					}, {
        						"id": "234143441",
        						"type": "EMPLOY",
        						"startNode": "91776593",
        						"endNode": "42411778",
        						"properties": {
        							"role": "经理"
        						}
        					}, {
        						"id": "234143442",
        						"type": "EMPLOY",
        						"startNode": "95221018",
        						"endNode": "42411778",
        						"properties": {
        							"role": "监事"
        						}
        					}, {
        						"id": "140129129",
        						"type": "LEGAL",
        						"startNode": "67821232",
        						"endNode": "19616549",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "5809005",
        						"type": "INVEST",
        						"startNode": "52260843",
        						"endNode": "4130136",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 60,
        							"shouldCapi": 12000
        						}
        					}, {
        						"id": "192874570",
        						"type": "EMPLOY",
        						"startNode": "67821232",
        						"endNode": "41067921",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "192874568",
        						"type": "EMPLOY",
        						"startNode": "102647336",
        						"endNode": "41067921",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "240360814",
        						"type": "EMPLOY",
        						"startNode": "101171886",
        						"endNode": "20076707",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "132385954",
        						"type": "LEGAL",
        						"startNode": "101171886",
        						"endNode": "44697085",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "188676194",
        						"type": "EMPLOY",
        						"startNode": "101171886",
        						"endNode": "38668570",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "188676193",
        						"type": "EMPLOY",
        						"startNode": "125265334",
        						"endNode": "38668570",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "188676191",
        						"type": "EMPLOY",
        						"startNode": "132887594",
        						"endNode": "38668570",
        						"properties": {
        							"role": "监事"
        						}
        					}, {
        						"id": "4836130",
        						"type": "INVEST",
        						"startNode": "28584701",
        						"endNode": "14049595",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 100,
        							"shouldCapi": 21000
        						}
        					}, {
        						"id": "3722062",
        						"type": "INVEST",
        						"startNode": "19106983",
        						"endNode": "26470526",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 0,
        							"shouldCapi": 0
        						}
        					}, {
        						"id": "4959181",
        						"type": "INVEST",
        						"startNode": "41428834",
        						"endNode": "53692134",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 18.4453,
        							"shouldCapi": 221.3436
        						}
        					}, {
        						"id": "98285130",
        						"type": "LEGAL",
        						"startNode": "67539962",
        						"endNode": "94456",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "240604612",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "20729514",
        						"properties": {
        							"role": "执行董事"
        						}
        					}, {
        						"id": "240604611",
        						"type": "EMPLOY",
        						"startNode": "111454216",
        						"endNode": "20729514",
        						"properties": {
        							"role": "总经理"
        						}
        					}, {
        						"id": "240604610",
        						"type": "EMPLOY",
        						"startNode": "91776593",
        						"endNode": "20729514",
        						"properties": {
        							"role": "监事"
        						}
        					}, {
        						"id": "94678586",
        						"type": "LEGAL",
        						"startNode": "67539962",
        						"endNode": "56017001",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "107046345",
        						"type": "LEGAL",
        						"startNode": "111494674",
        						"endNode": "25368839",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "2653073",
        						"type": "INVEST",
        						"startNode": "14121832",
        						"endNode": "25368839",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 100,
        							"shouldCapi": 1000
        						}
        					}, {
        						"id": "93339180",
        						"type": "LEGAL",
        						"startNode": "101171886",
        						"endNode": "53842109",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "109632840",
        						"type": "LEGAL",
        						"startNode": "138059368",
        						"endNode": "53815336",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "115819813",
        						"type": "LEGAL",
        						"startNode": "111454216",
        						"endNode": "46889411",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "5893018",
        						"type": "INVEST",
        						"startNode": "46630928",
        						"endNode": "20729514",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 100,
        							"shouldCapi": 30000
        						}
        					}, {
        						"id": "1973210",
        						"type": "INVEST",
        						"startNode": "29841901",
        						"endNode": "9386315",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 20.8,
        							"shouldCapi": 116.48
        						}
        					}, {
        						"id": "117218616",
        						"type": "LEGAL",
        						"startNode": "76032435",
        						"endNode": "53110181",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "1973209",
        						"type": "INVEST",
        						"startNode": "45124547",
        						"endNode": "9386315",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 62.5,
        							"shouldCapi": 350
        						}
        					}, {
        						"id": "2935787",
        						"type": "INVEST",
        						"startNode": "49801690",
        						"endNode": "41428834",
        						"properties": {
        							"role": "合伙企业",
        							"stockPercent": 0.45,
        							"shouldCapi": 12.2594
        						}
        					}, {
        						"id": "2935781",
        						"type": "INVEST",
        						"startNode": "6564926",
        						"endNode": "41428834",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 5.65,
        							"shouldCapi": 155.2752
        						}
        					}, {
        						"id": "2935782",
        						"type": "INVEST",
        						"startNode": "34862636",
        						"endNode": "41428834",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 5.43,
        							"shouldCapi": 149.3606
        						}
        					}, {
        						"id": "2935777",
        						"type": "INVEST",
        						"startNode": "40448122",
        						"endNode": "41428834",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 23.22,
        							"shouldCapi": 638.6374
        						}
        					}, {
        						"id": "2935778",
        						"type": "INVEST",
        						"startNode": "9358855",
        						"endNode": "41428834",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 19.53,
        							"shouldCapi": 537.1199
        						}
        					}, {
        						"id": "235826653",
        						"type": "EMPLOY",
        						"startNode": "138059368",
        						"endNode": "47032548",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "4477842",
        						"type": "INVEST",
        						"startNode": "52260843",
        						"endNode": "51048164",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 100,
        							"shouldCapi": 42000
        						}
        					}, {
        						"id": "233426435",
        						"type": "EMPLOY",
        						"startNode": "67821232",
        						"endNode": "30051058",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "233426434",
        						"type": "EMPLOY",
        						"startNode": "102647336",
        						"endNode": "30051058",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "3369935",
        						"type": "INVEST",
        						"startNode": "31039917",
        						"endNode": "47698527",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 0.96,
        							"shouldCapi": 1000
        						}
        					}, {
        						"id": "3369932",
        						"type": "INVEST",
        						"startNode": "20919641",
        						"endNode": "47698527",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 1,
        							"shouldCapi": 1040
        						}
        					}, {
        						"id": "135449619",
        						"type": "LEGAL",
        						"startNode": "111494674",
        						"endNode": "929751",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "212062379",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "17917391",
        						"properties": {
        							"role": "执行董事"
        						}
        					}, {
        						"id": "225931642",
        						"type": "EMPLOY",
        						"startNode": "125265334",
        						"endNode": "27382946",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "212062380",
        						"type": "EMPLOY",
        						"startNode": "111494674",
        						"endNode": "17917391",
        						"properties": {
        							"role": "经理"
        						}
        					}, {
        						"id": "3257379",
        						"type": "INVEST",
        						"startNode": "27906841",
        						"endNode": "31098074",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 100,
        							"shouldCapi": 1000
        						}
        					}, {
        						"id": "243640991",
        						"type": "EMPLOY",
        						"startNode": "111454216",
        						"endNode": "46630928",
        						"properties": {
        							"role": "总经理"
        						}
        					}, {
        						"id": "243640993",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "46630928",
        						"properties": {
        							"role": "执行董事"
        						}
        					}, {
        						"id": "243640992",
        						"type": "EMPLOY",
        						"startNode": "91776593",
        						"endNode": "46630928",
        						"properties": {
        							"role": "监事"
        						}
        					}, {
        						"id": "173942368",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "9386315",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "5878813",
        						"type": "INVEST",
        						"startNode": "44697085",
        						"endNode": "20076707",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 70,
        							"shouldCapi": 0
        						}
        					}, {
        						"id": "113967746",
        						"type": "LEGAL",
        						"startNode": "91776593",
        						"endNode": "30814253",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "6282259",
        						"type": "INVEST",
        						"startNode": "31039917",
        						"endNode": "6778704",
        						"properties": {
        							"role": "",
        							"stockPercent": 0.003,
        							"shouldCapi": 0
        						}
        					}, {
        						"id": "249490066",
        						"type": "EMPLOY",
        						"startNode": "102647336",
        						"endNode": "30841307",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "6282258",
        						"type": "INVEST",
        						"startNode": "46906758",
        						"endNode": "6778704",
        						"properties": {
        							"role": "",
        							"stockPercent": 3.0685,
        							"shouldCapi": 1020
        						}
        					}, {
        						"id": "110408411",
        						"type": "LEGAL",
        						"startNode": "102647336",
        						"endNode": "15868072",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "117201580",
        						"type": "LEGAL",
        						"startNode": "67539962",
        						"endNode": "34862636",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "6282255",
        						"type": "INVEST",
        						"startNode": "10336442",
        						"endNode": "6778704",
        						"properties": {
        							"role": "",
        							"stockPercent": 4.9938,
        							"shouldCapi": 1660
        						}
        					}, {
        						"id": "249490063",
        						"type": "EMPLOY",
        						"startNode": "67821232",
        						"endNode": "30841307",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "2057290",
        						"type": "INVEST",
        						"startNode": "52260843",
        						"endNode": "12273234",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 60,
        							"shouldCapi": 3316.2
        						}
        					}, {
        						"id": "150504610",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "14121832",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "6282244",
        						"type": "INVEST",
        						"startNode": "38514470",
        						"endNode": "6778704",
        						"properties": {
        							"role": "",
        							"stockPercent": 10.5292,
        							"shouldCapi": 3500
        						}
        					}, {
        						"id": "150504601",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "14121832",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "185175915",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "22793897",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "185175914",
        						"type": "EMPLOY",
        						"startNode": "105408528",
        						"endNode": "22793897",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "185175916",
        						"type": "EMPLOY",
        						"startNode": "95221018",
        						"endNode": "22793897",
        						"properties": {
        							"role": "监事"
        						}
        					}, {
        						"id": "150504605",
        						"type": "EMPLOY",
        						"startNode": "111494674",
        						"endNode": "14121832",
        						"properties": {
        							"role": "董事兼经理"
        						}
        					}, {
        						"id": "150504607",
        						"type": "EMPLOY",
        						"startNode": "111494674",
        						"endNode": "14121832",
        						"properties": {
        							"role": "董事兼经理"
        						}
        					}, {
        						"id": "95064539",
        						"type": "LEGAL",
        						"startNode": "101171886",
        						"endNode": "56441273",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "9332",
        						"type": "INVEST",
        						"startNode": "25368839",
        						"endNode": "17222095",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 0,
        							"shouldCapi": 0
        						}
        					}, {
        						"id": "9333",
        						"type": "INVEST",
        						"startNode": "34862636",
        						"endNode": "17222095",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 0,
        							"shouldCapi": 0
        						}
        					}, {
        						"id": "5706786",
        						"type": "INVEST",
        						"startNode": "17917391",
        						"endNode": "45124547",
        						"properties": {
        							"role": "其他投资者",
        							"stockPercent": 100,
        							"shouldCapi": 1000
        						}
        					}, {
        						"id": "237441625",
        						"type": "EMPLOY",
        						"startNode": "111494674",
        						"endNode": "45124547",
        						"properties": {
        							"role": "经理"
        						}
        					}, {
        						"id": "237441624",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "45124547",
        						"properties": {
        							"role": "执行董事"
        						}
        					}, {
        						"id": "184192626",
        						"type": "EMPLOY",
        						"startNode": "61750511",
        						"endNode": "21135315",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "184192627",
        						"type": "EMPLOY",
        						"startNode": "105408528",
        						"endNode": "21135315",
        						"properties": {
        							"role": "董事兼总经理"
        						}
        					}, {
        						"id": "184192625",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "21135315",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "184192628",
        						"type": "EMPLOY",
        						"startNode": "95221018",
        						"endNode": "21135315",
        						"properties": {
        							"role": "监事"
        						}
        					}, {
        						"id": "50386841",
        						"type": "INVEST",
        						"startNode": "132887594",
        						"endNode": "1481843",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 10,
        							"shouldCapi": 0
        						}
        					}, {
        						"id": "50386842",
        						"type": "INVEST",
        						"startNode": "101171886",
        						"endNode": "1481843",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 6,
        							"shouldCapi": 0
        						}
        					}, {
        						"id": "175357651",
        						"type": "EMPLOY",
        						"startNode": "102647336",
        						"endNode": "12273234",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "175357649",
        						"type": "EMPLOY",
        						"startNode": "67821232",
        						"endNode": "12273234",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "175357654",
        						"type": "EMPLOY",
        						"startNode": "72021583",
        						"endNode": "12273234",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "1948859",
        						"type": "INVEST",
        						"startNode": "34862636",
        						"endNode": "52260843",
        						"properties": {
        							"stockPercent": 1.25
        						}
        					}, {
        						"id": "158901",
        						"type": "INVEST",
        						"startNode": "28584701",
        						"endNode": "5189027",
        						"properties": {
        							"role": "法人股东",
        							"stockPercent": 100,
        							"shouldCapi": 28800
        						}
        					}, {
        						"id": "167527741",
        						"type": "EMPLOY",
        						"startNode": "95221018",
        						"endNode": "94456",
        						"properties": {
        							"role": "监事"
        						}
        					}, {
        						"id": "103768813",
        						"type": "LEGAL",
        						"startNode": "111454216",
        						"endNode": "13569812",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "128238439",
        						"type": "LEGAL",
        						"startNode": "111494674",
        						"endNode": "23304514",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "157801891",
        						"type": "EMPLOY",
        						"startNode": "121297792",
        						"endNode": "3802438",
        						"properties": {
        							"role": "监事"
        						}
        					}, {
        						"id": "157801890",
        						"type": "EMPLOY",
        						"startNode": "70995224",
        						"endNode": "3802438",
        						"properties": {
        							"role": "执行董事"
        						}
        					}, {
        						"id": "634063",
        						"type": "INVEST",
        						"startNode": "34862636",
        						"endNode": "27906841",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 19.32,
        							"shouldCapi": 136.37
        						}
        					}, {
        						"id": "167527738",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "94456",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "157801889",
        						"type": "EMPLOY",
        						"startNode": "70995224",
        						"endNode": "3802438",
        						"properties": {
        							"role": "经理"
        						}
        					}, {
        						"id": "167527739",
        						"type": "EMPLOY",
        						"startNode": "111454216",
        						"endNode": "94456",
        						"properties": {
        							"role": "董事兼总经理"
        						}
        					}, {
        						"id": "3085540",
        						"type": "INVEST",
        						"startNode": "52260843",
        						"endNode": "41067921",
        						"properties": {
        							"role": "法人股东",
        							"stockPercent": 49.5,
        							"shouldCapi": 1283.04
        						}
        					}, {
        						"id": "1686721",
        						"type": "INVEST",
        						"startNode": "31039917",
        						"endNode": "38514470",
        						"properties": {
        							"role": "",
        							"stockPercent": 0,
        							"shouldCapi": 0
        						}
        					}, {
        						"id": "2839797",
        						"type": "INVEST",
        						"startNode": "49801690",
        						"endNode": "38668570",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 0.45,
        							"shouldCapi": 4.5
        						}
        					}, {
        						"id": "2839796",
        						"type": "INVEST",
        						"startNode": "34862636",
        						"endNode": "38668570",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 1.58,
        							"shouldCapi": 15.78
        						}
        					}, {
        						"id": "107592332",
        						"type": "LEGAL",
        						"startNode": "105408528",
        						"endNode": "24465896",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "215605301",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "15162011",
        						"properties": {
        							"role": "执行董事"
        						}
        					}, {
        						"id": "215605300",
        						"type": "EMPLOY",
        						"startNode": "91776593",
        						"endNode": "15162011",
        						"properties": {
        							"role": "监事"
        						}
        					}, {
        						"id": "215605302",
        						"type": "EMPLOY",
        						"startNode": "111454216",
        						"endNode": "15162011",
        						"properties": {
        							"role": "经理"
        						}
        					}, {
        						"id": "84959712",
        						"type": "LEGAL",
        						"startNode": "20919641",
        						"endNode": "47698527",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "89967012",
        						"type": "LEGAL",
        						"startNode": "111494674",
        						"endNode": "14121832",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "3267787",
        						"type": "INVEST",
        						"startNode": "19106983",
        						"endNode": "21444787",
        						"properties": {
        							"role": "合伙企业",
        							"stockPercent": 0,
        							"shouldCapi": 0
        						}
        					}, {
        						"id": "3267786",
        						"type": "INVEST",
        						"startNode": "27906841",
        						"endNode": "21444787",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 0,
        							"shouldCapi": 0
        						}
        					}, {
        						"id": "2039011",
        						"type": "INVEST",
        						"startNode": "24465896",
        						"endNode": "11449639",
        						"properties": {
        							"role": "法人股东",
        							"stockPercent": 100,
        							"shouldCapi": 200
        						}
        					}, {
        						"id": "95908169",
        						"type": "LEGAL",
        						"startNode": "67821232",
        						"endNode": "52156389",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "4420934",
        						"type": "INVEST",
        						"startNode": "34862636",
        						"endNode": "15162011",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 100,
        							"shouldCapi": 10000
        						}
        					}, {
        						"id": "4132153",
        						"type": "INVEST",
        						"startNode": "19616549",
        						"endNode": "781373",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 5,
        							"shouldCapi": 250
        						}
        					}, {
        						"id": "4132152",
        						"type": "INVEST",
        						"startNode": "52260843",
        						"endNode": "781373",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 95,
        							"shouldCapi": 4750
        						}
        					}, {
        						"id": "2581807",
        						"type": "INVEST",
        						"startNode": "52260843",
        						"endNode": "17149007",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 75,
        							"shouldCapi": 28500
        						}
        					}, {
        						"id": "52235780",
        						"type": "INVEST",
        						"startNode": "101171886",
        						"endNode": "17559925",
        						"properties": {
        							"role": "",
        							"stockPercent": 76.25,
        							"shouldCapi": 19.0625
        						}
        					}, {
        						"id": "165565633",
        						"type": "EMPLOY",
        						"startNode": "70814180",
        						"endNode": "55105166",
        						"properties": {
        							"role": "总经理"
        						}
        					}, {
        						"id": "212609437",
        						"type": "EMPLOY",
        						"startNode": "91776593",
        						"endNode": "50514016",
        						"properties": {
        							"role": "监事"
        						}
        					}, {
        						"id": "212609438",
        						"type": "EMPLOY",
        						"startNode": "111454216",
        						"endNode": "50514016",
        						"properties": {
        							"role": "执行董事"
        						}
        					}, {
        						"id": "143932844",
        						"type": "EMPLOY",
        						"startNode": "136011627",
        						"endNode": "29507713",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "140524888",
        						"type": "EMPLOY",
        						"startNode": "61964144",
        						"endNode": "17222095",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "138341639",
        						"type": "LEGAL",
        						"startNode": "102647336",
        						"endNode": "30841307",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "3482892",
        						"type": "INVEST",
        						"startNode": "42411778",
        						"endNode": "30814253",
        						"properties": {
        							"role": "法人股东",
        							"stockPercent": 80,
        							"shouldCapi": 800
        						}
        					}, {
        						"id": "106716005",
        						"type": "LEGAL",
        						"startNode": "111494674",
        						"endNode": "14890432",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "140524889",
        						"type": "EMPLOY",
        						"startNode": "111494674",
        						"endNode": "17222095",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "134003395",
        						"type": "LEGAL",
        						"startNode": "111454216",
        						"endNode": "20729514",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "143932843",
        						"type": "EMPLOY",
        						"startNode": "138059368",
        						"endNode": "29507713",
        						"properties": {
        							"role": "董事长,经理"
        						}
        					}, {
        						"id": "1793375",
        						"type": "INVEST",
        						"startNode": "30814253",
        						"endNode": "25955383",
        						"properties": {
        							"role": "法人股东",
        							"stockPercent": 0.5,
        							"shouldCapi": 1000
        						}
        					}, {
        						"id": "1793374",
        						"type": "INVEST",
        						"startNode": "34862636",
        						"endNode": "25955383",
        						"properties": {
        							"role": "法人股东",
        							"stockPercent": 99.5,
        							"shouldCapi": 200000
        						}
        					}, {
        						"id": "26518750",
        						"type": "INVEST",
        						"startNode": "67539962",
        						"endNode": "38514470",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 0,
        							"shouldCapi": 200
        						}
        					}, {
        						"id": "206260507",
        						"type": "EMPLOY",
        						"startNode": "76032435",
        						"endNode": "53110181",
        						"properties": {
        							"role": "经理"
        						}
        					}, {
        						"id": "206260506",
        						"type": "EMPLOY",
        						"startNode": "76032435",
        						"endNode": "53110181",
        						"properties": {
        							"role": "执行董事"
        						}
        					}, {
        						"id": "195231472",
        						"type": "EMPLOY",
        						"startNode": "61964144",
        						"endNode": "38533138",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "195231473",
        						"type": "EMPLOY",
        						"startNode": "111494674",
        						"endNode": "38533138",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "1596739",
        						"type": "INVEST",
        						"startNode": "6015168",
        						"endNode": "94456",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 100,
        							"shouldCapi": 200000
        						}
        					}, {
        						"id": "165565630",
        						"type": "EMPLOY",
        						"startNode": "95221018",
        						"endNode": "55105166",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "175050510",
        						"type": "EMPLOY",
        						"startNode": "105408528",
        						"endNode": "11449639",
        						"properties": {
        							"role": "执行董事"
        						}
        					}, {
        						"id": "175050508",
        						"type": "EMPLOY",
        						"startNode": "95221018",
        						"endNode": "11449639",
        						"properties": {
        							"role": "监事"
        						}
        					}, {
        						"id": "165565629",
        						"type": "EMPLOY",
        						"startNode": "70814180",
        						"endNode": "55105166",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "237693772",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "29841901",
        						"properties": {
        							"role": "监事"
        						}
        					}, {
        						"id": "162673876",
        						"type": "EMPLOY",
        						"startNode": "67821232",
        						"endNode": "52156389",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "116794257",
        						"type": "LEGAL",
        						"startNode": "111494674",
        						"endNode": "26468356",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "26518757",
        						"type": "INVEST",
        						"startNode": "95221018",
        						"endNode": "38514470",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 0,
        							"shouldCapi": 1700
        						}
        					}, {
        						"id": "160140537",
        						"type": "EMPLOY",
        						"startNode": "111454216",
        						"endNode": "56017001",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "26518758",
        						"type": "INVEST",
        						"startNode": "111494674",
        						"endNode": "38514470",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 0,
        							"shouldCapi": 100
        						}
        					}, {
        						"id": "26518752",
        						"type": "INVEST",
        						"startNode": "111454216",
        						"endNode": "38514470",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 0,
        							"shouldCapi": 400
        						}
        					}, {
        						"id": "26518753",
        						"type": "INVEST",
        						"startNode": "61964144",
        						"endNode": "38514470",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 0,
        							"shouldCapi": 200
        						}
        					}, {
        						"id": "121682486",
        						"type": "LEGAL",
        						"startNode": "102647336",
        						"endNode": "8067068",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "26518755",
        						"type": "INVEST",
        						"startNode": "105408528",
        						"endNode": "38514470",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 0,
        							"shouldCapi": 200
        						}
        					}, {
        						"id": "160140535",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "56017001",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "160140533",
        						"type": "EMPLOY",
        						"startNode": "95221018",
        						"endNode": "56017001",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "216570219",
        						"type": "EMPLOY",
        						"startNode": "102647336",
        						"endNode": "51048164",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "216570220",
        						"type": "EMPLOY",
        						"startNode": "74767000",
        						"endNode": "51048164",
        						"properties": {
        							"role": "董事,经理"
        						}
        					}, {
        						"id": "220143756",
        						"type": "EMPLOY",
        						"startNode": "84306247",
        						"endNode": "9097458",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "220143755",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "9097458",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "183033715",
        						"type": "EMPLOY",
        						"startNode": "67821232",
        						"endNode": "21912320",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "1658245",
        						"type": "INVEST",
        						"startNode": "19616549",
        						"endNode": "33667381",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 10,
        							"shouldCapi": 600
        						}
        					}, {
        						"id": "183033716",
        						"type": "EMPLOY",
        						"startNode": "102647336",
        						"endNode": "21912320",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "205396386",
        						"type": "EMPLOY",
        						"startNode": "111494674",
        						"endNode": "26468356",
        						"properties": {
        							"role": "经理"
        						}
        					}, {
        						"id": "1658244",
        						"type": "INVEST",
        						"startNode": "52260843",
        						"endNode": "33667381",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 90,
        							"shouldCapi": 5400
        						}
        					}, {
        						"id": "205396387",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "26468356",
        						"properties": {
        							"role": "执行董事"
        						}
        					}, {
        						"id": "3845527",
        						"type": "INVEST",
        						"startNode": "51868419",
        						"endNode": "27426550",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 100,
        							"shouldCapi": 1000
        						}
        					}, {
        						"id": "229275675",
        						"type": "EMPLOY",
        						"startNode": "125265334",
        						"endNode": "41727146",
        						"properties": {
        							"role": "经理"
        						}
        					}, {
        						"id": "229275673",
        						"type": "EMPLOY",
        						"startNode": "125265334",
        						"endNode": "41727146",
        						"properties": {
        							"role": "执行董事"
        						}
        					}, {
        						"id": "4689394",
        						"type": "INVEST",
        						"startNode": "6778704",
        						"endNode": "19106983",
        						"properties": {
        							"role": "",
        							"stockPercent": 29.35,
        							"shouldCapi": 33240
        						}
        					}, {
        						"id": "4689393",
        						"type": "INVEST",
        						"startNode": "31039917",
        						"endNode": "19106983",
        						"properties": {
        							"role": "",
        							"stockPercent": 70.65,
        							"shouldCapi": 80000
        						}
        					}, {
        						"id": "68100536",
        						"type": "INVEST",
        						"startNode": "125265334",
        						"endNode": "41727146",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 40,
        							"shouldCapi": 0
        						}
        					}, {
        						"id": "205810172",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "27426550",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "205810175",
        						"type": "EMPLOY",
        						"startNode": "84306247",
        						"endNode": "27426550",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "240552848",
        						"type": "EMPLOY",
        						"startNode": "105408528",
        						"endNode": "36973248",
        						"properties": {
        							"role": "总经理"
        						}
        					}, {
        						"id": "240552849",
        						"type": "EMPLOY",
        						"startNode": "95221018",
        						"endNode": "36973248",
        						"properties": {
        							"role": "监事"
        						}
        					}, {
        						"id": "4015600",
        						"type": "INVEST",
        						"startNode": "31039917",
        						"endNode": "46906758",
        						"properties": {
        							"role": "",
        							"stockPercent": 0,
        							"shouldCapi": 0
        						}
        					}, {
        						"id": "2481643",
        						"type": "INVEST",
        						"startNode": "19106983",
        						"endNode": "26798560",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 9.919,
        							"shouldCapi": 112.6731
        						}
        					}, {
        						"id": "115929913",
        						"type": "LEGAL",
        						"startNode": "132887594",
        						"endNode": "1481843",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "2481649",
        						"type": "INVEST",
        						"startNode": "27906841",
        						"endNode": "26798560",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 2.8333,
        							"shouldCapi": 32.1846
        						}
        					}, {
        						"id": "128469628",
        						"type": "LEGAL",
        						"startNode": "125265334",
        						"endNode": "41727146",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "2481650",
        						"type": "INVEST",
        						"startNode": "16967162",
        						"endNode": "26798560",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 1.6104,
        							"shouldCapi": 18.2927
        						}
        					}, {
        						"id": "240552847",
        						"type": "EMPLOY",
        						"startNode": "105408528",
        						"endNode": "36973248",
        						"properties": {
        							"role": "执行董事"
        						}
        					}, {
        						"id": "38641581",
        						"type": "INVEST",
        						"startNode": "105408528",
        						"endNode": "24465896",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 87.92,
        							"shouldCapi": 4396.173
        						}
        					}, {
        						"id": "38641583",
        						"type": "INVEST",
        						"startNode": "95221018",
        						"endNode": "24465896",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 2.01,
        							"shouldCapi": 100.5
        						}
        					}, {
        						"id": "38641582",
        						"type": "INVEST",
        						"startNode": "111454216",
        						"endNode": "24465896",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 10.07,
        							"shouldCapi": 503.327
        						}
        					}, {
        						"id": "2575823",
        						"type": "INVEST",
        						"startNode": "28584701",
        						"endNode": "21135315",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 100,
        							"shouldCapi": 100
        						}
        					}, {
        						"id": "207503966",
        						"type": "EMPLOY",
        						"startNode": "111494674",
        						"endNode": "23436441",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "207503963",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "23436441",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "137195050",
        						"type": "LEGAL",
        						"startNode": "111454216",
        						"endNode": "24315942",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "5512798",
        						"type": "INVEST",
        						"startNode": "31039917",
        						"endNode": "42411778",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 100,
        							"shouldCapi": 5000
        						}
        					}, {
        						"id": "247134376",
        						"type": "EMPLOY",
        						"startNode": "111454216",
        						"endNode": "24315942",
        						"properties": {
        							"role": "经理"
        						}
        					}, {
        						"id": "86577981",
        						"type": "LEGAL",
        						"startNode": "138059368",
        						"endNode": "42704608",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "86336306",
        						"type": "LEGAL",
        						"startNode": "105408528",
        						"endNode": "5189027",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "247134375",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "24315942",
        						"properties": {
        							"role": "执行董事"
        						}
        					}, {
        						"id": "253137206",
        						"type": "EMPLOY",
        						"startNode": "67821232",
        						"endNode": "19616549",
        						"properties": {
        							"role": "执行董事,经理"
        						}
        					}, {
        						"id": "106889341",
        						"type": "LEGAL",
        						"startNode": "105408528",
        						"endNode": "22793897",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "1310271",
        						"type": "INVEST",
        						"startNode": "19616549",
        						"endNode": "52156389",
        						"properties": {
        							"role": "",
        							"stockPercent": 30,
        							"shouldCapi": 1500
        						}
        					}, {
        						"id": "1310270",
        						"type": "INVEST",
        						"startNode": "52260843",
        						"endNode": "52156389",
        						"properties": {
        							"role": "",
        							"stockPercent": 70,
        							"shouldCapi": 3500
        						}
        					}, {
        						"id": "155064080",
        						"type": "EMPLOY",
        						"startNode": "101171886",
        						"endNode": "25141798",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "189216117",
        						"type": "EMPLOY",
        						"startNode": "138059368",
        						"endNode": "17083398",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "120326424",
        						"type": "LEGAL",
        						"startNode": "111454216",
        						"endNode": "50514016",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "36553752",
        						"type": "INVEST",
        						"startNode": "84306247",
        						"endNode": "20919641",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 50,
        							"shouldCapi": 500
        						}
        					}, {
        						"id": "3872259",
        						"type": "INVEST",
        						"startNode": "34862636",
        						"endNode": "53110181",
        						"properties": {
        							"role": "法人股东",
        							"stockPercent": 10,
        							"shouldCapi": 20
        						}
        					}, {
        						"id": "820784",
        						"type": "INVEST",
        						"startNode": "52260843",
        						"endNode": "23919128",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 73,
        							"shouldCapi": 505.744
        						}
        					}, {
        						"id": "1998423",
        						"type": "INVEST",
        						"startNode": "34862636",
        						"endNode": "31039917",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 100,
        							"shouldCapi": 120000
        						}
        					}, {
        						"id": "44518638",
        						"type": "INVEST",
        						"startNode": "67539962",
        						"endNode": "38347294",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 51,
        							"shouldCapi": 1530
        						}
        					}, {
        						"id": "515700",
        						"type": "INVEST",
        						"startNode": "44697085",
        						"endNode": "35384641",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 80,
        							"shouldCapi": 300
        						}
        					}, {
        						"id": "108865550",
        						"type": "LEGAL",
        						"startNode": "138059368",
        						"endNode": "17083398",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "52198763",
        						"type": "INVEST",
        						"startNode": "76032435",
        						"endNode": "53110181",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 90,
        							"shouldCapi": 180
        						}
        					}, {
        						"id": "168817781",
        						"type": "EMPLOY",
        						"startNode": "111454216",
        						"endNode": "657610",
        						"properties": {
        							"role": "监事"
        						}
        					}, {
        						"id": "168817780",
        						"type": "EMPLOY",
        						"startNode": "95221018",
        						"endNode": "657610",
        						"properties": {
        							"role": "经理"
        						}
        					}, {
        						"id": "168817779",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "657610",
        						"properties": {
        							"role": "执行董事"
        						}
        					}, {
        						"id": "93535006",
        						"type": "LEGAL",
        						"startNode": "70995224",
        						"endNode": "3802438",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "221924258",
        						"type": "EMPLOY",
        						"startNode": "130712376",
        						"endNode": "9358855",
        						"properties": {
        							"role": "总经理"
        						}
        					}, {
        						"id": "221924257",
        						"type": "EMPLOY",
        						"startNode": "130712376",
        						"endNode": "9358855",
        						"properties": {
        							"role": "执行董事"
        						}
        					}, {
        						"id": "6071961",
        						"type": "INVEST",
        						"startNode": "31039917",
        						"endNode": "16648410",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 0,
        							"shouldCapi": 0
        						}
        					}, {
        						"id": "6071962",
        						"type": "INVEST",
        						"startNode": "6564926",
        						"endNode": "16648410",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 0,
        							"shouldCapi": 0
        						}
        					}, {
        						"id": "102508759",
        						"type": "LEGAL",
        						"startNode": "138059368",
        						"endNode": "37359097",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "3704565",
        						"type": "INVEST",
        						"startNode": "6015168",
        						"endNode": "46889411",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 100,
        							"shouldCapi": 5000
        						}
        					}, {
        						"id": "154329058",
        						"type": "EMPLOY",
        						"startNode": "102647336",
        						"endNode": "23919128",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "154329059",
        						"type": "EMPLOY",
        						"startNode": "136011627",
        						"endNode": "23919128",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "5215897",
        						"type": "INVEST",
        						"startNode": "38347294",
        						"endNode": "32117662",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 7.65,
        							"shouldCapi": 1530
        						}
        					}, {
        						"id": "154329061",
        						"type": "EMPLOY",
        						"startNode": "67821232",
        						"endNode": "23919128",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "5215896",
        						"type": "INVEST",
        						"startNode": "29841901",
        						"endNode": "32117662",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 89.35,
        							"shouldCapi": 17870
        						}
        					}, {
        						"id": "154329064",
        						"type": "EMPLOY",
        						"startNode": "138059368",
        						"endNode": "23919128",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "156444582",
        						"type": "EMPLOY",
        						"startNode": "102647336",
        						"endNode": "10062407",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "133884172",
        						"type": "LEGAL",
        						"startNode": "101171886",
        						"endNode": "20076707",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "156444585",
        						"type": "EMPLOY",
        						"startNode": "67821232",
        						"endNode": "10062407",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "156444589",
        						"type": "EMPLOY",
        						"startNode": "72021583",
        						"endNode": "10062407",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "243660922",
        						"type": "EMPLOY",
        						"startNode": "111454216",
        						"endNode": "16648410",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "4689735",
        						"type": "INVEST",
        						"startNode": "51868419",
        						"endNode": "9097458",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 100,
        							"shouldCapi": 1000
        						}
        					}, {
        						"id": "149112807",
        						"type": "EMPLOY",
        						"startNode": "87093455",
        						"endNode": "35384641",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "149112811",
        						"type": "EMPLOY",
        						"startNode": "101171886",
        						"endNode": "35384641",
        						"properties": {
        							"role": "总经理"
        						}
        					}, {
        						"id": "149112809",
        						"type": "EMPLOY",
        						"startNode": "101171886",
        						"endNode": "35384641",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "160931483",
        						"type": "EMPLOY",
        						"startNode": "101171886",
        						"endNode": "56441273",
        						"properties": {
        							"role": "执行董事"
        						}
        					}, {
        						"id": "160931481",
        						"type": "EMPLOY",
        						"startNode": "87093455",
        						"endNode": "56441273",
        						"properties": {
        							"role": "监事"
        						}
        					}, {
        						"id": "104304935",
        						"type": "LEGAL",
        						"startNode": "95221018",
        						"endNode": "53670436",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "206316382",
        						"type": "EMPLOY",
        						"startNode": "101171886",
        						"endNode": "17559925",
        						"properties": {
        							"role": "执行合伙人"
        						}
        					}, {
        						"id": "6276936",
        						"type": "INVEST",
        						"startNode": "5189027",
        						"endNode": "24315942",
        						"properties": {
        							"role": "法人股东",
        							"stockPercent": 100,
        							"shouldCapi": 100
        						}
        					}, {
        						"id": "124727411",
        						"type": "LEGAL",
        						"startNode": "102647336",
        						"endNode": "26278264",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "45215120",
        						"type": "INVEST",
        						"startNode": "102647336",
        						"endNode": "52260843",
        						"properties": {
        							"stockPercent": 2.08
        						}
        					}, {
        						"id": "160095907",
        						"type": "EMPLOY",
        						"startNode": "132887594",
        						"endNode": "13487102",
        						"properties": {
        							"role": "监事"
        						}
        					}, {
        						"id": "160095908",
        						"type": "EMPLOY",
        						"startNode": "101171886",
        						"endNode": "13487102",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "102295854",
        						"type": "LEGAL",
        						"startNode": "111454216",
        						"endNode": "16515752",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "90462803",
        						"type": "LEGAL",
        						"startNode": "102647336",
        						"endNode": "2810359",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "122251377",
        						"type": "LEGAL",
        						"startNode": "102647336",
        						"endNode": "51048164",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "188223",
        						"type": "INVEST",
        						"startNode": "52260843",
        						"endNode": "42704608",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 90,
        							"shouldCapi": 7200
        						}
        					}, {
        						"id": "188224",
        						"type": "INVEST",
        						"startNode": "19616549",
        						"endNode": "42704608",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 10,
        							"shouldCapi": 800
        						}
        					}, {
        						"id": "133177530",
        						"type": "LEGAL",
        						"startNode": "102647336",
        						"endNode": "49332088",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "5482265",
        						"type": "INVEST",
        						"startNode": "28584701",
        						"endNode": "7270847",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 100,
        							"shouldCapi": 10000
        						}
        					}, {
        						"id": "176190923",
        						"type": "EMPLOY",
        						"startNode": "138059368",
        						"endNode": "37359097",
        						"properties": {
        							"role": "董事长兼总经理"
        						}
        					}, {
        						"id": "186618959",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "24465896",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "186618958",
        						"type": "EMPLOY",
        						"startNode": "95221018",
        						"endNode": "24465896",
        						"properties": {
        							"role": "监事"
        						}
        					}, {
        						"id": "186618957",
        						"type": "EMPLOY",
        						"startNode": "111454216",
        						"endNode": "24465896",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "2826105",
        						"type": "INVEST",
        						"startNode": "44697085",
        						"endNode": "34862212",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 51,
        							"shouldCapi": 200.0016
        						}
        					}, {
        						"id": "186618956",
        						"type": "EMPLOY",
        						"startNode": "105408528",
        						"endNode": "24465896",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "186618955",
        						"type": "EMPLOY",
        						"startNode": "105408528",
        						"endNode": "24465896",
        						"properties": {
        							"role": "经理"
        						}
        					}, {
        						"id": "224731709",
        						"type": "EMPLOY",
        						"startNode": "70995224",
        						"endNode": "53692134",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "61801717",
        						"type": "INVEST",
        						"startNode": "95221018",
        						"endNode": "10336442",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 0,
        							"shouldCapi": 40
        						}
        					}, {
        						"id": "864110",
        						"type": "INVEST",
        						"startNode": "56441273",
        						"endNode": "25141798",
        						"properties": {
        							"role": "有限责任",
        							"stockPercent": 2,
        							"shouldCapi": 3.0769
        						}
        					}, {
        						"id": "3821399",
        						"type": "INVEST",
        						"startNode": "23304514",
        						"endNode": "26468356",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 100,
        							"shouldCapi": 21550
        						}
        					}, {
        						"id": "229104339",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "32117662",
        						"properties": {
        							"role": "执行董事兼经理"
        						}
        					}, {
        						"id": "6629151",
        						"type": "INVEST",
        						"startNode": "52260843",
        						"endNode": "19616549",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 100,
        							"shouldCapi": 2320
        						}
        					}, {
        						"id": "5029680",
        						"type": "INVEST",
        						"startNode": "41727146",
        						"endNode": "27382946",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 5.83,
        							"shouldCapi": 2.2462
        						}
        					}, {
        						"id": "178779431",
        						"type": "EMPLOY",
        						"startNode": "95221018",
        						"endNode": "13569812",
        						"properties": {
        							"role": "监事"
        						}
        					}, {
        						"id": "184820871",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "14890432",
        						"properties": {
        							"role": "执行董事"
        						}
        					}, {
        						"id": "94657063",
        						"type": "LEGAL",
        						"startNode": "101171886",
        						"endNode": "13487102",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "178779435",
        						"type": "EMPLOY",
        						"startNode": "111454216",
        						"endNode": "13569812",
        						"properties": {
        							"role": "经理"
        						}
        					}, {
        						"id": "178779434",
        						"type": "EMPLOY",
        						"startNode": "61750511",
        						"endNode": "13569812",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "184820873",
        						"type": "EMPLOY",
        						"startNode": "111494674",
        						"endNode": "14890432",
        						"properties": {
        							"role": "总经理"
        						}
        					}, {
        						"id": "178779433",
        						"type": "EMPLOY",
        						"startNode": "111454216",
        						"endNode": "13569812",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "178779432",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "13569812",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "222517971",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "38566723",
        						"properties": {
        							"role": "执行董事兼总经理"
        						}
        					}, {
        						"id": "222517970",
        						"type": "EMPLOY",
        						"startNode": "105408528",
        						"endNode": "38566723",
        						"properties": {
        							"role": "监事"
        						}
        					}, {
        						"id": "155102892",
        						"type": "EMPLOY",
        						"startNode": "111454216",
        						"endNode": "28343271",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "155102890",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "28343271",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "157400821",
        						"type": "EMPLOY",
        						"startNode": "101372578",
        						"endNode": "53842109",
        						"properties": {
        							"role": "监事"
        						}
        					}, {
        						"id": "157400823",
        						"type": "EMPLOY",
        						"startNode": "101171886",
        						"endNode": "53842109",
        						"properties": {
        							"role": "总经理"
        						}
        					}, {
        						"id": "73620469",
        						"type": "INVEST",
        						"startNode": "101181150",
        						"endNode": "44697085",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 0,
        							"shouldCapi": 20.4
        						}
        					}, {
        						"id": "155102889",
        						"type": "EMPLOY",
        						"startNode": "95221018",
        						"endNode": "28343271",
        						"properties": {
        							"role": "监事"
        						}
        					}, {
        						"id": "157400822",
        						"type": "EMPLOY",
        						"startNode": "101171886",
        						"endNode": "53842109",
        						"properties": {
        							"role": "执行董事"
        						}
        					}, {
        						"id": "73620468",
        						"type": "INVEST",
        						"startNode": "101372578",
        						"endNode": "44697085",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 0,
        							"shouldCapi": 19.5074
        						}
        					}, {
        						"id": "221620908",
        						"type": "EMPLOY",
        						"startNode": "102647336",
        						"endNode": "26278264",
        						"properties": {
        							"role": "董事长"
        						}
        					}, {
        						"id": "73620473",
        						"type": "INVEST",
        						"startNode": "101171886",
        						"endNode": "44697085",
        						"properties": {
        							"role": "自然人股东",
        							"stockPercent": 0,
        							"shouldCapi": 371.2394
        						}
        					}, {
        						"id": "221620910",
        						"type": "EMPLOY",
        						"startNode": "67821232",
        						"endNode": "26278264",
        						"properties": {
        							"role": "董事"
        						}
        					}, {
        						"id": "866220",
        						"type": "INVEST",
        						"startNode": "13569812",
        						"endNode": "28343271",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 100,
        							"shouldCapi": 3000
        						}
        					}, {
        						"id": "195126285",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "38347294",
        						"properties": {
        							"role": "执行董事"
        						}
        					}, {
        						"id": "195126284",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "38347294",
        						"properties": {
        							"role": "经理"
        						}
        					}, {
        						"id": "207641556",
        						"type": "EMPLOY",
        						"startNode": "67539962",
        						"endNode": "31157266",
        						"properties": {
        							"role": "执行董事"
        						}
        					}, {
        						"id": "207641557",
        						"type": "EMPLOY",
        						"startNode": "111494674",
        						"endNode": "31157266",
        						"properties": {
        							"role": "经理"
        						}
        					}, {
        						"id": "4409341",
        						"type": "INVEST",
        						"startNode": "52260843",
        						"endNode": "8067068",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 75,
        							"shouldCapi": 1125
        						}
        					}, {
        						"id": "5889928",
        						"type": "INVEST",
        						"startNode": "28584701",
        						"endNode": "36973248",
        						"properties": {
        							"role": "法人股东",
        							"stockPercent": 100,
        							"shouldCapi": 100
        						}
        					}, {
        						"id": "105843111",
        						"type": "LEGAL",
        						"startNode": "102647336",
        						"endNode": "21912320",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "106410428",
        						"type": "LEGAL",
        						"startNode": "105408528",
        						"endNode": "21135315",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "139073445",
        						"type": "LEGAL",
        						"startNode": "111454216",
        						"endNode": "27983365",
        						"properties": {
        							"role": ""
        						}
        					}, {
        						"id": "3223489",
        						"type": "INVEST",
        						"startNode": "17222095",
        						"endNode": "38533138",
        						"properties": {
        							"role": "法人股东",
        							"stockPercent": 100,
        							"shouldCapi": 100
        						}
        					}, {
        						"id": "757752",
        						"type": "INVEST",
        						"startNode": "19106983",
        						"endNode": "3370376",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 26,
        							"shouldCapi": 520
        						}
        					}, {
        						"id": "1159144",
        						"type": "INVEST",
        						"startNode": "38668570",
        						"endNode": "13487102",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 100,
        							"shouldCapi": 50
        						}
        					}, {
        						"id": "757750",
        						"type": "INVEST",
        						"startNode": "16648410",
        						"endNode": "3370376",
        						"properties": {
        							"role": "企业法人",
        							"stockPercent": 40,
        							"shouldCapi": 800
        						}
        					}]
        				}
        			}]
        		}],
        		"errors": []
        	}
        }

        return jsonify(dic)
    else:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True,port=5000)
