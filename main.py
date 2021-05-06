from calculate_matrix import calculate_matrix

if __name__ == "__main__":
	print("Hello in Matrix Calculator!".center(70, "*"))
	digits = input("Enter 9 digits separated by commas:\n")
	calculate_matrix(digits)
