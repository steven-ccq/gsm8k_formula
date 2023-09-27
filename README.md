---
### Intro
This code repository provides partial **gsm8k** dataset with calculation formulas. This **gsm8k_var** dataset is a by-product of our experiments.

---
### How we do this
We first parameterized the numbers in the question, e.g.

*I had 2 apples and after eating half of them I got 3 more apples. How many are left now?* ->

*I had x1 apples and after eating half of them I got x2 more apples. How many are left now?*

After that, we extracted the mathematical formula *(x1/2)+x2* from this question.

**All data has been verified and is basically guaranteed to be correct.**

---
### How to use this dataset
You can get the new question you want by simply replacing the parameters of the questions in the dataset, and then use the parameterized formula to get the answer of the new question.

We show how to use this dataset in **demo.py**.
