import sys

# 줄임말 번역 딕셔너리 생성
translations = {
    "CU": "see you",
    ":-)": "I’m happy",
    ":-(": "I’m unhappy",
    ";-)": "wink",
    ":-P": "stick out my tongue",
    "(~.~)": "sleepy",
    "TA": "totally awesome",
    "CCC": "Canadian Computing Competition",
    "CUZ": "because",
    "TY": "thank-you",
    "YW": "you’re welcome",
    "TTYL": "talk to you later"
}

while True:
    user_input = input()
    print(translations.get(user_input, user_input))
    
    # 종료 시점
    if user_input == "TTYL":
        break