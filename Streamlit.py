import streamlit as st

# -----------------------
# 페이지 기본 설정
# -----------------------
st.set_page_config(page_title="학년별 개념정리", layout="wide")

st.title("📚 학년별 중간/기말고사 개념 정리 웹앱")

# -----------------------
# 사이드바 - 선택 메뉴
# -----------------------
with st.sidebar:
    st.header("📌 설정")
    grade = st.selectbox("학년을 선택하세요", ["중1", "중2", "중3"])
    subject = st.selectbox("과목을 선택하세요", ["수학", "과학", "국어", "영어", "사회"])
    exam_type = st.radio("시험 종류", ["1학기 중간고사", "1학기 기말고사", "2학기 중간고사", "2학기 기말고사"])

# -----------------------
# 개념 데이터 (예시)
# -----------------------
concepts = {
    "중1": {
        "수학": {
            "1학기 중간고사": ["자연수의 성질", "정수와 유리수"],
            "1학기 기말고사": ["문자와 식", "일차방정식", "좌표평면과 그래프"],
            "2학기 중간고사": ["기본 도형", "작도와 합동", "평면도형"],
            "2학기 기말고사": ["입체도형", "통계"],
        },
        "과학": {
            "1학기 중간고사": ["생물의 구성과 다양성"],
            "1학기 기말고사": ["태양계"],
            "2학기 중간고사": ["온도와 열", "물질의 상태 변화"],
            "2학기 기말고사": ["여러 가지 힘", "기체의 성질"],
        },
    },
    "중2" : {
        "수학": {
            "1학기 중간고사": ["유리수와 순환소수", "식의 계산", "일차부등식"],
            "1학기 기말고사": ["연립방정식", "일차함수"],
            "2학기 중간고사": ["삼각형의 성질", "사각형의 성질", "도형의 닮음"],
            "2학기 기말고사": ["피타고라스의 정리", "확률"],
        },
        "과학": {
            "1학기 중간고사": ["물질의 구성", "전기와 자기"],
            "1학기 기말고사": ["지권의 변화", "식물과 에너지"],
            "2학기 중간고사": ["빛과 파동", "물질의 특성"],
            "2학기 기말고사": ["수권과 해수의 순환", "동물과 에너지"],
        },
    },
    "중3" : {
        "수학": {
            "1학기 중간고사": ["제곱근과 실수", "다항식의 곱셈과 인수분해"],
            "1학기 기말고사": ["이차방정식", "이차함수"],
            "2학기 중간고사": ["삼각비", "원의 성질"],
            "2학기 기말고사": ["통계"],
        },
        "과학": {
            "1학기 중간고사": ["화학 반응의 규칙성", "기권과 날씨"],
            "1학기 기말고사": ["운동과 에너지", "자극과 반응"],
            "2학기 중간고사": ["생식과 유전", "에너지 전환과 보존"],
            "2학기 기말고사": ["별과 우주"],
        },
    }
}

# -----------------------
# 선택에 따른 개념 출력
# -----------------------

st.subheader(f"✅ {grade} {subject} - {exam_type} 대비 개념 정리")

if grade in concepts and subject in concepts[grade] and exam_type in concepts[grade][subject]:
    selected_concepts = concepts[grade][subject][exam_type]
    
    # 초기화: 세션 상태에 저장된 설명이 없으면 기본 설명 세팅
    if 'concept_descriptions' not in st.session_state:
        st.session_state.concept_descriptions = {}
    
    for idx, concept in enumerate(selected_concepts, 1):
        st.markdown(f"**{idx}. {concept}**")
        
        # 세션 상태 키 생성 (학년-과목-시험-개념별 고유키)
        key = f"{grade}_{subject}_{exam_type}_{concept}"
        
        # 세션 상태에 없으면 기본 텍스트 세팅
        if key not in st.session_state.concept_descriptions:
            st.session_state.concept_descriptions[key] = ""
        
        with st.expander("자세히 보기"):
            # 텍스트 입력창
            description = st.text_area(
                "개념 설명 입력", 
                value=st.session_state.concept_descriptions[key], 
                key=key + "_textarea"
            )
            
            # 입력값을 세션 상태에 저장
            st.session_state.concept_descriptions[key] = description
else:
    st.info("선택한 항목에 대한 개념 정리가 아직 등록되지 않았습니다.")
