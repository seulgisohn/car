

def extract_plate_info(plate_number):
    # 번호판 길이 확인
    if len(plate_number) == 7:
        # 7자리 번호판 (숫자 2자리 + 한글 1글자 + 숫자 4자리)
        first_part = plate_number[:2]  # 앞 2자리 숫자
        korean_letter = plate_number[2]  # 한글 한 글자
        last_part = plate_number[3:]  # 뒤 4자리 숫자
    elif len(plate_number) == 8:
        # 8자리 번호판 (숫자 3자리 + 한글 1글자 + 숫자 4자리)
        first_part = plate_number[:3]  # 앞 3자리 숫자
        korean_letter = plate_number[3]  # 한글 한 글자
        last_part = plate_number[4:]  # 뒤 4자리 숫자
    else:
        return None, None, None
    
    return first_part, korean_letter, last_part

def classify_vehicle_type(first_part):
    # 앞부분 숫자를 정수로 변환
    first_num = int(first_part)
    
    # 차량 종류 분류
    if len(first_part) == 2:
        # 6자리 번호판
        if 1 <= first_num <= 69:
            return "승용차"
        elif 70 <= first_num <= 79:
            return "승합차"
        elif 80 <= first_num <= 97:
            return "화물차"
        elif 98 <= first_num <= 99:
            return "특수차"
    elif len(first_part) == 3:
        # 7자리 번호판
        if 100 <= first_num <= 699:
            return "승용차"
        elif 700 <= first_num <= 799:
            return "승합차"
        elif 800 <= first_num <= 979:
            return "화물차"
        elif 980 <= first_num <= 997:
            return "특수차"
        elif 998 <= first_num <= 999:
            return "긴급차"
    
    return "알 수 없는 종류"

def classify_vehicle_purpose(korean_letter):
    # 차량 용도 분류
    personal_use = {'가', '나', '다', '라', '마', '거', '너', '더', '러', '머', '버', '서', '어', '저', 
                    '고', '노', '도', '로', '모', '보', '소', '오', '조', '구', '누', '두', '루', '무', 
                    '부', '수', '우', '주'}
    business_use = {'아', '바', '사', '자'}
    rental_use = {'하', '허', '호'}
    delivery_use = {'배'}

    if korean_letter in personal_use:
        return "일반 자가용"
    elif korean_letter in business_use:
        return "영업용 자동차"
    elif korean_letter in rental_use:
        return "대여용 자동차"
    elif korean_letter in delivery_use:
        return "택배용 자동차"
    
    return "알 수 없는 용도"

def analyze_plate_number(plate_number):
    # 번호판 정보 추출
    first_part, korean_letter, last_part = extract_plate_info(plate_number)
    
    if first_part is None:
        print("잘못된 번호판 형식입니다.")
        return
    
    # 차량 종류와 용도 분석
    vehicle_type = classify_vehicle_type(first_part)
    vehicle_purpose = classify_vehicle_purpose(korean_letter)
    
    print(f"번호판: {plate_number}")
    print(f"차량 종류: {vehicle_type}")
    print(f"차량 용도: {vehicle_purpose}")

# 사용자 입력을 받아 처리
plate_number = input("자동차 번호판을 입력하세요: ")
analyze_plate_number(plate_number)
