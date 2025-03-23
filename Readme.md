## *Key Features*

### *Frontend:*  
•⁠  ⁠*Drag-and-Drop Resume Upload:* 3D hover effects using *Atropos.js* for an interactive resume import experience.  
•⁠  ⁠*Parsing Animation:* Smooth progress spinner (UI Ball) while extracting resume details.  
•⁠  ⁠*Chat-Based Q&A:*  
  - *Smooth, animated chat interface* (Buttermilk) for technical questions.  
  - Candidates provide paragraph-style answers.  
•⁠  ⁠*Code Editor for Skill Assessment:*  
  - Real-time coding challenges with *syntax highlighting*.  
  - Interactive submission button with micro-interactions (UI Ball).  
•⁠  ⁠*Final Report Page:*  
  - *3D interactive visualization* (Three.js) of skill scores and coding results.  
  - AI-generated insights shown in pre-styled cards (UIverse.io).  
  - Option to *download the report in PDF or AR format*.  
•⁠  ⁠*Recruiter Dashboard:*  
  - *3D globe* (Three.js) displaying candidate locations.  
  - Search filters and pre-built tables (UIverse.io) for seamless navigation.  

---

### *Backend:*  
•⁠  ⁠*Gemini API Integration:*  
  - Extracts and summarizes skills, projects, and experience from resumes.  
  - Generates *skill-based MCQs and descriptive coding questions*.  
•⁠  ⁠*Profile Verification:*  
  - *LinkedIn and GitHub API integration* to validate candidate claims.  
•⁠  ⁠*Final Report Generation:*  
  - Combines *technical performance, background verification, and proctoring results*.  
  - Displays the report in the *admin dashboard*.  

---

### *Remote Proctoring System:*  
•⁠  ⁠*Lip Movement Detection:* Verifies if the candidate is speaking unauthorizedly.  
•⁠  ⁠*Background Audio Analysis:* Identifies suspicious or external noises.  
•⁠  ⁠*Head Tracking Detection:* Monitors the candidate’s focus during the assessment.  

---

## 🛠️ *Tech Stack*

### 🔹 *Frontend:*
•⁠  ⁠*react.js* – React framework for building the web app.  
•⁠  ⁠*Three.js* – For 3D visualizations.  
•⁠  ⁠*Atropos.js* – 3D hover effects for resume upload.  
•⁠  ⁠*UI Ball & Buttermilk* – Micro-interactions and smooth animations.  
•⁠  ⁠*UIverse.io* – Pre-styled cards and tables.  

### 🔹 *Backend:*
•⁠  ⁠*Gemini AI Studio* – For resume parsing and skill validation.  
•⁠  ⁠*LinkedIn & GitHub APIs* – For profile verification.  
•⁠  ⁠*MongoDB* – For storing candidate reports and data.  

---

## 🚀 *Installation & Setup*

### *1. Clone the Repository*
```bash
git clone <your-repo-url>
cd 

2.⁠ ⁠Install Dependencies
Install frontend and backend dependencies
npm install

3.⁠ ⁠Start the Development Server
npm run dev
The app will be running at http://localhost:3000

✅ Usage

Upload a Resume: Drag and drop the candidate’s resume.
Automated Parsing: The platform extracts and summarizes the resume details.
Skill Assessment:
MCQs and descriptive technical questions are generated based on the skills mentioned.
Candidates solve coding challenges in a real-time code editor.
Profile Verification:
The platform verifies the candidate’s LinkedIn and GitHub profiles.
Remote Proctoring:
The system monitors lip movements, background audio, and head tracking.
Final Report:
The platform generates a comprehensive report with skill scores, verification results, and proctoring insights.
Recruiters can download the report in PDF or AR format.
