import streamlit as st

def largest_no(num1,num2,num3):
    return max(num1,num2,num3)
st.write("""
# Find largest number

This app gives the largest number among the provided three numbers
""")
def main():
    # st.title("Find Largest number")
    num1 = st.number_input("First number")
    num2 = st.number_input("Second number")
    num3 = st.number_input("Third number")

    if st.button("Find largest"):
        largest = largest_no(num1,num2,num3)
        st.success(f"The largest number among the given three numbers is - {largest}")
if __name__ == "__main__":
    main()