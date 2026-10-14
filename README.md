# Learn ML by Doing: Training Models Path

Hands-on course matching the learning path: define tasks/metrics (F1, RMSE), prepare data, train with sklearn, compare to type-safe LLMs.

## Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Lessons
1. [Metrics](lessons/01_metrics.py) - F1 (classification) and RMSE (regression)
2. [Sklearn Classification](lessons/02_sklearn_classification.py)
3. [Sklearn Regression](lessons/03_sklearn_regression.py)
4. [Type-safe LLM Classification](lessons/04_type_safe_llm.py) - requires OpenAI API key

## Learning Path Recap
- Define task + metrics
- Data prep (pandas, sklearn)
- Model + train (.fit or explicit loop)
- Evaluate (sklearn.metrics)
- Traditional vs structured LLM outputs

Run each script independently. Start with metrics.
