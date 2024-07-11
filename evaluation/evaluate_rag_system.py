import time
import sys
import os
from sklearn.metrics import precision_score, recall_score, f1_score
from nltk.translate.bleu_score import sentence_bleu
from rouge_score import rouge_scorer
import matplotlib.pyplot as plt
import json

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from rag_pipeline import RAGSystem  # Ensure this matches your actual module structure

# Define test queries and expected responses
test_queries = [
    "What is the contract duration?",
    "Who is the contractor?"
]

expected_responses = [
    "The contract duration is 2 years.",
    "The contractor is ABC Corp."
]

# Function to evaluate the RAG system
def evaluate_rag_system(rag_system, test_queries, expected_responses):
    start_time = time.time()
    generated_responses = [rag_system.query(query) for query in test_queries]
    response_time = time.time() - start_time

    # Accuracy and Relevance (simplified)
    accuracy = sum([gen == exp for gen, exp in zip(generated_responses, expected_responses)]) / len(test_queries)

    # Precision, Recall, F1 Score
    precision = precision_score(expected_responses, generated_responses, average='micro', zero_division=0)
    recall = recall_score(expected_responses, generated_responses, average='micro', zero_division=0)
    f1 = f1_score(expected_responses, generated_responses, average='micro', zero_division=0)

    # BLEU and ROUGE
    bleu_scores = [sentence_bleu([exp], gen) for gen, exp in zip(generated_responses, expected_responses)]
    bleu_score_avg = sum(bleu_scores) / len(bleu_scores)
    
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
    rouge_scores = [scorer.score(exp, gen) for gen, exp in zip(generated_responses, expected_responses)]
    rouge1_avg = sum([score['rouge1'].fmeasure for score in rouge_scores]) / len(rouge_scores)
    rougeL_avg = sum([score['rougeL'].fmeasure for score in rouge_scores]) / len(rouge_scores)

    return {
        "accuracy": accuracy,
        "response_time": response_time,
        "precision": precision,
        "recall": recall,
        "f1_score": f1,
        "bleu_score": bleu_score_avg,
        "rouge1_score": rouge1_avg,
        "rougeL_score": rougeL_avg
    }

# Initialize the RAG system
rag_system = RAGSystem()

# Run evaluation
metrics = evaluate_rag_system(rag_system, test_queries, expected_responses)

# Print results
for metric, value in metrics.items():
    print(f"{metric}: {value}")

# Save results to a JSON file
with open('evaluation/results.json', 'w') as f:
    json.dump(metrics, f)

# Plot results
plt.figure(figsize=(10, 5))
plt.bar(metrics.keys(), metrics.values())
plt.title("RAG System Evaluation Metrics")
plt.show()
