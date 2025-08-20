# Games-of-thrones-personality-matcher
![image alt](https://github.com/Talha4543/Games-of-thrones-personality-matcher-project/blob/ec64c7dde7e8c97d66bde256b491e9307865a88c/1.PNG)

🐉 Game of Thrones Personality Matcher
======================================

This is a **Streamlit-based web application** that fetches _Game of Thrones_ character data from **ThronesAPI** and allows users to explore characters and build personality-matching features.

🔗 **Repository Link:** [Games-of-thrones-personality-matcher-project](https://github.com/Talha4543/Games-of-thrones-personality-matcher-project.git)

🚀 Features
-----------

*   ✅ Live character data from **ThronesAPI**
    
*   ✅ Interactive **Streamlit web app**
    
*   ✅ Displays characters (Name, Title, Family, etc.)
    
*   ✅ Dropdown selection to view a character
    
*   ✅ Easy to extend with **personality matching** logic
    

📂 Project Structure
--------------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   Games-of-thrones-personality-matcher-project/  │── app.py              # Main Streamlit application  │── requirements.txt    # Python dependencies  │── README.md           # Project documentation (this file)   `

🛠️ Installation
----------------

1.  Clone the repository:
    

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   git clone https://github.com/Talha4543/Games-of-thrones-personality-matcher-project.git  cd Games-of-thrones-personality-matcher-project   `

1.  (Optional) Create a virtual environment:
    

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python -m venv venv  source venv/bin/activate   # Linux/Mac  venv\Scripts\activate      # Windows   `

1.  Install dependencies:
    

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pip install -r requirements.txt   `

▶️ Usage
--------

Run the app:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   streamlit run app.py   `

Open in your browser:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   http://localhost:8501   `

📊 Example Code (app.py)
------------------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   import streamlit as st  import requests  import pandas as pd  # Fetch data directly from ThronesAPI  api_data = requests.get("https://thronesapi.com/api/v2/Characters").json()  # Convert JSON into DataFrame  df = pd.DataFrame(api_data)  # Keep only first 25 characters  df = df.head(25)  # Clean character names for consistency  df['fullName'] = df['fullName'].str.replace('Jaime', 'Jamie')  df['fullName'] = df['fullName'].str.replace('Lord Varys', 'Varys')  # Streamlit UI  st.title("🐉 Game of Thrones Personality Matcher")  st.write("### Available Characters")  st.dataframe(df[['fullName', 'title', 'family']])  # Dropdown to select a character  character = st.selectbox("Choose a character", df['fullName'])  # Show selected character  st.write(f"You selected: **{character}**")   `

📦 Requirements (requirements.txt)
----------------------------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   streamlit  pandas  requests   `

🌟 Future Improvements
----------------------

*   Personality quiz → match user to GoT characters
    
*   Similarity matching using NLP/ML
    
*   Display **character images** in Streamlit
    
    

✍️ Author: **Muhammad Talha**

🔗 Repository: [Games-of-thrones-personality-matcher-project](https://github.com/Talha4543/Games-of-thrones-personality-matcher-project.git)
