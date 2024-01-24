USE master;

GO
IF EXISTS (
	SELECT name
		FROM sys.databases
		WHERE name = N'SalesProject'
)
DROP DATABASE SalesProject;

GO
CREATE DATABASE SalesProject;