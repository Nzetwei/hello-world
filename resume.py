import streamlit as st


# Function to display the resume content
def display_resume():
    st.markdown(
        """
        <style>
        body {
            background: linear-gradient(to right, #6a11cb, #2275fc); /* Gradient colors */
            color: white;  /* Text color */
        }
        </style>
        """,
        unsafe_allow_html=True
    )


    st.image(
        "https://lh3.googleusercontent.com/pw/AP1GczOuV8FTj8NGRlB6qEqNiRmLUMLMQYqXkyXeK7sZ7ZxL5kVP9PENACjVNFr1x84USnpC_eWw-Igfntv7Et79__Qnc-S5pCUAErER1RY6Y9x8VC79eruplyUwkklQu2H0I9Q3bC4_jn9W451aCj8aRYZjRw=w552-h831-s-no-gm?authuser=0",
        width=150)  # Placeholder image, replace with your own profile picture URL
    st.title("E N G   Y E E   W E I")

    st.subheader("Contact Information")
    st.write("""
    4, Lorong Budiman 2, Taman Budiman, 14000 Bukit Mertajam, Penang, Malaysia \n
    +60 18-9558996 \n
    9083wei@gmail.com
    """)

    st.subheader("Professional Summary")
    st.write("""
    Passionate about exploring knowledge, educating the younger generation, and possessing strong self-discipline. Combining knowledge with experience to create innovative solutions. Enjoy the learning process and continually seek to upgrade my skills.
    """)

    st.subheader("Education")
    st.write("""
    - **Master of Data Science and Analytics**  
      University of Science Malaysia (USM)  
      March 2021 - July 2022  
      CGPA: 3.52  

    - **Bachelor of Computer Science in Software Engineering (Hons)**  
      University of Malaysia Sarawak (UNIMAS)  
      September 2016 - September 2020  
      CGPA: 3.63
    """)

    st.subheader("Professional Skills")
    st.write("""
    - **Programming Languages**: C, C++, R, HTML, CSS, JavaScript, jQuery, Java, PHPMyAdmin, MySQL, Excel VBA, Python
    - **Tools**: Machine Learning, Data Analysis, Data Visualization, Microsoft Power BI, Tableau
    """)

    st.subheader("Certificates")
    st.write("""
    - Learning Data Analytics (Certified by Lynda.com, 04/2019)
    - IELTS (Band 6.0, 04/2016)
    - MUET (Band 4, 05/2014 - 03/2015)
    - Kumon Mathematics Program Completion (12/2009 - 09/2012)
    """)

    st.subheader("Work Experience")
    st.write("""
    - **MSSC Digital Transformation Automation Intern**  
      Intel, Penang (PG8) | Jan 2019 - Aug 2019  
      - Deployed automation for finance-related projects.
      - Trained project stakeholders on automation skills.
      - Handled lean training event registrations.

    - **Private Part-Time Clerk** | Feb 2016 - Aug 2016  
      - Designed PowerPoint slides for seminars and arranged documents.

    - **Mathematics Tutor**  
      Chan Pong Tuition Centre | Jan 2016 - Aug 2016  
      - Taught Mathematics to Standard 6 to Form 4 students and designed creative teaching methods.

    - **Diploma Lecturer/Vocational Training Officer**  
      New Era Institute and Vocational Continuing Education (NEIVCE) | July 2022 - October 2022  
      - Conducted courses and lectures for Software Engineering diploma students.

    - **Computer Science Lecturer**  
      Top Skills College (UTM SPACE) | Nov 2022 - May 2023  
      - Conducted programming-related modules for Professional Certificate and Diploma students.

    - **Computer Science Lecturer**  
      DISTED College | June 2023 - Present  
      - Conducted CS and DA-related modules for Diploma, Foundation, and Degree students.
    """)

    st.subheader("Personal Projects")
    st.write("""
    - **Final Year Project**: IoT Piggy Bank for Money Saving Habit Instillation  
      Developed an IoT piggy bank associated with an Android app for tracking children's saving goals. Evaluated usability through saving trends and reminder alert occurrence graphs.

    - **Master Practicum Project**: Environmental Waste Surveillance Detection on Water Bodies based Modeling. Developed an object detection model using a pre-trained model (Deep Learning).
    """)

    st.subheader("Achievements")
    st.write("""
    - **BlackLine Reconciliation Automation Internship Project Achievement** (08/2019)  
      Designed and automated BlackLine front end and data access for stakeholder convenience.

    - **Depreciation Module Mapping Automation Project** (07/2019 - 08/2019)  
      Coded macros to replace complicated manual processes on module mapping and file formatting.

    - **Malaysia WHT VBA Automation Internship Project** (06/2019)  
      Developed macros for specific criteria identification and filtering automation.

    - **ICUK Reverse Charge Automation Internship Project** (02/2019 - 04/2019)  
      Combined Python and VBA to reduce manual processes on data categorization.
    """)

    st.subheader("Workshops Conducted")
    st.write("""
    - **Python Automation Workshop** (05/2024): Conducted a 3-hour workshop for SPM leavers at DISTED College.
    - **Mobile App in React Native Workshop** (08/2024): Conducted a 3-hour basic React Native mobile app workshop for Form 4 students at Penang Chinese Girls School.
    """)

    st.subheader("Languages")
    st.write("""
    - **Chinese**: Native/Bilingual Proficiency
    - **English**: Full Professional Proficiency
    - **Malay**: Full Professional Proficiency
    - **French**: Elementary Proficiency
    """)

    st.subheader("References")
    st.write("""
    **Ms. Wee Bui Lin**  
    Senior Lecturer of Software Engineering Programme, Faculty of Computer Science and Information Technology, University Malaysia Sarawak  
    blwee@unimas.my  
    +60 149913163
    """)

    st.subheader("Published Paper")
    st.write("""
    Wee, B. L., & Eng, Y. W. (2021). IoT Piggy Bank for Money Saving Habit Instillation. *Journal of IT in Asia*, 9(1), 1-10.  
    [https://doi.org/10.33736/jita.2860.2021](https://doi.org/10.33736/jita.2860.2021)
    """)

    st.markdown('<div class="background">', unsafe_allow_html=True)

# Display the resume content
display_resume()
