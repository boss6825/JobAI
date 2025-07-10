# Resume Parser System

A comprehensive resume parsing system that extracts structured data from PDF resumes using LangChain and OpenAI, and stores the data in a SQLite database categorized by user.

## Features

- 📄 **PDF Text Extraction**: Extract text from PDF resume files using PyPDF2
- 🤖 **AI-Powered Parsing**: Use LangChain with OpenAI to intelligently parse resume content
- 🗃️ **Structured Data Storage**: Store parsed data in SQLite database with user categorization
- 👤 **User Management**: Automatically categorize resumes by user name (inferred or specified)
- 📊 **Comprehensive Data Extraction**: Extract education, experience, skills, projects, achievements, and more

## Installation

1. Clone or set up the project
2. Install required dependencies:

```bash
pip install -r requirements.txt
```

3. Set up your OpenAI API credentials in a `.env` file:

```env
OPENROUTER_API_KEY=your_api_key_here
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
YOUR_SITE_URL=your_site_url
YOUR_SITE_NAME=your_site_name
```

## Usage

### 1. Add Resume Files

Place your PDF resume files in the `resume/` folder:

```bash
resume/
├── arpit_solanki_resume.pdf
├── john_doe_cv.pdf
└── jane_smith_resume.pdf
```

### 2. Process Resumes

#### Process All Resumes

```bash
python main.py
```

This will process all PDF files in the `resume/` folder and automatically infer user names from the file content or filename.

#### Process All Resumes for a Specific User

```bash
python main.py --user "Arpit Solanki"
```

#### Process a Specific File

```bash
python main.py --file "resume.pdf" --user "John Doe"
```

#### List All Users and Resumes

```bash
python main.py --list
```

### 3. Command Line Options

- `--user, -u`: Specify user name to associate with resume(s)
- `--file, -f`: Process a specific PDF file
- `--list, -l`: List all users and their resumes in the database

## Project Structure

```
langchain/
├── resume/                 # Folder for PDF resume files
├── main.py                # Main script to run the resume parser
├── pdf_parser.py          # PDF text extraction module
├── resume_parser.py       # LangChain-based resume parsing module
├── database.py            # Database models and management
├── model.py               # Original LangChain model configuration
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (API keys)
└── README.md             # This file
```

## Database Schema

### Users Table

- `id`: Primary key
- `name`: User name
- `created_at`: Timestamp

### Resumes Table

- `id`: Primary key
- `user_id`: Foreign key to users table
- `file_name`: Original PDF filename
- `full_name`: Extracted full name
- `email`: Email address
- `phone`: Phone number
- `location`: Current location
- `linkedin`: LinkedIn profile URL
- `github`: GitHub profile URL
- `summary`: Professional summary
- `education`: JSON string of education details
- `experience`: JSON string of work experience
- `technical_skills`: JSON string of technical skills
- `soft_skills`: JSON string of soft skills
- `projects`: JSON string of projects
- `achievements`: JSON string of achievements
- `certifications`: JSON string of certifications
- `raw_text`: Original extracted text
- `created_at`: Timestamp
- `updated_at`: Last update timestamp

## Extracted Data Structure

The system extracts the following structured data from resumes:

### Personal Information

- Full name
- Email address
- Phone number
- Current location
- LinkedIn profile
- GitHub profile

### Professional Summary

- Brief professional summary or objective

### Education

- Institution name
- Degree/qualification
- Field of study
- Graduation year
- GPA (if mentioned)
- Location

### Work Experience

- Company name
- Position/job title
- Duration of employment
- Location
- Key responsibilities and achievements

### Skills

- Technical skills (programming languages, frameworks, tools)
- Soft skills

### Projects

- Project name
- Description
- Technologies used
- Duration
- Project links

### Achievements & Awards

- Achievement title
- Description
- Year achieved
- Awarding organization

### Certifications

- Certification name
- Issuing organization
- Issue date
- Expiry date
- Credential ID

## Example Usage

```python
from pdf_parser import PDFParser
from resume_parser import ResumeParser
from database import DatabaseManager

# Initialize components
pdf_parser = PDFParser()
resume_parser = ResumeParser()
db_manager = DatabaseManager()

# Extract text from a PDF
text = pdf_parser.extract_text_from_pdf("resume/arpit_resume.pdf")

# Parse the resume
parsed_data = resume_parser.parse_resume(text)

# Save to database
resume_record = db_manager.save_resume_data("Arpit Solanki", "arpit_resume.pdf", parsed_data)
```

## Error Handling

The system includes comprehensive error handling:

- Failed PDF text extraction
- AI parsing failures (falls back to regex-based extraction)
- Database connection issues
- File not found errors

## Output Example

```
🚀 Starting Resume Processing Pipeline
=====================================
🔧 Initializing components...
📄 Found 1 PDF file(s): ['arpit_resume.pdf']

============================================================
Processing: arpit_resume.pdf
============================================================
✅ Successfully extracted text (2847 characters)
🔄 Parsing resume with AI...
👤 User identified as: Arpit Solanki
💾 Saving to database...
✅ Successfully saved resume data for Arpit Solanki
📝 Resume ID: 1

📊 Extracted Data Summary:
   • Full Name: Arpit Solanki
   • Email: arpitsolanki6825@gmail.com
   • Phone: +91-8279824227
   • Location: N/A
   • Education entries: 1
   • Work experience entries: 1
   • Projects: 2
   • Technical skills: 8

🎯 Processing Complete!
========================================
✅ Successfully processed: 1
❌ Failed to process: 0
📊 Total files: 1

💾 Data saved to: resume_database.db
🔍 You can query the database to retrieve user resume data
```

## Contributing

Feel free to contribute by:

- Adding support for more file formats (DOC, DOCX)
- Improving the AI parsing prompts
- Adding more structured data fields
- Enhancing error handling
- Adding a web interface

## License

This project is open source. Feel free to use and modify as needed.
