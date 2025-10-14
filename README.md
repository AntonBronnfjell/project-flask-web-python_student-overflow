# Student Overflow - Flask Q&A Platform

A Stack Overflow-inspired Q&A platform for students, built with Flask. Features question posting, answering, voting, and community-driven knowledge sharing.

## Overview

Student-focused Q&A portal with:
- Question and answer system
- User authentication
- Voting mechanism
- Tag-based categorization
- Search functionality
- User profiles
- Reputation system

## Features

- **Post Questions**: Students can ask questions about subjects
- **Answer System**: Community provides answers
- **Voting**: Upvote/downvote questions and answers
- **Tags**: Categorize by subject/topic
- **Search**: Find relevant questions
- **User Profiles**: Track contributions and reputation
- **Best Answer**: Mark accepted solutions

## Tech Stack

- **Framework**: Flask + Jinja2
- **Database**: SQLAlchemy (SQLite for development)
- **Forms**: WTForms (optional)
- **Python**: 3.11+

## Installation

```bash
# Clone repository
git clone <repository-url>
cd project-flask-web-python_student-overflow

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py
```

Access at `http://localhost:5000`

## Project Structure

```
studentoverflow/
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── studentoverflow/
│   ├── __init__.py
│   ├── models.py
│   └── routes/
│       └── main.py
└── templates/
    └── base.html
```

## Usage

1. Register/Login
2. Ask questions
3. Browse questions by tags
4. Answer questions
5. Vote on content
6. Build reputation

## Database Models

- **User**: Authentication and profiles
- **Question**: Posted questions
- **Answer**: Responses to questions
- **Vote**: Voting system
- **Tag**: Categorization

## Contributing

See CONTRIBUTING.md for guidelines.

## License

MIT License

---

**Knowledge Sharing Platform for Students** 🎓
