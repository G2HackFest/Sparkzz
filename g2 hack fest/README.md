# Dynamic Addiction Recovery Companion

A web application that serves as a personalized recovery assistant for individuals overcoming addiction. The app uses AI to analyze user inputs, provide coping strategies, and track recovery milestones.

## Features

- User authentication and authorization
- Mood logging and tracking
- AI-powered coping strategies
- Milestone tracking with rewards
- Support chat system
- Mobile-responsive design

## Prerequisites

- Python 3.7 or higher
- Firebase account and project
- Firebase Admin SDK credentials

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd recovery-companion
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up Firebase:
   - Create a new Firebase project
   - Download your Firebase Admin SDK credentials
   - Save the credentials file as `firebase-credentials.json` in the project root

5. Run the application:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Project Structure

```
recovery-companion/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── firebase-credentials.json  # Firebase credentials
├── static/
│   └── css/
│       └── style.css     # Custom CSS styles
└── templates/
    ├── base.html         # Base template
    ├── index.html        # Home page
    ├── login.html        # Login page
    ├── register.html     # Registration page
    └── dashboard.html    # User dashboard
```

## Usage

1. Register a new account or login with existing credentials
2. Use the dashboard to:
   - Log your daily mood and triggers
   - View personalized coping strategies
   - Track your recovery milestones
   - Connect with support through the chat system

## Security Notes

- Never commit the `firebase-credentials.json` file to version control
- Use environment variables for sensitive configuration
- Implement proper input validation and sanitization
- Follow Firebase security rules best practices

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 