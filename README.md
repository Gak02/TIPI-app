# TIPI 性格特性診断テスト / TIPI Personality Trait Test

Ten-Item Personality Inventory (TIPI) を用いた性格特性診断Webアプリ
A web application for personality trait assessment using the Ten-Item Personality Inventory (TIPI).

## 概要 / Overview

このアプリは、TIPI (Ten-Item Personality Inventory) を使用して、ユーザーの性格特性をBig Five理論に基づいて分析します。10個の質問に回答することで、以下の5つの性格特性を評価します：

This application analyzes your personality traits based on the Big Five theory using TIPI (Ten-Item Personality Inventory). By answering 10 questions, it evaluates the following five personality traits:

- 外向性 / Extraversion
- 協調性 / Agreeableness
- 誠実性 / Conscientiousness
- 神経症傾向 / Neuroticism
- 開放性 / Openness

## 機能 / Features

- 日本語・英語の言語選択 / Language selection (Japanese/English)
- ウェルカムページによる説明表示 / Welcome page with introduction
- 10個の質問を1問ずつ表示 / 10 questions displayed one at a time
- 7段階評価による回答 / 7-point scale rating system
- プログレスバーによる進捗表示 / Progress bar
- レーダーチャートによる結果の可視化 / Results visualization with radar chart
- 平均値との比較 / Comparison with average scores
- 詳細な解釈コメント / Detailed interpretation comments
- テストの再実施機能 / Option to retake the test

## 評価方法 / Evaluation Method

- 各項目は1〜7点で評価 / Each item is rated on a scale of 1-7
- 最終的なBig5スコアは2〜14点の範囲 / Final Big5 scores range from 2 to 14
- 結果は大学生902人の平均値と比較して表示 / Results are compared with average scores from 902 university students

## 参考情報 / Reference Information

スコアの計算方法は以下の式に基づいています / Scores are calculated using the following formulas:
- 外向性/Extraversion = (Q1 + (8 - Q6)) / 2
- 協調性/Agreeableness = ((8 - Q2) + Q7) / 2
- 誠実性/Conscientiousness = (Q3 + (8 - Q8)) / 2
- 神経症傾向/Neuroticism = (Q4 + (8 - Q9)) / 2
- 開放性/Openness = (Q5 + (8 - Q10)) / 2

## 技術スタック / Technology Stack

- Python 3.11
- Streamlit
- Plotly
- Pandas
- NumPy

## 謝辞
- A very brief measure of the Big-Five personality domains: https://doi.org/10.1016/S0092-6566(03)00046-1 (Accessed: 19th Jan 2025)
- 日本語版Ten Item Personality Inventory（TIPI-J）作成の試み: https://www.jstage.jst.go.jp/article/personality/21/1/21_40/_article/-char/ja/ (Accessed: 19th Jan 2025)
