# Write your MySQL query statement below
select e.name as Employee
from Employee as e
join Employee as em
on e.managerId = em.id
where e.salary > em.salary;