* An **Excel sheet** with data.
* A **MySQL table** with the *same structure (same columns, same order)*.
* You want to **automate data insertion** from Excel → MySQL using **Automation Anywhere (A360 or v11)**.

Here’s how you can do it step by step 👇

---

## 🔹 Steps in **Automation Anywhere**

### 1. **Set up the database connection**

* Use **Database: Connect** command.
* Provide your MySQL connection details:

  * Connection string (e.g., `jdbc:mysql://hostname:3306/databasename`)
  * Username
  * Password
  * JDBC driver (`com.mysql.cj.jdbc.Driver`)

---

### 2. **Read the Excel data**

* Use **Excel: Open** → select your Excel file.
* Use **Excel: Get All Rows** to fetch all rows from the sheet.

  * This will store the data in a **DataTable variable** (e.g., `$ExcelDataTable$`).

---

### 3. **Loop through Excel rows**

* Use a **Loop: For each row in DataTable** (`$ExcelDataTable$`).
* Inside the loop:

  * Map each column value to variables (e.g., `$Column[0]$`, `$Column[1]$`, …).

---

### 4. **Insert into MySQL table**

* Inside the loop, use **Database: Run SQL Query**.
* Query Example:

  ```sql
  INSERT INTO your_table (col1, col2, col3)
  VALUES ('${Column[0]}', '${Column[1]}', '${Column[2]}');
  ```
* Make sure column order in SQL matches Excel’s column order.

---

### 5. **Close connections**

* After loop ends →

  * Use **Excel: Close**.
  * Use **Database: Disconnect**.



