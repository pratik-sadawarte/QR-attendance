import pandas as pd
import sqlite3

def export_to_excel():
    """
    Exports attendance data from SQLite3 to an Excel file.
    """
    conn = sqlite3.connect("attendance.db")
    query = "SELECT * FROM attendance"
    df = pd.read_sql_query(query, conn)
    conn.close()
    
    # Rename columns for clarity in the Excel file
    df.columns = ["ID", "Student ID", "Name", "Roll Number", "Section", "Date & Time"]
    
    # Save the DataFrame to an Excel file
    df.to_excel("attendance.xlsx", index=False)
    
    print("Attendance records exported to attendance.xlsx")

# --- MAIN EXECUTION ---
export_to_excel()