import math
from collections import Counter

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def get_frequency_vector(text):
    freq = Counter(text)
    return freq

def normalize_vector(vector):
    norm = math.sqrt(sum(v ** 2 for v in vector.values()))
    return {k: v / norm for k, v in vector.items()}

def cosine_similarity(vec1, vec2):
    all_keys = set(vec1.keys()).union(vec2.keys())
    vec1 = [vec1.get(k, 0) for k in all_keys]
    vec2 = [vec2.get(k, 0) for k in all_keys]
    dot_product = sum(v1 * v2 for v1, v2 in zip(vec1, vec2))
    norm1 = math.sqrt(sum(v1 ** 2 for v1 in vec1))
    norm2 = math.sqrt(sum(v2 ** 2 for v2 in vec2))
    return dot_product / (norm1 * norm2) if norm1 and norm2 else 0

def main():
    english_text = read_file('trainEN.txt')
    russian_text = read_file('trainRUS.txt')
    input_text = read_file('input.txt')

    english_vector = get_frequency_vector(english_text)
    russian_vector = get_frequency_vector(russian_text)
    input_vector = get_frequency_vector(input_text)

    english_vector_normalized = normalize_vector(english_vector)
    russian_vector_normalized = normalize_vector(russian_vector)
    input_vector_normalized = normalize_vector(input_vector)

    similarity_to_english = cosine_similarity(input_vector_normalized, english_vector_normalized)
    similarity_to_russian = cosine_similarity(input_vector_normalized, russian_vector_normalized)

    if similarity_to_english > similarity_to_russian:
        print("EN")
    else:
        print("RUS")

if __name__ == '__main__':
    main()
