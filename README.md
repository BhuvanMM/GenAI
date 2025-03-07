# AI Product Description Generator

A simple web application that uses AI to generate compelling product descriptions for e-commerce based on basic product specifications.

## Features

- Generate professional product descriptions with minimal input
- Multiple description templates (default, promotional, technical, minimalist)
- Simple web interface
- Copy-to-clipboard functionality
- Powered by OpenAI's language models

## Installation

1. Clone this repository:
   ```
   git clone <repository-url>
   cd product-description-generator
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   FLASK_ENV=development
   ```

## Usage

1. Start the Flask development server:
   ```
   python -m app.main
   ```

2. Open your browser and go to: `http://localhost:5000`

3. Fill in the product information form:
   - Select a product category
   - Enter the product name
   - Add materials or ingredients
   - List key features and benefits
   - Specify target audience
   - Include any additional information

4. Choose a template style:
   - Default: Balanced, general-purpose description
   - Promotional: Enthusiastic, marketing-focused text
   - Technical: Detailed specifications format
   - Minimalist: Concise, to-the-point description

5. Click "Generate Description" to create your product description

6. Copy the generated description to use on your e-commerce site

## Deployment

For production deployment:

1. Update the `.env` file with production settings:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   FLASK_ENV=production
   ```

2. Use a WSGI server like Gunicorn to run the application:
   ```
   gunicorn -w 4 "app:create_app()"
   ```

## Customization

You can customize the description templates by modifying the `TEMPLATES` dictionary in `config/config.py`.

## License

This project is licensed under the MIT License - see the LICENSE file for details.