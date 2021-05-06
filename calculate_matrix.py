import numpy as np


def calculate_matrix(numbers):
    # ======================
    # Calculation section
    # ======================
    # Reshape list to matrix 3x3
    matrix = np.array(numbers).reshape(3, 3)
    # Here here we will get the results
    results = {}
    # Here we have functions which we have to do
    actions = {
        "Mean": np.mean,
        "Variance": np.var,
        "Standard deviation": np.std,
        "Max": np.max,
        "Min": np.min,
        "Sum": np.sum
    }
    # For each function from actions
    for k, v in actions.items():
        # We calculate function for entire matrix
        results[k] = {"The entire matrix": v(matrix)}
        # And then, we calculate function for each row and column
        for index in range(len(matrix)):
            # And save results to results dictionary
            results[k].update({
                f"Row {index + 1}": v(matrix[index, :]),
                f"Column {index + 1}": v(matrix[:, index])
            })

    # ======================
    # Print section
    # ======================
    print("Matrix information".center(70, "."))
    # First we print how looks like matrix
    print(">>> Your matrix looks like this:")
    print(matrix)
    print()
    # For each function we print name of segment of calculations
    # And result of these calculations
    for func in results:
        print(">>>", func)
        for segment in sorted(results[func]):
            print("-", segment, "->", results[func][segment])
        print()
