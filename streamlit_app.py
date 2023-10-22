import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Computer Sciencet, MS.c.
##### *Resume* 
''')

image = Image.open('dp.png')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
With two years of research assistant experience and nearly five years as a data analyst in academia and industry, I bring a diverse skill set. I specialize in data science solutions, particularly in finance, healthcare, and social media. I have a proven track record of improving data accuracy and efficiency through thorough research. My background in finance, accounting, auditing, and a Master's degree in Management allows for cost-effective enhancements in financial analysis. I also excel at fostering cross-departmental collaboration, improving project efficiency.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Chanin Nantasenamat</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#bioinformatics-tools">Bioinformatics Tools</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')
txt('**Masters Computer Science** (Machine Learning), *University of Manitoba*, Canada',
'2022-2023')
st.markdown('''
- GPA: `4`
- Research thesis entitled `Volatility Forecasting with Transformer Network`.
- Published:2023 IEEE Symposium on Computational Intelligence for Financial Engineering and Economics (CIFEr).
- Recieved International Graduate Student Entrance Scholarship.                                         
''')

txt('**Master Management** (Industerial Management), *Islamic Azad University*, Iran',
'2011-2013')
st.markdown('''
- GPA: `4`
- Research thesis entitled `Strategic Plan Compilation by Using System Dynamics Modeling`.
- Graduated with First Class Honors.
- Member of Young Researchers and Elite Club Islamic Azad University of Tabriz.
''')

txt('**Bachelors Computer Engineering** , *Islamic Azad University*, Iran',
'2004-2009')
st.markdown('''
- GPA: `3.75`

''')

#####################
st.markdown('''
## Work Experience
''')

txt('**Machine Learning Research Assistant, University of Manitoba, Canada',
'2022-2023')
st.markdown('''
- Experienced data scientist with track record of taking projects from inception to industry-ready deployment, some published in IEEE Symposium Series conferences. 
- Proficient in a wide range of skills, including: data cleaning, data visualization and storytelling, machine learning and modeling, model interpretability, deployment and production. 
- Proficiently executed the implementation of complex machine learning models, as described in research articles, showing the ability to translate theoretical concepts into practical applications that drive impactful results. 
- Extensive experience in implementing fundamental models in the finance industry. Regularly communicated complex technical findings to non-technical/ cross-functional teams, bridging the gap between data science and fintech.
- As a reliable and punctual leader for project teams, I leverage strong time management skills to adapt to changing priorities and meet deadlines.

''')

txt('**Teaching Assistant, University of Manitoba, Canada',
'2022-2023')
st.markdown('''
- Managed grading and marking for assignments and exams for 400 students across courses in data structures, programming (Java and Python), and artificial intelligence. 
- Achieved a 95% accuracy rate in grading, ensuring students received fair and consistent evaluations. 
- Provided technical guidance and support to students, resulting in a 20% improvement in student performance and understanding of course materials. 
- Demonstrated exceptional time management skills by consistently being punctual and completing tasks well before deadlines, showcasing a strong commitment to efficient work scheduling.

''')

txt('**Data Analyst at Energy Gostar Company (EGECO), Iran',
'2017-2021')
st.markdown('''
- Managed spreadsheets and databases, maintaining a 99% accuracy rate in data entry and organization. 
- Produced detailed reports by skillfully and utilizing data manipulation techniques, resulting in a 15% reduction in report generation time.
- Leveraged PowerBI, Tableau, Excel, Word, and PowerPoint for data analysis, financial modeling, and report generation, consistently exceeding performance metrics by delivering reports 10% ahead of schedule.
- Demonstrated proficiency in accounting and auditing, enhancing data accuracy and aligning financial processes with industry standards. Utilized SQL to conduct in-depth financial data analysis.
- Led cross-functional collaboration, working seamlessly with diverse company departments, enhancing project efficiency by 20%.
- Applied exceptional risk management and volatility skills to analyze and mitigate potential financial risks
- Punctually led and managed three branches, optimizing team productivity by 30% through effective leadership and project coordination.
''')

txt('**Seasonal Instructor, Daneshvaran University College',
'2014-2021')
txt('**Seasonal Instructor, Osveh University College',
'2014-2021')
st.markdown('''
- Instructed courses in Information Technology in Accounting, Information Technology in Management, Foundations of Organizational Behavior, and Statistical Analysis for Decision Making.
- Proficient in leading classrooms, delivering engaging presentations, and utilizing presentation software.
- Created instructional video tutorials to support student learning and offer comprehensive training.
''')

#####################
st.markdown('''
## Skills
''')
txt3('Programing language',' Python, R, SAS')
txt3('Machine learning tools', 'Pandas, Numpy, Matplotlib, Pytorch, Tensorflow, Sickit-learn, keras, seaborn, scipy, os, SHAP, LIME')
txt3('Microsoft Office 365', '(SharePoint, OneDrive, Word, Excel, Outlook, and PowerPoint), MS Teams, Zoom')
txt3('Data analysis tools', 'SQL, MongoDB, Oracle, Tableau, PowerBI, Excel, SPSS, Snowflake')
txt3('Machine learning/deep learning models','Regression, K-means, Hierarchical clustering, XGBoost, Random Forest, decision tree, SVM, RNN, CNN, Transformer Network, GAN, Large language models (LLM), Statistics analysis')
txt3('Model`s Deployment Tools','AWS, Docker, Git')
txt3('Operating system','Linux, MacOs, Windows systems')
txt3('Familiar','Java, Django, Spark, ERP')

#####################
st.markdown('''
## Social Media
''')
txt2('A Comparative Analysis of Machine Learning Models for Diabetes Prediction', 'https://github.com/Golnaz-spa/ML_predict_webapp')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/golnaz-sababipour-asl-527930222/')
txt2('GitHub', 'https://github.com/Golnaz-spa')

