SELECT MAX(salary) From Emp
where not in (SELECT MAX(salary) From Emp)


SELECT id , empName,salary From Emp as E1 
where n-1 = (
    SELECT Count(Distinct salary) 
    From Emp as E2
    where E1.salary > E2.salary
)