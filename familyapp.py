import streamlit as st
import io

st.title("👨‍👩‍👧‍👦 Family Information Form")

# Form inputs
full_name = st.text_input("Your Full Name")
family_members = st.number_input("How many family members?", min_value=1, step=1)
address = st.text_area("Full Address")

# Submit button
if st.button("Submit"):
    st.success("✅ Form submitted successfully!")

    # Prepare content
    content = f"""Full Name: {full_name}
Family Members: {family_members}
Full Address: {address}
"""

    # Show preview
    st.write("### 📝 Your Submitted Data")
    st.code(content, language='text')

    # Create in-memory file
    file = io.StringIO(content)

    # Download button
    st.download_button(
        label="📥 Download as .txt file",
        data=file,
        file_name="family_info.txt",
        mime="text/plain"
    )
