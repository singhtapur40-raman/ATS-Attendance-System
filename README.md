# 🎓 ATS – AI-Powered Attendance Management System

### Smart Attendance Tracking Using Face Recognition, Voice Recognition & QR Codes

ATS (Attendance Tracking System), also known as **SnapClass**, is an AI-powered attendance management application designed to simplify and modernize classroom attendance.

The system combines Artificial Intelligence, Machine Learning, biometric recognition, and cloud database technology to automate attendance tracking. Instead of relying entirely on traditional manual roll calls, teachers can use face and voice recognition to identify students and maintain attendance records.

Built using **Python, Streamlit, Machine Learning, and Supabase**, the application provides separate portals for teachers and students, making attendance management more efficient, accessible, and organized.

---

## 🚀 Key Features

### 1. Face Recognition-Based Attendance
- Identifies registered students using facial recognition.
- Extracts facial embeddings for identity matching.
- Uses a machine learning classifier to recognize enrolled students.
- Helps automate classroom attendance recording.

### 2. Voice Recognition-Based Attendance
- Supports voice-based student identification.
- Uses audio processing to extract speaker embeddings.
- Compares voice features with previously enrolled voice data.
- Provides an additional biometric identification method.

### 3. Teacher Dashboard
- Dedicated teacher login and dashboard.
- Create and manage subjects.
- Manage enrolled students.
- Conduct attendance sessions.
- View and manage attendance records.

### 4. Student Portal
- Dedicated student interface.
- Student registration and biometric enrollment.
- Access subject enrollment functionality.
- Join subjects using a subject code or QR-based enrollment.
- View personal attendance information.

### 5. QR Code-Based Enrollment
- Generate QR codes for subject enrollment.
- Allow students to join subjects using shared enrollment information.
- Simplify the process of connecting students with their respective subjects.

### 6. Cloud Database Integration
- Uses Supabase as the backend database.
- Stores student and teacher information.
- Maintains subject and enrollment records.
- Stores attendance information and biometric embeddings.

---

## 🧠 How the System Works

The application combines different technologies to automate the attendance process.

### Face Recognition Workflow

1. Students register and provide facial data.
2. The system processes the facial image.
3. Facial embeddings are generated.
4. The trained machine learning classifier compares the embeddings with registered student data.
5. The recognized student's identity is used in the attendance workflow.

**Technology:** dlib, face_recognition_models, Scikit-learn.

### Voice Recognition Workflow

1. Audio data is collected through the voice attendance interface.
2. Audio processing techniques prepare the voice input.
3. Resemblyzer generates speaker embeddings.
4. The extracted embeddings are compared with stored voice data.
5. The identification result is used in the attendance workflow.

**Technology:** Resemblyzer, Librosa, WebRTC VAD.

### QR Code Enrollment Workflow

1. A teacher shares subject enrollment information.
2. A QR code or subject code is provided to students.
3. Students access the enrollment process.
4. The system associates the student with the selected subject.

---

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Frontend / UI | Streamlit |
| Face Recognition | dlib, face_recognition_models |
| Machine Learning | Scikit-learn |
| Voice Recognition | Resemblyzer |
| Audio Processing | Librosa, WebRTC VAD |
| Database | Supabase |
| Database Engine | PostgreSQL |
| Authentication | bcrypt |
| QR Code Generation | Segno |
| Image Processing | Pillow |
| Data Processing | NumPy, Pandas |
| Version Control | Git, GitHub |

---

## 🏗️ Project Architecture

The project follows a modular architecture that separates the user interface, database operations, biometric processing, and application logic.

```text
ATS-Attendance-System/
│
├── app.py
│
├── requirements.txt
│
└── src/
    │
    ├── screens/
    │   ├── home_screen.py
    │   ├── teacher_screen.py
    │   └── student_screen.py
    │
    ├── database/
    │   ├── config.py
    │   └── db.py
    │
    ├── pipelines/
    │   ├── face_pipeline.py
    │   └── voice_pipeline.py
    │
    └── components/
        ├── header.py
        ├── footer.py
        ├── subject_card.py
        └── dialog components
```

**Module descriptions:**

- `app.py`: Main application entry point and navigation between teacher and student portals.
- `screens/`: Contains the different application interfaces.
- `database/`: Handles Supabase configuration and database operations.
- `pipelines/`: Contains face and voice recognition processing logic.
- `components/`: Contains reusable interface elements and dialogs.

---

## 🗄️ Database Integration

The application uses **Supabase (PostgreSQL)** for cloud-based data management.

The database manages the following information:

| Data | Purpose |
|---|---|
| Teachers | Teacher account information |
| Students | Student profiles and biometric data |
| Subjects | Subject and classroom information |
| Subject-Students | Student enrollment records |
| Attendance Logs | Student attendance history |

Supabase provides persistent cloud storage, allowing the application to access and update attendance information.

---

## 🌟 What Makes This Project Different?

Traditional attendance systems generally depend on manual roll calls, paper registers, or basic attendance applications.

ATS introduces a combination of biometric identification and automated attendance management.

| Traditional Systems | ATS Attendance System |
|---|---|
| Manual roll calls | AI-assisted identification |
| Paper-based records | Cloud-based records |
| Manual student verification | Face and voice recognition |
| Manual subject enrollment | QR-code-based enrollment |
| Separate attendance processes | Integrated teacher and student portals |
| Limited automation | Machine learning-based workflows |

### Our Approach

The main objective is to bring multiple technologies together into one integrated platform rather than building a basic attendance application.

By combining face recognition, voice recognition, QR-based enrollment, and cloud database management, ATS aims to make classroom attendance more convenient and organized.

---

## 🔮 Future Scope

The project can be further enhanced with:

- Real-time classroom attendance monitoring.
- Improved biometric recognition accuracy.
- Advanced attendance analytics and visualization.
- Notification systems for attendance updates.
- Enhanced database security and role-based access control.
- Integration with university management systems.

---

## 🔐 Security Considerations

- Teacher passwords are handled using bcrypt hashing.
- Supabase credentials should be maintained using environment secrets.
- Biometric information should be protected with appropriate access controls.
- Database Row Level Security policies should be configured according to the application's authentication model.
- Access to student information should be restricted to authorized users.

---

## 🎯 Project Objective

The primary objective of ATS is to reduce the effort involved in traditional attendance management by introducing intelligent automation.

This project demonstrates the practical integration of:

- Artificial Intelligence
- Machine Learning
- Computer Vision
- Voice Processing
- Cloud Database Management
- Web Application Development

It serves as an application of AI and ML concepts to a real-world educational problem.

---

## 👨‍💻 Author

**Tapur Singh**

B.Tech – Computer Science Engineering  
Specialization: Artificial Intelligence and Machine Learning

GitHub: [@singhtapur40-raman](https://github.com/singhtapur40-raman)

---

## ⭐ Support

If you find this project interesting, consider giving the repository a star!

Contributions, suggestions, and feedback are always welcome.

**Built with Python, AI, Machine Learning, and a vision to make attendance smarter!**
