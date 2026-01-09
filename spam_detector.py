import pandas as pd
import numpy as np
import matplotlib
# ვიყენებთ 'Agg' ბექენდს, რომ Tcl შეცდომა არ ამოაგდოს
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score

# 1. მონაცემების ჩატვირთვა
df = pd.read_csv('g_bedoshvili25_56234.csv')

# 2. მონაცემების მომზადება
feature_names = ['words', 'links', 'capital_words', 'spam_word_count']
X = df[feature_names]
y = df['is_spam']

# 3. მონაცემების დაყოფა 70% / 30%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

# 4. მოდელის შექმნა და წვრთნა
model = LogisticRegression()
model.fit(X_train, y_train)

# 5. შედეგების გამოტანა
print(f"Coefficients: {model.coef_}")
print(f"Intercept: {model.intercept_}")

y_pred = model.predict(X_test)
print(f"Accuracy Score: {accuracy_score(y_test, y_pred)}")
print("Confusion Matrix:")
cm = confusion_matrix(y_test, y_pred)
print(cm)

# 6. ფუნქცია ერთი იმეილის შესამოწმებლად
def predict_email(words, links, capital_words, spam_words):
    features = pd.DataFrame([[words, links, capital_words, spam_words]], columns=feature_names)
    prediction = model.predict(features)
    probability = model.predict_proba(features)[0][1]
    result = "Spam" if prediction[0] == 1 else "Legitimate"
    return result, probability

# ტესტები
print(f"\nExample 1 (Legit): {predict_email(150, 1, 5, 0)}")
print(f"Example 2 (Spam): {predict_email(800, 15, 50, 12)}")

# 7. გრაფიკის შენახვა
plt.figure(figsize=(8,6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Greens')
plt.title('Spam Detection Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.savefig('confusion_matrix.png')
print("\nგრაფიკი 'confusion_matrix.png' წარმატებით შეინახა!")