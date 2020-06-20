import csv
def write_info_csv(info_list):
    with open("student_info_csv","a+") as csv_file:
        writer= csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["NAME","AGE","CONTACT_NO.","EMAIL ID"])
            writer.writerow(info_list)

if __name__=='__main__':
    condition=True
    student_num=1
    while(condition):
        student_info=input("Enter The School Information For Student # "+str(student_num)+" in the following format (NAME AGE CONTACT.NO EMAIL ID): ")
        student_info_list=student_info.split(" ")
        print("The Entered Information Is:")
        print("NMAE: "+student_info_list[0]+"\nAGE: "+str(student_info_list[1])+"\nCONTACT NO.: "+str(student_info_list[2])+"\nEMAIL ID: "+student_info_list[3])
        choice_check=input("Is The Entered Information Is Correct(yes/no): ")
        if choice_check =="yes":
            write_info_csv(student_info_list)
            condtion_check=input("Enter(yes/no) If You Wants To Enter The Information Of Another Student: ")
        if condtion_check =="yes":
            condition=True
            student_num+=1
        elif condtion_check =="no":
            condition=False
        elif choice_check =="no":
            print("Please Re-Enter The Information")


