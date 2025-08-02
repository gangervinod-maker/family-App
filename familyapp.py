import streamlit as st
import io

st.title("👨‍👩‍👧‍👦 Family Information Form")

# Input fields
full_name = st.text_input("Your Full Name")
family_members = st.number_input("How many family members?", min_value=1, step=1)
full_address = st.text_area("Full Address")

# Submit button
if st.button("Submit"):
    st.success("✅ Form submitted successfully!")

    # Display submitted data
    st.subheader("📝 Your Submitted Data")
    st.text(f"Full Name: {full_name}")
    st.text(f"Family Members: {int(family_members)}")
    st.text(f"Full Address: {full_address}")

    # Prepare the text data
    text_data = f"Full Name: {full_name}\nFamily Members: {int(family_members)}\nFull Address: {full_address}"
    file_data = io.StringIO(text_data)

    # Add download button
    st.download_button(
        label="📥 Download as .txt file",
        data=file_data,
        file_name="family_data.txt",
        mime="text/plain"
    )


