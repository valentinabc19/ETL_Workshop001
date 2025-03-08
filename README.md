# Workshop001

**Developed by**  
* [Valentina Bueno Collazos](https://github.com/valentinabc19)  

---

## **Project Overview**  
This project analyzes hiring data for job candidates who participated in technical recruitment processes. It includes an **ETL pipeline** (Extract, Transform, Load) to clean, transform, and load data into a PostgreSQL database, enabling dashboard visualizations to uncover trends in hiring outcomes.  

### **Key Features**  
- **ETL Workflow**:  
  - **Extract**: Load raw candidate data from a PostgreSQL database.  
  - **Transform**: Clean data, calculate hiring status, and derive analytical fields.  
  - **Load**: Store processed data in `candidates_final_data` for dashboard integration.  
- **Dashboard Visualizations**:  
  - Hires by technology (pie chart).  
  - Hires by year (horizontal bar chart).  
  - Hires by seniority (bar chart).  
  - Hires by country over years (USA, Brazil, Colombia, Ecuador) (multiline chart).  

### **Technologies Used**  
- **Python**: Data cleaning, transformation, and analysis.  
- **Jupyter Notebook**: Code execution and documentation.  
- **PostgreSQL**: Database storage and management.  
- **PowerBI**: Dashboard creation and data visualization.  

---

## **Dataset Schema**  
The dataset contains **50,000 records** with the following fields:  
- `application_date`: Date of application (converted to `datetime`).  
- `country`: Candidate's country (standardized to lowercase).  
- `yoe`: Years of experience (integer).  
- `seniority`: Seniority level (e.g., "intern", "mid-level", "senior").  
- `technology`: Job technology category (e.g., "data engineer", "devops").  
- `code_challenge_score`: Technical coding score (0–10).  
- `technical_interview_score`: Interview performance score (0–10).  
- `application_status`: `1` if hired (both scores ≥7), `0` otherwise.  
- `application_year`: Derived year from `application_date`.  

**Note**: Personal data (`first_name`, `last_name`, `email`) was removed during transformation for privacy compliance.  

---

## **Setup and Execution**  

### **1. Clone the Repository**  
```bash  
git clone https://github.com/valentinabc19/ETL_Workshop001
```  

### **2. Create a Virtual Environment**  
```bash  
python -m venv venv  
source venv/bin/activate  # Linux/Mac  
venv\Scripts\activate     # Windows  
```  

### **3. Configure Database Credentials**  
Create a `credentials.json` file in the project root:  
```json  
{  
    "db_host": "your_host",  
    "db_name": "your_db",  
    "db_user": "your_user",  
    "db_password": "your_password",  
    "db_port": "5432"  
}  
```  

### **4. Install Dependencies**  
```bash  
pip install -r requirements.txt  
```  

### **5. Run Jupyter Notebooks**  
Execute in order:  
1. `001_conn_and_data_load.ipynb`: Load raw data from PostgreSQL.  
2. `002_EDA.ipynb`: Perform exploratory data analysis.  
3. `003_clean_transform_load.ipynb`: Clean, transform, and load final data.  

### **6. Connect PowerBI to PostgreSQL**  
1. Open PowerBI Desktop → *Get Data* → *PostgreSQL Database*.  
2. Enter server and database credentials from `credentials.json`.  
3. Select the `candidates_final_data` table to build visualizations.  

---

## **Dashboard Insights**  
- **Hiring Trends**: Identify yearly hiring patterns and technology demand.  
- **Regional Analysis**: Compare hiring activity in key countries (USA, Brazil, Colombia, Ecuador).  
- **Performance Metrics**: Evaluate success rates by seniority and technical scores.  

---

**Note**: Ensure PostgreSQL is running and accessible during execution. For detailed visualization guidelines, refer to the [analysis document](link-to-analysis.md).  
```
