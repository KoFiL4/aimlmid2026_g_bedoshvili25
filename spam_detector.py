import pandas as pd
import numpy as np
import matplotlib
import warnings
warnings.filterwarnings('ignore')

# ვიყენებთ 'Agg' ბექენდს, რომ Tcl შეცდომა თავიდან ავიცილოთ
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score

# 1. მონაცემების ჩატვირთვა
file_name = 'g_bedoshvili25_56234.csv'
df = pd.read_csv(file_name)

# ვიზუალიზაცია 1: კლასების განაწილება (Assignment 2.7 - Option A) ---
plt.figure(figsize=(8, 6))
sns.countplot(x='is_spam', data=df, hue='is_spam', palette='viridis', legend=False)
plt.title('Class Distribution: Legitimate vs Spam')
plt.xlabel('Email Class (0: Legitimate, 1: Spam)')
plt.ylabel('Count')
plt.savefig('class_distribution.png')
print(" გრაფიკი 'class_distribution.png' წარმატებით შეინახა.")

# 2. მონაცემების მომზადება
feature_names = ['words', 'links', 'capital_words', 'spam_word_count']
X = df[feature_names]
y = df['is_spam']

# 3. მონაცემების დაყოფა 70% / 30%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

# 4. ლოგისტიკური რეგრესიის მოდელის წვრთნა
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 5. შედეგების გამოტანა
print("\n--- მოდელის პარამეტრები ---")
print(f"Coefficients: {model.coef_}")
print(f"Intercept: {model.intercept_}")

# 6. ვალიდაცია
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print("\n--- ვალიდაციის შედეგები ---")
print(f"Accuracy Score: {accuracy:.4f}")
print("Confusion Matrix:")
print(cm)

# --- ვიზუალიზაცია 2: Confusion Matrix Heatmap (Assignment 2.7 - Option B) ---
plt.figure(figsize=(8, 6))
sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    cmap='Blues',
    xticklabels=['Predicted Legit', 'Predicted Spam'],
    yticklabels=['Actual Legit', 'Actual Spam']
)
plt.title('Confusion Matrix Heatmap')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.savefig('confusion_matrix.png')
print(" გრაფიკი 'confusion_matrix.png' წარმატებით შეინახა.")

# 7. ფუნქცია ერთი იმეილის შესამოწმებლად
def predict_email(words, links, capital_words, spam_words):
    sample = pd.DataFrame([[words, links, capital_words, spam_words]], columns=feature_names)
    prediction = model.predict(sample)
    probability = model.predict_proba(sample)[0][1]
    result = "Spam" if prediction[0] == 1 else "Legitimate"
    return result, probability

# 8. ტესტირება
print("\n--- ინდივიდუალური ტესტები ---")
legit_res, legit_prob = predict_email(150, 1, 5, 0)
print(f"Example 1 (Legit): {legit_res}, Prob: {legit_prob:.4f}")

spam_res, spam_prob = predict_email(800, 15, 50, 12)
print(f"Example 2 (Spam): {spam_res}, Prob: {spam_prob:.4f}")

print("\n დავალება წარმატებით დასრულდა!")