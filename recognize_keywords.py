def initialising_keyword():
    import json
    file_name = 'json_files/keywords.json'
    with open(file_name, 'r') as file:
        global keywords_list
        keywords_list = json.load(file)
        keywords_list = keywords_list["program keywords"]

def recognize_keywords(text:str) -> list:
    try:
        text = text.split()
        for x in text:
            if x in keywords_list["music"]: return {'keyword-present': True, 'keyword':"music"}
            elif x in keywords_list["time"]: return {'keyword-present': True, 'keyword':"time"}
            elif x in keywords_list["terminate"]: return {'keyword-present': True, 'keyword':"terminate"}
            elif x in keywords_list["weather"]: return {'keyword-present': True, 'keyword':"weather"}
            elif x in keywords_list["news"]: return {'keyword-present': True, 'keyword':"news"}
            #print(x in keywords_list["terminate"], f"The keyword found is {x}")

        if len(text) > 6:
            print('gemini')
            return {'keyword-present': True, 'keyword':"gemini"}
        return {'keyword-present':False}
    except Exception:
        return {'keyword-present':False}

def find_seconds_in_text():
    pass

def testing():
    initialising_keyword()
    print(recognize_keywords(input('YOU:: (present in recognize kwywords):: ')))
