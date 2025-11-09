# EKVIRA-AN-VIDEO-COACHING-PLATFORM

**Democratizing Quality Education Through Online Video Coaching**

![Python](https://img.shields.io/badge/Python-68.2%25-blue)
![HTML](https://img.shields.io/badge/HTML-26.7%25-orange)
![CSS](https://img.shields.io/badge/CSS-5.1%25-green)

Built with the tools and technologies:

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

---

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Features](#features)
- [Screenshots](#screenshots)
- [Testing](#testing)

---

## Overview

**Ekvira-An-Video-Coaching-Platform** is an innovative web-based learning platform built with Django that enables educators to upload and share coaching videos, making quality education accessible to everyone. The platform bridges the gap between learners and instructors by providing a centralized hub for video-based learning and skill development.

### Why Ekvira?

This project addresses the growing demand for accessible, affordable, and flexible learning solutions. The core mission and features include:

- 🎓 **Knowledge Accessibility**: Make quality coaching and educational content available to learners globally.
- 📹 **Video Hosting**: Upload, organize, and manage coaching videos with easy-to-use interface.
- 👨‍🏫 **Instructor Empowerment**: Enable educators to reach wider audiences without technical barriers.
- 🌍 **Global Reach**: Democratize education and eliminate geographical and socio-economic constraints.
- 📚 **Content Organization**: Structured categories and playlists for seamless learning paths.
- 🎯 **User-Friendly Design**: Intuitive interface for both instructors and learners.

---

## Getting Started

### Prerequisites

This project requires the following dependencies:

- **Programming Language**: Python (3.8 or higher)
- **Framework**: Django (3.2+)
- **Frontend**: HTML5, CSS3
- **Database**: SQLite (default)
- **Package Manager**: pip or Conda

### Installation

Build Ekvira-An-Video-Coaching-Platform from the source and install dependencies:

1. **Clone the repository:**

```bash
git clone https://github.com/JayeshSPatel/Ekvira-An-Video-Coaching-Platform
cd Ekvira-An-Video-Coaching-Platform
```

2. **Create a virtual environment:**

Using venv:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Using conda:

```bash
conda create -n ekvira python=3.9
conda activate ekvira
```

3. **Install the dependencies:**

Using pip:

```bash
pip install -r requirements.txt
```

Using conda:

```bash
conda install --file requirements.txt
```

4. **Apply migrations:**

```bash
python manage.py migrate
```

5. **Create a superuser (optional):**

```bash
python manage.py createsuperuser
```

---

## Project Structure

```
Ekvira-An-Video-Coaching-Platform/
├── manage.py                 # Django management script
├── requirements.txt          # Project dependencies
├── db.sqlite3               # SQLite database
├── ekvira/                  # Main project directory
│   ├── settings.py          # Project settings
│   ├── urls.py              # URL routing
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
├── courses/                 # Main app directory
│   ├── models.py            # Database models (Course, Video, etc.)
│   ├── views.py             # View functions
│   ├── urls.py              # App URL routes
│   ├── forms.py             # Django forms
│   ├── admin.py             # Admin panel configuration
│   └── templates/           # HTML templates
│       ├── base.html        # Base template
│       ├── home.html        # Home page
│       ├── courses.html     # Courses listing
│       ├── video_detail.html # Video player page
│       └── ...
├── static/                  # Static files
│   ├── css/                 # CSS stylesheets
│   ├── js/                  # JavaScript files
│   └── images/              # Image assets
└── media/                   # Uploaded videos and files
```

---

## Usage

### Running the Development Server

Start the Django development server:

Using pip:

```bash
python manage.py runserver
```

Using conda:

```bash
conda activate ekvira
python manage.py runserver
```

The application will be accessible at `http://127.0.0.1:8000/`

### Accessing the Admin Panel

Open your browser and navigate to:

```
http://127.0.0.1:8000/admin/
```

Log in with your superuser credentials to manage courses, videos, and user content.

---

## Features

- ✅ **Video Upload & Management**: Instructors can upload and organize coaching videos
- ✅ **Course Creation**: Structure videos into organized courses and playlists
- ✅ **Video Streaming**: Smooth playback with video player controls
- ✅ **User Authentication**: Secure login and registration system
- ✅ **Progress Tracking**: Track learner progress through courses
- ✅ **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- ✅ **Search & Discovery**: Find courses and videos easily with search functionality
- ✅ **Categorization**: Organize content by subject and difficulty level

---

## Screenshots

### Ekvira-An-Video-Coaching-Platform
![image](https://github.com/user-attachments/assets/bfe7cd42-e107-457f-8703-40e1519d9756)

![image](https://github.com/user-attachments/assets/82bafb10-57e9-4c68-8753-3fa70542bff2)

![image](https://github.com/user-attachments/assets/4dee6f03-9a3b-4302-9463-a8879c0e89d8)

![image](https://github.com/user-attachments/assets/b18c62dd-9d42-48b0-bebc-237ba8b980c2)

![image](https://github.com/user-attachments/assets/b3516806-eab3-468f-8925-c7b2036dbb82)


---

## Testing

Run the test suite with:

Using pip:

```bash
python manage.py test
```

Using conda:

```bash
conda activate ekvira
python manage.py test
```

---

⬆ [Return to Top](#ekvira-an-video-coaching-platform)

