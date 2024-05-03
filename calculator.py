import streamlit as st

# Define functions for calculator operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

def exponentiate(x, y):
    return x ** y

def square_root(x):
    return x ** 0.5

# Define the Streamlit app
def main():
    st.title("Calculator")

    # Input fields for numbers
    num1 = st.number_input("Enter first number:")
    num2 = st.number_input("Enter second number (if needed):")

    # Dropdown for selecting operation
    operation = st.selectbox("Select operation:", ["Addition", "Subtraction", "Multiplication", "Division", "Exponentiation", "Square Root"])

    # Memory functionality
    memory = st.button("Memory:")
    if memory:
        st.write("M+ - Add result to memory")
        st.write("M- - Subtract result from memory")
        st.write("MR - Recall memory")
        st.write("MC - Clear memory")

    # Perform operation based on user selection
    if st.button("Calculate"):
        if operation == "Addition":
            result = add(num1, num2)
        elif operation == "Subtraction":
            result = subtract(num1, num2)
        elif operation == "Multiplication":
            result = multiply(num1, num2)
        elif operation == "Division":
            result = divide(num1, num2)
        elif operation == "Exponentiation":
            result = exponentiate(num1, num2)
        elif operation == "Square Root":
            result = square_root(num1)

        if result == "Cannot divide by zero!":
            st.error(result)
        else:
            st.write("Result:", result)

if __name__ == "__main__":
    main()
