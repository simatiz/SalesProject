USE SalesProject;

BULK INSERT SalesData
FROM 'C:\Users\simatiz\PycharmProjects\SalesProject\clear_source\data2.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
