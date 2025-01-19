import streamlit as st
import plotly.graph_objects as go
import numpy as np
import pandas as pd

# アプリケーションの状態管理のためのセッション状態の初期化
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'  # welcome, test, results
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'answers' not in st.session_state:
    st.session_state.answers = [None] * 10
if 'language' not in st.session_state:
    st.session_state.language = None  # 'ja' or 'en'

# 言語別のテキストコンテンツ
CONTENT = {
    'ja': {
        'title': "🎯 性格特性診断テスト - Ten Item Personality Inventory(TIPI)",
        'welcome_text': """
        ### ようこそ！
        
        このテストでは、あなたの性格特性を以下の5つの観点から分析します：
        
        1. 外向性 - 社交性や活動性の度合い
        2. 協調性 - 他者への思いやりや協力の度合い
        3. 誠実性 - 計画性や責任感の度合い
        4. 神経症傾向 - 不安や緊張の度合い
        5. 開放性 - 新しい経験への興味や創造性の度合い
        
        - 所要時間：約3分
        - 質問数：10問
        - 回答方法：7段階評価
        
        ※ このテストは一般的な性格特性の傾向を把握するためのものです。
        """,
        'start_button': "テストを開始する",
        'questions': [
            "私は活発、外向的だと思う。",
            "私は他人に不満をもち、もめごとを起こしやすいと思う。",
            "私はしっかりしていて、自分に厳しいと思う。",
            "私は心配性で、うろたえやすいと思う。",
            "私は新しいことが好きで、変わった考えをもつと思う。",
            "私はひかえめで、おとなしいと思う。",
            "私は人に気をつかう、やさしい人間だと思う。",
            "私はだらしなく、うっかりしていると思う。",
            "私は冷静で、気分が安定していると思う。",
            "私は発想力に欠けた、平凡な人間だと思う。"
        ],
        'options': {
            1: "全く違うと思う",
            2: "おおよそ違うと思う",
            3: "少し違うと思う",
            4: "どちらでもない",
            5: "少しそう思う",
            6: "まぁまぁそう思う",
            7: "強くそう思う"
        },
        'question_prefix': "質問",
        'select_answer': "あなたの回答を選択してください：",
        'prev_button': "前の質問",
        'next_button': "次の質問",
        'show_results': "結果を見る",
        'results_title': "🎉 あなたの性格特性診断結果",
        'detailed_interpretation': "📊 詳細な解釈",
        'your_score': "あなたのスコア",
        'diff_from_mean': "平均値との差",
        'evaluation': "評価",
        'mean': "平均",
        'retry_button': "テストをもう一度受ける",
        'high': "高い",
        'low': "低い",
        'average': "平均的",
        'chart_your_score': "あなたのスコア",
        'chart_average': "平均値",
        'traits': {
            "外向性": "社会性や活発さ、外界への興味関心。スコアが高いと他者との交流や人とのかかわりを好むタイプ。",
            "協調性": "他者への共感力や思いやり、協調性。スコアが高いと対立を避け、協調的で思いやりがあるタイプ。",
            "誠実性": "思考や行動をコントロールする力、良心、責任感の強さ。スコアが高いと真面目で責任感が強く、達成力がある。",
            "神経症傾向": "ネガティブ刺激への耐性、感情的な不安定性。スコアが高いとストレスや緊張に弱い傾向。",
            "開放性": "知的、美的、文化的に新しい経験への開放性を測定。スコアが高いと知的好奇心が高く、想像力や芸術的関心が豊か。"
        }
    },
    'en': {
        'title': "🎯 Personality Trait Test - Ten Item Personality Inventory(TIPI)",
        'welcome_text': """
        ### Welcome!
        
        This test analyses your personality traits across five dimensions:
        
        1. Extraversion - Level of sociability and activity
        2. Agreeableness - Level of empathy and cooperation
        3. Conscientiousness - Level of organization and responsibility
        4. Neuroticism - Level of emotional stability
        5. Openness - Level of curiosity and creativity
        
        - Time required: About 3 minutes
        - Number of questions: 10
        - Rating scale: 7 points
        
        Note: This test provides a general assessment of personality traits.
        """,
        'start_button': "Start Test",
        'questions': [
            "I see myself as extraverted, enthusiastic.",
            "I see myself as critical, quarrelsome.",
            "I see myself as dependable, self-disciplined.",
            "I see myself as anxious, easily upset.",
            "I see myself as open to new experiences, complex.",
            "I see myself as reserved, quiet.",
            "I see myself as sympathetic, warm.",
            "I see myself as disorganized, careless.",
            "I see myself as calm, emotionally stable.",
            "I see myself as conventional, uncreative."
        ],
        'options': {
            1: "Disagree strongly",
            2: "Disagree moderately",
            3: "Disagree a little",
            4: "Neither agree nor disagree",
            5: "Agree a little",
            6: "Agree moderately",
            7: "Agree strongly"
        },
        'question_prefix': "Question",
        'select_answer': "Select your answer:",
        'prev_button': "Previous",
        'next_button': "Next",
        'show_results': "Show Results",
        'results_title': "🎉 Your Personality Trait Results",
        'detailed_interpretation': "📊 Detailed Interpretation",
        'your_score': "Your Score",
        'diff_from_mean': "Difference from mean",
        'evaluation': "Evaluation",
        'mean': "Mean",
        'retry_button': "Take the Test Again",
        'high': "High",
        'low': "Low",
        'average': "Average",
        'chart_your_score': "Your Score",
        'chart_average': "Average",
        'traits': {
            "Extraversion": "Sociability and enthusiasm in external activities. High scorers tend to be outgoing and energetic.",
            "Agreeableness": "Empathy and warmth towards others. High scorers tend to be cooperative and considerate.",
            "Conscientiousness": "Organization and responsibility. High scorers tend to be disciplined and achievement-oriented.",
            "Neuroticism": "Emotional sensitivity and stability. High scorers tend to experience more stress and anxiety.",
            "Openness": "Curiosity and creativity. High scorers tend to be imaginative and interested in new experiences."
        }
    }
}

# 特性名の言語マッピング
TRAIT_NAMES = {
    'ja': {
        "外向性": "外向性",
        "協調性": "協調性",
        "誠実性": "誠実性",
        "神経症傾向": "神経症傾向",
        "開放性": "開放性"
    },
    'en': {
        "外向性": "Extraversion",
        "協調性": "Agreeableness",
        "誠実性": "Conscientiousness",
        "神経症傾向": "Neuroticism",
        "開放性": "Openness"
    }
}

def get_score_evaluation(score, mean, std):
    """スコアの評価を返す関数"""
    lang = st.session_state.language
    if score > mean + std:
        return CONTENT[lang]['high'], "⬆️"
    elif score < mean - std:
        return CONTENT[lang]['low'], "⬇️"
    else:
        return CONTENT[lang]['average'], "➡️"

# 大学生902人の平均値と標準偏差
population_stats = {
    "外向性": {"mean": 7.83, "std": 2.97},
    "協調性": {"mean": 9.48, "std": 2.16},
    "誠実性": {"mean": 6.14, "std": 2.41},
    "開放性": {"mean": 8.03, "std": 2.48},
    "神経症傾向": {"mean": 9.21, "std": 2.48}
}

def calculate_big5_scores(answers):
    """Big5スコアを計算する関数"""
    scores = {
        "外向性": (answers[0] + (8 - answers[5])) / 2,
        "協調性": ((8 - answers[1]) + answers[6]) / 2,
        "誠実性": (answers[2] + (8 - answers[7])) / 2,
        "神経症傾向": (answers[3] + (8 - answers[8])) / 2,
        "開放性": (answers[4] + (8 - answers[9])) / 2
    }
    return scores

def create_radar_chart(scores):
    """レーダーチャートを作成する関数"""
    lang = st.session_state.language
    categories = [TRAIT_NAMES[lang][trait] for trait in scores.keys()]
    values = list(scores.values())
    
    fig = go.Figure()
    
    # スコアのプロット
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name=CONTENT[lang]['chart_your_score']
    ))
    
    # 平均値のプロット
    mean_values = [population_stats[cat]["mean"] for cat in scores.keys()]
    fig.add_trace(go.Scatterpolar(
        r=mean_values,
        theta=categories,
        fill='toself',
        name=CONTENT[lang]['chart_average']
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[2, 14]
            )
        ),
        showlegend=True
    )
    
    return fig

def show_language_selection():
    """言語選択ページを表示する関数"""
    st.title("🌐 言語選択 / Language Selection")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("日本語", type="primary", key="ja"):
            st.session_state.language = 'ja'
            st.session_state.page = 'welcome'
            st.rerun()
    
    with col2:
        if st.button("English", type="primary", key="en"):
            st.session_state.language = 'en'
            st.session_state.page = 'welcome'
            st.rerun()

def show_welcome_page():
    """ウェルカムページを表示する関数"""
    lang = st.session_state.language
    content = CONTENT[lang]
    
    st.title(content['title'])
    st.write(content['welcome_text'])
    
    if st.button(content['start_button'], type="primary"):
        st.session_state.page = 'test'
        st.rerun()

def show_test_page():
    """テストページを表示する関数"""
    lang = st.session_state.language
    content = CONTENT[lang]
    
    # プログレスバーの表示
    progress = st.progress(st.session_state.current_question / 10)
    st.write(f"{content['question_prefix']} {st.session_state.current_question + 1}/10")
    
    # 現在の質問を表示
    current_q = content['questions'][st.session_state.current_question]
    st.write(f"### {current_q}")
    
    # 選択肢の表示
    answer = st.radio(
        content['select_answer'],
        options=list(range(1, 8)),
        format_func=lambda x: f"{x}. {content['options'][x]}",
        key=f"q_{st.session_state.current_question}"
    )
    
    # ナビゲーションボタン
    col1, col2 = st.columns(2)
    
    with col1:
        if st.session_state.current_question > 0:
            if st.button(content['prev_button']):
                st.session_state.current_question -= 1
                st.rerun()
    
    with col2:
        if st.session_state.current_question < 9:
            if st.button(content['next_button']):
                st.session_state.answers[st.session_state.current_question] = answer
                st.session_state.current_question += 1
                st.rerun()
        else:
            if st.button(content['show_results']):
                st.session_state.answers[st.session_state.current_question] = answer
                st.session_state.page = 'results'
                st.rerun()

def show_results_page():
    """結果ページを表示する関数"""
    lang = st.session_state.language
    content = CONTENT[lang]
    
    st.write(content['results_title'])
    
    # Big5スコアの計算
    scores = calculate_big5_scores(st.session_state.answers)
    
    # レーダーチャートの表示
    st.plotly_chart(create_radar_chart(scores))
    
    # 各因子のスコアと解釈の表示
    st.write(f"### {content['detailed_interpretation']}")
    for ja_factor, score in scores.items():
        factor = TRAIT_NAMES[lang][ja_factor]
        mean = population_stats[ja_factor]["mean"]
        std = population_stats[ja_factor]["std"]
        evaluation, emoji = get_score_evaluation(score, mean, std)
        
        st.write(f"#### {factor} {emoji}")
        col1, col2 = st.columns([1, 2])
        
        with col1:
            # スコアの表示
            st.metric(
                content['your_score'],
                f"{score:.1f}",
                f"{content['diff_from_mean']}: {score - mean:.1f}"
            )
            st.write(f"**{content['evaluation']}**: {evaluation}")
            st.write(f"**{content['mean']}**: {mean:.1f} ± {std:.1f}")
        
        with col2:
            # 解釈の表示
            st.write(content['traits'][factor])
    
    # テスト再実施ボタン
    if st.button(content['retry_button']):
        st.session_state.page = 'welcome'
        st.session_state.current_question = 0
        st.session_state.answers = [None] * 10
        st.rerun()

def main():
    """メイン関数"""
    if st.session_state.language is None:
        show_language_selection()
    elif st.session_state.page == 'welcome':
        show_welcome_page()
    elif st.session_state.page == 'test':
        show_test_page()
    else:  # results
        show_results_page()

if __name__ == "__main__":
    main()
