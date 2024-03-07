# CV-generator

CV-generator is a Django web application that allows users to enter their personal details and generate/download their resume in PDF format.

## Features

- **User Registration**: Users can register an account to save their resume details.
- **Resume Creation**: Users can enter their personal details, educational background, skills, work experience, projects, achievements, and links.
- **Resume Download**: Users can download their resume in PDF format.
- **Bootstrap UI**: Stylish user interface built with Bootstrap for a better user experience.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Shrey0226/CV-generator.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run migrations:

    ```bash
    python manage.py migrate
    ```

4. Start the development server:

    ```bash
    python manage.py runserver
    ```

5. Access the application at `http://localhost:8000`.

## Usage

1. Register an account or log in if you already have one.
2. Fill in your personal details, educational background, skills, work experience, projects, achievements, and links.
3. Click on the "Download Resume" button to generate and download your resume in PDF format.

## Dependencies

- [Django](https://www.djangoproject.com/): Web framework for building web applications in Python.
- [pdfkit](https://pypi.org/project/pdfkit/): Python library for converting HTML to PDF using wkhtmltopdf.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for any improvements or additional features you would like to see.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
