import json

KEYWORD_JSON_FILE_NAME = 'keywords.json'

def __init__():
    import_keywords_json()

def import_keywords_json():
    with open(KEYWORD_JSON_FILE_NAME) as file:
        global keywords
        keywords = json.load(file)


def keyword_in_text(text:str) -> dict:
    import_keywords_json()
    if text != None:
        #keyword_counter = 0
        for keyword in keywords['keywords'][0]:
            if keyword in text:
                return {'keyword_present':True, 'keyword_value':keywords['keywords'][0][keyword]}
            #keyword_counter += 1
        return {'keyword_present':False}

def find_numericals_in_text(text:str) -> list:
    list_numericals = []
    for char in text:
        try:
            list_numericals.append(float(char))
        except Exception:
            pass
    return list_numericals

def find_value_change_sign(text):
    pass

def find_units_in_text(text:str) -> list:
    units = ['hour', 'minute', 'second']
    for unit in units:
        if unit in text:
            return unit

def assistant_name_in_text(assistant_names:list, text:str) -> bool:
    for name in assistant_names:
        if name in text:
            return True
    return False

def find_seconds_in_text(text):
    import conversion
    value = find_numericals_in_text(text)
    units = find_units_in_text(text)
    time = value[0]
    #print(f'Thread is running, and has executed. Value->{value} Unit->{units}')
    if 'minute' in units:
        time = conversion.conversion_minute_to_second(value[0])
    elif 'hour' in units:
        time = conversion.conversion_hour_to_second(value[0])
    return time

def find_word_after(text:str, word:str) -> dict:
    ending_index = 0    #Boilerplate
    starting_index = 0  #Boilerplate
    return {'starts-at': starting_index, 'ends-at': ending_index}

def is_word_after(word:str, text:str) -> bool:
    pass

def find_month_in_text(text:str) -> dict:
    is_month_present = False #Boilerplate
    month_name = ''          #Boilerplate
    return {'is-month-present':is_month_present, 'month-name':month_name}