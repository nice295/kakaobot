#subway_return = SubwayInfo.get_subway_station(data)
import json
import urllib.request
import urllib.parse
import ast
import re
from operator import eq

subwayID = [[1001, "수도권 1호선"],[1002, "수도권 2호선"],[1003, "수도권 3호선"],[1004, "수도권 4호선"],[1005, "수도권 5호선"]
,[1006, "수도권 6호선"],[1007, "수도권 7호선"],[1008, "수도권 8호선"],[1009, "수도권 9호선"],[1065,"수도권 공항철도"],[1071,"수도권 수인선"],[1075,"수도권 분당선"]
,[1075,"수도권 분당선"],[1063,"경의중앙선"],[1067,"수도권 경춘선"],[1077,"수도권 신분당선"],[1077,"수도권 신분당선"]]

def get_subway_station(json_Data):
    searchST = str(json_Data['result']['parameters']['subway_station'])
    print("searchST " + searchST)
    res = ""
    ACCESS = "rxJqZMHh6oQDUSfc7Kh42uCXZuHEhmj7dY7VWber2ryr9L5t2CFRy3z834JMR7RygMzaVby7ZQ3sW%2ByCZZn0Ig%3D%3D"
    my = "n+1iCTjka3qgrhco9Xl3e05Depf0hpct6SJUYUEH38E"
    encMy = urllib.parse.quote_plus(my)
    encST = urllib.parse.quote_plus(searchST)

    odUrl = "https://api.odsay.com/v1/api/searchStation?lang=0&stationName="+encST+"&CID=1000&stationClass=2&apiKey="+encMy

    request = urllib.request.Request(odUrl)
    response = urllib.request.urlopen(request)

    json_rt = response.read().decode('utf-8')
    st = json.loads(json_rt)

    subway_station_list = []
    for i in range(0,len(st['result']['station'])):
        if st['result']['station'][i]['stationName'] == searchST:
            subway_station_list.append(st['result']['station'][i]['laneName'])

    if len(subway_station_list) == 1 :
        return [1,res,subway_station_list]

    else :
        res += "🤔 호선을 선택해 주세요. 🤗" + "\n"+"(올바른 숫자를 입력하는 센스!)\n\n"
        for idx, line_number in enumerate(subway_station_list):
            res += str(idx+1) +". " + line_number + "\n"
        return [2,res,subway_station_list]
#
#     res = ""
#     duplicate = False
#     stationName = str(json_Data['result']['parameters']['subway_station'])
#     # line_number = str(json_Data['result']['parameters']['line_number'])
#     SNList = [["반포역", "신반포역", "구반포역"], ["논현역", "신논현역"], ["뚝섬역", "뚝섬유원지역"]]
#
#     subway_station_dic = {}
#     print("입력한 역이름 :"+stationName)
#     for e in SNList:
#         if stationName in e:
#             duplicate = True#선택사항 존재
#             for s in e:
#                 data = getStationInfo(s)
#                 subway_station_dic[s].append(int(data['result']['station'][0]['stationID']))
#
#     if duplicate == False:
#         data = getStationInfo(stationName)
#         print(data)
#         subway_station_dic[stationName] = int(data['result']['station'][0]['stationID'])
#
#     if len(subway_station_dic.keys()) == 1:
#         return[1,res,list(subway_station_dic.keys()), subway_station_dic]
#     else:
#         res += "🤔 지하철 역을 선택해 주세요. 🤗" + "\n"
#         for i in range(0, len(subway_station_dic.keys())):
#             res += str(i+1)+". "+list(subway_station_dic.keys())[i]+"\n"
#         return [2,res,list(subway_station_dic.keys()),subway_station_dic]

# def get_result(stationName, line_number):
def config_exist_subway_station_and_number(subwayData):
    stationName = subwayData[0]
    data = getStationInfo(stationName)
    station_info = data['result']['station']
    Exist = False
    for idx, info in enumerate(station_info):
        if subwayData[1] in info['laneName'] and stationName in info['stationName']:
            Exist = True
    return Exist

def get_subway_station_and_number_information(subwayData):
#     option = get_option(stationName)
#
#     stationName = "서울역"
    #stationName = str(json_Data['result']['parameters']['subway_station'])
    stationName = subwayData[0]
    print("lineNumber : "+subwayData[1])
    print("lineNumber type: "+str(type(subwayData[1])))
    subwayData[1] = re.sub('\'',"",subwayData[1])
    subwayData[1] = re.sub('수도권 ',"",subwayData[1])
    print("stationName : "+subwayData[0])
    print("lineNumber : "+subwayData[1])
    print("lineNumber type: "+str(type(subwayData[1])))

    data = getStationInfo(stationName)

    station_info = data['result']['station']
    current_stationID = 0

    print(json.loads(json.dumps(data)))
    # print("station Dictionary : "+str(subwayData[1]))
    # print("station Dictionary type: "+str(type(subwayData[1])))
    # print("station ID : "+str(subwayData[1][subwayData[0]]))
    for idx, info in enumerate(station_info):
        if subwayData[1] in info['laneName']:
            current_stationID = int(data['result']['station'][idx]['stationID'])
            current_laneName = data['result']['station'][idx]['laneName'] #예:수도권 1호선

    line_number = subwayData[1]
    #if eq(direction,"상행") or eq(direction,"내선"):
    #상행일 때
    direction = "상행"
    stationID = [current_stationID+4,current_stationID+2, current_stationID]
    text=""
    canUse = True
    StationExistList=[]
    StationNameList=[]
    StationExistNameList = []
    for idx, get_stationID in enumerate(stationID):
        print("=======getStationResult INFO=======")
        print("current_stationID : "+str(current_stationID))
        print("get_stationID : "+str(get_stationID))
        print("idx*2 : "+str(idx*2))
        print("current_laneName : "+str(current_laneName))
        print("direction : "+direction)
        print("line_number : "+line_number)
        new_stationName = getStationName(get_stationID)
        if eq(new_stationName,"error"):
            text="공공데이터에 문제가 생겼어요😂😂\n10초 뒤에 다시 이용해주시겠어요?\n꼭 다시 오셔야해요❤"
            canUse = False
            break
        num = getStationResult(current_stationID,get_stationID,new_stationName, idx*2,current_laneName,direction,line_number)

        if eq(num,"error"):
            text="공공데이터에 문제가 생겼어요😂😂\n10초 뒤에 다시 이용해주시겠어요?\n꼭 다시 오셔야해요❤"
            canUse = False
            break
        elif eq(num,"none"):
            continue
        else:
            StationExistList.append(num)
    print("station Exist List : "+str(StationExistList))
    if canUse:
        StationExistNameList = []
        #if eq(direction,"상행") or eq(direction,"내선"):
        StationIDList = [current_stationID+6,current_stationID+5,current_stationID+4,current_stationID+3,current_stationID+2, current_stationID+1,current_stationID]
        # if eq(direction,"하행") or eq(direction,"외선"):
        #     StationIDList = [current_stationID-6,current_stationID-5,current_stationID-4,current_stationID-3,current_stationID-2, current_stationID-1,current_stationID]
        StationNameList = []
        for id in StationIDList:
            StationNameList.append(getStationName(id))#뒤로 -5정거장까지 전체 노선 정보
        for n in StationExistList:
            #if eq(direction,"상행") or eq(direction,"내선"):
            StationExistNameList.append(getStationName(current_stationID-n+6))
            # if eq(direction,"하행") or eq(direction,"외선"):
            #     StationExistNameList.append(getStationName(current_stationID-n))
        print("stationNameList : "+str(StationNameList))
        print("stationExistNameList : "+str(StationExistNameList))
        count_end = 0#종점인지 체크하는 변수
        text +="💌["+stationName+" "+line_number+" 상행선 정보입니다]💌\n"
        for total in StationNameList:
            exist = False
            for element in StationExistNameList:
                if eq(element,total):
                    if eq(total,StationNameList[6]):
                        text+=total+"🚋\n"
                    else:
                        text+=total+"🚋\n   ↓↓↓   \n"
                    exist = True
            if exist==False:
                if eq(total,"none"):
                    count_end = count_end+1
                    continue
                if eq(total,StationNameList[6]):
                    text +=total+"\n"
                else:
                    text+=total+"\n   ↓↓↓   \n"
        if count_end ==6:
            text +="종점인데 어딜가시려구요?👀\n"

    #하행일때
    direction = "하행"
    stationID = [current_stationID,current_stationID-2, current_stationID-4]

    canUse = True

    StationExistList=[]
    StationNameList=[]
    StationExistNameList = []

    for idx, get_stationID in enumerate(stationID):
        # print("=======getStationResult INFO=======")
        # print("current_stationID : "+str(current_stationID))
        # print("get_stationID : "+str(get_stationID))
        # print("idx*2 : "+str(idx*2))
        # print("current_laneName : "+str(current_laneName))
        # print("direction : "+direction)
        # print("line_number : "+line_number)
        new_stationName = getStationName(get_stationID)
        if new_stationName == "none":
            continue
        if eq(new_stationName,"error"):
            text="공공데이터에 문제가 생겼어요😂😂\n10초 뒤에 다시 이용해주시겠어요?\n꼭 다시 오셔야해요❤"
            canUse = False
            break

        num = getStationResult(current_stationID,get_stationID,new_stationName, idx*2,current_laneName,direction,line_number)

        if eq(num,"error"):
            text="공공데이터에 문제가 생겼어요😂😂\n10초 뒤에 다시 이용해주시겠어요?\n꼭 다시 오셔야해요❤"
            canUse = False
            break
        elif eq(num,"none"):
            continue
        else:
            StationExistList.append(num)

    print("station Exist List : "+str(StationExistList))
    if canUse:
        StationExistNameList = []
        #if eq(direction,"상행") or eq(direction,"내선"):
        #StationIDList = [current_stationID+6,current_stationID+5,current_stationID+4,current_stationID+3,current_stationID+2, current_stationID+1,current_stationID]
        # if eq(direction,"하행") or eq(direction,"외선"):
        StationIDList = [current_stationID-6,current_stationID-5,current_stationID-4,current_stationID-3,current_stationID-2, current_stationID-1,current_stationID]
        StationNameList = []
        for id in StationIDList:
            StationNameList.append(getStationName(id))#뒤로 -5정거장까지 전체 노선 정보
        for n in StationExistList:
            #if eq(direction,"상행") or eq(direction,"내선"):
            #StationExistNameList.append(getStationName(current_stationID-n+6))
            # if eq(direction,"하행") or eq(direction,"외선"):
            StationExistNameList.append(getStationName(current_stationID-n))

        print("stationNameList : "+str(StationNameList))
        print("stationExistNameList : "+str(StationExistNameList))
        count_end = 0#종점인지 체크하는 변수
        text +="\n\n💌["+stationName+" "+line_number+" 하행선 정보입니다]💌\n"
        for total in StationNameList:
            exist = False
            for element in StationExistNameList:
                if eq(element,total):
                    if eq(total,StationNameList[6]):
                        text+=total+"🚋\n"
                    else:
                        text+=total+"🚋\n   ↓↓↓   \n"
                    exist = True
            if exist==False:
                if eq(total,"none"):
                    count_end = count_end+1
                    continue
                if eq(total,StationNameList[6]):
                    text +=total+"\n"
                else:
                    text+=total+"\n   ↓↓↓   \n"
        if count_end ==6:
            text +="종점인데 어딜가시려구요?👀\n"

    print("===============result==============")
    print(text)
    return text



def getStationInfo(myStationName):
    myKey = "n+1iCTjka3qgrhco9Xl3e05Depf0hpct6SJUYUEH38E"
    encKey = urllib.parse.quote_plus(myKey)
    encStationname = urllib.parse.quote_plus(myStationName)
    odUrl = "https://api.odsay.com/v1/api/searchStation?lang=0&stationName="+encStationname+"&stationClass=2&apiKey="+encKey
    request = urllib.request.Request(odUrl)
    response = urllib.request.urlopen(request)

    json_rt = response.read().decode('utf-8')
    data = json.loads(json_rt)
    return data

def getStationName(stationID):
    myKey = "n+1iCTjka3qgrhco9Xl3e05Depf0hpct6SJUYUEH38E"
    encKey = urllib.parse.quote_plus(myKey)
    encStationID = urllib.parse.quote_plus(str(stationID))
    odUrl = "https://api.odsay.com/v1/api/subwayStationInfo?lang=0&stationID="+encStationID+"&apiKey="+encKey
    request = urllib.request.Request(odUrl)
    response = urllib.request.urlopen(request)

    od_json = response.read().decode('utf-8')
    od_data = json.loads(od_json)
    try:
        stationName = od_data['result']['stationName']
    except KeyError:
        return "error"
    return stationName

def getStationResult(cID, stationID, stationName, idx, current_laneName,direction,line_number): #예:서울역 수도권 4호선 426
    for (first, last) in subwayID:
        if current_laneName == last:
            open_data_subwayID = first #예:수도권 4호선인 경우 open_data_subwayID = 1004

    open_data_key = "714d78526b7369683130356e4d455357"
    enckey = urllib.parse.quote_plus(open_data_key)

    stationName = re.sub("[역]$","", stationName)

    encStationname = urllib.parse.quote_plus(stationName)
    open_data_url = "http://swopenapi.seoul.go.kr/api/subway/"+enckey+"/json/realtimeStationArrival/0/5/"+encStationname

    try:
        request = urllib.request.Request(open_data_url)
        response = urllib.request.urlopen(request)

        real_json = response.read().decode('utf-8')
        real_data = json.loads(real_json)
        realtimeList = real_data['realtimeArrivalList']

        for list in realtimeList:
            if list['subwayId'] == str(open_data_subwayID) and list['updnLine']==direction:
                if list['arvlMsg2'] == "전역 도착" or list['arvlMsg2'] == "전역 출발":
                    return idx+1
                elif "[" in list['arvlMsg2']:#[5]번째 전역 (화전)
                    info_str = list['arvlMsg2'].split()
                    info_str2 = info_str[2]
                    info_str2 = info_str2[1:len(info_str2)-1]

                    new_data = getStationInfo(info_str2)
                    new_station_info = new_data['result']['station']
                    new_stationID = 0

                    for idx, info in enumerate(new_station_info):
                        if line_number in info['laneName']:
                            new_stationID = int(new_data['result']['station'][idx]['stationID'])

                    if eq(direction,"상행") or eq(direction,"외선"):
                        return 6-(new_stationID-cID)
                    elif eq(direction,"하행") or eq(direction,"내선"):
                        return cID-new_stationID
                elif "(" in list['arvlMsg2']:#3분 58초 후 (삼각지)
                    my_str = list['arvlMsg2'].split()
                    for idx,i in enumerate(my_str):
                        if "(" in i:
                            my_str2 = my_str[idx]

                    my_str2 = my_str2[1:len(my_str2)-1]
                    new_data = getStationInfo(my_str2)
                    new_station_info = new_data['result']['station']
                    new_stationID = 0

                    for idx, info in enumerate(new_station_info):
                        if line_number in info['laneName']:
                            new_stationID = int(new_data['result']['station'][idx]['stationID'])

                    if eq(direction,"상행") or eq(direction,"외선"):
                        return 6-(new_stationID-cID)
                    elif eq(direction,"하행") or eq(direction,"내선"):
                        return cID-new_stationID
                else:
                    return idx
        return "none"
    except urllib.error.HTTPError:
        return "error"
    except KeyError:
        return "error"

# def get_subway_line(subway_station):
#     ##지하철 호선 리스트
#     my = "f/WM8od4VAXdGg4Q5ZaWSlJ8tIbSpw+nJ4WQ4AFRpsM"
#     encMy = urllib.parse.quote_plus(my)
#     encST = urllib.parse.quote_plus(subway_station)
#
#     odUrl = "https://api.odsay.com/v1/api/searchStation?lang=&stationName="+encST+"&CID=1000&stationClass=2&apiKey="+encMy
#
#     request = urllib.request.Request(odUrl)
#     response = urllib.request.urlopen(request)
#
#     json_rt = response.read().decode('utf-8')
#     data = json.loads(json_rt)
#
#     sub_line_list = []
#     stInfo = data['result']['station']
#
#     for i in stInfo:
#         if i['laneName'] not in sub_line_list:
#             sub_line_list.append(i['laneName'])
#
#     action = 1
#     re = "호선을 선택해 주세요." + "\n"
#     for i in range(0,len(sub_line_list)):
#         re += str(i+1) +". " + sub_line_list[i] + "\n"
#
#     return [re,action,sub_line_list]


# def get_option(stationName):
#
#     SNList = [["반포역", "신반포역", "구반포역"], ["논현역", "신논현역"]]
#
#     print("입력한 역이름 :"+stationName)
#     for e in SNList:
#         #print("e = "+str(e))
#         #print("stationName="+stationName+" line_number="+line_number+" direction="+direction)
#         if stationName in e:
#             #print("리스트에 있음")
#             #print("리스트 길이 : "+str(len(SNList)))
#             for i in range(0, len(SNList)):
#                 #print(str(i)+"번째 리스트 내용 :"+str(SNList[i]))
#                 if stationName in SNList[i]:
#                     option = SNList[i]
#                     #print("option = "+str(option))
#     print("선택사항 : "+str(option))
#
#     return option
