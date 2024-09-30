from count_islands import count_islands


if __name__ == "__main__":
    # Define test cases
    test_cases = [
        ([[0, 1, 0], [0, 0, 0], [0, 1, 1]], 2),
        ([[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0]], 3),
        ([[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 0, 1]], 2),
    ]

    # Run test cases
    for idx, (matrix, expected) in enumerate(test_cases):
        result = count_islands(matrix)
        print(f"Test Case {idx + 1}: Matrix: {matrix} -> Expected: {expected}, Got: {result}")