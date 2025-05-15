import numpy as np
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

def plot_confusion_matrix(y_true, y_pred, labels=None):
    """
    Funkcja do wizualizacji macierzy pomyłek.
    
    Args:
        y_true: Prawdziwe etykiety
        y_pred: Przewidywane etykiety
        labels: Lista etykiet klas
    """
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title('Macierz pomyłek')
    plt.ylabel('Prawdziwa klasa')
    plt.xlabel('Przewidywana klasa')
    if labels:
        plt.xticks(np.arange(len(labels)) + 0.5, labels)
        plt.yticks(np.arange(len(labels)) + 0.5, labels)
    plt.show()

def print_classification_metrics(y_true, y_pred):
    """
    Funkcja do wyświetlania metryk klasyfikacji.
    
    Args:
        y_true: Prawdziwe etykiety
        y_pred: Przewidywane etykiety
    """
    print(classification_report(y_true, y_pred))

def plot_feature_importance(model, feature_names):
    """
    Funkcja do wizualizacji ważności cech.
    
    Args:
        model: Wytrenowany model (musi mieć atrybut feature_importances_)
        feature_names: Lista nazw cech
    """
    importances = model.feature_importances_
    indices = np.argsort(importances)[::-1]
    
    plt.figure(figsize=(10, 6))
    plt.title('Ważność cech')
    plt.bar(range(len(importances)), importances[indices])
    plt.xticks(range(len(importances)), [feature_names[i] for i in indices], rotation=45, ha='right')
    plt.tight_layout()
    plt.show() 