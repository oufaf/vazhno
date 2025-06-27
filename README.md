# InStudy - Educational Platform

InStudy is a mobile application built with Python and KivyMD that helps students manage their educational activities, track assignments, view schedules, and access educational resources.

## Features

- Dashboard with quick actions
- Class schedule management
- Course tracking
- Assignment management
- Educational articles
- Student profile with achievements
- Academic performance tracking

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python main.py
```

## Building for Android

1. Install Buildozer:
```bash
pip install buildozer
```

2. Initialize Buildozer (already done in this repository):
```bash
buildozer init
```

3. Build the Android APK:
```bash
buildozer android debug
```

The APK file will be generated in the `bin` directory.

## Requirements

- Python 3.7+
- Kivy 2.2.1
- KivyMD 1.1.1
- Pillow 10.0.0
- Buildozer 1.5.0 (for Android builds)

## Development

The application is structured as follows:

- `main.py` - Main application file
- `buildozer.spec` - Buildozer configuration for Android builds
- `requirements.txt` - Python dependencies

## License

This project is licensed under the MIT License. 