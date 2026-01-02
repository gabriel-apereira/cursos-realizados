-- 1. Cria um relatório para todos os pedidos de 1996 e seus clientes (152 linhas)
SELECT * 
FROM orders o
INNER JOIN customers c ON o.CustomerID = c.CustomerID
WHERE YEAR(o.OrderDate) = 1996


-- 2. Cria um relatório que mostra o número de funcionários e clientes de cada cidade que tem funcionários (5 linhas)
SELECT e.City AS cidade, 
       COUNT(DISTINCT e.EmployeeID) AS numero_de_funcionarios, 
       COUNT(DISTINCT c.CustomerID) AS numero_de_clientes
FROM Employees e 
LEFT JOIN Customers c ON e.City = c.City
GROUP BY e.City
ORDER BY cidade

-- 3. Cria um relatório que mostra o número de funcionários e clientes de cada cidade que tem clientes (69 linhas)
SELECT c.city AS cidade, 
       COUNT(DISTINCT e.EmployeeID) AS numero_de_funcionarios, 
       COUNT(DISTINCT c.CustomerID) AS numero_de_clientes
FROM customers c
LEFT JOIN employees e  ON c.city = e.city
GROUP BY c.city
ORDER BY cidade


-- 4.Cria um relatório que mostra o número de funcionários e clientes de cada cidade (71 linhas)
SELECT COALESCE(e.city, c.city) AS cidade, 
       COUNT(DISTINCT e.EmployeeID) AS numero_de_funcionarios, 
       COUNT(DISTINCT c.CustomerID) AS numero_de_clientes
FROM customers c
FULL JOIN employees e  ON c.city = e.city
GROUP BY c.city, e.city
ORDER BY cidade

-- 5. Cria um relatório que mostra a quantidade total de produtos encomendados.
-- Mostra apenas registros para produtos para os quais a quantidade encomendada é menor que 200 (5 linhas)
SELECT p.ProductName as Produto, 
       SUM(o.Quantity) as Quantidade
FROM Products p
INNER JOIN [Order Details] o on p.ProductID = o.ProductID
GROUP BY p.ProductName
HAVING SUM(o.Quantity) < 200

-- 6. Cria um relatório que mostra o total de pedidos por cliente desde 31 de dezembro de 1996.
-- O relatório deve retornar apenas linhas para as quais o total de pedidos é maior que 15 (5 linhas)
SELECT c.CompanyName as Cliente, 
       COUNT(o.OrderID) as Quantidade
FROM Customers c
INNER JOIN Orders o ON c.CustomerID = o.CustomerID
WHERE o.OrderDate > convert(DATETIME,'1996-12-31',120)
GROUP BY c.CompanyName
HAVING COUNT(o.OrderID) > 15

