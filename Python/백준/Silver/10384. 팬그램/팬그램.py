import sys
from collections import Counter

def check_pangram(sentence):
    # 입력 문장이 팬그램, 더블 팬그램, 트리플 팬그램 중 어디에 해당하는지 판별하는 함수
    sentence_counter = Counter(sentence.lower())
    # 알파벳 리스트 안에서 문자열 내의 문자의 개수 카운트
    min_count = min(sentence_counter.get(c, 0) for c in "abcdefghijklmnopqrstuvwxyz")
    
    if min_count == 0:
        return "Not a pangram"
    elif min_count == 1:
        return "Pangram!"
    elif min_count == 2:
        return "Double pangram!!"
    else:
        return "Triple pangram!!!"

def main():
    n = int(sys.stdin.readline().strip())
    for i in range(1, n + 1):
        sentence = sys.stdin.readline().strip()
        result = check_pangram(sentence)
        print(f"Case {i}: {result}")

if __name__ == "__main__":
    main()