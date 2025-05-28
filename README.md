# Mango Surveillance Website

This is a Django-based web application for mango pest and disease surveillance, allowing growers to manage growers, plants, and surveillance records. Follow these instructions to set up, run, and push the project to your GitHub repository.

## Prerequisites
- **Python 3.10 or higher**: Download from [python.org](https://www.python.org/downloads/). Ensure Python is added to your system PATH.
- **pip**: Verify with `pip --version`.
- **Web Browser**: Chrome, Firefox, or similar.
- A terminal (Command Prompt on Windows, Terminal on macOS/Linux).
- **Git**: Install from [git-scm.com](https://git-scm.com/). Verify with `git --version`.

## Setup Instructions
1. **Unzip the Project**:
   - Extract `mango_surveillance.zip` to a folder (e.g., `C:\mango_surveillance`).
   - Ensure it contains `manage.py`, `db.sqlite3`, `requirements.txt`, `.gitignore`, `README.md`, and subfolders `mango_surveillance` and `surveillance`.

2. **Set Up a Virtual Environment**:
   - Navigate to the project folder:
     ```bash
     cd C:\mango_surveillance
     ```
   - Create and activate a virtual environment:
     ```bash
     python -m venv venv
     venv\Scripts\activate  # Windows
     
    or source venv/bin/activate  # macOS/Linux
     ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Database Migrations**:
   ```bash
   python manage.py migrate
   ```
   - The included `db.sqlite3` contains sample data (growers, plants, 10+ records).

## Running the Website
1. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```
   - Access at `http://127.0.0.1:8000`.

2. **Access the Website**:
   - Open a browser and go to `http://127.0.0.1:8000`.
   - Explore Growers, Plants, and Surveillance Records for CRUD operations.

3. **Optional: Access Admin Interface**:
   ```bash
   python manage.py createsuperuser
   ```
   - Log in at `http://127.0.0.1:8000/admin/`.

## Adding to Your GitHub Repository
To version-control the project, push it to your GitHub repository using these commands, which resolved issues like branch mismatches, unrelated histories, and merge conflicts during development:

1. **Initialize Git**:
   ```bash
   git init
   ```

2. **Stage and Commit Files**:
   ```bash
   git add .
   git commit -m "Initial commit of mango surveillance project"
   ```

3. **Link to GitHub Repository**:
   ```bash
   git remote add origin https://github.com/your-username/mango-surveillance.git
   ```

4. **Rename Branch to `main`**:
   ```bash
   git branch -m main
   ```

5. **Pull Remote Changes**:
   ```bash
   git pull origin main --allow-unrelated-histories
   ```
   - If a merge conflict occurs in `README.md`, edit the file to resolve conflicts, then:
     ```bash
     git add README.md
     git commit -m "Resolved merge conflicts for README.md"
     ```

6. **Push to GitHub**:
   ```bash
   git push -u origin main
   ```
   - Use a personal access token for authentication:
     - Generate at GitHub → Settings → Personal access tokens → Generate new token (select `repo` scope).

7. **Verify**:
   - Visit your GitHub repository to confirm files (`manage.py`, `db.sqlite3`, `requirements.txt`, `README.md`, etc.) are uploaded.

## Troubleshooting
- **Python not found**: Ensure Python is in PATH. Run `python --version`.
- **Module not found**: Verify dependencies with `pip install -r requirements.txt`.
- **Database errors**: Ensure `db.sqlite3` is writable. Run `python manage.py migrate`.
- **Port conflict**: Use `python manage.py runserver 8080`.
- **GitHub Issues**:
  - **Authentication**: Use a personal access token.
  - **Unrelated Histories**: Use `git pull origin main --allow-unrelated-histories`.
  - **Merge Conflicts**: Edit conflicted files (e.g., `README.md`), then `git add` and `git commit`.
  - **Line Endings**: Run `git config --global core.autocrlf true` to avoid CRLF/LF conflicts.

## Features
- **Homepage**: Severity distribution chart with Tailwind CSS for a responsive design.
- **Growers**: Manage grower details (name, email, location).
- **Plants**: Track plant information (grower, type, location, planting date).
- **Surveillance Records**: Record pest/disease data with a search filter.
- **Responsive UI**: Built with Tailwind CSS for a user-friendly interface.

For issues, contact [your name/email].