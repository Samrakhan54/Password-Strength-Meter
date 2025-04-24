import streamlit as st
import re

# Page setup
st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")
st.title("🔒Password Strength Checker")
st.markdown("""
## Welcome to the ultimate password strength checker! 👏
Use this simple tool to check the strength of your password and get suggestions on how to make it stronger.
We will give you strong tips to create a **strong password** 🔒 
""")

# User input
password = st.text_input("Enter your password", type="password")

# Variables to hold score and feedback
feedback = []
score = 0

# Main check
if password:
    # Check 1: Length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Check 2: Upper and lower case
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain both uppercase and lowercase letters.")

    # Check 3: At least one digit
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one digit.")

    # Check 4: At least one special character
    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one special character (!@#$%^&*).")

    # Final strength evaluation
    if score == 4:
        feedback.append("✅ Your password is strong.")
    elif score == 3:
        feedback.append("🟡 Your password is medium strength. Add more elements to make it strong.")
    else:
        feedback.append("🔴 Your password is weak. Please improve it.")

    # Display feedback
    st.markdown("## Password Feedback")
    for tip in feedback:
        st.write(tip)

else:
    # If no password entered
    st.info("Please enter your password to get started.")

                              
                          
            
            
                      
                  
                  
         
             
         
            
            
            
        


    
    