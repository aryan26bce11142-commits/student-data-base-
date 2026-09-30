import json, os
DB_FILE=os.path.join(os.path.dirname(os.path.abspath(__file__)),"student_database.json")
RESET="\033[0m"; GREEN="\033[92;1m"; BLUE="\033[94;1m"; RED="\033[91;1m"; YELLOW="\033[93;1m"; LIGHTRED="\033[38;5;210;1m"; CYAN="\033[96;1m"; BOLD="\033[1m"
def gi(g): return GREEN if g=="S" else BLUE if g in ("A","B","C") else LIGHTRED if g in ("D","E") else RED
def ai(a): return GREEN if a>=90 else BLUE if a>=75 else RED
def show(db,r):
 r=r.strip().upper(); s=db.get(r)
 if not s: print(RED+"Student not found: "+r+RESET); return
 print("\n"+"="*145); print(BOLD+CYAN+"STUDENT DATABASE MANAGEMENT SYSTEM"+RESET); print("="*145); print("Registration Number:",BOLD+r+RESET); print("Name:",BOLD+s["name"]+RESET); print("-"*145)
 print(f"{'Subject':<25}{'Attendance':<18}{'CAT1':>5}{'CAT2':>5}{'FAT':>5}{'Int':>5}{'Assign':>7}{'Discuss':>8}{'Quiz':>6}{'Marks':>8}{'Grade':>7}  Remark")
 for sub,m in s["subjects"].items():
  ar="Excellent" if m["attendance"]>=90 else "Good" if m["attendance"]>=75 else "Critical"; c=ai(m["attendance"]); g=gi(m["grade"]); print(f"{sub:<25}{c}{m['attendance']:>6.1f}% {ar:<10}{RESET}{m['cat1']:>5}{m['cat2']:>5}{m['fat']:>5}{m['internal']:>5}{m['assignment']:>7}{m['discussion']:>8}{m['quizzes']:>6}{m['final_score']:>8.2f}{g}{m['grade']:>7}{RESET}  {g}{m['remark']}{RESET}")
 print("-"*145); print("Overall Aggregate:",s["overall_aggregate"],"%  | Semester GPA:",s["semester_gpa"],"/ 10  | Average Attendance:",s["average_attendance"],"%")
 status=s["result_status"]; print("Result Status:",GREEN+status+RESET if status=="PROMOTED" else RED+status+RESET); print("="*145)
def main():
 db=json.load(open(DB_FILE,encoding="utf-8")); print(BOLD+CYAN+"\nSTUDENT DATABASE MANAGEMENT SYSTEM"+RESET)
 while True:
  print("\n1. Search student\n2. Show overall topper\n3. Show ALL students\n4. Exit"); ch=input("Enter choice: ").strip()
  if ch=="1": show(db,input("Enter Registration Number: "))
  elif ch=="2":
   r,s=max(db.items(),key=lambda x:x[1]["overall_aggregate"]); print(f"\nOverall Topper: {s['name']} ({r}) - {s['overall_aggregate']}%")
  elif ch=="3":
   for r in db: show(db,r)
   print(f"\nTotal students shown: {len(db)}")
  elif ch=="4": break
  else: print(YELLOW+"Enter 1, 2, 3 or 4."+RESET)
if __name__=="__main__": main()
