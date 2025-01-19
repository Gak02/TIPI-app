# TIPI 性格特性診断テスト

Ten-Item Personality Inventory (TIPI) を用いた性格特性診断Webアプリ

## 概要

このアプリは、TIPI (Ten-Item Personality Inventory) を使用して、ユーザーの性格特性をBig Five理論に基づいて分析します。10個の質問に回答することで、以下の5つの性格特性を評価します：

- 外向性 (Extraversion)
- 協調性 (Agreeableness)
- 誠実性 (Conscientiousness)
- 神経症傾向 (Neuroticism)
- 開放性 (Openness)

## 機能

- ウェルカムページによる説明表示
- 10個の質問を1問ずつ表示
- 7段階評価による回答
- プログレスバーによる進捗表示
- レーダーチャートによる結果の可視化
- 平均値との比較
- 詳細な解釈コメント
- テストの再実施機能

## 評価方法

- 各項目は1〜7点で評価
- 最終的なBig5スコアは2〜14点の範囲
- 結果は大学生902人の平均値と比較して表示

## 参考情報

- スコアの計算方法は以下の式に基づいています：
  - 外向性 = (Q1 + (8 - Q6)) / 2
  - 協調性 = ((8 - Q2) + Q7) / 2
  - 誠実性 = (Q3 + (8 - Q8)) / 2
  - 神経症傾向 = (Q4 + (8 - Q9)) / 2
  - 開放性 = (Q5 + (8 - Q10)) / 2

## 技術スタック

- Python 3.11
- Streamlit
- Plotly
- Pandas
- NumPy

## 謝辞
- A very brief measure of the Big-Five personality domains: https://doi.org/10.1016/S0092-6566(03)00046-1 (Accessed: 19th Jan 2025)
- 日本語版Ten Item Personality Inventory（TIPI-J）作成の試み: https://www.jstage.jst.go.jp/article/personality/21/1/21_40/_article/-char/ja/ (Accessed: 19th Jan 2025)
