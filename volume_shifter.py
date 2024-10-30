import keyword_filter

def volume_shift(text:str):
    value = keyword_filter.find_numericals_in_text(text)
    value_change = keyword_filter.find_value_change_sign(text)