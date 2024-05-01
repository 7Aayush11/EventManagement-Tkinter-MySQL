use EventManagement;

create table Employee
(
	empName varchar(40),
    empId int primary key,
    empDno int,
    empSal int
);

create table Emplogin
(
	empId int,
    foreign key(empId) references Employee(empId),
    empPass varchar(20)
);

create table Customer
(
	custName varchar(40),
    custId bigint primary key,
    custEmail varchar(100)
);
create table custlogin
(
	custId bigint,
    foreign key(custId) references Customer(custId),
    custPass varchar(20)
);

insert into Employee values("Aayush",1234,3,50000),("Raj",1230,2,50000),("Ash",5326,2,50000);
insert into Emplogin values(1230,"Rajesh230"),(1234,"Aayush@123");
select * from Customer;
select * from Custlogin;
select * from Emplogin;