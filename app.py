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

def get_score_evaluation(score, mean, std):
    """スコアの評価を返す関数"""
    if score > mean + std:
        return "高い", "⬆️"
    elif score < mean - std:
        return "低い", "⬇️"
    else:
        return "平均的", "➡️"

# 質問リスト
questions = [
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
]

# 選択肢
options = {
    1: "全く違うと思う",
    2: "おおよそ違うと思う",
    3: "少し違うと思う",
    4: "どちらでもない",
    5: "少しそう思う",
    6: "まぁまぁそう思う",
    7: "強くそう思う"
}

# Big5の因子名と説明
big5_descriptions = {
    "外向性": "社会性や活発さ、外界への興味関心。スコアが高いと他者との交流や人とのかかわりを好むタイプ。",
    "協調性": "他者への共感力や思いやり、協調性。スコアが高いと対立を避け、協調的で思いやりがあるタイプ。",
    "誠実性": "思考や行動をコントロールする力、良心、責任感の強さ。スコアが高いと真面目で責任感が強く、達成力がある。",
    "神経症傾向": "ネガティブ刺激への耐性、感情的な不安定性。スコアが高いとストレスや緊張に弱い傾向。",
    "開放性": "知的、美的、文化的に新しい経験への開放性を測定。スコアが高いと知的好奇心が高く、想像力や芸術的関心が豊か。"
}

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
    categories = list(scores.keys())
    values = list(scores.values())
    
    fig = go.Figure()
    
    # スコアのプロット
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='あなたのスコア'
    ))
    
    # 平均値のプロット
    mean_values = [population_stats[cat]["mean"] for cat in categories]
    fig.add_trace(go.Scatterpolar(
        r=mean_values,
        theta=categories,
        fill='toself',
        name='平均値'
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

def show_welcome_page():
    """ウェルカムページを表示する関数"""
    st.title("🎯 TIPI 性格特性診断テスト")
    
    st.write("""
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
    """)
    
    if st.button("テストを開始する", type="primary"):
        st.session_state.page = 'test'
        st.rerun()

def show_test_page():
    """テストページを表示する関数"""
    # プログレスバーの表示
    progress = st.progress(st.session_state.current_question / 10)
    st.write(f"質問 {st.session_state.current_question + 1}/10")
    
    # 現在の質問を表示
    current_q = questions[st.session_state.current_question]
    st.write(f"### {current_q}")
    
    # 選択肢の表示
    answer = st.radio(
        "あなたの回答を選択してください：",
        options=list(range(1, 8)),
        format_func=lambda x: f"{x}. {options[x]}",
        key=f"q_{st.session_state.current_question}"
    )
    
    # ナビゲーションボタン
    col1, col2 = st.columns(2)
    
    with col1:
        if st.session_state.current_question > 0:
            if st.button("前の質問"):
                st.session_state.current_question -= 1
                st.rerun()
    
    with col2:
        if st.session_state.current_question < 9:
            if st.button("次の質問"):
                st.session_state.answers[st.session_state.current_question] = answer
                st.session_state.current_question += 1
                st.rerun()
        else:
            if st.button("結果を見る"):
                st.session_state.answers[st.session_state.current_question] = answer
                st.session_state.page = 'results'
                st.rerun()

def show_results_page():
    """結果ページを表示する関数"""
    st.write("## 🎉 あなたの性格特性診断結果")
    
    # Big5スコアの計算
    scores = calculate_big5_scores(st.session_state.answers)
    
    # レーダーチャートの表示
    st.plotly_chart(create_radar_chart(scores))
    
    # 各因子のスコアと解釈の表示
    st.write("### 📊 詳細な解釈")
    for factor, score in scores.items():
        mean = population_stats[factor]["mean"]
        std = population_stats[factor]["std"]
        evaluation, emoji = get_score_evaluation(score, mean, std)
        
        st.write(f"#### {factor} {emoji}")
        col1, col2 = st.columns([1, 2])
        
        with col1:
            # スコアの表示
            st.metric(
                "あなたのスコア",
                f"{score:.1f}",
                f"平均値との差: {score - mean:.1f}"
            )
            st.write(f"**評価**: {evaluation}")
            st.write(f"**平均**: {mean:.1f} ± {std:.1f}")
        
        with col2:
            # 解釈の表示
            st.write(big5_descriptions[factor])
    
    # テスト再実施ボタン
    if st.button("テストをもう一度受ける"):
        st.session_state.page = 'welcome'
        st.session_state.current_question = 0
        st.session_state.answers = [None] * 10
        st.rerun()

def main():
    """メイン関数"""
    if st.session_state.page == 'welcome':
        show_welcome_page()
    elif st.session_state.page == 'test':
        show_test_page()
    else:  # results
        show_results_page()

if __name__ == "__main__":
    main()
