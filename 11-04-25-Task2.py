Employees={
    "emp1":{"emp_name":"vinay",
          "salary":50000
          },
    "emp2":{
        "emp_name":"abi",
        "salary":40000
        },
    "emp3":{
        "emp_name":"Ramu",
        "salary":45000
    },
    "emp4":{
        "emp_name":"vicky",
        "salary":47000
    }
}

Total_Emp_sal=0

for i in Employees:
    Emp_salary=Employees[i]["salary"]
    Total_Emp_sal+=Emp_salary
    print(f" {Employees[i]["emp_name"]} Salary in percentage :{(Emp_salary/50000)*100}%")

print("Total_Emp_sal",Total_Emp_sal)
