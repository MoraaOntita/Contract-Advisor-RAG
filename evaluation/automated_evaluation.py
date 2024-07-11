import os
from evaluation_tools import EvaluationTools
from rag_pipeline import RAGSystem

def main():
    # Load configuration from environment variables or a config file
    model_path = os.getenv('MODEL_SAVE_PATH', '/default/path/to/model')
    evaluation_data_path = os.getenv('EVALUATION_DATA_PATH', '/default/path/to/evaluation_data')
    
    # Initialize RAGSystem
    rag_system = RAGSystem(model_path)
    
    # Initialize EvaluationTools
    evaluator = EvaluationTools(rag_system)
    
    # Load evaluation data
    with open(evaluation_data_path, 'r') as f:
        evaluation_data = f.read()
    
    # Perform evaluation
    results = evaluator.evaluate(evaluation_data)
    
    # Print or save results
    print(results)

if __name__ == "__main__":
    main()