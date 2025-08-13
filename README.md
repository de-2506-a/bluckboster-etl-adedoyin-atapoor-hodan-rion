# BluckBoster: An ETL Pipeline 

Welcome to our **BluckBoster**, an ETL pipeline which extracts uncleaned data and transforms and processed the data.



## Data Analysis

1. Which country has the highest number of customers?
2. Which film has generated the highest revenue?
   
## How to Run It
1. **Clone this repo**:
```bash
git clone https://github.com/de-2506-a/bluckboster-etl-adedoyin-atapoor-hodan-rion.git
cd bluckboster-etl-adedoyin-atapoor-hodan-rion
```
2. **Setup up virtual environment**:
```bash
python3 -m venv .venv
```
- For Windows
```bash
source .venv/Scripts/activate
```
- For MacOS/Linux
```bash
source .venv/bin/activate
```
3. **Install the dependencies**:
```bash
pip install -r requirements.txt
```
4. **Run the project in editable mode**:
```bash
pip install -e .
```
5. **Add `.env.dev` file an add these variables (edit the `SOURCE_DB_USER` and `SOURCE_DB_PASSWORD`)** 
```env
SOURCE_DB_NAME=pagila
SOURCE_DB_USER=<your-db-user>
SOURCE_DB_PASSWORD=<your-db-password>
SOURCE_DB_HOST=data-sandbox.c1tykfvfhpit.eu-west-2.rds.amazonaws.com
SOURCE_DB_PORT=5432
```
6. To run the ETL pipeline:
```bash
run_etl dev
```
7. To run the streamlit app:
```bash
streamlit run vis1.py
```

