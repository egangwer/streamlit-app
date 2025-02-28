# Streamlit Artwork Recommendation

This project is a Streamlit application that allows users to explore artworks and find similar pieces. 


## Installation

To set up the project, follow these steps:

1. Clone the repository to your local machine:
   ```
   git clone <repository-url>
   cd streamlit-app
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the Streamlit application, execute the following command in your terminal:
```
streamlit run src/streamlit_app.py
```

This will start a local server, and you can access the application in your web browser at `http://localhost:8501`.

## Features

- **Find Similar Artworks**: Input an artwork title to receive recommendations for similar pieces.
- **Find an Artist**: Search for an artist to view their works and details.
- **Random Artworks**: Explore a selection of random artworks from the dataset.

## Data Sources

The application uses data from various art museums, including the Cleveland Art Museum, Museum of Modern Art in New York, Art Institute of Chicago, and Harvard Art Museum. The data was accessed through APIs and web scraping.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.